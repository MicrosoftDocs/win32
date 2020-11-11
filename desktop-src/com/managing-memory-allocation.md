---
title: Managing Memory Allocation
description: Managing Memory Allocation
ms.assetid: 8a189fe8-5555-44bb-968b-04408fa7fce4
ms.topic: article
ms.date: 05/31/2018
---

# Managing Memory Allocation

In COM, many, if not most, interface methods are called by code written by one programming organization and implemented by code written by another. Many of the parameters and return values of these functions are of types that can be passed around by value. Sometimes, however, it is necessary to pass data structures for which this is not the case, so it is necessary for both caller and called to have a compatible allocation and de-allocation policy. COM defines a universal convention for memory allocation, because it is more reasonable than defining case-by-case rules and so that the COM remote procedure call implementation can correctly manage memory.

The methods of a COM interface always provide memory management of pointers to the interface by calling the [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) functions found in the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface, from which all other COM interfaces derive. (See [Rules for Managing Reference Counts](rules-for-managing-reference-counts.md) for more information.)

This section describes only how to allocate memory for parameters that are not passed by value — not pointers to interfaces, but more mundane things like strings, pointers to structures, and so forth.

For more information, see the following topics:

-   [The OLE Memory Allocator](the-ole-memory-allocator.md)
-   [Memory Management Rules](memory-management-rules.md)
-   [Debugging Memory Allocations](debugging-memory-allocations.md)

 

 