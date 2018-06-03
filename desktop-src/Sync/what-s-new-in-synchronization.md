---
Description: Windows includes the following new programming elements for synchronization.
ms.assetid: 16cd98d2-adc5-4a14-ad39-a0c5b4cc00cc
title: What's New in Synchronization
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Synchronization

Windows includes the following new programming elements for synchronization.

## Windows 8

### New Functions

<dl> <dt>

[**DeleteSynchronizationBarrier**](/windows/desktop/api/SynchAPI/nf-synchapi-deletesynchronizationbarrier)
</dt> <dd>

Deletes a synchronization barrier.

</dd> <dt>

[**EnterSynchronizationBarrier**](/windows/desktop/api/synchapi/nf-synchapi-entersynchronizationbarrier)
</dt> <dd>

Causes the calling thread to wait at a synchronization barrier until the maximum number of threads have entered the barrier.

</dd> <dt>

[**GetOverlappedResultEx**](/windows/desktop/api/Ioapiset/nf-ioapiset-getoverlappedresultex)
</dt> <dd>

Retrieves the results of an overlapped operation on the specified file, named pipe, or communications device within the specified time-out interval. The calling thread can perform an alertable wait.

</dd> <dt>

[**InitializeSynchronizationBarrier**](/windows/desktop/api/synchapi/nf-synchapi-entersynchronizationbarrier)
</dt> <dd>

Specifies the maximum number of threads and spin count for a new synchronization barrier.

</dd> <dt>

[**WaitOnAddress**](/windows/desktop/api/SynchAPI/nf-synchapi-waitonaddress)
</dt> <dd>

Waits for the value at the specified address to change.

</dd> <dt>

[**WakeByAddressAll**](/windows/desktop/api/SynchAPI/nf-synchapi-wakebyaddressall)
</dt> <dd>

Wakes all threads that are waiting for the value of an address to change.

</dd> <dt>

[**WakeByAddressSingle**](/windows/desktop/api/SynchAPI/nf-synchapi-wakebyaddresssingle)
</dt> <dd>

Wakes one thread that is waiting for the value of an address to change.

</dd> </dl>

### New Interlocked Functions

<dl> <dt>

[**InterlockedAddNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic addition operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAddNoFence64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAndNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic AND operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd8NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic AND operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic AND operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd64NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedBitTestAndComplement64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Tests the specified bit of the specified **LONG64** value and complements it. The operation is atomic.

</dd> <dt>

[**InterlockedBitTestAndResetAcquire**](/windows/desktop/api/Winnt/)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndResetRelease**](/windows/desktop/api/Winnt/)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed using memory release semantics.

</dd> <dt>

[**InterlockedBitTestAndSetAcquire**](/windows/desktop/api/Winnt/)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndSetRelease**](/windows/desktop/api/Winnt/)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchangeNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange16**](/windows/desktop/api/Winnt/nf-winnt-interlockedcompareexchange16)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchange16Acquire**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16Release**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchangeNoFence64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange128**](/windows/desktop/api/Winnt/nf-winnt-interlockedcompareexchange128)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 128-bit values and exchanges with another 128-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchangePointerNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrement16**](/windows/desktop/api/Winnt/nf-winnt-interlockeddecrement16)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedDecrement16Acquire**](/windows/desktop/api/Winnt/)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16Release**](/windows/desktop/api/Winnt/)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchange8**](/windows/desktop/api/Winnt/nf-winnt-interlockedexchange8)
</dt> <dd>

Sets an 8-bit variable to the specified value as an atomic operation.

</dd> <dt>

[**InterlockedExchange16Acquire**](/windows/desktop/api/Winnt/)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedExchange16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangePointerNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Atomically exchanges a pair of addresses. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic addition of two 32-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic addition of two 64-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrement16**](/windows/desktop/api/Winnt/nf-winnt-interlockedincrement16)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedIncrement16Acquire**](/windows/desktop/api/Winnt/)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16Release**](/windows/desktop/api/Winnt/)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using release memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence64**](/windows/desktop/api/Winnt/)
</dt> <dd>

Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOrNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic OR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr8NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic OR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic OR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr64NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedPushListSListEx**](/windows/desktop/api/interlockedapi/nf-interlockedapi-interlockedpushlistslistex)
</dt> <dd>

Inserts a singly-linked list at the front of another singly linked list. Access to the lists is synchronized on a multiprocessor system. This version of the method does not use the [\_\_fastcall](https://msdn.microsoft.com/windows/desktop/bb5b9c8a-dfad-450c-9119-0ac2bc59544f) calling convention.

</dd> <dt>

[**InterlockedXorNoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor8NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic XOR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor16NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor64NoFence**](/windows/desktop/api/Winnt/)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> </dl>

## Windows 7

### New Functions

<dl> <dt>

[**SetWaitableTimerEx**](/windows/desktop/api/WinBase/nf-synchapi-setwaitabletimerex)
</dt> <dd>

Activates the specified waitable timer and provides context information for the timer.

</dd> <dt>

[**TryAcquireSRWLockExclusive**](/windows/desktop/api/WinBase/nf-synchapi-tryacquiresrwlockexclusive)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> <dt>

[**TryAcquireSRWLockShared**](/windows/desktop/api/WinBase/nf-synchapi-tryacquiresrwlockshared)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> </dl>

### New Structures

<dl> <dt>

[**REASON\_CONTEXT**](https://msdn.microsoft.com/windows/desktop/006bb84f-5e51-4f6e-8a44-6b50e763c5ca)
</dt> <dd>

Contains context information for a timer activated with [**SetWaitableTimerEx**](/windows/desktop/api/WinBase/nf-synchapi-setwaitabletimerex).

</dd> </dl>

 

 



