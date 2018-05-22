---
Description: 'The following functions are used in synchronization.'
ms.assetid: '9b6359c2-0113-49b6-83d0-316ad95aba1b'
title: Synchronization Functions
---

# Synchronization Functions

The following functions are used in synchronization.

-   [Asynchronous functions](#asynchronous-functions)
-   [Condition variable and SRW lock functions](#condition-variable-and-srw-lock-functions)
-   [Critical section functions](#critical-section-functions)
-   [Event functions](#event-functions)
-   [One-time initialization functions](#one-time-initialization-functions)
-   [Interlocked Functions](#interlocked-functions)
-   [Mutex functions](#mutex-functions)
-   [Private namespace functions](#private-namespace-functions)
-   [Semaphore functions](#semaphore-functions)
-   [Singly-linked list functions](#singly-linked-list-functions)
-   [Synchronization barrier functions](#synchronization-barrier-functions)
-   [Timer-queue timer functions](#timer-queue-timer-functions)
-   [Wait functions](#wait-functions)
-   [Waitable-timer functions](#waitable-timer-functions)

## Asynchronous functions



| Asynchronous function                                  | Description                                                                                           |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**APCProc**](apcproc.md)                             | An application-defined callback function used with the [**QueueUserAPC**](queueuserapc.md) function. |
| [**GetOverlappedResult**](getoverlappedresult.md)     | Retrieves the results of an overlapped operation.                                                     |
| [**GetOverlappedResultEx**](getoverlappedresultex.md) | Retrieves the results of an overlapped operation within a specified timeout interval.                 |
| [**QueueUserAPC**](queueuserapc.md)                   | Adds a user-mode asynchronous procedure call (APC) object to the APC queue of the specified thread.   |



 

## Condition variable and SRW lock functions



| Condition variable and SRW lock function                           | Description                                                                                                                                       |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireSRWLockExclusive**](acquiresrwlockexclusive.md)         | Acquires a slim reader/writer (SRW) lock in exclusive mode.                                                                                       |
| [**AcquireSRWLockShared**](acquiresrwlockshared.md)               | Acquires a slim reader/writer (SRW) lock in shared mode.                                                                                          |
| [**InitializeConditionVariable**](initializeconditionvariable.md) | Initializes a condition variable.                                                                                                                 |
| [**InitializeSRWLock**](initializesrwlock.md)                     | Initialize a slim reader/writer (SRW) lock.                                                                                                       |
| [**ReleaseSRWLockExclusive**](releasesrwlockexclusive.md)         | Releases a slim reader/writer (SRW) lock that was acquired in exclusive mode.                                                                     |
| [**ReleaseSRWLockShared**](releasesrwlockshared.md)               | Releases a slim reader/writer (SRW) lock that was acquired in shared mode.                                                                        |
| [**SleepConditionVariableCS**](sleepconditionvariablecs.md)       | Sleeps on the specified condition variable and releases the specified critical section as an atomic operation.                                    |
| [**SleepConditionVariableSRW**](sleepconditionvariablesrw.md)     | Sleeps on the specified condition variable and releases the specified lock as an atomic operation.                                                |
| [**TryAcquireSRWLockExclusive**](tryacquiresrwlockexclusive.md)   | Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock. |
| [**TryAcquireSRWLockShared**](tryacquiresrwlockshared.md)         | Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.    |
| [**WakeAllConditionVariable**](wakeallconditionvariable.md)       | Wake all threads waiting on the specified condition variable.                                                                                     |
| [**WakeConditionVariable**](wakeconditionvariable.md)             | Wake a single thread waiting on the specified condition variable.                                                                                 |



 

## Critical section functions



| Critical section function                                                              | Description                                                                             |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**DeleteCriticalSection**](deletecriticalsection.md)                                 | Releases all resources used by an unowned critical section object.                      |
| [**EnterCriticalSection**](entercriticalsection.md)                                   | Waits for ownership of the specified critical section object.                           |
| [**InitializeCriticalSection**](initializecriticalsection.md)                         | Initializes a critical section object.                                                  |
| [**InitializeCriticalSectionAndSpinCount**](initializecriticalsectionandspincount.md) | Initializes a critical section object and sets the spin count for the critical section. |
| [**InitializeCriticalSectionEx**](initializecriticalsectionex.md)                     | Initializes a critical section object with a spin count and optional flags.             |
| [**LeaveCriticalSection**](leavecriticalsection.md)                                   | Releases ownership of the specified critical section object.                            |
| [**SetCriticalSectionSpinCount**](setcriticalsectionspincount.md)                     | Sets the spin count for the specified critical section.                                 |
| [**TryEnterCriticalSection**](tryentercriticalsection.md)                             | Attempts to enter a critical section without blocking.                                  |



 

## Event functions



| Event function                         | Description                                                                                                                                                  |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateEvent**](createevent.md)     | Creates or opens a named or unnamed event object.                                                                                                            |
| [**CreateEventEx**](createeventex.md) | Creates or opens a named or unnamed event object and returns a handle to the object.                                                                         |
| [**OpenEvent**](openevent.md)         | Opens an existing named event object.                                                                                                                        |
| [**PulseEvent**](pulseevent.md)       | Sets the specified event object to the signaled state and then resets it to the nonsignaled state after releasing the appropriate number of waiting threads. |
| [**ResetEvent**](resetevent.md)       | Sets the specified event object to the nonsignaled state.                                                                                                    |
| [**SetEvent**](setevent.md)           | Sets the specified event object to the signaled state.                                                                                                       |



 

## One-time initialization functions



| One-time initialization function                           | Description                                                                                                                                                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InitOnceBeginInitialize**](initoncebegininitialize.md) | Begins one-time initialization.                                                                                                                                                                             |
| [**InitOnceComplete**](initoncecomplete.md)               | Completes one-time initialization.                                                                                                                                                                          |
| [**InitOnceExecuteOnce**](initonceexecuteonce.md)         | Executes the specified function successfully one time. No other threads that specify the same one-time initialization structure can execute this function while it is being executed by the current thread. |
| [**InitOnceInitialize**](initonceinitialize.md)           | Initializes a one-time initialization structure.                                                                                                                                                            |



 

## Interlocked Functions



| Interlocked function                                                                         | Description                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InterlockedAdd**](interlockedadd.md)                                                     | Performs an atomic addition operation on the specified **LONG** values.                                                                                                                                                                                                                   |
| [**InterlockedAddAcquire**](interlockedaddacquire.md)                                       | Performs an atomic addition operation on the specified **LONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                |
| [**InterlockedAddRelease**](interlockedaddrelease.md)                                       | Performs an atomic addition operation on the specified **LONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                |
| [**InterlockedAddNoFence**](interlockedaddnofence.md)                                       | Performs an atomic addition operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                          |
| [**InterlockedAdd64**](interlockedadd64.md)                                                 | Performs an atomic addition operation on the specified **LONGLONG** values.                                                                                                                                                                                                               |
| [**InterlockedAddAcquire64**](interlockedaddacquire64.md)                                   | Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                            |
| [**InterlockedAddRelease64**](interlockedaddrelease64.md)                                   | Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                            |
| [**InterlockedAddNoFence64**](interlockedaddnofence64.md)                                   | Performs an atomic addition operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                      |
| [**InterlockedAnd**](interlockedand.md)                                                     | Performs an atomic AND operation on the specified **LONG** values.                                                                                                                                                                                                                        |
| [**InterlockedAndAcquire**](interlockedandacquire.md)                                       | Performs an atomic AND operation on the specified **LONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                     |
| [**InterlockedAndRelease**](interlockedandrelease.md)                                       | Performs an atomic AND operation on the specified **LONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                     |
| [**InterlockedAndNoFence**](interlockedandnofence.md)                                       | Performs an atomic AND operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                               |
| [**InterlockedAnd8**](interlockedand8.md)                                                   | Performs an atomic AND operation on the specified **char** values.                                                                                                                                                                                                                        |
| [**InterlockedAnd8Acquire**](interlockedand8acquire.md)                                     | Performs an atomic AND operation on the specified **char** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                     |
| [**InterlockedAnd8Release**](interlockedand8release.md)                                     | Performs an atomic AND operation on the specified **char** values. The operation is performed with release memory ordering semantics.                                                                                                                                                     |
| [**InterlockedAnd8NoFence**](interlockedand8nofence.md)                                     | Performs an atomic AND operation on the specified **char** values. The operation is performed atomically, but without using memory barriers                                                                                                                                               |
| [**InterlockedAnd16**](interlockedand16.md)                                                 | Performs an atomic AND operation on the specified **SHORT** values.                                                                                                                                                                                                                       |
| [**InterlockedAnd16Acquire**](interlockedand16acquire.md)                                   | Performs an atomic AND operation on the specified **SHORT** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                    |
| [**InterlockedAnd16Release**](interlockedand16release.md)                                   | Performs an atomic AND operation on the specified **SHORT** values. The operation is performed with release memory ordering semantics.                                                                                                                                                    |
| [**InterlockedAnd16NoFence**](interlockedand16nofence.md)                                   | Performs an atomic AND operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers                                                                                                                                              |
| [**InterlockedAnd64**](interlockedand64.md)                                                 | Performs an atomic AND operation on the specified **LONGLONG** values.                                                                                                                                                                                                                    |
| [**InterlockedAnd64Acquire**](interlockedand64acquire.md)                                   | Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                 |
| [**InterlockedAnd64Release**](interlockedand64release.md)                                   | Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                 |
| [**InterlockedAnd64NoFence**](interlockedand64nofence.md)                                   | Performs an atomic AND operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                           |
| [**InterlockedBitTestAndComplement**](interlockedbittestandcomplement.md)                   | Tests the specified bit of the specified **LONG** value and complements it.                                                                                                                                                                                                               |
| [**InterlockedBitTestAndComplement64**](interlockedbittestandcomplement64.md)               | Tests the specified bit of the specified **LONG64** value and complements it. The operation is atomic                                                                                                                                                                                     |
| [**InterlockedBitTestAndResetAcquire**](interlockedbittestandresetacquire.md)               | Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed with acquire memory ordering semantics                                                                                                                             |
| [**InterlockedBitTestAndResetRelease**](interlockedbittestandresetrelease.md)               | Tests the specified bit of the specified **LONG** value and sets it to 0. The operation is atomic, and it is performed using memory release semantics                                                                                                                                     |
| [**InterlockedBitTestAndSetAcquire**](interlockedbittestandsetacquire.md)                   | Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with acquire memory ordering semantics                                                                                                                             |
| [**InterlockedBitTestAndSetRelease**](interlockedbittestandsetrelease.md)                   | Tests the specified bit of the specified **LONG** value and sets it to 1. The operation is atomic, and it is performed with release memory ordering semantics                                                                                                                             |
| [**InterlockedBitTestAndReset**](interlockedbittestandreset.md)                             | Tests the specified bit of the specified **LONG** value and sets it to 0.                                                                                                                                                                                                                 |
| [**InterlockedBitTestAndReset64**](interlockedbittestandreset64.md)                         | Tests the specified bit of the specified **LONG64** value and sets it to 0.                                                                                                                                                                                                               |
| [**InterlockedBitTestAndSet**](interlockedbittestandset.md)                                 | Tests the specified bit of the specified **LONG** value and sets it to 1.                                                                                                                                                                                                                 |
| [**InterlockedBitTestAndSet64**](interlockedbittestandset.md)                               | Tests the specified bit of the specified **LONG64** value and sets it to 1.                                                                                                                                                                                                               |
| [**InterlockedCompare64Exchange128**](interlockedcompare64exchange128.md)                   | Performs an atomic compare-and-exchange operation on the specified values. The function compares the specified 64-bit values and exchanges with the specified 128-bit value based on the outcome of the comparison.                                                                       |
| [**InterlockedCompare64ExchangeAcquire128**](interlockedcompare64exchangeacquire128.md)     | Performs an atomic compare-and-exchange operation on the specified values. The function compares the specified 64-bit values and exchanges with the specified 128-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics.    |
| [**InterlockedCompare64ExchangeRelease128**](interlockedcompare64exchangerelease128.md)     | Performs an atomic compare-and-exchange operation on the specified values. The function compares the specified 64-bit values and exchanges with the specified 128-bit value based on the outcome of the comparison. The operation is performed with release memory ordering semantics.    |
| [**InterlockedCompareExchange**](interlockedcompareexchange.md)                             | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison.                                                                              |
| [**InterlockedCompareExchangeAcquire**](interlockedcompareexchangeacquire.md)               | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics.           |
| [**InterlockedCompareExchangeRelease**](interlockedcompareexchangerelease.md)               | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics.            |
| [**InterlockedCompareExchangeNoFence**](interlockedcompareexchangenofence.md)               | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 32-bit values and exchanges with another 32-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers     |
| [**InterlockedCompareExchange64**](interlockedcompareexchange64.md)                         | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison.                                                                              |
| [**InterlockedCompareExchangeAcquire64**](interlockedcompareexchangeacquire64.md)           | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The exchange is performed with acquire memory ordering semantics.            |
| [**InterlockedCompareExchangeRelease64**](interlockedcompareexchangerelease64.md)           | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics.            |
| [**InterlockedCompareExchangeNoFence64**](interlockedcompareexchangenofence64.md)           | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 64-bit values and exchanges with another 64-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers     |
| [**InterlockedCompareExchange16**](interlockedcompareexchange16.md)                         | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison                                                                               |
| [**InterlockedCompareExchange16Acquire**](interlockedcompareexchange16acquire.md)           | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics            |
| [**InterlockedCompareExchange16Release**](interlockedcompareexchange16release.md)           | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The exchange is performed with release memory ordering semantics             |
| [**InterlockedCompareExchange16NoFence**](interlockedcompareexchange16nofence.md)           | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 16-bit values and exchanges with another 16-bit value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers     |
| [**InterlockedCompareExchange128**](interlockedcompareexchange128.md)                       | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified 128-bit values and exchanges with another 128-bit value based on the outcome of the comparison                                                                             |
| [**InterlockedCompareExchangePointer**](interlockedcompareexchangepointer.md)               | Performs an atomic compare-and-exchange operation on the specified pointer values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison.                                                                    |
| [**InterlockedCompareExchangePointerAcquire**](interlockedcompareexchangepointeracquire.md) | Performs an atomic compare-and-exchange operation on the specified pointer values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed with acquire memory ordering semantics. |
| [**InterlockedCompareExchangePointerRelease**](interlockedcompareexchangepointerrelease.md) | Performs an atomic compare-and-exchange operation on the specified pointer values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed with release memory ordering semantics. |
| [**InterlockedCompareExchangePointerNoFence**](interlockedcompareexchangepointernofence.md) | Performs an atomic compare-and-exchange operation on the specified values. The function compares two specified pointer values and exchanges with another pointer value based on the outcome of the comparison. The operation is performed atomically, but without using memory barriers   |
| [**InterlockedDecrement**](interlockeddecrement.md)                                         | Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation.                                                                                                                                                                                          |
| [**InterlockedDecrementAcquire**](interlockeddecrementacquire.md)                           | Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics.                                                                                                                       |
| [**InterlockedDecrementRelease**](interlockeddecrementrelease.md)                           | Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed with release memory ordering semantics.                                                                                                                       |
| [**InterlockedDecrementNoFence**](interlockeddecrementnofence.md)                           | Decrements (decreases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                 |
| [**InterlockedDecrement16**](interlockeddecrement16.md)                                     | Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation                                                                                                                                                                                           |
| [**InterlockedDecrement16Acquire**](interlockeddecrement16acquire.md)                       | Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics                                                                                                                        |
| [**InterlockedDecrement16Release**](interlockeddecrement16release.md)                       | Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed with release memory ordering semantics                                                                                                                        |
| [**InterlockedDecrement16NoFence**](interlockeddecrement16nofence.md)                       | Decrements (decreases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                 |
| [**InterlockedDecrement64**](interlockeddecrement64.md)                                     | Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation.                                                                                                                                                                                          |
| [**InterlockedDecrementAcquire64**](interlockeddecrementacquire64.md)                       | Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed with acquire memory ordering semantics.                                                                                                                       |
| [**InterlockedDecrementRelease64**](interlockeddecrementrelease64.md)                       | Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed with release memory ordering semantics.                                                                                                                       |
| [**InterlockedDecrementNoFence64**](interlockeddecrementnofence64.md)                       | Decrements (decreases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                 |
| [**InterlockedExchange**](interlockedexchange.md)                                           | Sets a 32-bit variable to the specified value as an atomic operation.                                                                                                                                                                                                                     |
| [**InterlockedExchangeAcquire**](interlockedexchangeacquire.md)                             | Sets a 32-bit variable to the specified value as an atomic operation. The operation is performed with acquire memory ordering semantics.                                                                                                                                                  |
| [**InterlockedExchangeNoFence**](interlockedexchangenofence.md)                             | Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                                            |
| [**InterlockedExchange8**](interlockedexchange8.md)                                         | Sets an 8-bit variable to the specified value as an atomic operation                                                                                                                                                                                                                      |
| [**InterlockedExchange16**](interlockedexchange16.md)                                       | Sets a 16-bit variable to the specified value as an atomic operation.                                                                                                                                                                                                                     |
| [**InterlockedExchange16Acquire**](interlockedexchange16acquire.md)                         | Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed using acquire memory ordering semantics                                                                                                                                                  |
| [**InterlockedExchange16NoFence**](interlockedexchange16nofence.md)                         | Sets a 16-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                                            |
| [**InterlockedExchange64**](interlockedexchange64.md)                                       | Sets a 64-bit variable to the specified value as an atomic operation.                                                                                                                                                                                                                     |
| [**InterlockedExchangeAcquire64**](interlockedexchangeacquire64.md)                         | Sets a 32-bit variable to the specified value as an atomic operation. The operation is performed with acquire memory ordering semantics.                                                                                                                                                  |
| [**InterlockedExchangeNoFence64**](interlockedexchangenofence64.md)                         | Sets a 64-bit variable to the specified value as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                                            |
| [**InterlockedExchangePointer**](interlockedexchangepointer.md)                             | Atomically exchanges a pair of pointer values.                                                                                                                                                                                                                                            |
| [**InterlockedExchangePointerAcquire**](interlockedexchangepointeracquire.md)               | Atomically exchanges a pair of pointer values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                                         |
| [**InterlockedExchangePointerNoFence**](interlockedexchangepointernofence.md)               | Atomically exchanges a pair of addresses. The operation is performed atomically, but without using memory barriers                                                                                                                                                                        |
| [**InterlockedExchangeSubtract**](interlockedexchangesubtract.md)                           | Performs an atomic subtraction of two values.                                                                                                                                                                                                                                             |
| [**InterlockedExchangeAdd**](interlockedexchangeadd.md)                                     | Performs an atomic addition of two 32-bit values.                                                                                                                                                                                                                                         |
| [**InterlockedExchangeAddAcquire**](interlockedexchangeaddacquire.md)                       | Performs an atomic addition of two 32-bit values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                                      |
| [**InterlockedExchangeAddRelease**](interlockedexchangeaddrelease.md)                       | Performs an atomic addition of two 32-bit values. The operation is performed with release memory ordering semantics.                                                                                                                                                                      |
| [**InterlockedExchangeAddNoFence**](interlockedexchangeaddnofence.md)                       | Performs an atomic addition of two 32-bit values. The operation is performed atomically, but without using memory barriers                                                                                                                                                                |
| [**InterlockedExchangeAdd64**](interlockedexchangeadd64.md)                                 | Performs an atomic addition of two 64-bit values.                                                                                                                                                                                                                                         |
| [**InterlockedExchangeAddAcquire64**](interlockedexchangeaddacquire64.md)                   | Performs an atomic addition of two 64-bit values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                                      |
| [**InterlockedExchangeAddRelease64**](interlockedexchangeaddrelease64.md)                   | Performs an atomic addition of two 64-bit values. The operation is performed with release memory ordering semantics.                                                                                                                                                                      |
| [**InterlockedExchangeAddNoFence64**](interlockedexchangeaddnofence64.md)                   | Performs an atomic addition of two 64-bit values. The operation is performed atomically, but without using memory barriers                                                                                                                                                                |
| [**InterlockedIncrement**](interlockedincrement.md)                                         | Increments (increases by one) the value of the specified 32-bit variable as an atomic operation.                                                                                                                                                                                          |
| [**InterlockedIncrementAcquire**](interlockedincrementacquire.md)                           | Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics.                                                                                                                      |
| [**InterlockedIncrementRelease**](interlockedincrementrelease.md)                           | Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed using release memory ordering semantics.                                                                                                                      |
| [**InterlockedIncrementNoFence**](interlockedincrementnofence.md)                           | Increments (increases by one) the value of the specified 32-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                 |
| [**InterlockedIncrement16**](interlockedincrement16.md)                                     | Increments (increases by one) the value of the specified 16-bit variable as an atomic operation                                                                                                                                                                                           |
| [**InterlockedIncrement16Acquire**](interlockedincrement16acquire.md)                       | Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics                                                                                                                       |
| [**InterlockedIncrement16Release**](interlockedincrement16release.md)                       | Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed using release memory ordering semantics                                                                                                                       |
| [**InterlockedIncrement16NoFence**](interlockedincrement16nofence.md)                       | Increments (increases by one) the value of the specified 16-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                 |
| [**InterlockedIncrement64**](interlockedincrement64.md)                                     | Increments (increases by one) the value of the specified 64-bit variable as an atomic operation.                                                                                                                                                                                          |
| [**InterlockedIncrementAcquire64**](interlockedincrementacquire64.md)                       | Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed using acquire memory ordering semantics.                                                                                                                      |
| [**InterlockedIncrementRelease64**](interlockedincrementrelease64.md)                       | Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed using release memory ordering semantics.                                                                                                                      |
| [**InterlockedIncrementNoFence64**](interlockedincrementnofence64.md)                       | Increments (increases by one) the value of the specified 64-bit variable as an atomic operation. The operation is performed atomically, but without using memory barriers                                                                                                                 |
| [**InterlockedOr**](interlockedor.md)                                                       | Performs an atomic OR operation on the specified **LONG** values.                                                                                                                                                                                                                         |
| [**InterlockedOrAcquire**](interlockedoracquire.md)                                         | Performs an atomic OR operation on the specified **LONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                      |
| [**InterlockedOrRelease**](interlockedorrelease.md)                                         | Performs an atomic OR operation on the specified **LONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                      |
| [**InterlockedOrNoFence**](interlockedornofence.md)                                         | Performs an atomic OR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                                |
| [**InterlockedOr8**](interlockedor8.md)                                                     | Performs an atomic OR operation on the specified **char** values.                                                                                                                                                                                                                         |
| [**InterlockedOr8Acquire**](interlockedor8acquire.md)                                       | Performs an atomic OR operation on the specified **char** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                      |
| [**InterlockedOr8Release**](interlockedor8release.md)                                       | Performs an atomic OR operation on the specified **char** values. The operation is performed with release memory ordering semantics.                                                                                                                                                      |
| [**InterlockedOr8NoFence**](interlockedor8nofence.md)                                       | Performs an atomic OR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers                                                                                                                                                |
| [**InterlockedOr16**](interlockedor16.md)                                                   | Performs an atomic OR operation on the specified **SHORT** values.                                                                                                                                                                                                                        |
| [**InterlockedOr16Acquire**](interlockedor16acquire.md)                                     | Performs an atomic OR operation on the specified **SHORT** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                     |
| [**InterlockedOr16Release**](interlockedor16release.md)                                     | Performs an atomic OR operation on the specified **SHORT** values. The operation is performed with release memory ordering semantics.                                                                                                                                                     |
| [**InterlockedOr16NoFence**](interlockedor16nofence.md)                                     | Performs an atomic OR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers                                                                                                                                               |
| [**InterlockedOr64**](interlockedor64.md)                                                   | Performs an atomic OR operation on the specified **LONGLONG** values.                                                                                                                                                                                                                     |
| [**InterlockedOr64Acquire**](interlockedor64acquire.md)                                     | Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                  |
| [**InterlockedOr64Release**](interlockedor64release.md)                                     | Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                  |
| [**InterlockedOr64NoFence**](interlockedor64nofence.md)                                     | Performs an atomic OR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                            |
| [**InterlockedXor**](interlockedxor.md)                                                     | Performs an atomic XOR operation on the specified **LONG** values.                                                                                                                                                                                                                        |
| [**InterlockedXorAcquire**](interlockedxoracquire.md)                                       | Performs an atomic XOR operation on the specified **LONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                     |
| [**InterlockedXorRelease**](interlockedxorrelease.md)                                       | Performs an atomic XOR operation on the specified **LONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                     |
| [**InterlockedXorNoFence**](interlockedxornofence.md)                                       | Performs an atomic XOR operation on the specified **LONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                               |
| [**InterlockedXor8**](interlockedxor8.md)                                                   | Performs an atomic XOR operation on the specified **char** values.                                                                                                                                                                                                                        |
| [**InterlockedXor8Acquire**](interlockedxor8acquire.md)                                     | Performs an atomic XOR operation on the specified **char** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                     |
| [**InterlockedXor8Release**](interlockedxor8release.md)                                     | Performs an atomic XOR operation on the specified **char** values. The operation is performed with release memory ordering semantics.                                                                                                                                                     |
| [**InterlockedXor8NoFence**](interlockedxor8nofence.md)                                     | Performs an atomic XOR operation on the specified **char** values. The operation is performed atomically, but without using memory barriers                                                                                                                                               |
| [**InterlockedXor16**](interlockedxor16.md)                                                 | Performs an atomic XOR operation on the specified **SHORT** values.                                                                                                                                                                                                                       |
| [**InterlockedXor16Acquire**](interlockedxor16acquire.md)                                   | Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                    |
| [**InterlockedXor16Release**](interlockedxor16release.md)                                   | Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed with release memory ordering semantics.                                                                                                                                                    |
| [**InterlockedXor16NoFence**](interlockedxor16nofence.md)                                   | Performs an atomic XOR operation on the specified **SHORT** values. The operation is performed atomically, but without using memory barriers                                                                                                                                              |
| [**InterlockedXor64**](interlockedxor64.md)                                                 | Performs an atomic XOR operation on the specified **LONGLONG** values.                                                                                                                                                                                                                    |
| [**InterlockedXor64Acquire**](interlockedxor64acquire.md)                                   | Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed with acquire memory ordering semantics.                                                                                                                                                 |
| [**InterlockedXor64Release**](interlockedxor64release.md)                                   | Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed with release memory ordering semantics.                                                                                                                                                 |
| [**InterlockedXor64NoFence**](interlockedxor64nofence.md)                                   | Performs an atomic XOR operation on the specified **LONGLONG** values. The operation is performed atomically, but without using memory barriers                                                                                                                                           |



 

## Mutex functions



| Mutex function                         | Description                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------|
| [**CreateMutex**](createmutex.md)     | Creates or opens a named or unnamed mutex object.                                    |
| [**CreateMutexEx**](createmutexex.md) | Creates or opens a named or unnamed mutex object and returns a handle to the object. |
| [**OpenMutex**](openmutex.md)         | Opens an existing named mutex object.                                                |
| [**ReleaseMutex**](releasemutex.md)   | Releases ownership of the specified mutex object.                                    |



 

## Private namespace functions



| Private namespace function                                                             | Description                                                                         |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**AddSIDToBoundaryDescriptor**](addsidtoboundarydescriptor.md)                       | Adds a new security identifier (SID) to the specified boundary descriptor.          |
| [**AddIntegrityLabelToBoundaryDescriptor**](addintegritylabeltoboundarydescriptor.md) | Adds a new required security identifier (SID) to the specified boundary descriptor. |
| [**ClosePrivateNamespace**](closeprivatenamespace.md)                                 | Closes an open namespace handle.                                                    |
| [**CreateBoundaryDescriptor**](createboundarydescriptor.md)                           | Creates a boundary descriptor.                                                      |
| [**CreatePrivateNamespace**](createprivatenamespace.md)                               | Creates a private namespace.                                                        |
| [**DeleteBoundaryDescriptor**](deleteboundarydescriptor.md)                           | Deletes the specified boundary descriptor.                                          |
| [**OpenPrivateNamespace**](openprivatenamespace.md)                                   | Opens a private namespace.                                                          |



 

## Semaphore functions



| Semaphore function                             | Description                                                                              |
|------------------------------------------------|------------------------------------------------------------------------------------------|
| [**CreateSemaphore**](createsemaphore.md)     | Creates or opens a named or unnamed semaphore object.                                    |
| [**CreateSemaphoreEx**](createsemaphoreex.md) | Creates or opens a named or unnamed semaphore object and returns a handle to the object. |
| [**OpenSemaphore**](opensemaphore.md)         | Opens an existing named semaphore object.                                                |
| [**ReleaseSemaphore**](releasesemaphore.md)   | Increases the count of the specified semaphore object by a specified amount.             |



 

## Singly-linked list functions



| Singly-linked list function                                          | Description                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InitializeSListHead**](initializeslisthead.md)                   | Initializes the head of a singly linked list.                                                                                                                                                                                                                |
| [**InterlockedFlushSList**](interlockedflushslist.md)               | Flushes the entire list of items in a singly linked list.                                                                                                                                                                                                    |
| [**InterlockedPopEntrySList**](interlockedpopentryslist.md)         | Removes an item from the front of a singly linked list.                                                                                                                                                                                                      |
| [**InterlockedPushEntrySList**](interlockedpushentryslist.md)       | Inserts an item at the front of a singly linked list.                                                                                                                                                                                                        |
| [**InterlockedPushListSList**](interlockedpushlistslist.md)         | Inserts a singly-linked list at the front of another singly linked list.                                                                                                                                                                                     |
| [**InterlockedPushListSListEx**](interlockedpushlistslistex.md)     | Inserts a singly-linked list at the front of another singly linked list. Access to the lists is synchronized on a multiprocessor system. This version of the method does not use the [\_\_fastcall](bb5b9c8a-dfad-450c-9119-0ac2bc59544f) calling convention |
| [**QueryDepthSList**](querydepthslist.md)                           | Retrieves the number of entries in the specified singly linked list.                                                                                                                                                                                         |
| [**RtlFirstEntrySList**](rtlfirstentryslist.md)                     | Retrieves the first entry in a singly linked list.                                                                                                                                                                                                           |
| [**RtlInitializeSListHead**](rtlinitializeslisthead.md)             | Initializes the head of a singly linked list. Applications should call [**InitializeSListHead**](initializeslisthead.md) instead.                                                                                                                           |
| [**RtlInterlockedFlushSList**](rtlinterlockedflushslist.md)         | Flushes the entire list of items in a singly linked list. Applications should call [**InterlockedFlushSList**](interlockedflushslist.md) instead.                                                                                                           |
| [**RtlInterlockedPopEntrySList**](rtlinterlockedpopentryslist.md)   | Removes an item from the front of a singly linked list. Applications should call [**InterlockedPopEntrySList**](interlockedpopentryslist.md) instead.                                                                                                       |
| [**RtlInterlockedPushEntrySList**](rtlinterlockedpushentryslist.md) | Inserts an item at the front of a singly linked list. Applications should call [**InterlockedPushEntrySList**](interlockedpushentryslist.md) instead.                                                                                                       |
| [**RtlQueryDepthSList**](rtlquerydepthslist.md)                     | Retrieves the number of entries in the specified singly linked list. Applications should call [**QueryDepthSList**](querydepthslist.md) instead.                                                                                                            |



 

## Synchronization barrier functions



| Synchronization barrier function                                             | Description                                                                                                    |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**DeleteSynchronizationBarrier**](deletesynchronizationbarrier.md)         | Deletes a synchronization barrier.                                                                             |
| [**EnterSynchronizationBarrier**](entersynchronizationbarrier.md)           | Enters a synchronization barrier and waits for the appropriate number of threads to rendezvous at the barrier. |
| [**InitializeSynchronizationBarrier**](initializesynchronizationbarrier.md) | Initializes a new synchronization barrier.                                                                     |



 

## Timer-queue timer functions



| Timer-queue timer function                             | Description                  |
|--------------------------------------------------------|------------------------------|
| [**ChangeTimerQueueTimer**](changetimerqueuetimer.md) | Updates a timer-queue timer. |
| [**CreateTimerQueue**](createtimerqueue.md)           | Creates a queue for timers.  |
| [**CreateTimerQueueTimer**](createtimerqueuetimer.md) | Creates a timer-queue timer. |
| [**DeleteTimerQueue**](deletetimerqueue.md)           | Deletes a timer queue.       |
| [**DeleteTimerQueueEx**](deletetimerqueueex.md)       | Deletes a timer queue.       |
| [**DeleteTimerQueueTimer**](deletetimerqueuetimer.md) | Cancels a timer-queue timer. |



 

## Wait functions



| Wait function                                                      | Description                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsgWaitForMultipleObjects**](msgwaitformultipleobjects.md)     | Waits until one or all of the specified objects are in the signaled state or the time-out interval elapses. The objects can include input event objects.                                                                                                   |
| [**MsgWaitForMultipleObjectsEx**](msgwaitformultipleobjectsex.md) | Waits until one or all of the specified objects are in the signaled state, an I/O completion routine or asynchronous procedure call (APC) is queued to the thread, or the time-out interval elapses. The array of objects can include input event objects. |
| [**RegisterWaitForSingleObject**](registerwaitforsingleobject.md) | Directs a wait thread in the thread pool to wait on the object.                                                                                                                                                                                            |
| [**SignalObjectAndWait**](signalobjectandwait.md)                 | Signals one object and waits on another object as a single operation.                                                                                                                                                                                      |
| [**UnregisterWait**](unregisterwait.md)                           | Cancels a registered wait operation.                                                                                                                                                                                                                       |
| [**UnregisterWaitEx**](unregisterwaitex.md)                       | Cancels a registered wait operation.                                                                                                                                                                                                                       |
| [**WaitForMultipleObjects**](waitformultipleobjects.md)           | Waits until one or all of the specified objects are in the signaled state or the time-out interval elapses.                                                                                                                                                |
| [**WaitForMultipleObjectsEx**](waitformultipleobjectsex.md)       | Waits until one or all of the specified objects are in the signaled state, an I/O completion routine or asynchronous procedure call (APC) is queued to the thread, or the time-out interval elapses.                                                       |
| [**WaitForSingleObject**](waitforsingleobject.md)                 | Waits until the specified object is in the signaled state or the time-out interval elapses.                                                                                                                                                                |
| [**WaitForSingleObjectEx**](waitforsingleobjectex.md)             | Waits until the specified object is in the signaled state, an I/O completion routine or asynchronous procedure call (APC) is queued to the thread, or the time-out interval elapses.                                                                       |
| [**WaitOnAddress**](waitonaddress.md)                             | Waits for the value at the specified address to change.                                                                                                                                                                                                    |
| [**WaitOrTimerCallback**](waitortimercallback.md)                 | An application-defined function that serves as the starting address for a timer callback or a registered wait callback.                                                                                                                                    |
| [**WakeByAddressAll**](wakebyaddressall.md)                       | Wakes all threads waiting for the value of an address to change.                                                                                                                                                                                           |
| [**WakeByAddressSingle**](wakebyaddresssingle.md)                 | Wakes a thread waiting for the value of an address to change.                                                                                                                                                                                              |



 

## Waitable-timer functions



| Waitable-timer function                                | Description                                                                                                       |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**CancelWaitableTimer**](cancelwaitabletimer.md)     | Sets the specified waitable timer to the inactive state.                                                          |
| [**CreateWaitableTimer**](createwaitabletimer.md)     | Creates or opens a waitable timer object.                                                                         |
| [**CreateWaitableTimerEx**](createwaitabletimerex.md) | Creates or opens a waitable timer object and returns a handle to the object.                                      |
| [**OpenWaitableTimer**](openwaitabletimer.md)         | Opens an existing named waitable timer object.                                                                    |
| [**SetWaitableTimer**](setwaitabletimer.md)           | Activates the specified waitable timer.                                                                           |
| [**SetWaitableTimerEx**](setwaitabletimerex.md)       | Activates the specified waitable timer and provides context information for the timer. .                          |
| [**TimerAPCProc**](timerapcproc.md)                   | Application-defined timer completion routine used with the [**SetWaitableTimer**](setwaitabletimer.md) function. |



 

 

 



