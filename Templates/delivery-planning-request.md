Use Delivery Planning Skill.

## Inputs

### Discovery Output

{{engineering_discovery_output}}

### Decisions Locked

{{decisions}}

### Scope

{{scope}}

### Jira / release context

| Input | Example |
|-------|---------|
| **Jira project(s)** | `ROS`, `COST` |
| **Target fix version / release** | `ROS 1.x` |
| **Components / teams** | `ros-ocp-backend`, `platform-kruize` |
| **MVP scope** | What must ship in iteration N vs defer |
| **QE policy** | Same sprint (QE blocked by Dev) or next sprint |

{{jira_context}}

---

## Instructions

Create a delivery plan.

Break work into meaningful Jira tasks.

Generate tasks for:

- Development
    
- QE
    
- Documentation
    

Requirements:

- Tasks must be reasonably small
    
- Tasks must be independently testable
    
- Tasks must have clear acceptance criteria
    
- Tasks must identify dependencies
    
- Tasks should support parallel execution where possible
    
- Apply **INVEST** gate, **Agile slicing** (MVP labels), and **Jira mapping** from `Skills/delivery-planning.md`
    
- Tag epics with MVP / Phase 2 / Stretch where scope may be cut
    

---

## Output Format

Produce the task list artifacts:

| File | Required |
|------|----------|
| **`{{Feature}}-Iteration{{N}}-Task-List.md`** | Yes — source of truth |
| **`{{Feature}}-Iteration{{N}}-Task-List.docx`** | Yes — Google Docs import (epic page breaks) |

Follow `Skills/delivery-planning.md`:

- **Output format (required)** — epic grouping, paired Dev/QE per ID, seven fields per task (Title, Jira, Description, Test Instructions, Expected Results, Additional Results, Acceptance Criteria)
- **Google Docs export** — Google-Docs-friendly markdown (no `-` lists; blank line between every field/bullet); generate `.docx` with page break before each epic; stakeholders import via Drive → Open with Google Docs (not copy-paste)
- **Jira mapping** — issue types, Description layout, dependencies
- **Agile slicing** — MVP / phase labels on epics
- **Dev/QE workflow** — QE blocked by Dev unless N/A

Optionally produce a short companion:

**`docs/07-implementation-tasks.md`** (or equivalent) — epic index, suggested execution order, critical path, and links to feature docs. Do **not** duplicate full task bodies in the companion doc.

### Optional: Google Sheets progress tracker

When requested, also follow **`Skills/delivery-planning-sheets-tracker.md`**:

| File | Purpose |
|------|---------|
| **`[Internal ONLY] {{Feature}} Iteration {{N}} JIRA Issues - {{Feature}} pending Tasks.csv`** | Google Sheets import — same columns as namespace feature tracker (no Comments column) |

Generate with `scripts/task-list-to-sheets-csv.py` from the task-list markdown.