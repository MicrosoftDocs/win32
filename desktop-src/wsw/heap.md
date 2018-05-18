---
title: Heap
description: A heap tracks a group of allocations that are freed as a unit.
ms.assetid: '3a25284a-8f15-42d4-a292-ece28a08fb69'
keywords: ["Heap Web Services for Windows", "WWSAPI", "WWS"]
---

# Heap

A heap tracks a group of allocations that are freed as a unit.

This allows you to avoid complex patterns of allocating and deallocating memory when you use the WWSAPI.

## 

There is a heap associated with every message. As a message is being sent, or as a message is being received, the heap of the message is used for any allocations relating to that particular message. After a message is sent or received, the heap is reset (which cleans up any allocations related to the particular message).

Heaps can also be used to store message data separately from the lifetime of a message. Many of the API's allow specification of the heap to use when reading data give explicit control over the lifetime of any data read.

Allocations from a heap are guaranteed to be aligned on at least an 8 byte boundary.

Zero byte allocations will return a non-NULL pointer.

In Windows 7, if PageHeap is enabled, a heap returned from HeapCreate is used to manage the memory. In this case, [**WsAlloc**](wsalloc.md) maps directly to HeapAlloc and [**WsResetHeap**](wsresetheap.md) maps to HeapDestroy.

The following enumeration is used with the heap:

-   [**WS\_HEAP\_PROPERTY\_ID**](ws-heap-property-id.md)

The following functions are used with the heap:

-   [**WsAlloc**](wsalloc.md)
-   [**WsCreateHeap**](wscreateheap.md)
-   [**WsFreeHeap**](wsfreeheap.md)
-   [**WsGetHeapProperty**](wsgetheapproperty.md)
-   [**WsResetHeap**](wsresetheap.md)

The following handle is used with the heap:

-   [WS\_HEAP](ws-heap.md)

The following structures are used with the heap:

-   [**WS\_HEAP\_PROPERTIES**](ws-heap-properties.md)
-   [**WS\_HEAP\_PROPERTY**](ws-heap-property.md)

 

 




