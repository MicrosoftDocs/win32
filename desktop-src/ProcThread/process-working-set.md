---
Description: 'The working set of a program is a collection of those pages in its virtual address space that have been recently referenced.'
ms.assetid: '6017ef59-d2e9-4245-a406-8965024dbb35'
title: Process Working Set
---

# Process Working Set

The *working set* of a program is a collection of those pages in its virtual address space that have been recently referenced. It includes both shared and private data. The shared data includes pages that contain all instructions your application executes, including those in your DLLs and the system DLLs. As the working set size increases, memory demand increases.

A process has an associated minimum working set size and maximum working set size. Each time you call [**CreateProcess**](createprocess.md), it reserves the minimum working set size for the process. The virtual memory manager attempts to keep enough memory for the minimum working set resident when the process is active, but keeps no more than the maximum size.

To get the requested minimum and maximum sizes of the working set for your application, call the [**GetProcessWorkingSetSize**](getprocessworkingsetsize.md) function.

The system sets the default working set sizes. You can also modify the working set sizes using the [**SetProcessWorkingSetSize**](setprocessworkingsetsize.md) function. Setting these values is not a guarantee that the memory will be reserved or resident. Be careful about requesting too large a minimum or maximum working set size, because doing so can degrade system performance.

To obtain the current or peak size of the working set for your process, use the [**GetProcessMemoryInfo**](base.getprocessmemoryinfo) function.

## Related topics

<dl> <dt>

[Memory Performance Information](base.memory_performance_information)
</dt> <dt>

[Working Set](base.working_set)
</dt> </dl>

 

 



