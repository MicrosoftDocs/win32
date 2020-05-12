---
title: Interfaces and Interface Implementations
description: COM makes a fundamental distinction between interface definitions and their implementations.
ms.assetid: f50b3e8f-bf87-4525-b47b-96e75b3a05b9
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces and Interface Implementations

COM makes a fundamental distinction between interface definitions and their implementations.

An *interface* is actually a contract that consists of a group of related function prototypes whose usage is defined but whose implementation is not. These function prototypes are equivalent to pure virtual base classes in C++ programming. An interface definition specifies the interface's member functions, called *methods*, their return types, the number and types of their parameters, and what they must do. There is no implementation associated with an interface.

An *interface implementation* is the code a programmer supplies to carry out the actions specified in an interface definition. Implementations of many of the interfaces a programmer can use in an object-based application are included in the COM libraries. However, programmers are free to ignore these implementations and write their own. An interface implementation is to be associated with an object when an instance of that object is created, and the implementation provides the services that the object offers.

For example, a hypothetical interface named IStack might define two methods, named Push and Pop, specifying that successive calls to the Pop method return, in reverse order, values previously passed to the Push method. This interface definition would not specify how the functions are to be implemented in code. In implementing the interface, one programmer might implement the stack as an array and implement the Push and Pop methods in such a way as to access that array, while another programmer might use a linked list and would implement the methods accordingly. Regardless of a particular implementation of the Push and Pop methods, the in-memory representation of a pointer to an IStack interface, and therefore its use by a client, is completely determined by the interface definition.

Simple objects support only a single interface. More complicated objects, such as embeddable objects, typically support several interfaces. Clients have access to a COM object only through a pointer to one of its interfaces, which, in turn, allows the client to call any of the methods that make up that interface. These methods determine how a client can use the object's data.

Interfaces define a contract between an object and its clients. The contract specifies the methods that must be associated with each interface and what the behavior of each of the methods must be in terms of input and output. The contract generally does not define how to implement the methods in an interface. Another important aspect of the contract is that if an object supports an interface, it must support all of that interface's methods in some way. Not all of the methods in an implementation need to do something. If an object does not support the function implied by a method, its implementation may be a simple return or perhaps the return of a meaningful error message—but the methods must exist.

## Related topics

<dl> <dt>

[COM Objects and Interfaces](com-objects-and-interfaces.md)
</dt> </dl>

 

 




