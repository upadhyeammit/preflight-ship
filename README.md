# Preflight Ship

**Think. Review. Ship.**

AI-assisted engineering workflows — discovery, architecture review, delivery planning, and retrospectives — before implementation begins.

---

## Purpose

Structured engineering before you ship. Reduce rework, surface risks early, and get features implementation-ready.

---

## Skills

Skills define workflows. Activate a skill only when explicitly requested.

| Skill | File |
|-------|------|
| Engineering Discovery | `Skills/engineering-discovery.md` |
| Architecture Review | `Skills/architecture-review.md` |
| Delivery Planning | `Skills/delivery-planning.md` |
| Feature Retrospective | `Skills/feature-retrospective.md` |

---

## Workflow

```
Think    → Discovery
Review   → Architecture Review → Decision Locking
Ship     → Delivery Planning → Implementation → Retrospective
```

---

## Structure

```
preflight-ship/
├── Skills/           # Workflows (behavior)
├── Checklists/       # Analysis criteria
├── Frameworks/       # Process guidance
├── Templates/        # Request inputs only
├── Examples/         # Sample executions
├── Lessons-Learned/  # Captured improvements
├── README.md
└── LICENSE
```

| Directory | Purpose |
|-----------|---------|
| `Skills/` | Workflow behavior — the source of truth for each engineering phase |
| `Checklists/` | Analysis criteria applied during discovery and review |
| `Frameworks/` | End-to-end process guidance across the engineering lifecycle |
| `Templates/` | Input-only request templates — no workflow logic |
| `Examples/` | Sample skill executions for reference |
| `Lessons-Learned/` | Outcomes from retrospectives that drive future improvements |

---

## Checklists

| Checklist | File |
|-----------|------|
| Database | `Checklists/database.md` |
| Kafka | `Checklists/kafka.md` |
| REST API | `Checklists/rest-api.md` |
| Microservice | `Checklists/microservice.md` |
| Observability | `Checklists/observability.md` |
| Security | `Checklists/security.md` |
| Performance | `Checklists/performance.md` |
| Query Performance | `Checklists/query-performance.md` |
| Scalability | `Checklists/scalability.md` |
| Maintainability | `Checklists/maintainability.md` |
| DRY & Design | `Checklists/dry-design.md` |

---

## Templates

| Template | File |
|----------|------|
| Discovery Request | `Templates/discovery-request.md` |
| Quick Discovery Request | `Templates/quick-discovery-request.md` |
| Architecture Review Request | `Templates/architecture-review-request.md` |
| Delivery Planning Request | `Templates/delivery-planning-request.md` |
| Retrospective Request | `Templates/retrospective-request.md` |

---

## Frameworks

| Framework | File |
|-----------|------|
| Engineering Lifecycle | `Frameworks/Engineering Lifecycle Framework.md` |

---

## Getting Started

```bash
git clone https://github.com/<your-org>/preflight-ship.git
cd preflight-ship
```

You can use Preflight Ship in two ways:

| Setup | Best for |
|-------|----------|
| **Standalone workspace** | Running discovery, review, or planning sessions |
| **Alongside your project** | Applying workflows while working in your codebase |

Skills are not automatically activated. Normal coding tasks do not trigger workflows.

---

## Usage in Cursor

Cursor is the recommended IDE. This repository includes a project rule at `.cursor/rules/preflight-ship.mdc` that configures skill activation behavior.

### Option 1 — Open as workspace

1. Open the `preflight-ship` folder in Cursor.
2. The project rule loads automatically.
3. Start a chat and run a workflow (see [Running a workflow](#running-a-workflow)).

### Option 2 — Use alongside your project

1. **File → Add Folder to Workspace** and add `preflight-ship`.
2. Save as a multi-root workspace (e.g., `my-app.code-workspace`).
3. In chat, reference skill and template files with `@`:

   ```
   @Skills/engineering-discovery.md
   @Templates/quick-discovery-request.md
   ```

4. Paste your filled-in template and send.

### Option 3 — Global user rule

Add a [user rule](https://docs.cursor.com/context/rules) so Preflight Ship works across all projects without adding the folder each time. Point it at your local clone path and list the skill files. Use this when you want discovery and planning available in any repo you open.

### Cursor tips

- **Agent mode** — best for discovery and delivery planning (reads skills, checklists, and your codebase).
- **Ask mode** — good for read-only architecture review.
- **Explicit activation** — say *"Run Engineering Discovery"* or *"Use the Architecture Review skill"*. The AI will not enter a workflow unless you ask.
- **@ references** — attach the skill file and a template to give the AI the full workflow and your inputs.

---

## Usage in Other IDEs

Preflight Ship is plain Markdown. Any AI-assisted editor or chat tool can use it — the pattern is always: **load the skill → fill a template → run explicitly**.

### VS Code + GitHub Copilot

1. Clone this repository locally.
2. Optionally add a `.github/copilot-instructions.md` in your project:

   ```markdown
   For engineering discovery, architecture review, delivery planning, or
   retrospectives, load skills from /path/to/preflight-ship/Skills/ and follow
   the workflow defined in the skill. Do not activate these workflows unless
   explicitly requested.
   ```

3. In Copilot Chat, attach or reference the skill and template files.
4. Paste your filled-in template and request the skill by name.

### Windsurf

1. Add Preflight Ship guidance to your Windsurf rules (`.windsurfrules` or workspace rules).
2. Reference skill and template paths from your local clone.
3. Request skills explicitly in Cascade, same as Cursor.

### JetBrains AI Assistant

1. Add Preflight Ship instructions under **Settings → Tools → AI Assistant → Custom Instructions**.
2. In the AI chat, paste the skill content or point to the file on disk.
3. Fill in a template and request the workflow.

### Claude, ChatGPT, or other AI chats

1. Copy the contents of the relevant skill (e.g., `Skills/engineering-discovery.md`) into the conversation.
2. Copy a filled-in template below it.
3. Ask the model to follow the skill workflow and output format.

No IDE integration required — skills and templates are self-contained.

---

## Running a Workflow

This is the same regardless of IDE.

### 1. Choose a template

| Phase | Template |
|-------|----------|
| Discovery (detailed) | `Templates/discovery-request.md` |
| Discovery (quick) | `Templates/quick-discovery-request.md` |
| Architecture review | `Templates/architecture-review-request.md` |
| Delivery planning | `Templates/delivery-planning-request.md` |
| Retrospective | `Templates/retrospective-request.md` |

### 2. Fill in the template

Replace placeholders with your context:

```markdown
Use Engineering Discovery Skill.

## Context

Payment service monolith migrating to event-driven architecture.
Team of 4, target launch Q3.

## Feature

Add idempotent refund processing with Kafka event publishing.

## Current Understanding

Refunds today are synchronous REST calls. We need to emit RefundCompleted
events for downstream analytics and ledger reconciliation.
```

### 3. Request the skill explicitly

Example prompts:

```
Run Engineering Discovery using the input below. Follow the skill workflow
and output format exactly.

[paste filled template]
```

```
Use the Architecture Review skill on this discovery output and proposed design.

[paste filled template]
```

### 4. Review and iterate

The active skill selects relevant checklists from `Checklists/` and frameworks from `Frameworks/`. Review the output, lock decisions, then move to the next phase.

### End-to-end example

```
Think    →  Templates/quick-discovery-request.md  +  Skills/engineering-discovery.md
Review   →  Templates/architecture-review-request.md  +  Skills/architecture-review.md
Ship     →  Templates/delivery-planning-request.md  +  Skills/delivery-planning.md
Improve  →  Templates/retrospective-request.md  +  Skills/feature-retrospective.md
```

---

## Contributing

Improvements from retrospectives belong in `Lessons-Learned/`. Sample outputs belong in `Examples/`. See existing skills and checklists for conventions before adding new ones.
