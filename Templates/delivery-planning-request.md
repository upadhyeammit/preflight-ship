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

Produce a single markdown file:

**`{{Feature}}-Iteration{{N}}-Task-List.md`**

Follow `Skills/delivery-planning.md`:

- **Output format (required)** — epic grouping, paired Dev/QE per ID, six fields + **Jira** metadata per task
- **Jira mapping** — issue types, Description layout, dependencies
- **Agile slicing** — MVP / phase labels on epics
- **Dev/QE workflow** — QE blocked by Dev unless N/A

Optionally produce a short companion:

**`docs/07-implementation-tasks.md`** (or equivalent) — epic index, suggested execution order, critical path, and links to feature docs. Do **not** duplicate full task bodies in the companion doc.