[Reference 1: Python Interview Questions](https://www.edureka.co/blog/interview-questions/python-interview-questions/)
[Reference 2: Python tips](https://book.pythontips.com/en/latest/index.html)

### Key Features

#### Interpreted language

Languages that do not need to be compiled before it is run, e.g. Python, PHP, Ruby.

#### Dynamically typed language

You do not need to declare the type of a variable like you have to do with C or Java.

#### OOP

An object oriented programming language, as opposed to procedure oriented programming. Related concepts: class, object, method, constructor.

##### Inheritence

- Base class (parent class) -> derived class (child class)
- Multiple inheritence: inherit from multiple parent classes 
- Call `mro()` to view the execution order

### Memory management

1. Python private heap space: all Python objects and data structures are stored in a private heap that's managed by Python's memory manager. Programmers do not have access to this private heap.

2. Python has an inbuilt garbage collector that recycles unused memory so that it can be made available to the heap space.

### Important Concepts

#### Namespace

A naming system to make sure that names are unique.

#### PYTHONPATH

An environment variable that is used when importing modules. The interpreter will look for the imported modules in various directories included in PYTHONPATH.

#### Global variables vs. Local variables

Declared outside of a function or in global space vs. declared inside a function

#### Attibutes

- Instance attributes: unique to each object
- Class attributes: unique to each class

#### \*args and \*kwargs

- `*args` for passing in an unknown number of arguments
- `*kwargs` for passing in an unknown number of keyword arguments (dictionary)

#### Dunder methods

- Dunder for "Double Underscores" methods
- Commonly used for [operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)

#### Multithreading

- Dividing a process into multiple threads that share the same address space. While these processes can be ran on different CPUs concurrently to achieve speedups, Python disallows such behavior through its Global Interpreter Lock (GIL). GIL makes sure that only one of the processes can execute at any given time. Actually, GIL adds overhead to the running time, so the total running time could increase due to multithreading.
- Benefits: when a thread is executing a blocking operation, such as reading or writing to file, another thread could be executed first.
- Synchronization: necessary to prevent two threads from accessing shared resources. Python prevents this using a lock mechanism.

### Data Structures

#### List

Mutable, ordered, can hold different data types

#### Array

Mutable, ordered, hold a single data type

#### Tuple

Immutable, ordered, can hold different data types

#### Set

Mutable, orodered, can not store duplicated items

#### Dictionary

Keys must be unique; ordered in Python 3.7

## Numpy

#### Ravel vs. Flatten

`a1 = a.flatten('F')` is the same as `a2 = np.ravel(a)` except that `flatten()` will return a new array while `ravel()` only creates a shallow copy of the array. Thus, changing `a2` will change `a` as well.

#### Squeezing & Expanding

- Reduce array dimensions by dropping axes that are of unit length. E.g. an array of shape (1,4,1,5) becomes shape(4,5) after calling `a = np.squeeze(a)`. You can specify the specific axis to reduce by passing in the `axis` parameter.
- `np.expand_dims(a, axis = 1)` is the opposite operation to `np.squeeze(a, axis = 1)`.

#### Concatenate vs. Stack

- `np.concatenate((arr1, arr2), axis = 0)` requires arrays to have the same shape. The return value has the same dimension as the input arrays.
- `np.stack((arr1, arr2), axis = 0)` requires arrays to have the same shape. The return value will have one more dimension than the input arrays (the new dimension is specified with `axis` parameter).

#### Repeat

`np.repeat(arr, 3, axis = 1)`: repeat each element along axis 1 by 3 times

#### Broadcasting

Makes possible numeric operations between two arrays of different shapes.

## PyTorch Tensors

Similar to numpy arrays except that they can run on GPUs or other hardware accelerators. Their computations can be parallelized to reduce runtime.

- numpy to tensor: `torch.from_numpy(arr)`
- tensor to numpy: `t1.detach().numpy()`
