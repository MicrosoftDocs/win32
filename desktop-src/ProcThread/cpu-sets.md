---
description: CPU Sets provide APIs to declare application affinity in a 'soft' manner that is compatible with OS power management.
ms.assetid: FF8BE790-19D9-473F-B184-C54FB392D61A
title: CPU Sets
ms.topic: article
ms.date: 05/31/2018
---

# CPU Sets

CPU Sets provide APIs to declare application affinity in a 'soft' manner that is compatible with OS power management. Additionally, the API provides applications with the ability to reaffinitize all background threads in the process to a subset of processors using the **Process Default** mechanism to avoid interference from OS threads within the process. Some versions of Windows support Core Reservation policies, in which a subset of the system’s CPU Sets can be devoted to the exclusive use of individual applications and workloads.

The CPU Set API works with CPU Set IDs, which are associated with virtual processor affinities. On most systems, and under most conditions, each CPU Set ID will map directly to a single **home** logical processor. A thread affinitized to a given CPU Set will typically execute on one of the processors in its list of selected CPU Set IDs.

CPU Sets that are reserved can be determined by inspecting the **Allocated** flag in the SYSTEM\_CPU\_SET\_INFORMATION. The system controls access to reserved CPU Sets and the assignment can be queried using the **AllocatedToTargetProcess** flag of the SYSTEM\_CPU\_SET\_INFORMATION structure. If a process attempts to use a CPU Set assignment which is allocated exclusively to other processes, its request is ignored and threads assigned to disallowed CPU sets are scheduled elsewhere. CPU Sets can be assigned at two levels. The Process Default CPU sets are assigned to all threads in a process that do not have an assignment at the Thread Selected level. If a thread or process has a restrictive affinity mask set, the affinity mask is respected above any conflicting CPU Set assignment. On multi-group systems, CPU assignments are ignored if they are in groups that do not match the group in the thread’s affinity mask. If a thread is assigned to multiple valid CPU Sets, it will run on one of the corresponding processors according to its priorities and the priorities of competing threads on those processors.

**CPU Set Functions/Enumerations/Structures**

-   [**GetProcessDefaultCpuSets**](getprocessdefaultcpusets.md) function
-   [**GetSystemCpuSetInformation**](getsystemcpusetinformation.md) function
-   [**GetThreadSelectedCpuSets**](getthreadselectedcpusets.md) function
-   [**SetProcessDefaultCpuSets**](setprocessdefaultcpusets.md) function
-   [**SetThreadSelectedCpuSets**](setthreadselectedcpusets.md) function
-   [**CPU\_SET\_INFORMATION\_TYPE**](cpu-set-information-type.md) enumeration
-   [**SYSTEM\_CPU\_SET\_INFORMATION**](/windows/desktop/api/winnt/ns-winnt-system_cpu_set_information) structure

 

 



