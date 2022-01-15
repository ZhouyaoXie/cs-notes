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

# Chapter V. Evolutionary Requirement

**Def. A systematic approach to finding, documenting, organizing, and tracking the changing requirements of a system**

### FURPS+ Model

In UP, requirements can be broadly divided into functional and non-functional and are characterized by the FURPS+ model:
- Functional
- Usability
- Reliability
- Performance
- Supportability
- Implementation, interface, operations, packaging, legal, etc.

### Key Artifacts

- Use-case models (mostly for functional requirements)
- Supplementary specifications (non-functional)
- Glossory (including data dictionary)
- Vision (big idea, business overview)
- Business rules (domain rules)

# Chapter VI. Use Cases

- Use cases are textual stories.
- Terms:
  - Actor
  - Scenerio/Use case instance
- The outcome of a series actions by the actor can be success or failure.

### Use Case Model

- Use case name (start with a verb)
- Level ("user-goal" or "subfunction")
- Primary actor
- Stakeholders and interests (supporting actors and offstage actors): the use case shold satisfies all the stakeholders' interests.
- Preconditions (what must be true on start): not tested within the use case, they are conditions that are assumed to be true.
- Success guarantee/Postconditions (what must be true on successful completion)
- Main success scenario/Basic flow/"happy path" scenario
- Extensions (alternate scenarios of success or failure)
  - Has two parts: the condition and the handling
  - The condition is written as sth. that can be detected by the system or an actor
  - If an extension is too complicated, express as a separate use case
- Special requirements (related non-functional requirements)
- Technology and data variations list (varying I/O methods and data formats): these are constraints that need 
- Frequence of occurrence 
- Open issues

### Guidelines for writing use case models
- Keep UI out, focus on intent
- Investigate the goal of the goal
- Write in black-box style, focus on responsibility, not "how"
