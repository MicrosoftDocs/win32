---
title: Managing Object Lifetimes Through Reference Counting
description: Managing Object Lifetimes Through Reference Counting
ms.assetid: 7f9da5a9-0435-431c-8f90-56e2e489c431
ms.topic: article
ms.date: 05/31/2018
---

# Managing Object Lifetimes Through Reference Counting

In traditional object systems, the life cycle of objects—that is, the issues surrounding the creation and deletion of objects—is handled implicitly by the language (or the language run time) or explicitly by application programmers.

In an evolving, decentrally constructed system made up of reused components, it is no longer true that any client, or even any programmer, always "knows" how to deal with a component's lifetime. For a client with the right security privileges, it is still relatively easy to create objects through a simple request, but object deletion is another matter entirely. It is not necessarily clear when an object is no longer needed and should be deleted. (Readers familiar with garbage-collected programming environments, such as Java, may disagree; however, Java objects do not span machine or even process boundaries, and therefore the garbage collection is restricted to objects living within a single-process space. In addition, Java forces the use of a single programming language.) Even when the original client is done with the object, it cannot simply shut the object down, because some other client or clients might still have a reference to it.

One way to ensure that an object is no longer needed is to depend entirely on an underlying communication channel to inform the system when all connections to a cross-process or cross-channel object have disappeared. However, schemes that use this method are unacceptable for several reasons. One problem is that it could require a major difference between the cross-process/cross-network programming model and the single-process programming model. In the cross-process/cross-network programming model, the communication system would provide the hooks necessary for object lifetime management, while in the single-process programming model, objects are directly connected without any intervening communications channel. Another problem is that this scheme could also result in a layer of system-provided software that would interfere with component performance in the in-process case. Furthermore, a mechanism based on explicit monitoring would not tend to scale toward many thousands or millions of objects.

COM offers a scalable and distributed approach to this set of problems. Clients tell an object when they are using it and when they are done, and objects delete themselves when they are no longer needed. This approach mandates that all objects count references to themselves. Programming languages such as Java, which inherently have their own lifetime management schemes, such as garbage collection, can use COM's reference counting to implement and use COM objects internally, allowing the programmer to avoid dealing with it.

Just as an application must free memory it has allocated once that memory is no longer in use, a client of an object is responsible for freeing its references to the object when that object is no longer needed. In an object-oriented system, the client can do this only by giving the object an instruction to free itself.

It is important that an object be deallocated when it is no longer being used. The difficulty lies in determining when it is appropriate to deallocate an object. This is easy with automatic variables (those allocated on the stack)—they cannot be used outside the block in which they're declared, so the compiler deallocates them when the end of the block is reached. For COM objects, which are dynamically allocated, it is up to the clients of an object to decide when they no longer need to use the object—especially local or remote objects that might be in use by multiple clients at the same time. The object must wait until all clients are finished with it before freeing itself. Because COM objects are manipulated through interface pointers and can be used by objects in different processes or on other machines, the system cannot keep track of an object's clients.

COM's method of determining when it is appropriate to deallocate an object is manual reference counting. Each object maintains a reference count that tracks how many clients are connected to it - that is, how many pointers exist to any of its interfaces in any client.

For more information, see the following topics:

-   [Implementing Reference Counting](implementing-reference-counting.md)
-   [Rules for Managing Reference Counts](rules-for-managing-reference-counts.md)

## Related topics

<dl> <dt>

[Using and Implementing IUnknown](using-and-implementing-iunknown.md)
</dt> </dl>

 

 




