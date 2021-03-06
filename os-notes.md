
## Processes

### Processes

A running program

- Address space: the memory that the program can address. Stores instructions and data.
- Registers: many programs explicitly read and update registers.
	- Program counter (PC): which instruction to execute next?
	- Stack pointer 
	- Frame pointer
- I/O information
	- A list of files that the program currently has open


### Mechanism vs. Policy

Mechanisms are low-level methods or protocols that implement a needed piece of functionality. 

- Time-sharing mechanism: a CPU is used by one process for a given amount of time, then to another process, and so forth.
- Space-sharing mechanism: a resource (e.g. disk space) is divided and shared by multiple programs.

Policies are algorithms for making decisions in the OS.

- Scheduling policy: a CPU decides which program to run among a list of programs based on some sort of intelligence.x

### Process Creation

0. Create entry for process list
1. Load code and static data into memory from disk or flash-based SSD
2. Allocate memory for stack
3. Allocate memory for heap
4. Initialize file I/O 
5. Start the process by running main()

### Process States

- Running
- Ready to run
- Blocked

Different actions could transition from one state to another. E.g. blocked --> file I/O --> Ready.

### Data Structures

- Process list: a data structure that stores information about all processes in the OS
- Process control block (PCB): a data structure that stores info about individual processes

### The Process API in UNIX

#### fork()

- Create a copy of the exact process 
- Everything is the same except for the PID returned by the call: parent get the PID of the child, child get 0
- Indeterministic: parent and child run simultaneously on the CPU, so we don't know which will be executed first. This is determined by the CPU scheduler.

#### wait()

Wait for the child process to run and exit before continuing the parent process.

#### exec()

- Overwrites the current code segment with the code and static data from the new program
- Re-initialize stack and heap memory
- Never returns if successful

### Process Control in UNIX

Users/superusers can control processes by sending signals to cause jobs to stop, continue, or terminate. Each user can only control its own recourses, while a superuser (root) can control all processes.


## Limited Direct Execution (LDE) Protocol

#### User mode vs. Kernel mode

- The OS runs in the kernel mode, which can execute all privileged operations and restricted instructions.
- Code that runs in user mode is restricted in what operations it can execute. To perform restricted instructions, it performs a system call.

#### System Call

A program calls a special trap instruction to perform a system call.

1. CPU: save registers and PCs to **kernel stack** (a stack to store program state so that later we could pick up where we've left)
2. CPU: move to kernel mode
3. CPU: jump to **trap handler** (a place, whose address is known by CPU but not the user, that tells the OS which code to run. Initialized during booting)
4. OS: handle trap, run code
5. OS: execute return-from-trap
6. CPU: restore registers and PCs from kernel stack
7. CPU: move to user mode
8. CPU: jump to PC after trap
9. Program: resume execution
