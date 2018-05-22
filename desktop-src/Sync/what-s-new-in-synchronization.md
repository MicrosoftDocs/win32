---
Description: 'Windows includes the following new programming elements for synchronization.'
ms.assetid: '16cd98d2-adc5-4a14-ad39-a0c5b4cc00cc'
title: 'What''s New in Synchronization'
---

# What's New in Synchronization

Windows includes the following new programming elements for synchronization.

## Windows 8

### New Functions

<dl> <dt>

[**DeleteSynchronizationBarrier**](deletesynchronizationbarrier.md)
</dt> <dd>

Deletes a synchronization barrier.

</dd> <dt>

[**EnterSynchronizationBarrier**](entersynchronizationbarrier.md)
</dt> <dd>

Causes the calling thread to wait at a synchronization barrier until the maximum number of threads have entered the barrier.

</dd> <dt>

[**GetOverlappedResultEx**](getoverlappedresultex.md)
</dt> <dd>

Retrieves the results of an overlapped operation on the specified file, named pipe, or communications device within the specified time-out interval. The calling thread can perform an alertable wait.

</dd> <dt>

[**InitializeSynchronizationBarrier**](entersynchronizationbarrier.md)
</dt> <dd>

Specifies the maximum number of threads and spin count for a new synchronization barrier.

</dd> <dt>

[**WaitOnAddress**](waitonaddress.md)
</dt> <dd>

Waits for the value at the specified address to change.

</dd> <dt>

[**WakeByAddressAll**](wakebyaddressall.md)
</dt> <dd>

Wakes all threads that are waiting for the value of an address to change.

</dd> <dt>

[**WakeByAddressSingle**](wakebyaddresssingle.md)
</dt> <dd>

Wakes one thread that is waiting for the value of an address to change.

</dd> </dl>

### New Interlocked Functions

<dl> <dt>

[**InterlockedAddNoFence**](interlockedaddnofence.md)
</dt> <dd>

Performs an atomic addition operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAddNoFence64**](interlockedaddnofence64.md)
</dt> <dd>

Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAndNoFence**](interlockedandnofence.md)
</dt> <dd>

Performs an atomic AND operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd8NoFence**](interlockedand8nofence.md)
</dt> <dd>

Performs an atomic AND operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd16NoFence**](interlockedand16nofence.md)
</dt> <dd>

Performs an atomic AND operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd64NoFence**](interlockedand64nofence.md)
</dt> <dd>

Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedBitTestAndComplement64**](interlockedbittestandcomplement64.md)
</dt> <dd>

Tests the specified bit of the specified **LONG64** value and complements it. The operation is atomic.

</dd> <dt>

[**InterlockedBitTestAndResetAcquire**](interlockedbittestandresetacquire.md)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndResetRelease**](interlockedbittestandresetrelease.md)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed using memory release semantics.

</dd> <dt>

[**InterlockedBitTestAndSetAcquire**](interlockedbittestandsetacquire.md)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndSetRelease**](interlockedbittestandsetrelease.md)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchangeNoFence**](interlockedcompareexchangenofence.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange16**](interlockedcompareexchange16.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchange16Acquire**](interlockedcompareexchange16acquire.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16Release**](interlockedcompareexchange16release.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16NoFence**](interlockedcompareexchange16nofence.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchangeNoFence64**](interlockedcompareexchangenofence64.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange128**](interlockedcompareexchange128.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 128-bit values and exchanges with another 128-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchangePointerNoFence**](interlockedcompareexchangepointernofence.md)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence**](interlockeddecrementnofence.md)
</dt> <dd>

Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrement16**](interlockeddecrement16.md)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedDecrement16Acquire**](interlockeddecrement16acquire.md)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16Release**](interlockeddecrement16release.md)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16NoFence**](interlockeddecrement16nofence.md)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence64**](interlockeddecrementnofence64.md)
</dt> <dd>

Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence**](interlockedexchangenofence.md)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchange8**](interlockedexchange8.md)
</dt> <dd>

Sets an 8-bit variable to the specified value as an atomic operation.

</dd> <dt>

[**InterlockedExchange16Acquire**](interlockedexchange16acquire.md)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedExchange16NoFence**](interlockedexchange16nofence.md)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence64**](interlockedexchangenofence64.md)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangePointerNoFence**](interlockedexchangepointernofence.md)
</dt> <dd>

Atomically exchanges a pair of addresses. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence**](interlockedexchangeaddnofence.md)
</dt> <dd>

Performs an atomic addition of two 32-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence64**](interlockedexchangeaddnofence64.md)
</dt> <dd>

Performs an atomic addition of two 64-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence**](interlockedincrementnofence.md)
</dt> <dd>

Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrement16**](interlockedincrement16.md)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedIncrement16Acquire**](interlockedincrement16acquire.md)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16Release**](interlockedincrement16release.md)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using release memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16NoFence**](interlockedincrement16nofence.md)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence64**](interlockedincrementnofence64.md)
</dt> <dd>

Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOrNoFence**](interlockedornofence.md)
</dt> <dd>

Performs an atomic OR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr8NoFence**](interlockedor8nofence.md)
</dt> <dd>

Performs an atomic OR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr16NoFence**](interlockedor16nofence.md)
</dt> <dd>

Performs an atomic OR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr64NoFence**](interlockedor64nofence.md)
</dt> <dd>

Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedPushListSListEx**](interlockedpushlistslistex.md)
</dt> <dd>

Inserts a singly-linked list at the front of another singly linked list. Access to the lists is synchronized on a multiprocessor system. This version of the method does not use the [\_\_fastcall](bb5b9c8a-dfad-450c-9119-0ac2bc59544f) calling convention.

</dd> <dt>

[**InterlockedXorNoFence**](interlockedxornofence.md)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor8NoFence**](interlockedxor8nofence.md)
</dt> <dd>

Performs an atomic XOR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor16NoFence**](interlockedxor16nofence.md)
</dt> <dd>

Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor64NoFence**](interlockedxor64nofence.md)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> </dl>

## Windows 7

### New Functions

<dl> <dt>

[**SetWaitableTimerEx**](setwaitabletimerex.md)
</dt> <dd>

Activates the specified waitable timer and provides context information for the timer.

</dd> <dt>

[**TryAcquireSRWLockExclusive**](tryacquiresrwlockexclusive.md)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> <dt>

[**TryAcquireSRWLockShared**](tryacquiresrwlockshared.md)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> </dl>

### New Structures

<dl> <dt>

[**REASON\_CONTEXT**](base.reason_context)
</dt> <dd>

Contains context information for a timer activated with [**SetWaitableTimerEx**](setwaitabletimerex.md).

</dd> </dl>

 

 



