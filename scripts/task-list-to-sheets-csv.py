#!/usr/bin/env python3
"""Convert a delivery-planning *-Task-List.md to a Google Sheets progress tracker CSV.

Column layout matches the namespace feature tracker (no Comments column).
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

TASK_HEADING = re.compile(r"^### ([A-Z]\d+) \((DEV|QE)\) (.+)$")
FIELD = re.compile(r"^\*\*(Title|Jira|Description)\*\*:\s*(.*)$")
EPIC_HEADING = re.compile(r"^## Epic ([A-Z]) — (.+)$")
MILESTONE_TABLE_ROW = re.compile(r"^\|\s*\*\*([^*|]+)\*\*\s*\|")

COLUMNS = [
    "Issue link",
    "Summary",
    "Area",
    "Custom field (Story Points)",
    "Milestones",
    "Status",
    "Must for Production release?",
    "Labels",
    "Assignee",
    "Sprint",
    "Issue key",
    "Custom field (Epic Link)",
]


def strip_md(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def parse_jira_line(line: str) -> dict:
    info = {
        "issue_type": "",
        "component": "",
        "labels": "",
        "points": "",
        "blocked_by": "",
        "assignee": "",
        "notes": "",
    }
    m = re.match(r"(Story|Task|Spike)", line)
    if m:
        info["issue_type"] = m.group(1)

    m = re.search(r"Component `([^`]+)`", line)
    if m:
        info["component"] = m.group(1)

    m = re.search(r"Labels (.+?) · Fix version", line)
    if m:
        labels = re.findall(r"`([^`]+)`", m.group(1))
        info["labels"] = ", ".join(labels)

    m = re.search(r"Points:\s*(\d+)", line)
    if m:
        info["points"] = m.group(1)

    m = re.search(
        r"Blocked by:\s*(.+?)(?:\s*·\s*\*\*Assignee|\s*·\s*Note:|\s*·\s*\*\*Start|$)",
        line,
    )
    if m:
        info["blocked_by"] = strip_md(m.group(1).strip())

    m = re.search(r"\*\*Assignee:\s*([^*]+)\*\*", line)
    if m:
        info["assignee"] = m.group(1).strip()

    if "Note:" in line:
        info["notes"] = strip_md(line.split("Note:", 1)[1].strip())

    return info


def derive_area(component: str, role: str, issue_type: str) -> str:
    parts: list[str] = []
    if role == "QE":
        parts.extend(["QE", "integration testing"])
    elif component.startswith("platform-"):
        parts.extend(["Platform", component.replace("platform-", "").title()])
    else:
        parts.extend(["Backend", component or "ros-ocp-backend"])
    if issue_type == "Task" and role == "DEV":
        parts.append("documentation")
    return ", ".join(parts)


def must_for_production(task_id: str, role: str, labels: str, notes: str) -> str:
    if "N/A" in notes or (task_id == "D2" and role == "QE"):
        return "No"
    if "mvp" in labels.lower():
        return "Yes"
    return "Yes"


def parse_milestones_from_companion(path: Path) -> dict[str, str]:
    """Parse MVP increment table: first column label -> M1, M2, ..."""
    if not path.exists():
        return {}

    text = path.read_text()
    mapping: dict[str, str] = {}
    in_table = False
    milestone_idx = 0

    for line in text.splitlines():
        if "## MVP increment" in line or "### MVP increment" in line:
            in_table = True
            continue
        if in_table and line.startswith("## ") and "MVP" not in line:
            break
        if not in_table or not line.startswith("|"):
            continue
        if re.match(r"^\|\s*-+", line) or "Milestone" in line and "Outcome" in line:
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue

        milestone_idx += 1
        milestone = f"M{milestone_idx}"
        task_cell = cells[1]

        # Ranges like A1–A3 and comma lists F3, E1, E2
        for part in re.split(r",\s*", task_cell):
            part = part.strip()
            range_m = re.match(r"([A-Z]\d+)[–-]([A-Z]\d+)", part)
            if range_m:
                letter = range_m.group(1)[0]
                start = int(range_m.group(1)[1:])
                end = int(range_m.group(2)[1:])
                for n in range(start, end + 1):
                    mapping[f"{letter}{n}"] = milestone
            else:
                id_m = re.match(r"([A-Z]\d+)", part)
                if id_m:
                    mapping[id_m.group(1)] = milestone

    return mapping


def epic_link_name(feature: str, epic_letter: str, epic_title: str) -> str:
    short = re.sub(r"\s*·\s*\*\*MVP\*\*.*$", "", epic_title).strip()
    short = strip_md(short)
    return f"{feature} Epic {epic_letter} — {short}"


def parse_tasks(md_path: Path, feature: str, milestones: dict[str, str]) -> list[dict]:
    lines = md_path.read_text().splitlines()
    current_epic = ""
    current_epic_title = ""
    tasks: list[dict] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m_epic = EPIC_HEADING.match(line)
        if m_epic:
            current_epic = m_epic.group(1)
            current_epic_title = m_epic.group(2)
            i += 1
            continue

        m_task = TASK_HEADING.match(line)
        if m_task:
            task_id, role, _slug = m_task.groups()
            title = ""
            jira_line = ""
            i += 1
            while i < len(lines):
                ln = lines[i]
                if TASK_HEADING.match(ln) or EPIC_HEADING.match(ln):
                    break
                fm = FIELD.match(ln)
                if fm:
                    key, val = fm.group(1), fm.group(2)
                    if key == "Title":
                        title = strip_md(val)
                    elif key == "Jira":
                        jira_line = val
                i += 1

            jira = parse_jira_line(jira_line)
            tasks.append(
                {
                    "summary": title,
                    "area": derive_area(jira["component"], role, jira["issue_type"]),
                    "story_points": jira["points"],
                    "milestones": milestones.get(task_id, "MVP"),
                    "status": "New",
                    "must_for_production": must_for_production(
                        task_id, role, jira["labels"], jira["notes"]
                    ),
                    "labels": jira["labels"],
                    "assignee": jira["assignee"],
                    "epic_link": epic_link_name(feature, current_epic, current_epic_title),
                    "_task_id": task_id,
                    "_role": role,
                }
            )
            continue
        i += 1

    milestone_order = {f"M{n}": n for n in range(1, 20)}
    milestone_order["MVP"] = 99

    def sort_key(t: dict) -> tuple:
        tid = t["_task_id"]
        num = int(re.search(r"\d+", tid).group())
        role_order = 0 if t["_role"] == "DEV" else 1
        return (milestone_order.get(t["milestones"], 98), tid[0], num, role_order)

    tasks.sort(key=sort_key)
    return tasks


def write_csv(tasks: list[dict], out_path: Path) -> None:
    total = sum(int(t["story_points"]) for t in tasks if t["story_points"].isdigit())
    dev = sum(
        int(t["story_points"])
        for t in tasks
        if t["story_points"].isdigit() and t["_role"] == "DEV"
    )
    qe = sum(
        int(t["story_points"])
        for t in tasks
        if t["story_points"].isdigit() and t["_role"] == "QE"
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for t in tasks:
            writer.writerow(
                [
                    "",
                    t["summary"],
                    t["area"],
                    t["story_points"],
                    t["milestones"],
                    t["status"],
                    t["must_for_production"],
                    t["labels"],
                    t["assignee"],
                    "",
                    "",
                    t["epic_link"],
                ]
            )
        writer.writerow([])
        writer.writerow(["", "Total story pts for feature", "", str(total)])
        writer.writerow(["", "Total story pts (Dev)", "", str(dev)])
        writer.writerow(["", "Total story pts (QE)", "", str(qe)])
        writer.writerow(["", "Pending work (all tasks)", "", str(total)])
        writer.writerow([])
        writer.writerow(
            [
                "",
                f"Task count: {len(tasks)} (Dev: {sum(1 for t in tasks if t['_role']=='DEV')}, QE: {sum(1 for t in tasks if t['_role']=='QE')})",
            ]
        )
        writer.writerow([])
        writer.writerow(["WIP", "0"])
        writer.writerow(["DONE", "0"])
        writer.writerow(["NEXT PLANNED", str(len(tasks))])
        writer.writerow(["TBD/Blocked", "0"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--feature", required=True, help="Feature short name for Epic Link column")
    parser.add_argument(
        "--milestones",
        type=Path,
        default=None,
        help="Companion doc with ## MVP increment table",
    )
    parser.add_argument(
        "--milestone-json",
        type=Path,
        default=None,
        help='JSON file: {"A1": "M1", "A4": "M2"}',
    )
    args = parser.parse_args()

    milestones: dict[str, str] = {}
    if args.milestone_json:
        milestones = json.loads(args.milestone_json.read_text())
    elif args.milestones:
        milestones = parse_milestones_from_companion(args.milestones)

    tasks = parse_tasks(args.input, args.feature, milestones)
    if not tasks:
        print("No tasks parsed — check markdown format.", file=sys.stderr)
        return 1

    write_csv(tasks, args.output)
    total = sum(int(t["story_points"]) for t in tasks if t["story_points"].isdigit())
    print(f"Wrote {len(tasks)} tasks ({total} pts) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
