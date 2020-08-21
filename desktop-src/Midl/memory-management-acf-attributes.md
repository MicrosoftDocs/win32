---
title: Memory Management ACF Attributes
description: The attributes listed in the following table enable you to perform memory management from the client side.
ms.assetid: ca03c7fe-6649-431b-89dc-5d07a3c8d591
keywords:
- ACF MIDL , attributes, memory management
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management ACF Attributes

The attributes listed in the following table enable you to perform memory management from the client side.



| Attribute                                   | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**allocate**](allocate.md)                | Specifies the way the client application and stub allocate and release memory for pointers. This attribute is particularly useful when you want certain pointer structures to remain accessible to the server application after the remote procedure call returns to the client. You can also use the [**allocate**](allocate.md) attribute to direct the stub to compute the size of all memory referenced through the pointer of the specified type and to make a single call to [**midl\_user\_allocate**](/windows/desktop/Rpc/the-midl-user-allocate-function). |
| [**byte\_count**](byte-count.md)           | Enables you to create a persistent, contiguous block of memory that can be reused over multiple remote procedure calls. This frees the client application from the overhead of repeatedly allocating and releasing memory that may include multiple pointers and other complex data structures.                                                                                                                                                                                                                                                      |
| [**enable\_allocate**](enable-allocate.md) | Specifies that the server stub code should enable the stub memory-management environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



 

 

 