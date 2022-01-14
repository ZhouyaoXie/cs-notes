Notes on reading *Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and Iterative Development, Third Edition* by Craig Larman.

# Chapter I. Object-Oriented Analysis and Development (OOA/D)

- Most critical skill: responsibility assignment. How should responsibilities be assigned to different software objects?

### Four steps of OOA
1. Define use cases: tell a story.
2. Define a domain model: identify key concepts and their associations (in the real-world problem domain)
3. Assign software object responsibilities and draw interaction diagrams (e.g. a sequence diagram shows a flow of events and how objects interact with each other)
4. Define design class diagrams: a static diagram illustrating attributes and methods of classes

# Chapter II. Iterative, Evolutionary, and Agile 

### Iterative development vs. waterfall

**Iterative development is organized into a series of short, fixed-length mini projects, the outcome of each project being an executable, integrated, tested partial system. **

In contrast, waterfall development involves big design steps before programming.

Iterative development has lower failure rate while waterfall has the highest failure rate. The reason is that software development specifications are highly unstable and constantly changing (studies suggest about 25% specifications are changed), so it is impossible to design everything beforehand.

### Unified Process (UP)

UP is one type of iterative software development process that this book will use. Some elements of UP:
- short timeboxed iterations
- iterative, evolutionary, and adaptive development 
- build high-risk and high-visibility features first
- build a core architecture in early iterations
- constantly engage users for evaluation, testing, feedbacks

##### Phases
- Inception
- Elaboration
- Construction
- Transition

##### Disciplines
A general term for a set of activities and related artifacts in one domain, e.g. business modeling, requirement, design, implementation, etc.

##### Artifacts
A general term for a work product, e.g. code, models, diagrams, documents, etc.

### Risk-driven and client-driven iterative planning

UP encourages a combination of risk-driven and client-driven planning:
- Risk-driven: at each iteration, drive down the highest risks first. This often equivalents to architecture-centric planning, because not having the core architecture is a major risk.
- Client-driven: at each iteration, set the goal to build visible featuers that the client cares the most about.

### Agile

- Agile methods are a (loosely defined) set of methods that encourages agility - rapid and flexible response to change.
- Agile modeling is meant for understanding, not documenting.

# Chapter III. Case Studies

- Case I: NextGen POS system
- Case II: Monopoly game

# Chapter IV. Inception is Not the Requirement Phase

The goal of inception is to align business vision, determine feasibility, and decide whether the project is worth deeper investigation. 
Most use cases should be identified by name, about 10% use cases should be analyzed in detail, but note that they are not expected to be final or correct.
