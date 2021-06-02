---
description: The scheduler maintains a queue of executable threads for each priority level.
ms.assetid: 82463d71-9cef-4608-b997-25dc9c1e1c0a
title: Context Switches
ms.topic: article
ms.date: 05/31/2018
---

# Context Switches

The scheduler maintains a queue of executable threads for each priority level. These are known as *ready threads*. When a processor becomes available, the system performs a *context switch*. The steps in a context switch are:

1.  Save the context of the thread that just finished executing.
2.  Place the thread that just finished executing at the end of the queue for its priority.
3.  Find the highest priority queue that contains ready threads.
4.  Remove the thread at the head of the queue, load its context, and execute it.

The following classes of threads are not ready threads.

-   Threads created with the CREATE\_SUSPENDED flag
-   Threads halted during execution with the [**SuspendThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-suspendthread) or [**SwitchToThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-switchtothread) function
-   Threads waiting for a synchronization object or input.

Until threads that are suspended or blocked become ready to run, the scheduler does not allocate any processor time to them, regardless of their priority.

The most common reasons for a context switch are:

-   The time slice has elapsed.
-   A thread with a higher priority has become ready to run.
-   A running thread needs to wait.

When a running thread needs to wait, it relinquishes the remainder of its time slice.

 

 
