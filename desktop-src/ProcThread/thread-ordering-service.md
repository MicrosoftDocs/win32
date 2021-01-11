---
description: The thread ordering service controls the execution of one or more client threads. It ensures that each client thread runs once during the specified period and in relative order.
ms.assetid: 5c37873a-ced4-447e-a6e1-55cfa8ab24b4
title: Thread Ordering Service
ms.topic: article
ms.date: 05/31/2018
---

# Thread Ordering Service

The *thread ordering service* controls the execution of one or more client threads. It ensures that each client thread runs once during the specified period and in relative order.

**Windows Server 2003 and Windows XP:** The thread ordering service is available starting with Windows Vista and Windows Server 2008.

The thread ordering service is off by default and must be started by the user. While the thread ordering service is running, it is activated every 5 seconds to check whether there is a new request, even if the system is idle. This prevents the system from sleeping for longer than 5 seconds, causing the system to consume more power. If energy efficiency is critical to the application, it is better not to use the thread ordering service and instead allow the system scheduler to manage execution of threads.

Each client thread belongs to a *thread ordering group*. The *parent thread* creates one or more thread ordering groups by calling the [**AvRtCreateThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtcreatethreadorderinggroup) function. The parent thread uses this function to specify the period for the thread ordering group and a time-out interval.

Additional client threads call the [**AvRtJoinThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtjointhreadorderinggroup) function to join an existing thread ordering group. These threads indicate whether they are to be a predecessor or successor to the parent thread in the execution order. Each client thread is expected to complete a certain amount of processing each period. All threads within the group should complete their execution within the period plus the time-out interval.

The threads of a thread ordering group enclose their processing code within a loop that is controlled by the [**AvRtWaitOnThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtwaitonthreadorderinggroup) function. First, the predecessor threads are executed one at a time in the order that they joined the group, while the parent and successor threads are blocked on their calls to **AvRtWaitOnThreadOrderingGroup**. When each predecessor thread is finished with its processing, control of execution returns to the top of its processing loop and the thread calls **AvRtWaitOnThreadOrderingGroup** again to block until its next turn. After all predecessor threads have called this function, the thread ordering service can schedule the parent thread. Finally, when the parent thread finishes its processing and calls **AvRtWaitOnThreadOrderingGroup** again, the thread ordering service can schedule the successor threads one at a time in the order that they joined the group. If all threads complete their execution before a period ends, all threads wait until the remainder of the period elapses before any are executed again.

When the client need no longer run as part of the thread ordering group, it calls the [**AvRtLeaveThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtleavethreadorderinggroup) function to remove itself from the group. Note that the parent thread should not remove itself from a thread ordering group. If a thread does not complete its execution before the period plus the time-out interval elapses, then it is deleted from the group.

The parent thread calls the [**AvRtDeleteThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtdeletethreadorderinggroup) function to delete the thread ordering group. The thread ordering group is also destroyed if the parent thread does not complete its execution before the period plus the time-out interval elapses. When the thread ordering group is destroyed, any calls to [**AvRtWaitOnThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtwaitonthreadorderinggroup) from threads of that group fail or time out.

 

 



