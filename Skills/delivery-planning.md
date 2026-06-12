# Delivery Planning Checklist

## Why This Matters

Poor task decomposition causes:

- Long-running tickets
    
- Difficult reviews
    
- Delayed testing
    
- Hidden dependencies
    
- Inaccurate estimates
    

The goal is to create tasks that are independently understandable, reviewable, testable, and deliverable.

---

## Scope Validation

### Questions

- Is the task solving one problem?
    
- Is the task addressing one primary concern?
    
- Does the task have a clear outcome?
    

### Risks

- Scope creep
    
- Hidden complexity
    
- Ambiguous ownership
    

### Decisions

- Task boundary
    
- Task ownership
    

---

## Size Validation

### Questions

- Can this task reasonably be completed within 1-3 days?
    
- Can the work be reviewed in a single PR?
    
- Can the work be tested independently?
    
- Can this task be split further?
    

### Risks

- Large PRs
    
- Long review cycles
    
- Difficult testing
    

### Decisions

- Split task
    
- Keep task as-is
    

### INVEST story quality gate

Apply to each Dev/QE story before finalizing:

| Letter | Question |
|--------|----------|
| **I** — Independent | Can it merge without unrelated work in the same ticket? |
| **N** — Negotiable | Is scope clear but not over-specified? |
| **V** — Valuable | Does it advance the iteration goal or MVP? |
| **E** — Estimable | Is it ~1–3 days (or a time-boxed spike)? |
| **S** — Small | Should it be split further? |
| **T** — Testable | Do Test Instructions + Acceptance Criteria suffice for sign-off? |

If any letter fails, split, spike, or re-scope before writing Jira tickets.

---

## Dependency Analysis

### Questions

- Does this task depend on another task?
    
- Can this task run in parallel?
    
- What blocks this task?
    
- What does this task block?
    

### Risks

- Hidden dependencies
    
- Delivery delays
    

### Decisions

- Dependency mapping
    
- Execution order
    

---

## Development Coverage

### Questions

- Are schema changes represented?
    
- Are API changes represented?
    
- Are integration changes represented?
    
- Are observability changes represented?
    

### Risks

- Missing implementation work
    

### Decisions

- Additional development tasks
    

---

## QE Coverage

### Questions

- Is a test plan needed?
    
- Is regression testing needed?
    
- Is integration testing needed?
    
- Is failure testing needed?
    

### Risks

- Untested functionality
    

### Decisions

- QE task creation
    

---

## Documentation Coverage

### Questions

- Is API documentation impacted?
    
- Is architecture documentation impacted?
    
- Is a runbook needed?
    
- Are release notes required?
    

### Risks

- Knowledge gaps
    
- Operational confusion
    

### Decisions

- Documentation tasks
    

---

## Acceptance Criteria Quality

### Questions

- Is success measurable?
    
- Can QE validate it?
    
- Is the outcome observable?
    
- Is ambiguity removed?
    

### Risks

- Incomplete implementation
    
- Disputed completion
    

### Decisions

- Acceptance criteria refinement
    

---

## Operational Readiness

### Questions

- Are metrics defined?
    
- Are logs defined?
    
- Are alerts defined?
    
- Is monitoring updated?
    

### Risks

- Production blind spots
    

### Decisions

- Observability tasks
    

---

## Final Validation

Before task creation verify:

- No oversized tasks
    
- No hidden dependencies
    
- Development tasks exist
    
- QE tasks exist
    
- Documentation tasks exist
    
- Acceptance criteria are measurable
    
- Observability is covered
    
- Deployment impact is considered
    
- MVP / phase labels assigned where scope may be cut
    
- Jira issue types and dependencies identified per ticket
    
- Dev/QE pairing policy applied (QE blocked by Dev unless N/A)

---

## Agile slicing

Before grouping into epics, define delivery increments:

### Questions

- What is the **smallest demoable or verifiable** outcome for the iteration?
- Which epics are **MVP** vs **Phase 2** vs **stretch**?
- Can any work be a **vertical slice** (thin end-to-end path) instead of only horizontal layers?
- Are **spikes** needed (time-boxed 1–2 days, output = decision doc, not production code)?

### Decisions

- Mark each epic: `MVP` | `Phase 2` | `Stretch` | `Spike`
- Document **increment goal** in the companion doc (e.g. "MVP = Epics A + E + B1 → internal GPU path in stage")
- Prefer vertical slices when the team can ship and learn early; horizontal epics are OK for platform/backend features when increments are still testable per epic

### Risks

- All horizontal work with no integratable milestone until the end
    
- Stretch scope bundled into MVP epics

---

## Jira mapping

Map markdown output to Jira as follows.

### Issue hierarchy

| Markdown | Jira issue type | Notes |
|----------|-----------------|-------|
| `## Epic A — …` | **Epic** | One Jira Epic per markdown epic; summary = heading text |
| `### A1 (DEV) …` | **Story** or **Task** | **Story** when there is a clear deliverable/outcome; **Task** for pure plumbing |
| `### A1 (QE) …` | **Story** or **Task** | Same type as paired Dev; distinguish with label `qe` |
| Time-boxed investigation | **Spike** (or Story labeled `spike`) | Output is a decision or doc, not production code |
| Cross-team work (e.g. platform) | **Story** with separate **Component** | Different assignee/team than application work |

Dev and QE tickets are **sibling issues** under the same Epic — not sub-tasks of each other unless the team explicitly uses sub-tasks for QE.

### Standard fields (per story/task)

Include in each task block when generating the import-ready list:

| Field | Guidance |
|-------|----------|
| **Project** | From planning inputs (e.g. `ROS`, `COST`) |
| **Component / team** | Service or owning team (e.g. `ros-ocp-backend`, `platform-kruize`) |
| **Labels** | Feature slug, `iteration-{{N}}`, `dev` or `qe`, optional `mvp`, `feature-flag` |
| **Fix version / target release** | From planning inputs when known |
| **Priority** | Set only for true blockers; avoid defaulting all tickets to High |
| **Story points** | Optional; ~1 day ≈ 1–2 pts, ~3 days ≈ 3–5 pts; **split if > 5** |
| **External ID** | Stable id in title: `(DEV) A1` — use label `A1` or custom field for traceability |
| **Epic link** | Parent Epic A, B, … |
| **Depends on** | Issue ids or markdown ids: `Blocked by: A1` |

### Description layout (Jira paste)

Compose Jira **Description** from the six markdown fields:

    ## Summary
    {Description — 1–3 sentences}

    ## Context
    - Docs: {links to feature docs, ADRs, diagrams}
    - Locked decisions: {bullets if relevant}

    ## Test plan
    {Test Instructions}

    ## Expected results
    {Expected Results}

    ## Additional deliverables
    {Additional Results}

Put **Acceptance Criteria** in the Jira AC field (Cloud) or a checklist under `## Acceptance criteria` in Description (Server/Data Center). AC bullets must be **copy-paste ready** — one observable outcome per bullet.

### Dependencies in Jira

- Document **per ticket**: `Blocked by: {id}` / `Blocks: {id}`.
- Document **epic-level** critical path and phases in the companion doc (`07-implementation-tasks.md`).
- External teams: add **External dependency** in Description (owner, expected date).

### Cross-team and release

- Multi-repo features: include **deploy order** in companion doc and reference from release epics (e.g. Kruize profile before ROS GPU payload in lower envs).
- Stories that change customer-visible behavior: note **feature flag / kill switch** in Description and AC.

---

## Dev/QE workflow

Default pairing policy for Agile sprints:

| Policy | When | Jira link |
|--------|------|-----------|
| **Same sprint, sequential** | QE starts when Dev is code-complete in sprint | QE **blocked by** Dev |
| **Next sprint** | QE only valid in integrated env after merge | QE in sprint N+1; label `regression` |
| **QE N/A** | Doc-only or spike with no test harness | Document reason on epic; no QE ticket |

Unless the team agrees otherwise: **every `(QE) Xn` is blocked by `(DEV) Xn`**.

QE Acceptance Criteria must require **evidence** (logs, snapshots, matrices, test report links).

---

## Definition of Done (shared)

Stories inherit this DoD; do not repeat on every ticket unless team requires it:

- Code merged and reviewed
- Unit tests added/updated (Dev); integration evidence attached (QE)
- Acceptance criteria met
- Docs/runbook updated when listed in Additional Results
- Feature flag / kill switch behavior verified when applicable
- No PII in new logs or metrics
- Dependencies and release notes considered for cross-team work

---

## Output format (required)

After completing the checklist above, generate an **import-ready** task list suitable for Jira copy/paste.

### Document header

Use this header (fill in feature name and iteration):

    # {{Feature Name}} — Iteration {{N}}: Dev + QE task list (import-ready)

    Each task below includes:

    1. **Title**
    2. **Description**
    3. **Test Instructions**
    4. **Expected Results**
    5. **Additional Results**
    6. **Acceptance Criteria**

    Tasks are **paired** (Dev + QE) per ID.

### Epic structure

- Group work into **Epics** (A, B, C, … or domain-named epics).
- Under each epic heading, include **one sentence** describing what the epic delivers.
- Tag each epic with increment: **MVP** | **Phase 2** | **Stretch** | **Spike** (when applicable).
- For every Dev task ID `Xn`, create a **paired** `(QE) Xn` task unless explicitly N/A (state why in the epic intro).
- Per epic, optional bullets: **Assumptions**, **Risks**, **Out of scope** (keeps sprint planning honest).

### Per-task template

Use this structure for **every** Dev and QE task:

    ### Xn (DEV) Short slug

    - **Title**: (DEV) Xn — Human-readable title
    - **Jira**: Issue type (Story/Task) · Component · Labels · Fix version · Story points · Depends on
    - **Description**: What and why (1–3 sentences). Reference locked decisions where relevant.
    - **Test Instructions**:
      - Concrete steps (fixtures, env, commands, assertions).
    - **Expected Results**:
      - Observable outcomes after test instructions.
    - **Additional Results**:
      - Docs, metrics, runbook snippets, evidence artifacts (or omit section only if truly none).
    - **Acceptance Criteria**:
      - Measurable bullets; QE must be able to sign off from these alone.

For QE tasks: use `### Xn (QE) …`, **Title** `(QE) Xn — …`, and emphasize integration evidence, matrices, and regression.

### Naming conventions

| Element | Pattern | Example |
|---------|---------|---------|
| Epic | `## Epic A — Short name` | `## Epic A — Container CSV ingestion & updateResults` |
| Dev block | `### A1 (DEV) Slug` | `### A1 (DEV) Optional GPU columns in container CSV` |
| Dev title | `(DEV) A1 — …` | `(DEV) A1 — Accept optional GPU columns in container CSV` |
| QE title | `(QE) A1 — …` | `(QE) A1 — Validate CSV ingestion with/without GPU columns` |

### Pairing rules

1. **Same ID** for Dev and QE (`A1` ↔ `A1`).
2. QE **Test Instructions** reuse the same fixtures/scenarios as Dev where applicable.
3. QE **Acceptance Criteria** require **evidence** (logs, snapshots, test matrices).
4. Documentation deliverables: fold into Dev **Additional Results** or a dedicated epic (e.g. observability/fixtures).

### Companion doc (optional)

If the repo uses a thin implementation-tasks page, keep it as **epic index + MVP increment + execution order + critical path + external dependencies** only. Put the full task bodies in `{{Feature}}-Iteration{{N}}-Task-List.md`.

### Bulk Jira import (optional)

If using CSV/API import instead of paste:

- One row per issue; **Epic Link** = epic summary or key
- Stable **External id** column or label matching `A1`, `B2`, …
- **Issue Type**, **Summary**, **Description**, **Acceptance Criteria**, **Labels**, **Components**, **Fix Version**, **Story Points**, **Depends on** as separate columns
- Do not rely on markdown structure for automated import without a transform step

### Checklist → output mapping

| Checklist area | Must appear in output |
|----------------|------------------------|
| Size validation | Tasks sized for ~1–3 days / one reviewable PR |
| QE coverage | Paired `(QE)` per `(DEV)` |
| Documentation | Dev **Additional Results** or doc epic |
| Dependencies | Epic order + optional execution-order section in companion doc |
| Observability | Dedicated tasks when metrics/logs are required |

### Do not use

- `DEV-1`, `QE-1`, `DOC-1` numbering (use epic IDs: A1, B2, …).
- Unpaired Dev tasks without QE or documented N/A.
- Vague acceptance criteria (e.g. "works correctly").