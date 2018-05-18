---
title: Implementing Reference Counting
description: Implementing Reference Counting
ms.assetid: 'd4fd98c9-afa4-4c5c-a3c9-44d34881cbdb'
---

# Implementing Reference Counting

Reference counting requires work on the part of both the implementor of a class and the clients who use objects of that class. When you implement a class, you must implement the [**AddRef**](iunknown-addref.md) and [**Release**](iunknown-release.md) methods as part of the [**IUnknown**](iunknown.md) interface. These two methods have the following simple implementations:

-   [**AddRef**](iunknown-addref.md) increments the object's internal reference count.
-   [**Release**](iunknown-release.md) first decrements the object's internal reference count, and then it checks whether the reference count has fallen to zero. If it has, that means no one is using the object any longer, so the **Release** function deallocates the object.

A common implementation approach for most objects is to have only one implementation of these methods (along with [**QueryInterface**](iunknown-queryinterface.md)), which is shared between all interfaces, and therefore a reference count that applies to the entire object. However, from a client's perspective, reference counting is strictly and clearly a per-interface-pointer notion, and therefore objects that take advantage of this capability by dynamically constructing, destroying, loading, or unloading portions of their functionality based on the currently extant interface pointers may be implemented. These are colloquially called *tear-off interfaces*.

Whenever a client calls a method (or API function), such as [**QueryInterface**](iunknown-queryinterface.md), that returns a new interface pointer, the method being called is responsible for incrementing the reference count through the returned pointer. For example, when a client first creates an object, it receives an interface pointer to an object that, from the client's point of view, has a reference count of one. If the client then calls [**AddRef**](iunknown-addref.md) on the interface pointer, the reference count becomes two. The client must call [**Release**](iunknown-release.md) twice on the interface pointer to drop all of its references to the object.

An example of how reference counts are strictly per-interface-pointer occurs when a client calls [**QueryInterface**](iunknown-queryinterface.md) on the first pointer for either a new interface or the same interface. In either of these cases, the client is required to call [**Release**](iunknown-release.md) once for each pointer. COM does not require that an object return the same pointer when asked for the same interface multiple times. (The only exception to this is a query to [**IUnknown**](iunknown.md), which identifies an object to COM.) This allows the object implementation to manage resources efficiently.

Thread-safety is also an important issue in implementing [**AddRef**](iunknown-addref.md) and [**Release**](iunknown-release.md). For more information, see [Processes, Threads, and Apartments](processes--threads--and-apartments.md).

## Related topics

<dl> <dt>

[Managing Object Lifetimes Through Reference Counting](managing-object-lifetimes-through-reference-counting.md)
</dt> </dl>

 

 




