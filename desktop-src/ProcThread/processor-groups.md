---
description: The 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions of Windows support more than 64 logical processors on a single computer. This functionality is not available on 32-bit versions of Windows.
ms.assetid: c627ac0f-96e8-48b5-9103-4316f487e173
title: Processor Groups
ms.topic: article
ms.date: 05/31/2018
---

# Processor Groups

The 64-bit versions of Windows 7 and Windows Server 2008 R2 and later versions of Windows support more than 64 logical processors on a single computer. This functionality is not available on 32-bit versions of Windows.

Systems with more than one physical processor or systems with physical processors that have multiple cores provide the operating system with multiple logical processors. A *logical processor* is one logical computing engine from the perspective of the operating system, application or driver. A *core* is one processor unit, which can consist of one or more logical processors. A *physical processor* can consist of one or more cores. A physical processor is the same as a processor package, a socket, or a CPU.

Support for systems that have more than 64 logical processors is based on the concept of a *processor group*, which is a static set of up to 64 logical processors that is treated as a single scheduling entity. Processor groups are numbered starting with 0. Systems with fewer than 64 logical processors always have a single group, Group 0.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** Processor groups are not supported.

When the system starts, the operating system creates processor groups and assigns logical processors to the groups. If the system is capable of hot-adding processors, the operating system allows space in groups for processors that might arrive while the system is running. The operating system minimizes the number of groups in a system. For example, a system with 128 logical processors would have two processor groups with 64 processors in each group, not four groups with 32 logical processors in each group.

For better performance, the operating system takes physical locality into account when assigning logical processors to groups. All of the logical processors in a core, and all of the cores in a physical processor, are assigned to the same group, if possible. Physical processors that are physically close to one another are assigned to the same group. A NUMA node is assigned to a single group unless the capacity of the node exceeds the maximum group size. For more information, see [NUMA Support](numa-support.md).

On systems with 64 or fewer processors, existing applications will operate correctly without modification. Applications that do not call any functions that use processor affinity masks or processor numbers will operate correctly on all systems, regardless of the number of processors. To operate correctly on systems with more than 64 logical processors, the following kinds of applications might require modification:

-   Applications that manage, maintain, or display per-processor information for the entire system must be modified to support more than 64 logical processors. An example of such an application is Windows Task Manager, which displays the workload of each processor in the system.
-   Applications for which performance is critical and that can scale efficiently beyond 64 logical processors must be modified to run on such systems. For example, database applications might benefit from modifications.
-   If an application uses a DLL that has per-processor data structures, and the DLL has not been modified to support more than 64 logical processors, all threads in the application that call functions exported by the DLL must be assigned to the same group.

By default, an application is constrained to a single group, which should provide ample processing capability for the typical application. The operating system initially assigns each process to a single group in a round-robin manner across the groups in the system. A process begins its execution assigned to one group. The first thread of a process initially runs in the group to which the process is assigned. Each newly created thread is assigned to the same group as the thread that created it.

An application that requires the use of multiple groups so that it can run on more than 64 processors must explicitly determine where to run its threads and is responsible for setting the threads' processor affinities to the desired groups. The [INHERIT\_PARENT\_AFFINITY](process-creation-flags.md) flag can be used to specify a parent process (which can be different than the current process) from which to generate the affinity for a new process. If the process is running in a single group, it can read and modify its affinity using [**GetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-getprocessaffinitymask) and [**SetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setprocessaffinitymask) while remaining in the same group; if the process affinity is modified, the new affinity is applied to its threads.

A thread's affinity can be specified at creation using the [**PROC\_THREAD\_ATTRIBUTE\_GROUP\_AFFINITY**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute) extended attribute with the [**CreateRemoteThreadEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex) function. After the thread is created, its affinity can be changed by calling [**SetThreadAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setthreadaffinitymask) or [**SetThreadGroupAffinity**](/windows/win32/api/processtopologyapi/nf-processtopologyapi-setthreadgroupaffinity). If a thread is assigned to a different group than the process, the process's affinity is updated to include the thread's affinity and the process becomes a multi-group process. Further affinity changes must be made for individual threads; a multi-group process's affinity cannot be modified using [**SetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setprocessaffinitymask). The [**GetProcessGroupAffinity**](/windows/win32/api/processtopologyapi/nf-processtopologyapi-getprocessgroupaffinity) function retrieves the set of groups to which a process and its threads are assigned.

To specify affinity for all processes associated with a job object, use the [**SetInformationJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-setinformationjobobject) function with the **JobObjectGroupInformation** or **JobObjectGroupInformationEx** information class.

A logical processor is identified by its group number and its group-relative processor number. This is represented by a [**PROCESSOR\_NUMBER**](/windows/desktop/api/WinNT/ns-winnt-processor_number) structure. Numeric processor numbers used by legacy functions are group-relative.

For a discussion of operating system architecture changes to support more than 64 processors, see the white paper [Supporting Systems That Have More Than 64 Processors](https://www.microsoft.com/whdc/system/Sysinternals/MoreThan64proc.mspx).

For a list of new functions and structures that support processor groups, see [What's New in Processes and Threads](what-s-new-in-processes-and-threads.md).

## Related topics

<dl> <dt>

[Multiple Processors](multiple-processors.md)
</dt> <dt>

[NUMA Support](numa-support.md)
</dt> </dl>

 

 
