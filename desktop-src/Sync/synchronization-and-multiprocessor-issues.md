---
description: Applications may encounter problems when run on multiprocessor systems due to assumptions they make which are valid only on single-processor systems.
ms.assetid: b20a1d2c-b795-4ed8-ac33-539a347020c8
title: Synchronization and Multiprocessor Issues
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization and Multiprocessor Issues

Applications may encounter problems when run on multiprocessor systems due to assumptions they make which are valid only on single-processor systems.

## Thread Priorities

Consider a program with two threads, one with a higher priority than the other. On a single-processor system, the higher priority thread will not relinquish control to the lower priority thread because the scheduler gives preference to higher priority threads. On a multiprocessor system, both threads can run simultaneously, each on its own processor.

Applications should synchronize access to data structures to avoid race conditions. Code that assumes that higher priority threads run without interference from lower priority threads will fail on multiprocessor systems.

## Memory Ordering

When a processor writes to a memory location, the value is cached to improve performance. Similarly, the processor attempts to satisfy read requests from the cache to improve performance. Furthermore, processors begin to fetch values from memory before they are requested by the application. This can happen as part of speculative execution or due to cache line issues.

CPU caches can be partitioned into banks that can be accessed in parallel. This means that memory operations can be completed out of order. To ensure that memory operations are completed in order, most processors provide memory-barrier instructions. A *full memory barrier* ensures that memory read and write operations that appear before the memory barrier instruction are committed to memory before any memory read and write operations that appear after the memory barrier instruction. A *read memory barrier* orders only the memory read operations and a *write memory barrier* orders only the memory write operations. These instructions also ensure that the compiler disables any optimizations that could reorder memory operations across the barriers.

Processors can support instructions for memory barriers with acquire, release, and fence semantics. These semantics describe the order in which results of an operation become available. With acquire semantics, the results of the operation are available before the results of any operation that appears after it in code. With release semantics, the results of the operation are available after the results of any operation that appears before it in code. Fence semantics combine acquire and release semantics. The results of an operation with fence semantics are available before those of any operation that appears after it in code and after those of any operation that appears before it.

On x86 and x64 processors that support SSE2, the instructions are **mfence** (memory fence), **lfence** (load fence), and **sfence** (store fence). On ARM processors, the instrutions are **dmb** and **dsb**. For more information, see the documentation for the processor.

The following synchronization functions use the appropriate barriers to ensure memory ordering:

-   Functions that enter or leave critical sections
-   Functions that acquire or release SRW locks
-   One-time initialization begin and completion
-   **EnterSynchronizationBarrier** function
-   Functions that signal synchronization objects
-   Wait functions
-   Interlocked functions (except functions with _NoFence_ suffix, or intrinsics with _\_nf_ suffix)

## Fixing a Race Condition

The following code has a race condition on a multiprocessor systems because the processor that executes `CacheComputedValue` the first time may write `fValueHasBeenComputed` to main memory before writing `iValue` to main memory. Consequently, a second processor executing `FetchComputedValue` at the same time reads `fValueHasBeenComputed` as **TRUE**, but the new value of `iValue` is still in the first processor's cache and has not been written to memory.

``` syntax
int iValue;
BOOL fValueHasBeenComputed = FALSE;
extern int ComputeValue();

void CacheComputedValue()
{
  if (!fValueHasBeenComputed) 
  {
    iValue = ComputeValue();
    fValueHasBeenComputed = TRUE;
  }
}
 
BOOL FetchComputedValue(int *piResult)
{
  if (fValueHasBeenComputed) 
  {
    *piResult = iValue;
    return TRUE;
  } 

  else return FALSE;
}
```

This race condition above can be repaired by using the **volatile** keyword or the [**InterlockedExchange**](/windows/desktop/api/winnt/nf-winnt-interlockedexchange.md) function to ensure that the value of `iValue` is updated for all processors before the value of `fValueHasBeenComputed` is set to **TRUE**.

Starting Visual Studio 2005, if compiled in **/volatile:ms** mode, the compiler uses acquire semantics for read operations on **volatile** variables and release semantics for write operations on **volatile** variables (when supported by the CPU). Therefore, you can correct the example as follows:

``` syntax
volatile int iValue;
volatile BOOL fValueHasBeenComputed = FALSE;
extern int ComputeValue();

void CacheComputedValue()
{
  if (!fValueHasBeenComputed) 
  {
    iValue = ComputeValue();
    fValueHasBeenComputed = TRUE;
  }
}
 
BOOL FetchComputedValue(int *piResult)
{
  if (fValueHasBeenComputed) 
  {
    *piResult = iValue;
    return TRUE;
  } 

  else return FALSE;
}
```

With Visual Studio 2003, **volatile** to **volatile** references are ordered; the compiler will not re-order **volatile** variable access. However, these operations could be re-ordered by the processor. Therefore, you can correct the example as follows:

``` syntax
int iValue;
BOOL fValueHasBeenComputed = FALSE;
extern int ComputeValue();

void CacheComputedValue()
{
  if (InterlockedCompareExchange((LONG*)&fValueHasBeenComputed, 
          FALSE, FALSE)==FALSE) 
  {
    InterlockedExchange ((LONG*)&iValue, (LONG)ComputeValue());
    InterlockedExchange ((LONG*)&fValueHasBeenComputed, TRUE);
  }
}
 
BOOL FetchComputedValue(int *piResult)
{
  if (InterlockedCompareExchange((LONG*)&fValueHasBeenComputed, 
          TRUE, TRUE)==TRUE) 
  {
    InterlockedExchange((LONG*)piResult, (LONG)iValue);
    return TRUE;
  } 

  else return FALSE;
}
```

## Related topics

<dl> <dt>

[Critical Section Objects](critical-section-objects.md)
</dt> <dt>

[Interlocked Variable Access](interlocked-variable-access.md)
</dt> <dt>

[Wait Functions](wait-functions.md)
</dt> </dl>

 

 



