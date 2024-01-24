---
description: A synchronization barrier enables multiple threads to wait until all threads have all reached a particular point of execution before any thread continues.
ms.assetid: 3A76E6F7-C38B-4843-9496-36F3C78B700C
title: Synchronization Barriers
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Barriers

A synchronization barrier enables multiple threads to wait until all threads have all reached a particular point of execution before any thread continues. Synchronization barriers cannot be shared across processes.

Synchronization barriers are useful for phased computations, in which threads executing the same code in parallel must all complete one phase before moving on to the next.

To create a synchronization barrier, call the [**InitializeSynchronizationBarrier**](/windows/desktop/api/SynchAPI/nf-synchapi-initializesynchronizationbarrier) function and specify a maximum number of threads and how many times a thread should spin before it blocks. Then launch the threads that will use the barrier. After each thread finishes its work, it calls [**EnterSynchronizationBarrier**](/windows/desktop/api/synchapi/nf-synchapi-entersynchronizationbarrier) to wait at the barrier. The **EnterSynchronizationBarrier** function blocks each thread until the number of threads blocked in the barrier reaches the maximum thread count for the barrier, at which point **EnterSynchronizationBarrier** unblocks all the threads. The **EnterSynchronizationBarrier** function returns **TRUE** for exactly one of the threads that entered the barrier, and returns **FALSE** for all other threads.

To release a synchronization barrier when it is no longer needed, call [**DeleteSynchronizationBarrier**](/windows/desktop/api/SynchAPI/nf-synchapi-deletesynchronizationbarrier). It is safe to call this function immediately after calling [**EnterSynchronizationBarrier**](/windows/desktop/api/synchapi/nf-synchapi-entersynchronizationbarrier) because that function ensures that all threads have finished using the barrier before it is released.

If a synchronization barrier will never be deleted, threads can specify the **SYNCHRONIZATION\_BARRIER\_FLAGS\_NO\_DELETE** flag when they enter the barrier. All threads using the barrier must specify this flag; if any thread does not, the flag is ignored. This flag causes the function to skip the extra work required for deletion safety, which can improve performance. Note that deleting a barrier while this flag is in effect may result in an invalid handle access and one or more permanently blocked threads.

 

 



