---
title: Interface Pointers and Interfaces
description: Interface Pointers and Interfaces
ms.assetid: 8a8671fe-f0b2-4698-8c98-89753fffce0b
ms.topic: article
ms.date: 05/31/2018
---

# Interface Pointers and Interfaces

An instance of an interface implementation is actually a pointer to an array of pointers to methods - that is, a function table that refers to an implementation of all of the methods specified in the interface. Objects with multiple interfaces can provide pointers to more than one function table. Any code that has a pointer through which it can access the array can call the methods in that interface.

Speaking precisely about this multiple indirection is inconvenient, so instead, the pointer to the interface function table that another object must have to call its methods is called simply an *interface pointer*. You can manually create function tables in a C application or almost automatically by using Visual C++ (or other object-oriented languages that support COM).

With appropriate compiler support (which is inherent in C and C++), a client can call an interface method through its name, not its position in the array. Because an interface is a type, the compiler, given the names of methods, can check the types of parameters and return values of each interface method call. In contrast, if a client uses a position-based calling scheme, such type-checking is not available, even in C or C++.

Each interface is an immutable contract of a functional group of methods. You reference an interface at run time with a globally unique interface identifier (IID). This IID, which is a specific instance of a globally unique identifier (GUID) supported by COM, allows a client to ask an object precisely whether it supports the semantics of the interface, without unnecessary overhead and without the confusion that could arise in a system from having multiple versions of the same interface with the same name.

To summarize, it is important to understand what a COM interface is, and is not:

-   A COM interface is not the same as a C++ class. The pure virtual definition carries no implementation. If you are a C++ programmer, you can define your implementation of an interface as a class, but this falls under the heading of implementation details, which COM does not specify. An instance of an object that implements an interface must be created for the interface actually to exist. Furthermore, different object classes may implement an interface differently yet be used interchangeably in binary form, as long as the behavior conforms to the interface definition.
-   A COM interface is not an object. It is simply a related group of functions and is the binary standard through which clients and objects communicate. As long as it can provide pointers to interface methods, the object can be implemented in any language with any internal state representation.
-   COM interfaces are strongly typed. Every interface has its own interface identifier (a GUID), which eliminates the possibility of duplication that could occur with any other naming scheme.
-   COM interfaces are immutable. You cannot define a new version of an old interface and give it the same identifier. Adding or removing methods of an interface or changing semantics creates a new interface, not a new version of an old interface. Therefore, a new interface cannot conflict with an old interface. However, objects can support multiple interfaces simultaneously and can expose interfaces that are successive revisions of an interface, with different identifiers. Thus, each interface is a separate contract, and systemwide objects need not be concerned about whether the version of the interface they are calling is the one they expect. The interface ID (IID) defines the interface contract explicitly and uniquely.

## Related topics

<dl> <dt>

[COM Objects and Interfaces](com-objects-and-interfaces.md)
</dt> </dl>

 

 




