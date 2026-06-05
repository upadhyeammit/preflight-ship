
## Purpose

Transform a feature request into an implementation-ready design.

Focus on:

- understanding
    
- assumptions
    
- unknowns
    
- risks
    
- tradeoffs
    
- decisions
    

The goal is to discover problems before implementation begins.

Do not jump directly to implementation.

---

# Phase 1 - Discovery Planning

Understand the current system and the scope of change.

Determine:

- affected repositories
    
- affected services
    
- affected APIs
    
- affected Kafka topics/events
    
- affected databases
    
- affected integrations
    
- affected external dependencies
    

Create a high-level impact summary.

---

# Phase 2 - Checklist Discovery

Determine which checklists are relevant.

Available Checklists (in `Checklists/`):

- microservice.md
- rest-api.md
- kafka.md
- database.md
- query-performance.md
- security.md
- performance.md
- scalability.md
- observability.md
- maintainability.md
- dry-design.md
    

Apply only relevant checklists.

Do not apply irrelevant checklists.

For each selected checklist:

- Explain why it is relevant
    
- Apply the checklist
    
- Capture findings
    

---

# Phase 3 - Requirements Discovery

Identify:

- functional requirements
    
- non-functional requirements
    
- business requirements
    
- operational requirements
    

Determine:

- missing requirements
    
- ambiguous requirements
    
- conflicting requirements
    

---

# Phase 4 - Assumption Discovery

Identify:

- technical assumptions
    
- business assumptions
    
- operational assumptions
    

Challenge assumptions where appropriate.

Highlight assumptions requiring validation.

---

# Phase 5 - Unknown Discovery

Identify:

- technical unknowns
    
- operational unknowns
    
- integration unknowns
    
- deployment unknowns
    

Highlight unknowns that require investigation.

---

# Phase 6 - Risk Analysis

Identify:

- reliability risks
    
- scalability risks
    
- security risks
    
- operational risks
    
- maintenance risks
    

Classify:

- High Risk
    
- Medium Risk
    
- Low Risk
    

---

# Phase 7 - Edge Case Analysis

Identify:

- failure scenarios
    
- recovery scenarios
    
- boundary conditions
    
- unusual user behavior
    
- integration failure cases
    

---

# Phase 8 - Decision Analysis

Identify decisions requiring alignment.

For each decision:

- available options
    
- tradeoffs
    
- recommendation
    

Capture:

- open questions
    
- unresolved decisions
    

---

# Phase 9 - Recommended Approach

Provide:

- proposed solution
    
- reasoning
    
- tradeoffs
    
- implementation considerations
    

Do not generate implementation tasks.

Do not generate code.

Focus on design readiness.

---

# Output Format

## Feature Summary

## Relevant Checklists Applied

For each checklist:

### Why Selected

### Key Findings

### Risks Identified

### Decisions Required

### Recommended Actions

---

## Requirements

### Functional Requirements

### Non-Functional Requirements

---

## Assumptions

---

## Unknowns

### Technical Unknowns

### Operational Unknowns

### Integration Unknowns

### Deployment Unknowns

---

## Risks

### High Risk

### Medium Risk

### Low Risk

---

## Edge Cases

---

## Decisions Requiring Alignment

---

## Open Questions

---

## Recommended Approach

---

## Next Steps