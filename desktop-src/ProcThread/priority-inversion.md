---
description: Priority inversion occurs when two or more threads with different priorities are in contention to be scheduled.
ms.assetid: 1cb2f3c9-4641-40d8-892c-768abaf6affb
title: Priority Inversion
ms.topic: article
ms.date: 05/31/2018
---

# Priority Inversion

Priority inversion occurs when two or more threads with different priorities are in contention to be scheduled. Consider a simple case with three threads: thread 1, thread 2, and thread 3. Thread 1 is high priority and becomes ready to be scheduled. Thread 2, a low-priority thread, is executing code in a critical section. Thread 1, the high-priority thread, begins waiting for a shared resource from thread 2. Thread 3 has medium priority. Thread 3 receives all the processor time, because the high-priority thread (thread 1) is waiting for shared resources from the low-priority thread (thread 2). Thread 2 will not leave the critical section, because it does not have the highest priority and will not be scheduled.

The scheduler solves this problem by randomly boosting the priority of the ready threads (in this case, the low priority lock-holders). The low priority threads run long enough to exit the critical section, and the high-priority thread can enter the critical section. If the low-priority thread does not get enough CPU time to exit the critical section the first time, it will get another chance during the next round of scheduling.

 

 



