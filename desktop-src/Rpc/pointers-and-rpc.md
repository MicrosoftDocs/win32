---
title: Pointers and RPC
description: It is very efficient to use pointers as C-function parameters.
ms.assetid: 5792bd45-9c2a-4dd2-b050-17082fd0c929
ms.topic: article
ms.date: 05/31/2018
---

# Pointers and RPC

It is very efficient to use pointers as C-function parameters. The pointer costs only a few bytes and can be used to access a large amount of memory. However, in a distributed application, the client and server procedures reside in different address spaces—they can be on different computers. Therefore, the client and the server usually do not have access to the same memory space.

When one of the remote procedure's parameters is a pointer to an object, the client must transmit a copy of that object and its pointer to the server. If the remote procedure modifies the object through its pointer, the server returns the pointer and its modified copy.

MIDL offers pointer attributes to minimize the amount of required overhead and the size of your application. This section discusses the purpose and uses of MIDL pointer attributes. It also presents information on pointer handling in RPC applications. It is divided into the following topics:

-   [Kinds of Pointers](kinds-of-pointers.md)
-   [Pointers and Memory Allocation](pointers-and-memory-allocation.md)
-   [Default Pointer Types](default-pointer-types.md)
-   [Pointer-Attribute Type Inheritance](pointer-attribute-type-inheritance.md)

 

 




