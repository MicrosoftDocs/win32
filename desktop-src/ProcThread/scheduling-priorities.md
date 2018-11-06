---
Description: Threads are scheduled to run based on their scheduling priority.
ms.assetid: 8710cd56-6bf3-4317-a1f6-1a159394ce2a
title: Scheduling Priorities
ms.topic: article
ms.date: 05/31/2018
---

# Scheduling Priorities

Threads are scheduled to run based on their *scheduling priority*. Each thread is assigned a scheduling priority. The priority levels range from zero (lowest priority) to 31 (highest priority). Only the zero-page thread can have a priority of zero. (The zero-page thread is a system thread responsible for zeroing any free pages when there are no other threads that need to run.)

The system treats all threads with the same priority as equal. The system assigns time slices in a round-robin fashion to all threads with the highest priority. If none of these threads are ready to run, the system assigns time slices in a round-robin fashion to all threads with the next highest priority. If a higher-priority thread becomes available to run, the system ceases to execute the lower-priority thread (without allowing it to finish using its time slice), and assigns a full time slice to the higher-priority thread. For more information, see [Context Switches](context-switches.md).

The priority of each thread is determined by the following criteria:

-   The priority class of its process
-   The priority level of the thread within the priority class of its process

The priority class and priority level are combined to form the *base priority* of a thread. For information on the dynamic priority of a thread, see [Priority Boosts](priority-boosts.md).

## Priority Class

Each process belongs to one of the following priority classes:<dl> IDLE\_PRIORITY\_CLASS  
BELOW\_NORMAL\_PRIORITY\_CLASS  
NORMAL\_PRIORITY\_CLASS  
ABOVE\_NORMAL\_PRIORITY\_CLASS  
HIGH\_PRIORITY\_CLASS  
REALTIME\_PRIORITY\_CLASS  
</dl>

By default, the priority class of a process is NORMAL\_PRIORITY\_CLASS. Use the [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function to specify the priority class of a child process when you create it. If the calling process is IDLE\_PRIORITY\_CLASS or BELOW\_NORMAL\_PRIORITY\_CLASS, the new process will inherit this class. Use the [**GetPriorityClass**](https://msdn.microsoft.com/en-us/library/ms683211(v=VS.85).aspx) function to determine the current priority class of a process and the [**SetPriorityClass**](https://msdn.microsoft.com/en-us/library/ms686219(v=VS.85).aspx) function to change the priority class of a process.

Processes that monitor the system, such as screen savers or applications that periodically update a display, should use IDLE\_PRIORITY\_CLASS. This prevents the threads of this process, which do not have high priority, from interfering with higher priority threads.

Use HIGH\_PRIORITY\_CLASS with care. If a thread runs at the highest priority level for extended periods, other threads in the system will not get processor time. If several threads are set at high priority at the same time, the threads lose their effectiveness. The high-priority class should be reserved for threads that must respond to time-critical events. If your application performs one task that requires the high-priority class while the rest of its tasks are normal priority, use [**SetPriorityClass**](https://msdn.microsoft.com/en-us/library/ms686219(v=VS.85).aspx) to raise the priority class of the application temporarily; then reduce it after the time-critical task has been completed. Another strategy is to create a high-priority process that has all of its threads blocked most of the time, awakening threads only when critical tasks are needed. The important point is that a high-priority thread should execute for a brief time, and only when it has time-critical work to perform.

You should almost never use REALTIME\_PRIORITY\_CLASS, because this interrupts system threads that manage mouse input, keyboard input, and background disk flushing. This class can be appropriate for applications that "talk" directly to hardware or that perform brief tasks that should have limited interruptions.

## Priority Level

The following are priority levels within each priority class:<dl> THREAD\_PRIORITY\_IDLE  
THREAD\_PRIORITY\_LOWEST  
THREAD\_PRIORITY\_BELOW\_NORMAL  
THREAD\_PRIORITY\_NORMAL  
THREAD\_PRIORITY\_ABOVE\_NORMAL  
THREAD\_PRIORITY\_HIGHEST  
THREAD\_PRIORITY\_TIME\_CRITICAL  
</dl>

All threads are created using THREAD\_PRIORITY\_NORMAL. This means that the thread priority is the same as the process priority class. After you create a thread, use the [**SetThreadPriority**](https://msdn.microsoft.com/en-us/library/ms686277(v=VS.85).aspx) function to adjust its priority relative to other threads in the process.

A typical strategy is to use THREAD\_PRIORITY\_ABOVE\_NORMAL or THREAD\_PRIORITY\_HIGHEST for the process's input thread, to ensure that the application is responsive to the user. Background threads, particularly those that are processor intensive, can be set to THREAD\_PRIORITY\_BELOW\_NORMAL or THREAD\_PRIORITY\_LOWEST, to ensure that they can be preempted when necessary. However, if you have a thread waiting for another thread with a lower priority to complete some task, be sure to block the execution of the waiting high-priority thread. To do this, use a [wait function](https://msdn.microsoft.com/en-us/library/ms687069(v=VS.85).aspx), [critical section](https://msdn.microsoft.com/en-us/library/ms682530(v=VS.85).aspx), or the [**Sleep**](https://msdn.microsoft.com/en-us/library/ms686298(v=VS.85).aspx) function, [**SleepEx**](https://msdn.microsoft.com/en-us/library/ms686307(v=VS.85).aspx), or [**SwitchToThread**](https://msdn.microsoft.com/en-us/library/ms686352(v=VS.85).aspx) function. This is preferable to having the thread execute a loop. Otherwise, the process may become deadlocked, because the thread with lower priority is never scheduled.

To determine the current priority level of a thread, use the [**GetThreadPriority**](https://msdn.microsoft.com/en-us/library/ms683235(v=VS.85).aspx) function.

## Base Priority

The process priority class and thread priority level are combined to form the base priority of each thread.

The following table shows the base priority for combinations of process priority class and thread priority value.



Process priority class

Thread priority level

Base priority

IDLE\_PRIORITY\_CLASS

THREAD\_PRIORITY\_IDLE

1

THREAD\_PRIORITY\_LOWEST

2

THREAD\_PRIORITY\_BELOW\_NORMAL

3

THREAD\_PRIORITY\_NORMAL

4

THREAD\_PRIORITY\_ABOVE\_NORMAL

5

THREAD\_PRIORITY\_HIGHEST

6

THREAD\_PRIORITY\_TIME\_CRITICAL

15

BELOW\_NORMAL\_PRIORITY\_CLASS

THREAD\_PRIORITY\_IDLE

1

THREAD\_PRIORITY\_LOWEST

4

THREAD\_PRIORITY\_BELOW\_NORMAL

5

THREAD\_PRIORITY\_NORMAL

6

THREAD\_PRIORITY\_ABOVE\_NORMAL

7

THREAD\_PRIORITY\_HIGHEST

8

THREAD\_PRIORITY\_TIME\_CRITICAL

15

NORMAL\_PRIORITY\_CLASS

THREAD\_PRIORITY\_IDLE

1

THREAD\_PRIORITY\_LOWEST

6

THREAD\_PRIORITY\_BELOW\_NORMAL

7

THREAD\_PRIORITY\_NORMAL

8

THREAD\_PRIORITY\_ABOVE\_NORMAL

9

THREAD\_PRIORITY\_HIGHEST

10

THREAD\_PRIORITY\_TIME\_CRITICAL

15

ABOVE\_NORMAL\_PRIORITY\_CLASS

THREAD\_PRIORITY\_IDLE

1

THREAD\_PRIORITY\_LOWEST

8

THREAD\_PRIORITY\_BELOW\_NORMAL

9

THREAD\_PRIORITY\_NORMAL

10

THREAD\_PRIORITY\_ABOVE\_NORMAL

11

THREAD\_PRIORITY\_HIGHEST

12

THREAD\_PRIORITY\_TIME\_CRITICAL

15

HIGH\_PRIORITY\_CLASS

THREAD\_PRIORITY\_IDLE

1

THREAD\_PRIORITY\_LOWEST

11

THREAD\_PRIORITY\_BELOW\_NORMAL

12

THREAD\_PRIORITY\_NORMAL

13

THREAD\_PRIORITY\_ABOVE\_NORMAL

14

THREAD\_PRIORITY\_HIGHEST

15

THREAD\_PRIORITY\_TIME\_CRITICAL

15

REALTIME\_PRIORITY\_CLASS

THREAD\_PRIORITY\_IDLE

16

THREAD\_PRIORITY\_LOWEST

22

THREAD\_PRIORITY\_BELOW\_NORMAL

23

THREAD\_PRIORITY\_NORMAL

24

THREAD\_PRIORITY\_ABOVE\_NORMAL

25

THREAD\_PRIORITY\_HIGHEST

26

THREAD\_PRIORITY\_TIME\_CRITICAL

31



 

 

 



