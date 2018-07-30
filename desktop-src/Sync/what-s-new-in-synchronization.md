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

[**InterlockedAddNoFence**](https://msdn.microsoft.com/en-us/library/Hh972629(v=VS.85).aspx)
</dt> <dd>

Performs an atomic addition operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAddNoFence64**](https://msdn.microsoft.com/en-us/library/Hh972630(v=VS.85).aspx)
</dt> <dd>

Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAndNoFence**](https://msdn.microsoft.com/en-us/library/Hh972634(v=VS.85).aspx)
</dt> <dd>

Performs an atomic AND operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd8NoFence**](https://msdn.microsoft.com/en-us/library/Hh972633(v=VS.85).aspx)
</dt> <dd>

Performs an atomic AND operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972631(v=VS.85).aspx)
</dt> <dd>

Performs an atomic AND operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedAnd64NoFence**](https://msdn.microsoft.com/en-us/library/Hh972632(v=VS.85).aspx)
</dt> <dd>

Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedBitTestAndComplement64**](https://msdn.microsoft.com/en-us/library/Hh972635(v=VS.85).aspx)
</dt> <dd>

Tests the specified bit of the specified **LONG64** value and complements it. The operation is atomic.

</dd> <dt>

[**InterlockedBitTestAndResetAcquire**](https://msdn.microsoft.com/en-us/library/Hh972636(v=VS.85).aspx)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndResetRelease**](https://msdn.microsoft.com/en-us/library/Hh972637(v=VS.85).aspx)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed using memory release semantics.

</dd> <dt>

[**InterlockedBitTestAndSetAcquire**](https://msdn.microsoft.com/en-us/library/Hh972638(v=VS.85).aspx)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedBitTestAndSetRelease**](https://msdn.microsoft.com/en-us/library/Hh972639(v=VS.85).aspx)
</dt> <dd>

Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchangeNoFence**](https://msdn.microsoft.com/en-us/library/Hh972645(v=VS.85).aspx)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange16**](/windows/desktop/api/Winnt/nf-winnt-interlockedcompareexchange16)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchange16Acquire**](https://msdn.microsoft.com/en-us/library/Hh972642(v=VS.85).aspx)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16Release**](https://msdn.microsoft.com/en-us/library/Hh972644(v=VS.85).aspx)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedCompareExchange16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972643(v=VS.85).aspx)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchangeNoFence64**](https://msdn.microsoft.com/en-us/library/Hh972646(v=VS.85).aspx)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedCompareExchange128**](/windows/desktop/api/Winnt/nf-winnt-interlockedcompareexchange128)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 128-bit values and exchanges with another 128-bit value based on the outcome of the comparison.

</dd> <dt>

[**InterlockedCompareExchangePointerNoFence**](https://msdn.microsoft.com/en-us/library/Hh972647(v=VS.85).aspx)
</dt> <dd>

Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence**](https://msdn.microsoft.com/en-us/library/Hh972652(v=VS.85).aspx)
</dt> <dd>

Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrement16**](/windows/desktop/api/Winnt/nf-winnt-interlockeddecrement16)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedDecrement16Acquire**](https://msdn.microsoft.com/en-us/library/Hh972649(v=VS.85).aspx)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16Release**](https://msdn.microsoft.com/en-us/library/Hh972651(v=VS.85).aspx)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with release memory ordering semantics.

</dd> <dt>

[**InterlockedDecrement16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972650(v=VS.85).aspx)
</dt> <dd>

Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedDecrementNoFence64**](https://msdn.microsoft.com/en-us/library/Hh972653(v=VS.85).aspx)
</dt> <dd>

Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence**](https://msdn.microsoft.com/en-us/library/Hh972659(v=VS.85).aspx)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchange8**](/windows/desktop/api/Winnt/nf-winnt-interlockedexchange8)
</dt> <dd>

Sets an 8-bit variable to the specified value as an atomic operation.

</dd> <dt>

[**InterlockedExchange16Acquire**](https://msdn.microsoft.com/en-us/library/Hh972654(v=VS.85).aspx)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedExchange16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972655(v=VS.85).aspx)
</dt> <dd>

Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeNoFence64**](https://msdn.microsoft.com/en-us/library/Hh972660(v=VS.85).aspx)
</dt> <dd>

Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangePointerNoFence**](https://msdn.microsoft.com/en-us/library/Hh972661(v=VS.85).aspx)
</dt> <dd>

Atomically exchanges a pair of addresses. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence**](https://msdn.microsoft.com/en-us/library/Hh972657(v=VS.85).aspx)
</dt> <dd>

Performs an atomic addition of two 32-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedExchangeAddNoFence64**](https://msdn.microsoft.com/en-us/library/Hh972658(v=VS.85).aspx)
</dt> <dd>

Performs an atomic addition of two 64-bit values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence**](https://msdn.microsoft.com/en-us/library/Hh972667(v=VS.85).aspx)
</dt> <dd>

Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrement16**](/windows/desktop/api/Winnt/nf-winnt-interlockedincrement16)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation.

</dd> <dt>

[**InterlockedIncrement16Acquire**](https://msdn.microsoft.com/en-us/library/Hh972663(v=VS.85).aspx)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16Release**](https://msdn.microsoft.com/en-us/library/Hh972665(v=VS.85).aspx)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using release memory ordering semantics.

</dd> <dt>

[**InterlockedIncrement16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972664(v=VS.85).aspx)
</dt> <dd>

Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedIncrementNoFence64**](https://msdn.microsoft.com/en-us/library/Hh972668(v=VS.85).aspx)
</dt> <dd>

Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOrNoFence**](https://msdn.microsoft.com/en-us/library/Hh972672(v=VS.85).aspx)
</dt> <dd>

Performs an atomic OR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr8NoFence**](https://msdn.microsoft.com/en-us/library/Hh972671(v=VS.85).aspx)
</dt> <dd>

Performs an atomic OR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972669(v=VS.85).aspx)
</dt> <dd>

Performs an atomic OR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedOr64NoFence**](https://msdn.microsoft.com/en-us/library/Hh972670(v=VS.85).aspx)
</dt> <dd>

Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedPushListSListEx**](/windows/desktop/api/interlockedapi/nf-interlockedapi-interlockedpushlistslistex)
</dt> <dd>

Inserts a singly-linked list at the front of another singly linked list. Access to the lists is synchronized on a multiprocessor system. This version of the method does not use the [\_\_fastcall](https://msdn.microsoft.com/en-us/library/6xa169sk(v=VS.71).aspx) calling convention.

</dd> <dt>

[**InterlockedXorNoFence**](https://msdn.microsoft.com/en-us/library/Hh972677(v=VS.85).aspx)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor8NoFence**](https://msdn.microsoft.com/en-us/library/Hh972676(v=VS.85).aspx)
</dt> <dd>

Performs an atomic XOR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor16NoFence**](https://msdn.microsoft.com/en-us/library/Hh972674(v=VS.85).aspx)
</dt> <dd>

Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers.

</dd> <dt>

[**InterlockedXor64NoFence**](https://msdn.microsoft.com/en-us/library/Hh972675(v=VS.85).aspx)
</dt> <dd>

Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers.

</dd> </dl>

## Windows 7

### New Functions

<dl> <dt>

[**SetWaitableTimerEx**](https://msdn.microsoft.com/en-us/library/Dd405521(v=VS.85).aspx)
</dt> <dd>

Activates the specified waitable timer and provides context information for the timer.

</dd> <dt>

[**TryAcquireSRWLockExclusive**](https://msdn.microsoft.com/en-us/library/Dd405523(v=VS.85).aspx)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> <dt>

[**TryAcquireSRWLockShared**](https://msdn.microsoft.com/en-us/library/Dd405524(v=VS.85).aspx)
</dt> <dd>

Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.

</dd> </dl>

### New Structures

<dl> <dt>

[**REASON\_CONTEXT**](https://msdn.microsoft.com/en-us/library/Dd405536(v=VS.85).aspx)
</dt> <dd>

Contains context information for a timer activated with [**SetWaitableTimerEx**](https://msdn.microsoft.com/en-us/library/Dd405521(v=VS.85).aspx).

</dd> </dl>

 

 



