## Why This Matters

Poor service boundaries create long-term coupling, operational complexity, and deployment bottlenecks.

---
## Service Ownership

### Questions

- Which team owns this service?
- Which team owns the data?
- Who is responsible when production incidents occur?
- Can ownership become ambiguous?
### Risks

- Ownership confusion
- Cross-team dependencies
- Escalation delays

### Decisions

- Service owner
- Data owner
- Operational owner
    

---

## Service Boundaries

### Questions

- Does this capability belong in this service?    
- Are we violating bounded contexts?
- Are we introducing business logic duplication?
- Are we creating a distributed monolith?

### Risks

- Tight coupling
- Duplicate business logic
- Excessive cross-service communication

### Decisions

- Responsibility allocation    
- Boundary definition
    

---

## Dependency Management

### Questions

- Which services does this depend on?
- What happens if each dependency fails?
- What happens if a dependency becomes slow?
- Can this service operate in degraded mode?
    

### Risks

- Cascading failures
- Latency amplification
- System-wide outages
    

### Decisions

- Timeout strategy
- Retry strategy    
- Fallback strategy
    

---

## Evolution

### Questions

- Can this service evolve independently?
- Does this change require coordinated deployments?
- How will future consumers be affected?
    

### Risks

- Deployment coupling
- Breaking consumers
    

### Decisions

- Versioning strategy
- Compatibility strategy