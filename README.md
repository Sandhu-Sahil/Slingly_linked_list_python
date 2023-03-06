# Singly Linked List in Python using Classes

This repository contains a Python implementation of a singly linked list using classes. 

## Introduction

A singly linked list is a data structure consisting of a sequence of nodes, where each node contains a value and a reference (link) to the next node in the sequence. The first node is called the head, and the last node is called the tail. 

In this implementation, we have defined a `Node` class that represents a node in the linked list, and a `LinkedList` class that represents the linked list itself. 

## Installation

1. Clone the repository
2. Navigate to the project directory

## Usage

Create a new linked list:
```python
my_list = LinkedList()
```

Add a new node to the list:
```
my_list.add_node(5)
```

Traverse the list:
```
my_list.traverse()
```

Delete a node from the list:
```
my_list.delete_node(5)
```

## Classes

### Node
Represents a node in the linked list.

#### Properties:
- `data`: The value of the node.
- `next_node`: A reference to the next node in the list.

#### Methods:
- `__init__(self, data)`: Initializes a new instance of the `Node` class.

### LinkedList
Represents a singly linked list.

#### Properties:
- `head`: The first node in the list.
- `size`: The number of nodes in the list.

#### Methods:
- `__init__(self)`: Initializes a new instance of the `LinkedList` class.
- `add_node(self, data)`: Adds a new node with the specified value to the end of the list.
- `delete_node(self, data)`: Deletes the first node with the specified value from the list.
- `traverse(self)`: Traverses the list and prints the value of each node.

## Conclusion

This project provides a basic implementation of a singly linked list in Python using classes. You can customize and extend the implementation based on your specific requirements.
