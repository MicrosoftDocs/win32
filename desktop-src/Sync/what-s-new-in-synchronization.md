---
Description: Windows includes the following new programming elements for synchronization.
ms.assetid: 16cd98d2-adc5-4a14-ad39-a0c5b4cc00cc
title: Whats New in Synchronization
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Synchronization

Windows includes the following new programming elements for synchronization.

## Windows 8

### New Functions

<dl> <dt>

[**DeleteSynchronizationBarrier**](/windows/win32/SynchAPI/nf-synchapi-deletesynchronizationbarrier?branch=master)
</dt> <dd>

Deletes a synchronization barrier.

</dd> <dt>

[**EnterSynchronizationBarrier**](/windows/win32/synchapi/nf-synchapi-entersynchronizationbarrier?branch=master)
</dt> <dd>

Causes the calling thread to wait at a synchronization barrier until the maximum number of threads have entered the barrier.

</dd> <dt>

[**GetOverlappedResultEx**](/windows/win32/Ioapiset/nf-ioapiset-getoverlappedresultex?branch=master)
</dt> <dd>

Retrieves the results of an overlapped operation on the specified file, named pipe, or communications device within the specified time-out interval. The calling thread can perform an alertable wait.

</dd> <dt>

[**InitializeSynchronizationBarrier**](/windows/win32/synchapi/nf-synchapi-entersynchronizationbarrier?branch=master)
</dt> <dd>

Specifies the maximum number of threads and spin count for a new synchronization barrier.

</dd> <dt>

[**WaitOnAddress**](/windows/win32/SynchAPI/nf-synchapi-waitonaddress?branch=master)
</dt> <dd>

Waits for the value at the specified address to change.

</dd> <dt>

[**WakeByAddressAll**](/windows/win32/SynchAPI/nf-synchapi-wakebyaddressall?branch=master)
</dt> <dd>

Wakes all threads that are waiting for the value of an address to change.

</dd> <dt>

[**WakeByAddressSingle**](/windows/win32/SynchAPI/nf-synchapi-wakebyaddresssingle?branch=master)
</dt> <dd>

Wakes one thread that is waiting for the value of an address to change.

</dd> </dl>

### New Interlocked Functions

<dl> <dt>

[**InterlockedAddNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic addition operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAddNoFence64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAndNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic AND operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd8NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic AND operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic AND operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd64NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedBitTestAndComplement64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Tests the specified bit of the specified **LONG64** value and complements it. The operation is atomic.

</dd> <dt>

[**InterlockedBitTestAndResetAcquire**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndResetRelease**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed using memory release semantics.

</dd> <dt>

[**InterlockedBitTestAndSetAcquire**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndSetRelease**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchangeNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange16**](/windows/win32/Winnt/nf-winnt-interlockedcompareexchange16?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchange16Acquire**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16Release**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchangeNoFence64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange128**](/windows/win32/Winnt/nf-winnt-interlockedcompareexchange128?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 128-bit values and exchanges with another 128-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchangePointerNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrement16**](/windows/win32/Winnt/nf-winnt-interlockeddecrement16?branch=master)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedDecrement16Acquire**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16Release**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchange8**](/windows/win32/Winnt/nf-winnt-interlockedexchange8?branch=master)
</dt> <dd>

Sets an 8-bit variable to the specified value as an atomic operation.

</dd> <dt>

[**InterlockedExchange16Acquire**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedExchange16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangePointerNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Atomically exchanges a pair of addresses. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic addition of two 32-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic addition of two 64-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrement16**](/windows/win32/Winnt/nf-winnt-interlockedincrement16?branch=master)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedIncrement16Acquire**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16Release**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using release memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence64**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOrNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic OR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr8NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic OR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic OR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr64NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedPushListSListEx**](/windows/win32/interlockedapi/nf-interlockedapi-interlockedpushlistslistex?branch=master)
</dt> <dd>

Inserts a singly-linked list at the front of another singly linked list. Access to the lists is synchronized on a multiprocessor system. This version of the method does not use the [\_\_fastcall](bb5b9c8a-dfad-450c-9119-0ac2bc59544f) calling convention.

</dd> <dt>

[**InterlockedXorNoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor8NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic XOR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor16NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor64NoFence**](/windows/win32/Winnt/?branch=master)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> </dl>

## Windows 7

### New Functions

<dl> <dt>

[**SetWaitableTimerEx**](/windows/win32/WinBase/nf-synchapi-setwaitabletimerex?branch=master)
</dt> <dd>

Activates the specified waitable timer and provides context information for the timer.

</dd> <dt>

[**TryAcquireSRWLockExclusive**](/windows/win32/WinBase/nf-synchapi-tryacquiresrwlockexclusive?branch=master)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> <dt>

[**TryAcquireSRWLockShared**](/windows/win32/WinBase/nf-synchapi-tryacquiresrwlockshared?branch=master)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> </dl>

### New Structures

<dl> <dt>

[**REASON\_CONTEXT**](base.reason_context)
</dt> <dd>

Contains context information for a timer activated with [**SetWaitableTimerEx**](/windows/win32/WinBase/nf-synchapi-setwaitabletimerex?branch=master).

</dd> </dl>

 

 



