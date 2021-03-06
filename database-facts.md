### Hive

[Reference](https://medium.com/plumbersofdatascience/hive-architecture-in-depth-ba44e8946cbc)

An ETL and data warehousing tool built on top of Hadoop. Its main architecture has four components:

- Hadoop core components
  - HDFS (Hadoop Distributed File System): data is internally stored under HDFS paths when loaded into Hive
  - MapReduce: where queries are run
- Metastore: a namespace for tables
- Driver: parses the query, generates an exection plan with the help of metastore, converts the queries into equivalent MapReduce jobs by converting or compiling a Java class and building a jar and executing the jar file
  - Parser
  - Planner
  - Execution
  - Optimizer
- Hive client: provides the interface that users interact with
