---
description: To avoid race conditions and deadlocks, it is necessary to synchronize access by multiple threads to shared resources. Synchronization is also necessary to ensure that interdependent code is executed in the proper sequence.
ms.assetid: 74af0502-dae1-438c-8e4b-7663093b3fe3
title: Synchronizing Execution of Multiple Threads
ms.topic: article
ms.date: 05/31/2018
---

# Synchronizing Execution of Multiple Threads

To avoid race conditions and deadlocks, it is necessary to synchronize access by multiple threads to shared resources. Synchronization is also necessary to ensure that interdependent code is executed in the proper sequence.

There are a number of objects whose handles can be used to synchronize multiple threads. These objects include:

-   Console input buffers
-   Events
-   Mutexes
-   Processes
-   Semaphores
-   Threads
-   Timers

The state of each of these objects is either signaled or not signaled. When you specify a handle to any of these objects in a call to one of the [wait functions](../sync/wait-functions.md), the execution of the calling thread is blocked until the state of the specified object becomes signaled.

Some of these objects are useful in blocking a thread until some event occurs. For example, a console input buffer handle is signaled when there is unread input, such as a keystroke or mouse button click. Process and thread handles are signaled when the process or thread terminates. This allows a process, for example, to create a child process and then block its own execution until the new process has terminated.

Other objects are useful in protecting shared resources from simultaneous access. For example, multiple threads can each have a handle to a mutex object. Before accessing a shared resource, the threads must call one of the [wait functions](../sync/wait-functions.md) to wait for the state of the mutex to be signaled. When the mutex becomes signaled, only one waiting thread is released to access the resource. The state of the mutex is immediately reset to not signaled so any other waiting threads remain blocked. When the thread is finished with the resource, it must set the state of the mutex to signaled to allow other threads to access the resource.

For the threads of a single process, critical-section objects provide a more efficient means of synchronization than mutexes. A critical section is used like a mutex to enable one thread at a time to use the protected resource. A thread can use the [**EnterCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-entercriticalsection) function to request ownership of a critical section. If it is already owned by another thread, the requesting thread is blocked. A thread can use the [**TryEnterCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-tryentercriticalsection) function to request ownership of a critical section, without blocking upon failure to obtain the critical section. After it receives ownership, the thread is free to use the protected resource. The execution of the other threads of the process is not affected unless they attempt to enter the same critical section.

The [**WaitForInputIdle**](/windows/desktop/api/Winuser/nf-winuser-waitforinputidle) function makes a thread wait until a specified process is initialized and waiting for user input with no input pending. Calling **WaitForInputIdle** can be useful for synchronizing parent and child processes, because [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) returns without waiting for the child process to complete its initialization.

For more information, see [Synchronization](../sync/synchronization.md).

 

 
