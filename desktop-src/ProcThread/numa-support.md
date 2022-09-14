---
description: The traditional model for multiprocessor support is symmetric multiprocessor (SMP). In this model, each processor has equal access to memory and I/O. As more processors are added, the processor bus becomes a limitation for system performance.
ms.assetid: a1263968-2b26-45cc-bdd7-6aa354821a5a
title: NUMA Support
ms.topic: article
ms.date: 05/31/2018
---

# NUMA Architecture

The traditional model for multiprocessor architecture is symmetric multiprocessor (SMP). In this model, each processor has equal access to memory and I/O. As more processors are added, the processor bus becomes a limitation for system performance.

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


### Behavior starting with Windows 10 Build 20348 

> [!NOTE]
> Starting with Windows 10 Build 20348, the behavior of this and other NUMA functions has been modified to better support systems with nodes containing more that 64 processors.

Creating "fake" nodes to accommodate a 1:1 mapping between groups and nodes has resulted in confusing behaviors where unexpected numbers of NUMA nodes are reported and so, starting with Windows 10 Build 20348, the OS has changed to allow multiple groups to be associated with a node, and so now the true NUMA topology of the system can be reported.  

As part of these changes to the OS, a number of NUMA APIs have changed to support reporting the multiple groups which can now be associated with a single NUMA node. Updated and new APIs are labeled in the table in the **NUMA API** section below.

Because the removal of node splitting can potentially impact existing applications, a registry value is available to allow opting back into the legacy node splitting behavior. Node splitting can be re-enabled by creating a **REG_DWORD** value named "SplitLargeNodes" with value 1 underneath HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\NUMA. Changes to this setting require a reboot to take effect.

```powershell
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NUMA" /v SplitLargeNodes /t REG_DWORD /d 1
```

> [!NOTE]
> Applications that are updated to use the new API functionality that reports the true NUMA topology will continue to work properly on systems where large node splitting has been reenabled with this registry key.

The following example first demonstrates potential issues with builds tables mapping processors to NUMA nodes using the legacy affinity APIs, which no longer provide a full cover of all processors in the system this can result in an incomplete table. The implications of such incompleteness depend on the contents of the table. If the table simply stores the corresponding node number then this is likely only a performance issue with uncovered processors being left as part of node 0. However, if the table contains pointers to a per-node context structure this can result in NULL dereferences at runtime.

Next, the code example illustrates two workarounds for the issue. The first is to migrate to the multi-group node affinity APIs (user-mode and kernel-mode). The second is to use **KeQueryLogicalProcessorRelationship** to directly query the NUMA node associated with a given processor number.

```cpp

//
// Problematic implementation using KeQueryNodeActiveAffinity.
//

USHORT CurrentNode;
USHORT HighestNodeNumber;
GROUP_AFFINITY NodeAffinity;
ULONG ProcessorIndex;
PROCESSOR_NUMBER ProcessorNumber;

HighestNodeNumber = KeQueryHighestNodeNumber();
for (CurrentNode = 0; CurrentNode <= HighestNodeNumber; CurrentNode += 1) {

    KeQueryNodeActiveAffinity(CurrentNode, &NodeAffinity, NULL);
    while (NodeAffinity.Mask != 0) {

        ProcessorNumber.Group = NodeAffinity.Group;
        BitScanForward(&ProcessorNumber.Number, NodeAffinity.Mask);

        ProcessorIndex = KeGetProcessorIndexFromNumber(&ProcessorNumber);

        ProcessorNodeContexts[ProcessorIndex] = NodeContexts[CurrentNode;]

        NodeAffinity.Mask &= ~((KAFFINITY)1 << ProcessorNumber.Number);
    }
}

//
// Resolution using KeQueryNodeActiveAffinity2.
//

USHORT CurrentIndex;
USHORT CurrentNode;
USHORT CurrentNodeAffinityCount;
USHORT HighestNodeNumber;
ULONG MaximumGroupCount;
PGROUP_AFFINITY NodeAffinityMasks;
ULONG ProcessorIndex;
PROCESSOR_NUMBER ProcessorNumber;
NTSTATUS Status;

MaximumGroupCount = KeQueryMaximumGroupCount();
NodeAffinityMasks = ExAllocatePool2(POOL_FLAG_PAGED,
                                    sizeof(GROUP_AFFINITY) * MaximumGroupCount,
                                    'tseT');

if (NodeAffinityMasks == NULL) {
    return STATUS_NO_MEMORY;
}

HighestNodeNumber = KeQueryHighestNodeNumber();
for (CurrentNode = 0; CurrentNode <= HighestNodeNumber; CurrentNode += 1) {

    Status = KeQueryNodeActiveAffinity2(CurrentNode,
                                        NodeAffinityMasks,
                                        MaximumGroupCount,
                                        &CurrentNodeAffinityCount);
    NT_ASSERT(NT_SUCCESS(Status));

    for (CurrentIndex = 0; CurrentIndex < CurrentNodeAffinityCount; CurrentIndex += 1) {

        CurrentAffinity = &NodeAffinityMasks[CurrentIndex];

        while (CurrentAffinity->Mask != 0) {

            ProcessorNumber.Group = CurrentAffinity.Group;
            BitScanForward(&ProcessorNumber.Number, CurrentAffinity->Mask);

            ProcessorIndex = KeGetProcessorIndexFromNumber(&ProcessorNumber);

            ProcessorNodeContexts[ProcessorIndex] = NodeContexts[CurrentNode];

            CurrentAffinity->Mask &= ~((KAFFINITY)1 << ProcessorNumber.Number);
        }
    }
}

//
// Resolution using KeQueryLogicalProcessorRelationship.
//

ULONG ProcessorCount;
ULONG ProcessorIndex;
SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX ProcessorInformation;
ULONG ProcessorInformationSize;
PROCESSOR_NUMBER ProcessorNumber;
NTSTATUS Status;

ProcessorCount = KeQueryActiveProcessorCountEx(ALL_PROCESSOR_GROUPS);

for (ProcessorIndex = 0; ProcessorIndex < ProcessorCount; ProcessorIndex += 1) {

    Status = KeGetProcessorNumberFromIndex(ProcessorIndex, &ProcessorNumber);
    NT_ASSERT(NT_SUCCESS(Status));

    ProcessorInformationSize = sizeof(ProcessorInformation);
    Status = KeQueryLogicalProcessorRelationship(&ProcessorNumber,
                                                    RelationNumaNode,
                                                    &ProcessorInformation,
                                                    &ProcesorInformationSize);
    NT_ASSERT(NT_SUCCESS(Status));

    NodeNumber = ProcessorInformation.NumaNode.NodeNumber;

    ProcessorNodeContexts[ProcessorIndex] = NodeContexts[NodeNumber];
}
```

## NUMA API

The following table describes the NUMA API.



| Function                                                                     | Description                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPagesNuma**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpagesnuma)      | Allocates physical memory pages to be mapped and unmapped within any [Address Windowing Extensions](../memory/address-windowing-extensions.md) (AWE) region of a specified process and specifies the NUMA node for the physical memory. |
| [**CreateFileMappingNuma**](/windows/win32/api/memoryapi/nf-memoryapi-createfilemappingnumaw)                      | Creates or opens a named or unnamed file mapping object for a specified file, and specifies the NUMA node for the physical memory.                                                                                              |
| [**GetLogicalProcessorInformation**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformation)     | Updated in Windows 10 Build 20348. Retrieves information about logical processors and related hardware.                                                                                                                                                            |
| [**GetLogicalProcessorInformationEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformationex) | Updated in Windows 10 Build 20348. Retrieves information about the relationships of logical processors and related hardware.                                                                                                                                       |
| [**GetNumaAvailableMemoryNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynode)             | Retrieves the amount of memory available in the specified node.                                                                                                                                                                 |
| [**GetNumaAvailableMemoryNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynodeex)         | Retrieves the amount of memory available in a node specified as a **USHORT** value.                                                                                                                                             |
| [**GetNumaHighestNodeNumber**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumahighestnodenumber)                 | Retrieves the node that currently has the highest number.                                                                                                                                                                       |
| [**GetNumaNodeProcessorMask**](/windows/desktop/api/WinBase/nf-winbase-getnumanodeprocessormask)                 | Updated in Windows 10 Build 20348. Retrieves the processor mask for the specified node.                                                                                                                                                                            |
| [**GetNumaNodeProcessorMask2**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumanodeprocessormask2)                         | New in Windows 10 Build 20348. Retrieves the multi-group processor mask of the specified node.                                                                                                                                                                          |
| [**GetNumaNodeProcessorMaskEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumanodeprocessormaskex)             | Updated in Windows 10 Build 20348. Retrieves the processor mask for a node specified as a **USHORT** value.                                                                                                                                                        |
| [**GetNumaProcessorNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornode)                         | Retrieves the node number for the specified processor.                                                                                                                                                                          |
| [**GetNumaProcessorNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornodeex)                     | Retrieves the node number as a **USHORT** value for the specified processor.                                                                                                                                                    |
| [**GetNumaProximityNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaproximitynode)                         | Retrieves the node number for the specified proximity identifier.                                                                                                                                                               |
| [**GetNumaProximityNodeEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumaproximitynodeex)                     | Retrieves the node number as a **USHORT** value for the specified proximity identifier.                                                                                                                                         |
| [**GetProcessDefaultCpuSetMasks**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessdefaultcpusetmasks)                     | New in Windows 10 Build 20348. Retrieves the list of CPU Sets in the process default set that was set by SetProcessDefaultCpuSetMasks or SetProcessDefaultCpuSets.                                                                                                                                         |
| [**GetThreadSelectedCpuSetMasks**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadselectedcpusetmasks)                     | New in Windows 10 Build 20348. Sets the selected CPU Sets assignment for the specified thread. This assignment overrides the process default assignment, if one is set.                                                                                                                                          |
| [**MapViewOfFileExNuma**](/windows/win32/api/winbase/nf-winbase-mapviewoffileexnuma)                          | Maps a view of a file mapping into the address space of a calling process, and specifies the NUMA node for the physical memory.                                                                                                 |
| [**SetProcessDefaultCpuSetMasks**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdefaultcpusetmasks)                     | New in Windows 10 Build 20348. Sets the default CPU Sets assignment for threads in the specified process.                                                                                                                                          |
| [**SetThreadSelectedCpuSetMasks**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadselectedcpusetmasks)                     | New in Windows 10 Build 20348. Sets the selected CPU Sets assignment for the specified thread. This assignment overrides the process default assignment, if one is set.                                                                                                                                          |
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

 

 
