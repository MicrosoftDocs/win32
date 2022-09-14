---
description: To synchronize access to a resource, use one of the synchronization objects in one of the wait functions.
ms.assetid: 0930bf12-6d5f-4f2c-914d-53e6e862d3bd
title: About Synchronization
ms.topic: article
ms.date: 05/31/2018
---

# About Synchronization

To synchronize access to a resource, use one of the [synchronization objects](synchronization-objects.md) in one of the [wait functions](wait-functions.md). The state of a synchronization object is either *signaled* or *nonsignaled*. The wait functions allow a thread to block its own execution until a specified nonsignaled object is set to the signaled state. For more information, see [Interprocess Synchronization](interprocess-synchronization.md).

The following are other synchronization mechanisms:

-   [overlapped input and output](synchronization-and-overlapped-input-and-output.md)
-   [asynchronous procedure calls](asynchronous-procedure-calls.md)
-   [critical section objects](critical-section-objects.md)
-   [condition variables](condition-variables.md)
-   [slim reader/writer locks](slim-reader-writer--srw--locks.md)
-   [one-time initialization](one-time-initialization.md)
-   [interlocked variable access](interlocked-variable-access.md)
-   [interlocked singly linked lists](interlocked-singly-linked-lists.md)
-   [timer queues](timer-queues.md)
-   the [**MemoryBarrier**](/windows/win32/api/winnt/nf-winnt-memorybarrier) macro

For additional information on synchronization, see [Synchronization and Multiprocessor Issues](synchronization-and-multiprocessor-issues.md).

 

 
