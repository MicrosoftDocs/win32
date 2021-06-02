---
description: A multitasking operating system divides the available processor time among the processes or threads that need it.
ms.assetid: 'ac45bef6-f078-40ac-95f4-06bd61ff46c4'
title: Multitasking
ms.topic: article
ms.date: 05/31/2018
---

# Multitasking

A multitasking operating system divides the available processor time among the processes or threads that need it. The system is designed for preemptive multitasking; it allocates a processor *time slice* to each thread it executes. The currently executing thread is suspended when its time slice elapses, allowing another thread to run. When the system switches from one thread to another, it saves the context of the preempted thread and restores the saved context of the next thread in the queue.

The length of the time slice depends on the operating system and the processor. Because each time slice is small (approximately 20 milliseconds), multiple threads appear to be executing at the same time. This is actually the case on multiprocessor systems, where the executable threads are distributed among the available processors. However, you must use caution when using multiple threads in an application, because system performance can decrease if there are too many threads.

For more information, see the following topics:

-   [Advantages of Multitasking](advantages-of-multitasking.md)
-   [When to Use Multitasking](when-to-use-multitasking.md)
-   [Multitasking Considerations](multitasking-considerations.md)

 

 



