## Why This Matters

Many engineering issues originate from incomplete discovery, rushed design reviews, poor task decomposition, or missing feedback loops.

This checklist ensures that a feature moves through a consistent engineering lifecycle before implementation begins.

---

# Phase 1 - Engineering Discovery

## Objective

Understand the feature, identify unknowns, assumptions, risks, and required decisions.

### Questions

- Is the business problem clearly understood?
    
- Are functional requirements defined?
    
- Are non-functional requirements defined?
    
- Are assumptions documented?
    
- Have unknowns been identified?
    
- Have risks been identified?
    
- Have relevant checklists been applied?
    

### Deliverables

- Feature Summary
    
- Requirements
    
- Assumptions
    
- Unknowns
    
- Risks
    
- Decisions Required
    

### Exit Criteria

- Major unknowns identified
    
- Risks documented
    
- Relevant checklists completed
    

---

# Phase 2 - Architecture / Design Review

## Objective

Validate the proposed solution before implementation begins.

### Questions

- Is the design understandable?
    
- Is the design maintainable?
    
- Is the design scalable?
    
- Is the design secure?
    
- Is the design observable?
    
- Are service boundaries appropriate?
    
- Are integration patterns appropriate?
    

### Deliverables

- Proposed Design
    
- Design Alternatives
    
- Tradeoff Analysis
    

### Exit Criteria

- Design approved
    
- Major concerns addressed
    
- Tradeoffs documented
    

---

# Phase 3 - Decision Locking

## Objective

Ensure important decisions are explicit and agreed upon.

### Questions

- What decisions were made?
    
- What assumptions remain?
    
- What constraints exist?
    
- What alternatives were rejected?
    
- Who approved the decisions?
    

### Deliverables

- Decision Log
    
- Assumption Log
    
- Constraints List
    

### Exit Criteria

- Decisions documented
    
- Stakeholder alignment achieved
    

---

# Phase 4 - Delivery Planning

## Objective

Transform design into an execution plan.

### Questions

- What work must be completed?
    
- Which teams are involved?
    
- Which tasks can run in parallel?
    
- What dependencies exist?
    

### Deliverables

- Delivery Plan
    
- Dependency Map
    
- Work Breakdown
    

### Exit Criteria

- Work decomposition completed
    
- Dependencies identified
    

---

# Phase 5 - Task Sizing Review

## Objective

Ensure Jira tasks are small, testable, and reviewable.

### Questions

- Is each task focused on one concern?
    
- Can each task be completed in 1-3 days?
    
- Can each task be reviewed independently?
    
- Can each task be tested independently?
    
- Can any task be split further?
    

### Deliverables

- Sized Task List
    

### Exit Criteria

- No oversized tasks
    
- No ambiguous ownership
    
- Clear dependencies
    

---

# Phase 6 - Jira Generation

## Objective

Create actionable implementation tasks.

### Questions

- Are Development tasks present?
    
- Are QE tasks present?
    
- Are Documentation tasks present?
    
- Do all tasks have acceptance criteria?
    
- Are dependencies documented?
    

### Deliverables

- Development Tickets
    
- QE Tickets
    
- Documentation Tickets
    

### Exit Criteria

- Jira backlog ready
    
- Acceptance criteria defined
    

---

# Phase 7 - Implementation Review

## Objective

Validate implementation quality before release.

### Questions

- Are requirements implemented?
    
- Are acceptance criteria satisfied?
    
- Are observability requirements implemented?
    
- Are security requirements satisfied?
    
- Are tests completed?
    

### Deliverables

- Completed Implementation
    
- Test Results
    

### Exit Criteria

- Feature ready for release
    

---

# Phase 8 - Feature Retrospective

## Objective

Capture lessons and improve future delivery.

### Questions

- What worked well?
    
- What did not work well?
    
- Which unknowns were missed?
    
- Which assumptions were incorrect?
    
- Which decisions proved valuable?
    
- What should be added to the Engineering Discovery Skill (`engineering-discovery.md`)?
    
- What should be added to existing checklists?
    

### Deliverables

- Retrospective Report
    
- Lessons Learned
    

### Exit Criteria

- Lessons documented
    
- Skill improvements identified
    

---

# Final Validation

Before closing a feature verify:

- Discovery completed
    
- Design reviewed
    
- Decisions documented
    
- Delivery planned
    
- Tasks sized correctly
    
- Jira created
    
- Implementation validated
    
- Retrospective completed
    
- Lessons captured
    

If any phase was skipped, document why.