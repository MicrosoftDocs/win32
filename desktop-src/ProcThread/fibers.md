---
description: A fiber is a unit of execution that must be manually scheduled by the application.
ms.assetid: 6283f56b-23ae-4840-abd0-2478a50c670c
title: Fibers
ms.topic: article
ms.date: 05/31/2018
---

# Fibers

A *fiber* is a unit of execution that must be manually scheduled by the application. Fibers run in the context of the threads that schedule them. Each thread can schedule multiple fibers. In general, fibers do not provide advantages over a well-designed multithreaded application. However, using fibers can make it easier to port applications that were designed to schedule their own threads.

From a system standpoint, a fiber assumes the identity of the thread that runs it. For example, if a fiber accesses [thread local storage](thread-local-storage.md) (TLS), it is accessing the thread local storage of the thread that is running it. In addition, if a fiber calls the [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread) function, the thread that is running it exits. However, a fiber does not have all the same state information associated with it as that associated with a thread. The only state information maintained for a fiber is its stack, a subset of its registers, and the fiber data provided during fiber creation. The saved registers are the set of registers typically preserved across a function call.

Fibers are not preemptively scheduled. You schedule a fiber by switching to it from another fiber. The system still schedules threads to run. When a thread running fibers is preempted, its currently running fiber is preempted but remains selected. The selected fiber runs when its thread runs.

Before scheduling the first fiber, call the [**ConvertThreadToFiber**](/windows/desktop/api/WinBase/nf-winbase-convertthreadtofiber) function to create an area in which to save fiber state information. The calling thread is now the currently executing fiber. The stored state information for this fiber includes the fiber data passed as an argument to **ConvertThreadToFiber**.

The [**CreateFiber**](/windows/desktop/api/WinBase/nf-winbase-createfiber) function is used to create a new fiber from an existing fiber; the call requires the stack size, the starting address, and the fiber data. The starting address is typically a user-supplied function, called the fiber function, that takes one parameter (the fiber data) and does not return a value. If your fiber function returns, the thread running the fiber exits. To execute any fiber created with **CreateFiber**, call the [**SwitchToFiber**](/windows/desktop/api/WinBase/nf-winbase-switchtofiber) function. You can call **SwitchToFiber** with the address of a fiber created by a different thread. To do this, you must have the address returned to the other thread when it called **CreateFiber** and you must use proper synchronization.

A fiber can retrieve the fiber data by calling the [**GetFiberData**](/windows/win32/api/winnt/nf-winnt-getfiberdata) macro. A fiber can retrieve the fiber address at any time by calling the [**GetCurrentFiber**](/windows/win32/api/winnt/nf-winnt-getcurrentfiber) macro.

## Fiber Local Storage

A fiber can use *fiber local storage* (FLS) to create a unique copy of a variable for each fiber. If no fiber switching occurs, FLS acts exactly the same as [thread local storage](thread-local-storage.md). The FLS functions ([**FlsAlloc**](/windows/win32/api/fibersapi/nf-fibersapi-flsalloc), [**FlsFree**](/windows/win32/api/fibersapi/nf-fibersapi-flsfree), [**FlsGetValue**](/windows/win32/api/fibersapi/nf-fibersapi-flsgetvalue), and [**FlsSetValue**](/windows/win32/api/fibersapi/nf-fibersapi-flssetvalue)) manipulate the FLS associated with the current thread. If the thread is executing a fiber and the fiber is switched, the FLS is also switched.

To clean up the data associated with a fiber, call the [**DeleteFiber**](/windows/desktop/api/WinBase/nf-winbase-deletefiber) function. This data includes the stack, a subset of the registers, and the fiber data. If the currently running fiber calls **DeleteFiber**, its thread calls [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread) and terminates. However, if the selected fiber of a thread is deleted by a fiber running in another thread, the thread with the deleted fiber is likely to terminate abnormally because the fiber stack has been freed.

## Related topics

<dl> <dt>

[Using Fibers](using-fibers.md)
</dt> </dl>

 

 
