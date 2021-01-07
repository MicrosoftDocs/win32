---
description: A thread can suspend and resume the execution of another thread. While a thread is suspended, it is not scheduled for time on the processor.
ms.assetid: b76d7af7-e3ec-4663-a9e7-832c01733c8c
title: Suspending Thread Execution
ms.topic: article
ms.date: 05/31/2018
---

# Suspending Thread Execution

A thread can suspend and resume the execution of another thread. While a thread is suspended, it is not scheduled for time on the processor.

If a thread is created in a suspended state (with the [**CREATE\_SUSPENDED**](process-creation-flags.md) flag), it does not begin to execute until another thread calls the [**ResumeThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-resumethread) function with a handle to the suspended thread. This can be useful for initializing the thread's state before it begins to execute. Suspending a thread at creation can be useful for one-time synchronization, because this ensures that the suspended thread will execute the starting point of its code when you call **ResumeThread**.

The [**SuspendThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-suspendthread) function is not intended to be used for thread synchronization because it does not control the point in the code at which the thread's execution is suspended. This function is primarily designed for use by debuggers.

A thread can temporarily yield its execution for a specified interval by calling the [**Sleep**](/windows/win32/api/synchapi/nf-synchapi-sleep) or [**SleepEx**](/windows/win32/api/synchapi/nf-synchapi-sleepex) functions This is useful particularly in cases where the thread responds to user interaction, because it can delay execution long enough to allow users to observe the results of their actions. During the sleep interval, the thread is not scheduled for time on the processor.

The [**SwitchToThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-switchtothread) function is similar to [**Sleep**](/windows/win32/api/synchapi/nf-synchapi-sleep) and [**SleepEx**](/windows/win32/api/synchapi/nf-synchapi-sleepex), except that you cannot specify the interval. **SwitchToThread** allows the thread to give up its time slice.

 

 
