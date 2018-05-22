---
Description: 'A thread can suspend and resume the execution of another thread. While a thread is suspended, it is not scheduled for time on the processor.'
ms.assetid: 'b76d7af7-e3ec-4663-a9e7-832c01733c8c'
title: Suspending Thread Execution
---

# Suspending Thread Execution

A thread can suspend and resume the execution of another thread. While a thread is suspended, it is not scheduled for time on the processor.

If a thread is created in a suspended state (with the [**CREATE\_SUSPENDED**](process-creation-flags.md) flag), it does not begin to execute until another thread calls the [**ResumeThread**](resumethread.md) function with a handle to the suspended thread. This can be useful for initializing the thread's state before it begins to execute. Suspending a thread at creation can be useful for one-time synchronization, because this ensures that the suspended thread will execute the starting point of its code when you call **ResumeThread**.

The [**SuspendThread**](suspendthread.md) function is not intended to be used for thread synchronization because it does not control the point in the code at which the thread's execution is suspended. This function is primarily designed for use by debuggers.

A thread can temporarily yield its execution for a specified interval by calling the [**Sleep**](sleep.md) or [**SleepEx**](sleepex.md) functions This is useful particularly in cases where the thread responds to user interaction, because it can delay execution long enough to allow users to observe the results of their actions. During the sleep interval, the thread is not scheduled for time on the processor.

The [**SwitchToThread**](switchtothread.md) function is similar to [**Sleep**](sleep.md) and [**SleepEx**](sleepex.md), except that you cannot specify the interval. **SwitchToThread** allows the thread to give up its time slice.

 

 



