---
description: User-mode scheduling (UMS) is a lightweight mechanism that applications can use to schedule their own threads.
ms.assetid: f9dd92fe-6d7a-452c-893e-e6df1757e377
title: User-Mode Scheduling
ms.topic: article
ms.date: 05/31/2018
---

# User-Mode Scheduling

> [!WARNING]
> As of Windows 11, user-mode scheduling is not supported. All calls fail with the error `ERROR_NOT_SUPPORTED`.]

User-mode scheduling (UMS) is a lightweight mechanism that applications can use to schedule their own threads. An application can switch between UMS threads in user mode without involving the [system scheduler](scheduling.md) and regain control of the processor if a UMS thread blocks in the kernel. UMS threads differ from [fibers](fibers.md) in that each UMS thread has its own thread context instead of sharing the thread context of a single thread. The ability to switch between threads in user mode makes UMS more efficient than [thread pools](thread-pools.md) for managing large numbers of short-duration work items that require few system calls.

UMS is recommended for applications with high performance requirements that need to efficiently run many threads concurrently on multiprocessor or multicore systems. To take advantage of UMS, an application must implement a scheduler component that manages the application's UMS threads and determines when they should run. Developers should consider whether their application performance requirements justify the work involved in developing such a component. Applications with moderate performance requirements might be better served by allowing the system scheduler to schedule their threads.

UMS is available for 64-bit applications running on 64-bit versions of Windows 7 and Windows Server 2008 R2 through Windows 10 Version 21H2 and Windows Server 2022.
This feature is not available on 32-bit versions of Windows or on Windows 11.

For details, see the following sections:

-   [UMS Scheduler](#ums-scheduler)
-   [UMS Scheduler Thread](#ums-scheduler-thread)
-   [UMS Worker Threads, Thread Contexts, and Completion Lists](#ums-worker-threads-thread-contexts-and-completion-lists)
-   [UMS Scheduler Entry Point Function](#ums-scheduler-entry-point-function)
-   [UMS Thread Execution](#ums-thread-execution)
-   [UMS Best Practices](#ums-best-practices)

## UMS Scheduler

An application's UMS scheduler is responsible for creating, managing, and deleting UMS threads and determining which UMS thread to run. An application's scheduler performs the following tasks:

-   Creates one UMS scheduler thread for each processor on which the application will run UMS worker threads.
-   Creates UMS worker threads to perform the work of the application.
-   Maintains its own ready-thread queue of worker threads that are ready to run, and selects threads to run based on the application's scheduling policies.
-   Creates and monitors one or more completion lists where the system queues threads after they finish processing in the kernel. These include newly created worker threads and threads previously blocked on a system call that become unblocked.
-   Provides a scheduler entry point function to handle notifications from the system. The system calls the entry point function when a scheduler thread is created, a worker thread blocks on a system call, or a worker thread explicitly yields control.
-   Performs cleanup tasks for worker threads that have finished running.
-   Performs an orderly shutdown of the scheduler when requested by the application.

## UMS Scheduler Thread

A UMS scheduler thread is an ordinary thread that has converted itself to UMS by calling the [**EnterUmsSchedulingMode**](/windows/desktop/api/WinBase/nf-winbase-enterumsschedulingmode) function. The system scheduler determines when the UMS scheduler thread runs based on its priority relative to other ready threads. The processor on which the scheduler thread runs is influenced by the thread's affinity, same as for non-UMS threads.

The caller of [**EnterUmsSchedulingMode**](/windows/desktop/api/WinBase/nf-winbase-enterumsschedulingmode) specifies a completion list and a [*UmsSchedulerProc*](/windows/desktop/api/WinNT/nc-winnt-rtl_ums_scheduler_entry_point) entry point function to associate with the UMS scheduler thread. The system calls the specified entry point function when it is finished converting the calling thread to UMS. The scheduler entry point function is responsible for determining the appropriate next action for the specified thread. For more information, see [UMS Scheduler Entry Point Function](#ums-scheduler-entry-point-function) later in this topic.

An application might create one UMS scheduler thread for each processor that will be used to run UMS threads. The application might also set the affinity of each UMS scheduler thread for a specific logical processor, which tends to exclude unrelated threads from running on that processor, effectively reserving it for that scheduler thread. Be aware that setting thread affinity in this way can affect overall system performance by starving other processes that may be running on the system. For more information about thread affinity, see [Multiple Processors](multiple-processors.md).

## UMS Worker Threads, Thread Contexts, and Completion Lists

A UMS worker thread is created by calling [**CreateRemoteThreadEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex) with the PROC\_THREAD\_ATTRIBUTE\_UMS\_THREAD attribute and specifying a UMS thread context and a completion list.

A UMS thread context represents the UMS thread state of a worker thread and is used to identify the worker thread in UMS function calls. It is created by calling [**CreateUmsThreadContext**](/windows/desktop/api/WinBase/nf-winbase-createumsthreadcontext).

A completion list is created by calling the [**CreateUmsCompletionList**](/windows/desktop/api/WinBase/nf-winbase-createumscompletionlist) function. A completion list receives UMS worker threads that have completed execution in the kernel and are ready to run in user mode. Only the system can queue worker threads to a completion list. New UMS worker threads are automatically queued to the completion list specified when the threads were created. Previously blocked worker threads are also queued to the completion list when they are no longer blocked.

Each UMS scheduler thread is associated with a single completion list. However, the same completion list can be associated with any number of UMS scheduler threads, and a scheduler thread can retrieve UMS contexts from any completion list for which it has a pointer.

Each completion list has an associated event that is signaled by the system when it queues one or more worker threads to an empty list. The [**GetUmsCompletionListEvent**](/windows/desktop/api/WinBase/nf-winbase-getumscompletionlistevent) function retrieves a handle to the event for a specified completion list. An application can wait on more than one completion list event along with other events that make sense for the application.

## UMS Scheduler Entry Point Function

An application's scheduler entry point function is implemented as a [*UmsSchedulerProc*](/windows/desktop/api/WinNT/nc-winnt-rtl_ums_scheduler_entry_point) function. The system calls the application's scheduler entry point function at the following times:

-   When a non-UMS thread is converted to a UMS scheduler thread by calling [**EnterUmsSchedulingMode**](/windows/desktop/api/WinBase/nf-winbase-enterumsschedulingmode).
-   When a UMS worker thread calls [**UmsThreadYield**](/windows/desktop/api/WinBase/nf-winbase-umsthreadyield).
-   When a UMS worker thread blocks on a system service such as a system call or a page fault.

The *Reason* parameter of the [*UmsSchedulerProc*](/windows/desktop/api/WinNT/nc-winnt-rtl_ums_scheduler_entry_point) function specifies the reason that the entry point function was called. If the entry point function was called because a new UMS scheduler thread was created, the *SchedulerParam* parameter contains data specified by the caller of [**EnterUmsSchedulingMode**](/windows/desktop/api/WinBase/nf-winbase-enterumsschedulingmode). If the entry point function was called because a UMS worker thread yielded, the *SchedulerParam* parameter contains data specified by the caller of [**UmsThreadYield**](/windows/desktop/api/WinBase/nf-winbase-umsthreadyield). If the entry point function was called because a UMS worker thread blocked in the kernel, the *SchedulerParam* parameter is NULL.

The scheduler entry point function is responsible for determining the appropriate next action for the specified thread. For example, if a worker thread is blocked, the scheduler entry point function might run the next available ready UMS worker thread.

When the scheduler entry point function is called, the application's scheduler should attempt to retrieve all of the items in its associated completion list by calling the [**DequeueUmsCompletionListItems**](/windows/desktop/api/WinBase/nf-winbase-dequeueumscompletionlistitems) function. This function retrieves a list of UMS thread contexts that have finished processing in the kernel and are ready to run in user mode. The application's scheduler should not run UMS threads directly from this list because this can cause unpredictable behavior in the application. Instead, the scheduler should retrieve all UMS thread contexts by calling the [**GetNextUmsListItem**](/windows/desktop/api/WinBase/nf-winbase-getnextumslistitem) function once for each context, insert the UMS thread contexts in the scheduler’s ready thread queue, and only then run UMS threads from the ready thread queue.

If the scheduler does not need to wait on multiple events, it should call [**DequeueUmsCompletionListItems**](/windows/desktop/api/WinBase/nf-winbase-dequeueumscompletionlistitems) with a nonzero timeout parameter so the function waits on the completion list event before returning. If the scheduler does need to wait on multiple completion list events, it should call **DequeueUmsCompletionListItems** with a timeout parameter of zero so the function returns immediately, even if the completion list is empty. In this case, the scheduler can wait explicitly on completion list events, for example, by using [**WaitForMultipleObjects**](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjects).

## UMS Thread Execution

A newly created UMS worker thread is queued to the specified completion list and does not begin running until the application's UMS scheduler selects it to run. This differs from non-UMS threads, which the system scheduler automatically schedules to run unless the caller explicitly creates the thread suspended.

The scheduler runs a worker thread by calling [**ExecuteUmsThread**](/windows/desktop/api/WinBase/nf-winbase-executeumsthread) with the worker thread's UMS context. A UMS worker thread runs until it yields by calling the [**UmsThreadYield**](/windows/desktop/api/WinBase/nf-winbase-umsthreadyield) function, blocks, or terminates.

## UMS Best Practices

Applications that implement UMS should follow these best practices:

-   The underlying structures for UMS thread contexts are managed by the system and should not be modified directly. Instead, use [**QueryUmsThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-queryumsthreadinformation) and [**SetUmsThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-setumsthreadinformation) to retrieve and set information about a UMS worker thread.
-   To help prevent deadlocks, the UMS scheduler thread should not share locks with UMS worker threads. This includes both application-created locks and system locks that are acquired indirectly by operations such as allocating from the heap or loading DLLs. For example, suppose the scheduler runs a UMS worker thread that loads a DLL. The worker thread acquires the loader lock and blocks. The system calls the scheduler entry point function, which then loads a DLL. This causes a deadlock, because the loader lock is already held and cannot be released until the first thread unblocks. To help avoid this problem, delegate work that might share locks with UMS worker threads to a dedicated UMS worker thread or a non-UMS thread.
-   UMS is most efficient when most processing is done in user mode. Whenever possible, avoid making system calls in UMS worker threads.
-   UMS worker threads should not assume the system scheduler is being used. This assumption can have subtle effects; for example, if a thread in the unknown code sets a thread priority or affinity, the UMS scheduler might still override it. Code that assumes the system scheduler is being used may not behave as expected and may break when called by a UMS thread.
-   The system may need to lock the thread context of a UMS worker thread. For example, a kernel-mode asynchronous procedure call (APC) might change the context of the UMS thread, so the thread context must be locked. If the scheduler tries to execute the UMS thread context while it is locked, the call will fail. This behavior is by design, and the scheduler should be designed to retry access to the UMS thread context.

 

 
