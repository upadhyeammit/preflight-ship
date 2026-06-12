# Delivery Planning — Google Sheets progress tracker (optional)

Optional add-on to **Delivery Planning**. Use when the team tracks feature delivery in a **Google Sheet** (same layout as the namespace feature tracker).

**Activate when:** user asks for a progress tracker CSV, Google Sheets import, or pending-tasks sheet alongside the task list.

**Requires:** `{{Feature}}-Iteration{{N}}-Task-List.md` already generated per `Skills/delivery-planning.md`.

**Reference example:** `[Internal ONLY] Namespace level recs JIRA Issues - Namespace level recs_pending Tasks .csv` (column layout).

---

## Output artifact

| File | Purpose |
|------|---------|
| `[Internal ONLY] {{Feature}} Iteration {{N}} JIRA Issues - {{Feature}} pending Tasks.csv` | Import to Google Sheets; fill Issue key / Assignee / Sprint as Jira tickets are created |

Place next to the task list (typically `docs/`). Regenerate whenever `*-Task-List.md` changes.

---

## CSV columns (fixed — do not add Comments)

| Column | Source | Initial value |
|--------|--------|---------------|
| Issue link | Jira | Empty |
| Summary | `**Title**:` | Plain text |
| Area | Component + role | e.g. `Backend, ros-ocp-backend` or `QE, integration testing` |
| Custom field (Story Points) | `Points:` in Jira line | Number |
| Milestones | Companion doc MVP phases | `M1`, `M2`, … (see below) |
| Status | — | `New` for all pending rows |
| Must for Production release? | MVP / N/A rules | `Yes` or `No` |
| Labels | Jira line | Comma-separated, no backticks |
| Assignee | Jira line if present | Empty until assigned |
| Sprint | — | Empty |
| Issue key | Jira | Empty |
| Custom field (Epic Link) | Epic heading | `{{Feature}} Epic A — short name` until Jira epic key exists |

**Do not include a Comments column.**

---

## Milestone mapping

Define task-id → milestone in the companion doc (`07-implementation-tasks.md` **MVP increment** table). Example:

| Milestone | Task IDs | Outcome |
|-----------|----------|---------|
| M1 | F3, E1, E2, B1, A1–A3, X2 | First integratable path |
| M2 | A4, F1, F2 | Wire-through / harden |
| M3 | C1, C2, D1, D2 | Recommendations + API |
| M4 | B2 | Release smoke |

Sort rows: milestone order → epic letter → task number → DEV before QE.

---

## Field derivation rules

**Area**

- QE → `QE, integration testing` + component when not platform
- `platform-*` + DEV → `Platform, {name}`
- `ros-ocp-backend` + DEV → `Backend, ros-ocp-backend`
- Task-type doc work → append `documentation`

**Must for Production release?**

- Default `Yes` for MVP tasks
- `No` when task is explicitly optional / N/A (e.g. QE smoke with no consumer in iteration)

**Labels**

- Extract all backtick-wrapped labels from the Jira line: `gpu, iteration-1, dev, mvp, A1`

**Epic Link**

- Map `## Epic X — …` to a stable display name: `{{Feature}} Epic X — {short name from heading}`

---

## Summary rows (append after task rows)

Match the namespace tracker pattern:

```
(empty row)
,Total story pts for feature,,{total}
,Total story pts (Dev),,{dev_total}
,Total story pts (QE),,{qe_total}
,Pending work (all tasks),,{total}
(empty row)
,Task count: {n} (Dev: {d}, QE: {q})
(empty row)
WIP,0
DONE,0
NEXT PLANNED,{n}
TBD/Blocked,0
```

---

## Generation workflow

1. Confirm `*-Task-List.md` exists and uses the Google-Docs-friendly format from `delivery-planning.md`.
2. Read milestone mapping from companion doc or planning inputs.
3. Run the converter script (preferred — consistent output):

    python3 scripts/task-list-to-sheets-csv.py \
      --input docs/{{Feature}}-Iteration{{N}}-Task-List.md \
      --output "docs/[Internal ONLY] {{Feature}} Iteration {{N}} JIRA Issues - {{Feature}} pending Tasks.csv" \
      --feature "{{Feature}}" \
      --milestones docs/07-implementation-tasks.md

   Or pass `--milestone-json` with `{"A1":"M1","A4":"M2",...}` when no companion doc exists.

4. Link the CSV from `docs/README.md` and `07-implementation-tasks.md`.
5. Tell the user: **File → Import** in Google Sheets (or upload to Drive → Open with Google Sheets). Do not copy-paste from CSV.

---

## Google Sheets usage

- **Issue key** / **Issue link**: fill when Jira ticket is created
- **Assignee** / **Sprint**: fill during sprint planning
- **Status**: update (`New` → `In Progress` → `Closed`) to drive WIP/DONE summary counts manually or via sheet formulas
- **Custom field (Epic Link)**: replace display name with Jira epic key when epics exist

---

## Relationship to other delivery-planning outputs

| Artifact | Required | Purpose |
|----------|----------|---------|
| `*-Task-List.md` | Yes | Source of truth |
| `*-Task-List.docx` | When stakeholders use Google Docs | Formatted review doc |
| `*-pending Tasks.csv` | **Optional** | Progress tracking in Google Sheets |

This skill does not replace Jira import or the markdown task list.
