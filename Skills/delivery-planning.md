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

After completing the checklist above, generate an **import-ready** task list suitable for Jira copy/paste **and** stakeholder review in Google Docs.

Produce **two artifacts** from the same content:

| Artifact | Purpose |
|----------|---------|
| `{{Feature}}-Iteration{{N}}-Task-List.md` | Source of truth; version-controlled; Jira field copy/paste |
| `{{Feature}}-Iteration{{N}}-Task-List.docx` | Google Docs import with epic page breaks and paragraph layout |

Regenerate the `.docx` whenever the markdown task list changes.

### Document header

Use this header (fill in feature name and iteration):

    # {{Feature Name}} — Iteration {{N}}: Dev + QE task list (import-ready)

    Each task below includes:

    1. **Title**
    2. **Jira** (issue type, component, labels, fix version, story points, dependencies)
    3. **Description**
    4. **Test Instructions**
    5. **Expected Results**
    6. **Additional Results**
    7. **Acceptance Criteria**

    Tasks are **paired** (Dev + QE) per ID. **QE is blocked by Dev** unless noted.

    ### Jira / release context

    **Projects**: …
    **Fix version**: …
    **QE policy**: …
    **MVP increment**: …

    **Definition of Done:** …

### Epic structure

- Group work into **Epics** (A, B, C, … or domain-named epics).
- Under each epic heading, include **one sentence** describing what the epic delivers.
- Tag each epic with increment: **MVP** | **Phase 2** | **Stretch** | **Spike** (when applicable).
- For every Dev task ID `Xn`, create a **paired** `(QE) Xn` task unless explicitly N/A (state why in the epic intro).
- Per epic, optional context lines (not markdown list dashes): `• **Assumptions:** …`, `• **Risks:** …`, `• **Out of scope:** …`.

### Per-task template (Google Docs–friendly markdown)

Use this structure for **every** Dev and QE task. Format for **paragraph breaks**, not markdown list nesting — Google Docs ignores single line breaks and treats `-` prefixes as literal dashes on paste.

    ### Xn (DEV) Short slug

    **Title**: (DEV) Xn — Human-readable title

    **Jira**: Issue type (Story/Task) · Component · Labels · Fix version · Story points · Blocked by

    **Description**: What and why (1–3 sentences). Reference locked decisions where relevant.

    **Test Instructions**:

    • Concrete step (fixtures, env, commands, assertions).

    • Another step when needed.

    **Expected Results**:

    • Observable outcome after test instructions.

    **Additional Results**:

    • Docs, metrics, runbook snippets, evidence artifacts (or omit section only if truly none).

    **Acceptance Criteria**:

    • Measurable bullet; QE must be able to sign off from these alone.

Formatting rules for the task-list markdown:

- **No `-` list markers** on task fields or sub-items — use labeled lines (`**Title**:`) and `•` / `◦` for bullets.
- **Blank line between every field and every bullet** — each block must be its own paragraph (double newline) or Google Docs merges content into one run-on line.
- **No markdown tables** in the task list — use `**Field**: value` lines (tables paste poorly).
- **No `---` horizontal rules** — use blank lines between sections.
- Nested sub-bullets: `◦` under a `•` parent, each on its own line with blank lines between siblings.

For QE tasks: use `### Xn (QE) …`, **Title** `(QE) Xn — …`, and emphasize integration evidence, matrices, and regression.

### Google Docs export (required when stakeholders use Google Docs)

Copy-paste from `.md` **cannot** create page breaks and often breaks layout. Use **file import** instead.

**Workflow (verified):**

1. Generate `{{Feature}}-Iteration{{N}}-Task-List.docx` from the markdown (page break before each `## Epic`).
2. Upload the `.docx` to Google Drive.
3. Right-click → **Open with → Google Docs**.

Do **not** open the file locally and copy-paste into an existing Google Doc — that strips page breaks and paragraph structure.

**DOCX generation requirements:**

- Insert a **page break** immediately before each `## Epic …` heading (intro + Jira context on page 1; each epic starts on a new page).
- Preserve one paragraph per field and per bullet (match the blank-line structure in markdown).
- Strip markdown syntax to plain text in the Word file (`**bold**` → bold or plain; `` `code` `` → plain).
- Use a readable body font (e.g. Arial 11pt); epic headings as Heading 1; task headings (`###`) as Heading 2.

**Optional fallback:** generate `.html` with `page-break-before: always` on epic headings if `.docx` import is unavailable. HTML import is less reliable than `.docx` in Google Docs.

**Do not use for page breaks:**

- Form-feed characters (`\f`) in markdown — invisible and ignored by Google Docs on paste.
- Copy-paste from markdown expecting epic page breaks.
- `---` or extra blank pages as manual markers — use real page breaks in `.docx` only.

**Jira vs Google Docs:** Jira Description paste (see **Jira mapping** above) may still use `-` bullets — that is separate from the stakeholder task-list file format.

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

### Google Sheets progress tracker (optional)

When the team tracks delivery in a shared Google Sheet (namespace-feature pattern), activate **`Skills/delivery-planning-sheets-tracker.md`**.

Produces:

    [Internal ONLY] {{Feature}} Iteration {{N}} JIRA Issues - {{Feature}} pending Tasks.csv

- Same column layout as the namespace reference tracker — **no Comments column**
- One row per Dev/QE task; **Issue key** / **Assignee** / **Sprint** left empty until Jira planning
- Milestones from companion doc **MVP increment** table
- Generate via `scripts/task-list-to-sheets-csv.py` (see optional skill)

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
| Stakeholder review | `.md` task list + `.docx` with epic page breaks for Google Docs import |
| Progress tracking | Optional `.csv` for Google Sheets — see `delivery-planning-sheets-tracker.md` |

### Do not use

- `DEV-1`, `QE-1`, `DOC-1` numbering (use epic IDs: A1, B2, …).
- Unpaired Dev tasks without QE or documented N/A.
- Vague acceptance criteria (e.g. "works correctly").
- `-` markdown list syntax in `*-Task-List.md` (pastes as a dash on every row in Google Docs).
- Single line breaks between task fields without a blank line (Google Docs merges into one paragraph).
- Copy-paste from markdown into Google Docs when page breaks or clean layout are required — import `.docx` instead.