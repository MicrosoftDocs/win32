---
description: Wait functions allow a thread to block its own execution.
ms.assetid: 9c66c71d-fdfd-42ae-895c-2fc842b5bc7a
title: Wait Functions
ms.topic: article
ms.date: 06/25/2020
---

# Wait Functions

*Wait functions* allow a thread to block its own execution. The wait functions do not return until the specified criteria have been met. The type of wait function determines the set of criteria used. When a wait function is called, it checks whether the wait criteria have been met. If the criteria have not been met, the calling thread enters the wait state until the conditions of the wait criteria have been met or the specified time-out interval elapses.

-   [Single-object Wait Functions](#single-object-wait-functions)
-   [Multiple-object Wait Functions](#multiple-object-wait-functions)
-   [Alertable Wait Functions](#alertable-wait-functions)
-   [Registered Wait Functions](#registered-wait-functions)
-   [Waiting on an Address](#waiting-on-an-address)
-   [Wait Functions and Time-out Intervals](#wait-functions-and-time-out-intervals)
-   [Wait Functions and Synchronization Objects](#wait-functions-and-synchronization-objects)
-   [Wait Functions and Creating Windows](#wait-functions-and-creating-windows)

## Single-object Wait Functions

The [**SignalObjectAndWait**](/windows/win32/api/synchapi/nf-synchapi-signalobjectandwait), [**WaitForSingleObject**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject), and [**WaitForSingleObjectEx**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex) functions require a handle to one synchronization object. These functions return when one of the following occurs:

-   The specified object is in the signaled state.
-   The time-out interval elapses. The time-out interval can be set to **INFINITE** to specify that the wait will not time out.

The [**SignalObjectAndWait**](/windows/win32/api/synchapi/nf-synchapi-signalobjectandwait) function enables the calling thread to atomically set the state of an object to signaled and wait for the state of another object to be set to signaled.

## Multiple-object Wait Functions

The [**WaitForMultipleObjects**](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjects), [**WaitForMultipleObjectsEx**](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjectsex), [**MsgWaitForMultipleObjects**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjects), and [**MsgWaitForMultipleObjectsEx**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjectsex) functions enable the calling thread to specify an array containing one or more synchronization object handles. These functions return when one of the following occurs:

-   The state of any one of the specified objects is set to signaled or the states of all objects have been set to signaled. You control whether one or all of the states will be used in the function call.
-   The time-out interval elapses. The time-out interval can be set to **INFINITE** to specify that the wait will not time out.

The [**MsgWaitForMultipleObjects**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjects) and [**MsgWaitForMultipleObjectsEx**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjectsex) function allow you to specify input event objects in the object handle array. This is done when you specify the type of input to wait for in the thread's input queue. For example, a thread could use **MsgWaitForMultipleObjects** to block its execution until the state of a specified object has been set to signaled and there is mouse input available in the thread's input queue. The thread can use the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) or [**PeekMessageA**](/windows/win32/api/winuser/nf-winuser-peekmessagea) or [**PeekMessageW**](/windows/win32/api/winuser/nf-winuser-peekmessagew) function to retrieve the input.

When waiting for the states of all objects to be set to signaled, these multiple-object functions do not modify the states of the specified objects until the states of all objects have been set signaled. For example, the state of a mutex object can be signaled, but the calling thread does not get ownership until the states of the other objects specified in the array have also been set to signaled. In the meantime, some other thread may get ownership of the mutex object, thereby setting its state to nonsignaled.

When waiting for the state of a single object to be set to signaled, these multiple-object functions check the handles in the array in order starting with index 0, until one of the objects is signaled. If multiple objects become signaled, the function returns the index of the first handle in the array whose object was signaled.

## Alertable Wait Functions

The [**MsgWaitForMultipleObjectsEx**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjectsex), [**SignalObjectAndWait**](/windows/win32/api/synchapi/nf-synchapi-signalobjectandwait), [**WaitForMultipleObjectsEx**](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjectsex), and [**WaitForSingleObjectEx**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex) functions differ from the other wait functions in that they can optionally perform an *alertable wait operation*. In an alertable wait operation, the function can return when the specified conditions are met, but it can also return if the system queues an I/O completion routine or an APC for execution by the waiting thread. For more information about alertable wait operations and I/O completion routines, see [Synchronization and Overlapped Input and Output](synchronization-and-overlapped-input-and-output.md). For more information about APCs, see [Asynchronous Procedure Calls](asynchronous-procedure-calls.md).

## Registered Wait Functions

The [**RegisterWaitForSingleObject**](/windows/desktop/api/WinBase/nf-winbase-registerwaitforsingleobject) function differs from the other wait functions in that the wait operation is performed by a thread from the [thread pool](../procthread/thread-pooling.md). When the specified conditions are met, the callback function is executed by a worker thread from the thread pool.

By default, a registered wait operation is a multiple-wait operation. The system resets the timer every time the event is signaled (or the time-out interval elapses) until you call the [**UnregisterWaitEx**](unregisterwaitex.md) function to cancel the operation. To specify that a wait operation should be executed only once, set the *dwFlags* parameter of [**RegisterWaitForSingleObject**](/windows/desktop/api/WinBase/nf-winbase-registerwaitforsingleobject) to **WT\_EXECUTEONLYONCE**.

If the thread calls functions that use APCs, set the *dwFlags* parameter of [**RegisterWaitForSingleObject**](/windows/desktop/api/WinBase/nf-winbase-registerwaitforsingleobject) to **WT\_EXECUTEINPERSISTENTTHREAD**.

## Waiting on an Address

A thread can use the [**WaitOnAddress**](/windows/desktop/api/SynchAPI/nf-synchapi-waitonaddress) function to wait for the value of a target address to change from some undesired value to any other value. This enables threads to wait for a value to change without having to spin or handle the synchronization problems that can arise when the thread captures an undesired value but the value changes before the thread can wait.

[**WaitOnAddress**](/windows/desktop/api/SynchAPI/nf-synchapi-waitonaddress) returns when code that modifies the target value signals the change by calling [**WakeByAddressSingle**](/windows/desktop/api/SynchAPI/nf-synchapi-wakebyaddresssingle) to wake a single waiting thread or [**WakeByAddressAll**](/windows/desktop/api/SynchAPI/nf-synchapi-wakebyaddressall) to wake all waiting threads. If a time-out interval is specified with **WaitOnAddress** and no thread calls a wake function, the function returns when the time-out interval elapses. If no time-out interval is specified, the thread waits indefinitely.

## Wait Functions and Time-out Intervals

The accuracy of the specified time-out interval depends on the resolution of the system clock. The system clock "ticks" at a constant rate. If the time-out interval is less than the resolution of the system clock, the wait may time out in less than the specified length of time. If the time-out interval is greater than one tick but less than two, the wait can be anywhere between one and two ticks, and so on.

To increase the accuracy of the time-out interval for the wait functions, call the **timeGetDevCaps** function to determine the supported minimum timer resolution and the **timeBeginPeriod** function to set the timer resolution to its minimum. Use caution when calling **timeBeginPeriod**, as frequent calls can significantly affect the system clock, system power usage, and the scheduler. If you call **timeBeginPeriod**, call it one time early in the application and be sure to call the **timeEndPeriod** function at the very end of the application.

## Wait Functions and Synchronization Objects

The wait functions can modify the states of some types of [synchronization objects](synchronization-objects.md). Modification occurs only for the object or objects whose signaled state caused the function to return. Wait functions can modify the states of synchronization objects as follows:

-   The count of a semaphore object decreases by one, and the state of the semaphore is set to nonsignaled if its count is zero.
-   The states of mutex, auto-reset event, and change-notification objects are set to nonsignaled.
-   The state of a synchronization timer is set to nonsignaled.
-   The states of manual-reset event, manual-reset timer, process, thread, and console input objects are not affected by a wait function.

## Wait Functions and Creating Windows

You have to be careful when using the wait functions and code that directly or indirectly creates windows. If a thread creates any windows, it must process messages. Message broadcasts are sent to all windows in the system. If you have a thread that uses a wait function with no time-out interval, the system will deadlock. Two examples of code that indirectly creates windows are DDE and the **CoInitialize** function. Therefore, if you have a thread that creates windows, use [**MsgWaitForMultipleObjects**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjects) or [**MsgWaitForMultipleObjectsEx**](/windows/desktop/api/Winuser/nf-winuser-msgwaitformultipleobjectsex), rather than the other wait functions.

 

 
