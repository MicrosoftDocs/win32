---
description: The traditional model for multiprocessor support is symmetric multiprocessor (SMP). In this model, each processor has equal access to memory and I/O. As more processors are added, the processor bus becomes a limitation for system performance.
ms.assetid: a1263968-2b26-45cc-bdd7-6aa354821a5a
title: NUMA Support
ms.topic: article
ms.date: 05/31/2018
---

# NUMA Support

The traditional model for multiprocessor support is symmetric multiprocessor (SMP). In this model, each processor has equal access to memory and I/O. As more processors are added, the processor bus becomes a limitation for system performance.

System designers use non-uniform memory access (NUMA) to increase processor speed without increasing the load on the processor bus. The architecture is non-uniform because each processor is close to some parts of memory and farther from other parts of memory. The processor quickly gains access to the memory it is close to, while it can take longer to gain access to memory that is farther away.

In a NUMA system, CPUs are arranged in smaller systems called *nodes*. Each node has its own processors and memory, and is connected to the larger system through a cache-coherent interconnect bus.

The system attempts to improve performance by scheduling threads on processors that are in the same node as the memory being used. It attempts to satisfy memory-allocation requests from within the node, but will allocate memory from other nodes if necessary. It also provides an API to make the topology of the system available to applications. You can improve the performance of your applications by using the NUMA functions to optimize scheduling and memory usage.

First of all, you will need to determine the layout of nodes in the system. To retrieve the highest numbered node in the system, use the [**GetNumaHighestNodeNumber**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumahighestnodenumber) function. Note that this number is not guaranteed to equal the total number of nodes in the system. Also, nodes with sequential numbers are not guaranteed to be close together. To retrieve the list of processors on the system, use the [**GetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-getprocessaffinitymask) function. You can determine the node for each processor in the list by using the [**GetNumaProcessorNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornode) function. Alternatively, to retrieve a list of all processors in a node, use the [**GetNumaNodeProcessorMask**](/windows/desktop/api/WinBase/nf-winbase-getnumanodeprocessormask) function.

After you have determined which processors belong to which nodes, you can optimize your application's performance. To ensure that all threads for your process run on the same node, use the [**SetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setprocessaffinitymask) function with a process affinity mask that specifies processors in the same node. This increases the efficiency of applications whose threads need to access the same memory. Alternatively, to limit the number of threads on each node, use the [**SetThreadAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setthreadaffinitymask) function.

Memory-intensive applications will need to optimize their memory usage. To retrieve the amount of free memory available to a node, use the [**GetNumaAvailableMemoryNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynode) function. The [**VirtualAllocExNuma**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocexnuma) function enables the application to specify a preferred node for the memory allocation. **VirtualAllocExNuma** does not allocate any physical pages, so it will succeed whether or not the pages are available on that node or elsewhere in the system. The physical pages are allocated on demand. If the preferred node runs out of pages, the memory manager will use pages from other nodes. If the memory is paged out, the same process is used when it is brought back in.

### NUMA Support on Systems With More Than 64 Logical Processors

On systems with more than 64 logical processors, nodes are assigned to [processor groups](processor-groups.md) according to the capacity of the nodes. The capacity of a node is the number of processors that are present when the system starts together with any additional logical processors that can be added while the system is running.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** Processor groups are not supported.

Each node must be fully contained within a group. If the capacities of the nodes are relatively small, the system assigns more than one node to the same group, choosing nodes that are physically close to one another for better performance. If a node's capacity exceeds the maximum number of processors in a group, the system splits the node into multiple smaller nodes, each small enough to fit in a group.

An ideal NUMA node for a new process can be requested using the [**PROC\_THREAD\_ATTRIBUTE\_PREFERRED\_NODE**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute) extended attribute when the process is created. Like a thread ideal processor, the ideal node is a hint to the scheduler, which assigns the new process to the group that contains the requested node if possible.

The extended NUMA functions [**GetNumaAvailableMemoryNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynodeex), [**GetNumaNodeProcessorMaskEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumanodeprocessormaskex), [**GetNumaProcessorNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornodeex), and [**GetNumaProximityNodeEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumaproximitynodeex) differ from their unextended counterparts in that the node number is a **USHORT** value rather than a **UCHAR**, to accommodate the potentially greater number of nodes on a system with more than 64 logical processors. Also, the processor specified with or retrieved by the extended functions includes the processor group; the processor specified with or retrieved by the unextended functions is group-relative. For details, see the individual function reference topics.

A group-aware application can assign all of its threads to a particular node in a similar fashion to that described earlier in this topic, using the corresponding extended NUMA functions. The application uses [**GetLogicalProcessorInformationEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformationex) to get the list of all processors on the system. Note that the application cannot set the process affinity mask unless the process is assigned to a single group and the intended node is located in that group. Usually the application must call [**SetThreadGroupAffinity**](/windows/win32/api/processtopologyapi/nf-processtopologyapi-setthreadgroupaffinity) to limit its threads to the intended node.

## NUMA API

The following table describes the NUMA API.



| Function                                                                     | Description                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPagesNuma**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpagesnuma)      | Allocates physical memory pages to be mapped and unmapped within any [Address Windowing Extensions](../memory/address-windowing-extensions.md) (AWE) region of a specified process and specifies the NUMA node for the physical memory. |
| [**CreateFileMappingNuma**](/windows/win32/api/memoryapi/nf-memoryapi-createfilemappingnumaw)                      | Creates or opens a named or unnamed file mapping object for a specified file, and specifies the NUMA node for the physical memory.                                                                                              |
| [**GetLogicalProcessorInformation**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformation)     | Retrieves information about logical processors and related hardware.                                                                                                                                                            |
| [**GetLogicalProcessorInformationEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformationex) | Retrieves information about the relationships of logical processors and related hardware.                                                                                                                                       |
| [**GetNumaAvailableMemoryNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynode)             | Retrieves the amount of memory available in the specified node.                                                                                                                                                                 |
| [**GetNumaAvailableMemoryNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynodeex)         | Retrieves the amount of memory available in a node specified as a **USHORT** value.                                                                                                                                             |
| [**GetNumaHighestNodeNumber**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumahighestnodenumber)                 | Retrieves the node that currently has the highest number.                                                                                                                                                                       |
| [**GetNumaNodeProcessorMask**](/windows/desktop/api/WinBase/nf-winbase-getnumanodeprocessormask)                 | Retrieves the processor mask for the specified node.                                                                                                                                                                            |
| [**GetNumaNodeProcessorMaskEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumanodeprocessormaskex)             | Retrieves the processor mask for a node specified as a **USHORT** value.                                                                                                                                                        |
| [**GetNumaProcessorNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornode)                         | Retrieves the node number for the specified processor.                                                                                                                                                                          |
| [**GetNumaProcessorNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornodeex)                     | Retrieves the node number as a **USHORT** value for the specified processor.                                                                                                                                                    |
| [**GetNumaProximityNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaproximitynode)                         | Retrieves the node number for the specified proximity identifier.                                                                                                                                                               |
| [**GetNumaProximityNodeEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumaproximitynodeex)                     | Retrieves the node number as a **USHORT** value for the specified proximity identifier.                                                                                                                                         |
| [**MapViewOfFileExNuma**](/windows/win32/api/winbase/nf-winbase-mapviewoffileexnuma)                          | Maps a view of a file mapping into the address space of a calling process, and specifies the NUMA node for the physical memory.                                                                                                 |
| [**VirtualAllocExNuma**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocexnuma)                            | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory.                                                                          |



 

The [**QueryWorkingSetEx**](/windows/win32/api/psapi/nf-psapi-queryworkingsetex) function can be used to retrieve the NUMA node on which a page is allocated. For an example, see [Allocating Memory from a NUMA Node](../memory/allocating-memory-from-a-numa-node.md).

## Related topics

<dl> <dt>

[Allocating Memory from a NUMA Node](../memory/allocating-memory-from-a-numa-node.md)
</dt> <dt>

[Multiple Processors](multiple-processors.md)
</dt> <dt>

[Processor Groups](processor-groups.md)
</dt> </dl>

 

 
