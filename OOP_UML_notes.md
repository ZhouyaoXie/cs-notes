Notes on reading *Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and Iterative Development, Third Edition* by Craig Larman.

[Chapter I. OOA/D](https://github.com/ZhouyaoXie/cs-notes/blob/main/OOP_UML_notes.md#chapter-i-object-oriented-analysis-and-development-ooad)  
[Chapter II. Iterative, Evolutionary, and Agile](https://github.com/ZhouyaoXie/cs-notes/blob/main/OOP_UML_notes.md#chapter-ii-iterative-evolutionary-and-agile)  
[Chapter III. Case Studies](https://github.com/ZhouyaoXie/cs-notes/blob/main/OOP_UML_notes.md#chapter-iii-case-studies)  
[Chapter IV. Inception is Not the Requirement Phase](https://github.com/ZhouyaoXie/cs-notes/blob/main/OOP_UML_notes.md#chapter-iv-inception-is-not-the-requirement-phase)
[Chapter V. Evolutionary Requirement](https://github.com/ZhouyaoXie/cs-notes/blob/main/OOP_UML_notes.md#chapter-v-evolutionary-requirement)
[Chapter VI. Use Cases]()
[Chapter VII. Other Requirements]()
[Chapter IX. Domain Models]()

# Chapter I. Object-Oriented Analysis and Development (OOA/D)

- Most critical skill: responsibility assignment. How should responsibilities be assigned to different software objects?

### Four steps of OOA
1. Define use cases: tell a story.
2. Define a domain model: identify key concepts and their associations (in the real-world problem domain)
3. Assign software object responsibilities and draw interaction diagrams (e.g. a sequence diagram shows a flow of events and how objects interact with each other)
4. Define design class diagrams: a static diagram illustrating attributes and methods of classes

# Chapter II. Iterative, Evolutionary, and Agile 

### Iterative development vs. waterfall

**Iterative development is organized into a series of short, fixed-length mini projects, the outcome of each project being an executable, integrated, tested partial system.**

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

### How to find use cases
1. Choose system boundary (just software, or plus hardware, or plus the user, or plus the entire org?)
2. Find primary actors and goals: brainstorm primary actors first, then find their goals
3. Define use cases: define one use case for each user goal

# Chapter VII. Other Requirements
- **Supplementary specification**: all requirements not captured in the use cases. Including common functionality requirements (e.g. error handling, logging, security, etc.) and non-functional requirements (e.g. UI, performance, hardware and interfaces, business rules, etc.)
- **Vision**: 
  - Summarize the goals and problems of the stackholders at a high level, reveal important non-functional goals
  - Summarize system features, should pass the test "the system does X". A vision should try to have <10 features.
- **Glossary**: definition of certain terms
- **Domain rules**

During inception, vision is written to help decision makers decide if the project is worth continuing. Other requirements start to develop during inception. During elaboration, the vision and other requirements are refined. By construction, major requirements should be stablized. 

# Chapter IX. Domain Models
A visual representation of conceptual classes or real-situation objects in a domain. In UML, a domain model is a set of class diagrams in which no operations are defined. It offers a conceptual perspective, not a software perspective.

### Conceptual classes
- Symbol: name or image representing the class
- Intension: definition of the class
- Extension: set of examples of the class

### Associations
- Association: a relationship between classes that needs to be preserved for some duration
- Avoid adding too many associations
- Verbs like "has" or "uses" are bad association names as they do not enhance meaning of the domain
- There can be more than one associations between two classes
- Multiplicity: how many instances of a class A can be associated with one instance of a class B

### Attributes
- Attributes should be primitive data types such as string, number, enumerations (e.g. size = {small, large}), data, etc. Complex attributes should be modeled as a separate clas with associaton.
- Attributes should be modeled as a new data type class if:
  - it has different sections
  - there are operations associated with it
  - it has other attributes
  - it is a quantity with a unit (e.g. `Money` class with `price` and `amount` attributes)
  - it is an abstraction of one or more types
- Relate two classes with an association, not with an attribute (like a foreign key)

### How to create a domain model
1. find the conceptual classes
  - Determine whether sth. is an attribute or a class: if we do not think of X as a number or text in the real world, X is probably a conceptual class.
  - Description class: if each item instance has a price, sku, ... parameter, there is duplicate data in the model. It is space-inefficient and error-prone.
2. draw them as classes in a UML class diagram
3. add associations and attributes
