---
description: 'Computers with multiple processors are typically designed for one of two architectures: non-uniform memory access (NUMA) or symmetric multiprocessing (SMP).'
ms.assetid: 3c9186c8-a54d-4536-8237-bfff78cc7d11
title: Multiple Processors
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Processors

Computers with multiple processors are typically designed for one of two architectures: non-uniform memory access (NUMA) or symmetric multiprocessing (SMP).

In a NUMA computer, each processor is closer to some parts of memory than others, making memory access faster for some parts of memory than other parts. Under the NUMA model, the system attempts to schedule threads on processors that are close to the memory being used. For more information about NUMA, see [NUMA Support](numa-support.md).

In an SMP computer, two or more identical processors or cores connect to a single shared main memory. Under the SMP model, any thread can be assigned to any processor. Therefore, scheduling threads on an SMP computer is similar to scheduling threads on a computer with a single processor. However, the scheduler has a pool of processors, so that it can schedule threads to run concurrently. Scheduling is still determined by thread priority, but it can be influenced by setting thread affinity and thread ideal processor, as discussed in this topic.

## Thread Affinity

*Thread affinity* forces a thread to run on a specific subset of processors. Setting thread affinity should generally be avoided, because it can interfere with the scheduler's ability to schedule threads effectively across processors. This can decrease the performance gains produced by parallel processing. An appropriate use of thread affinity is testing each processor.

The system represents affinity with a bitmask called a processor affinity mask. The affinity mask is the size of the maximum number of processors in the system, with bits set to identify a subset of processors. Initially, the system determines the subset of processors in the mask.

You can obtain the current thread affinity for all threads of the process by calling the [**GetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-getprocessaffinitymask) function. Use the [**SetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setprocessaffinitymask) function to specify thread affinity for all threads of the process. To set the thread affinity for a single thread, use the [**SetThreadAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setthreadaffinitymask) function. The thread affinity must be a subset of the process affinity.

On systems with more than 64 processors, the affinity mask initially represents processors in a single processor group. However, thread affinity can be set to a processor in a different group, which alters the affinity mask for the process. For more information, see [Processor Groups](processor-groups.md).

## Thread Ideal Processor

When you specify a *thread ideal processor*, the scheduler runs the thread on the specified processor when possible. Use the [**SetThreadIdealProcessor**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessor) function to specify a preferred processor for a thread. This does not guarantee that the ideal processor will be chosen but provides a useful hint to the scheduler. On systems with more than 64 processors, you can use the [**SetThreadIdealProcessorEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessorex) function to specify a preferred processor in a specific processor group.

## Related topics

<dl> <dt>

[NUMA Support](numa-support.md)
</dt> <dt>

[Processor Groups](processor-groups.md)
</dt> </dl>

 

 
