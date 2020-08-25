---
title: Implementing Reference Counting
description: Implementing Reference Counting
ms.assetid: d4fd98c9-afa4-4c5c-a3c9-44d34881cbdb
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Reference Counting

Reference counting requires work on the part of both the implementor of a class and the clients who use objects of that class. When you implement a class, you must implement the [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) methods as part of the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. These two methods have the following simple implementations:

-   [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) increments the object's internal reference count.
-   [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) first decrements the object's internal reference count, and then it checks whether the reference count has fallen to zero. If it has, that means no one is using the object any longer, so the **Release** function deallocates the object.

A common implementation approach for most objects is to have only one implementation of these methods (along with [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q))), which is shared between all interfaces, and therefore a reference count that applies to the entire object. However, from a client's perspective, reference counting is strictly and clearly a per-interface-pointer notion, and therefore objects that take advantage of this capability by dynamically constructing, destroying, loading, or unloading portions of their functionality based on the currently extant interface pointers may be implemented. These are colloquially called *tear-off interfaces*.

Whenever a client calls a method (or API function), such as [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)), that returns a new interface pointer, the method being called is responsible for incrementing the reference count through the returned pointer. For example, when a client first creates an object, it receives an interface pointer to an object that, from the client's point of view, has a reference count of one. If the client then calls [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) on the interface pointer, the reference count becomes two. The client must call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) twice on the interface pointer to drop all of its references to the object.

An example of how reference counts are strictly per-interface-pointer occurs when a client calls [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) on the first pointer for either a new interface or the same interface. In either of these cases, the client is required to call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) once for each pointer. COM does not require that an object return the same pointer when asked for the same interface multiple times. (The only exception to this is a query to [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown), which identifies an object to COM.) This allows the object implementation to manage resources efficiently.

Thread-safety is also an important issue in implementing [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release). For more information, see [Processes, Threads, and Apartments](processes--threads--and-apartments.md).

## Related topics

<dl> <dt>

[Managing Object Lifetimes Through Reference Counting](managing-object-lifetimes-through-reference-counting.md)
</dt> </dl>

 

 