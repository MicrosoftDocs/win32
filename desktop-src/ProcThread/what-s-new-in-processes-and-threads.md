---
description: Windows 7 and Windows Server 2008 R2 include the following new programming elements for processes and threads.
ms.assetid: 69cd8713-b40c-4fec-a256-9c2ee3d73da5
title: What's New in Processes and Threads
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Processes and Threads

Windows 7 and Windows Server 2008 R2 include the following new programming elements for processes and threads.

## New Capabilities

The 64-bit versions of Windows 7 and Windows Server 2008 R2 support more than 64 logical processors on a single computer. For more information, see [Processor Groups](processor-groups.md).

User-mode scheduling (UMS) is a lightweight mechanism that applications can use to schedule their own threads. For more information, see [User-Mode Scheduling](user-mode-scheduling.md).

## New Functions

The following new functions are used with processors and processor groups.



| Function                                                                                | Description                                                                                                                                                          |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRemoteThreadEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethreadex)<br/>                         | Creates a thread that runs in the virtual address space of another process and optionally specifies extended attributes such as processor group affinity.<br/> |
| [**GetActiveProcessorCount**](/windows/desktop/api/WinBase/nf-winbase-getactiveprocessorcount)<br/>                   | Returns the number of active processors in a processor group or in the system.<br/>                                                                            |
| [**GetActiveProcessorGroupCount**](/windows/desktop/api/WinBase/nf-winbase-getactiveprocessorgroupcount)<br/>         | Returns the number of active processor groups in the system.<br/>                                                                                              |
| [**GetCurrentProcessorNumberEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocessornumberex)<br/>           | Retrieves the processor group and number of the logical processor in which the calling thread is running.<br/>                                                 |
| [**GetLogicalProcessorInformationEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformationex)<br/> | Retrieves information about the relationships of logical processors and related hardware.<br/>                                                                 |
| [**GetMaximumProcessorCount**](/windows/desktop/api/WinBase/nf-winbase-getmaximumprocessorcount)<br/>                 | Returns the maximum number of logical processors that a processor group or the system can have.<br/>                                                           |
| [**GetMaximumProcessorGroupCount**](/windows/desktop/api/WinBase/nf-winbase-getmaximumprocessorgroupcount)<br/>       | Returns the maximum number of processor groups that the system can have. <br/>                                                                                 |
| [**GetNumaAvailableMemoryNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynodeex)<br/>         | Retrieves the amount of memory that is available in the specified node as a USHORT value.<br/>                                                                 |
| [**GetNumaNodeNumberFromHandle**](/windows/desktop/api/WinBase/nf-winbase-getnumanodenumberfromhandle)<br/>           | Retrieves the NUMA node associated with the underlying device for a file handle.<br/>                                                                          |
| [**GetNumaNodeProcessorMaskEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumanodeprocessormaskex)<br/>             | Retrieves the processor mask for the specified NUMA node as a USHORT value.<br/>                                                                               |
| [**GetNumaProcessorNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornodeex)<br/>                     | Retrieves the node number of the specified logical processor as a USHORT value.<br/>                                                                           |
| [**GetNumaProximityNodeEx**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumaproximitynodeex)<br/>                     | Retrieves the node number as a USHORT value for the specified proximity identifier.<br/>                                                                       |
| [**GetProcessGroupAffinity**](/windows/win32/api/processtopologyapi/nf-processtopologyapi-getprocessgroupaffinity)<br/>                   | Retrieves the processor group affinity of the specified process.<br/>                                                                                          |
| [**GetProcessorSystemCycleTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getprocessorsystemcycletime)<br/>           | Retrieves the cycle time each processor in the specified group spent executing deferred procedure calls (DPCs) and interrupt service routines (ISRs).<br/>     |
| [**GetThreadGroupAffinity**](/windows/win32/api/processtopologyapi/nf-processtopologyapi-getthreadgroupaffinity)<br/>                     | Retrieves the processor group affinity of the specified thread.<br/>                                                                                           |
| [**GetThreadIdealProcessorEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadidealprocessorex)<br/>               | Retrieves the processor number of the ideal processor for the specified thread.<br/>                                                                           |
| [**QueryIdleProcessorCycleTimeEx**](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryidleprocessorcycletimeex)<br/>       | Retrieves the accumulated cycle time for the idle thread on each logical processor in the specified processor group. <br/>                                     |
| [**SetThreadGroupAffinity**](/windows/win32/api/processtopologyapi/nf-processtopologyapi-setthreadgroupaffinity)<br/>                     | Sets the processor group affinity for the specified thread.<br/>                                                                                               |
| [**SetThreadIdealProcessorEx**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessorex)<br/>               | Sets the ideal processor for the specified thread and optionally retrieves the previous ideal processor.<br/>                                                  |



 

The following new functions are used with thread pools.



| Function                                                                              | Description                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**QueryThreadpoolStackInformation**](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-querythreadpoolstackinformation)<br/> | Retrieves the stack reserve and commit sizes for threads in the specified thread pool.<br/>              |
| [**SetThreadpoolCallbackPersistent**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackpersistent)<br/> | Specifies that the callback should run on a persistent thread.<br/>                                      |
| [**SetThreadpoolCallbackPriority**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackpriority)<br/>     | Specifies the priority of a callback function relative to other work items in the same thread pool.<br/> |
| [**SetThreadpoolStackInformation**](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolstackinformation)<br/>     | Sets the stack reserve and commit sizes for new threads in the specified thread pool. <br/>              |



 

The following new functions are used with UMS.



| Function                                                                          | Description                                                                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**CreateUmsCompletionList**](/windows/desktop/api/WinBase/nf-winbase-createumscompletionlist)<br/>             | Creates a UMS completion list.<br/>                                                                     |
| [**CreateUmsThreadContext**](/windows/desktop/api/WinBase/nf-winbase-createumsthreadcontext)<br/>               | Creates a UMS thread context to represent a UMS worker thread.<br/>                                     |
| [**DeleteUmsCompletionList**](/windows/desktop/api/WinBase/nf-winbase-deleteumscompletionlist)<br/>             | Deletes the specified UMS completion list. The list must be empty.<br/>                                 |
| [**DeleteUmsThreadContext**](/windows/desktop/api/WinBase/nf-winbase-deleteumsthreadcontext)<br/>               | Deletes the specified UMS thread context. The thread must be terminated.<br/>                           |
| [**DequeueUmsCompletionListItems**](/windows/desktop/api/WinBase/nf-winbase-dequeueumscompletionlistitems)<br/> | Retrieves UMS worker threads from the specified UMS completion list.<br/>                               |
| [**EnterUmsSchedulingMode**](/windows/desktop/api/WinBase/nf-winbase-enterumsschedulingmode)<br/>               | Converts the calling thread into a UMS scheduler thread.<br/>                                           |
| [**ExecuteUmsThread**](/windows/desktop/api/WinBase/nf-winbase-executeumsthread)<br/>                           | Runs the specified UMS worker thread.<br/>                                                              |
| [**GetCurrentUmsThread**](/windows/desktop/api/WinBase/nf-winbase-getcurrentumsthread)<br/>                     | Returns the UMS thread context of the calling UMS thread.<br/>                                          |
| [**GetNextUmsListItem**](/windows/desktop/api/WinBase/nf-winbase-getnextumslistitem)<br/>                       | Returns the next UMS thread context in a list of UMS thread contexts.<br/>                              |
| [**GetUmsCompletionListEvent**](/windows/desktop/api/WinBase/nf-winbase-getumscompletionlistevent)<br/>         | Retrieves a handle to the event associated with the specified UMS completion list.<br/>                 |
| [**QueryUmsThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-queryumsthreadinformation)<br/>         | Retrieves information about the specified UMS worker thread.<br/>                                       |
| [**SetUmsThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-setumsthreadinformation)<br/>             | Sets application-specific context information for the specified UMS worker thread.<br/>                 |
| [*UmsSchedulerProc*](/windows/desktop/api/WinNT/nc-winnt-rtl_ums_scheduler_entry_point)<br/>                             | The application-defined UMS scheduler entry point function associated with a UMS completion list. <br/> |
| [**UmsThreadYield**](/windows/desktop/api/WinBase/nf-winbase-umsthreadyield)<br/>                               | Yields control to the UMS scheduler thread on which the calling UMS worker thread is running.<br/>      |



 

## New Structures



| Structure                                                                                                 | Description                                                                                         |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**CACHE\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-cache_relationship)<br/>                                              | Describes cache attributes. <br/>                                                             |
| [**GROUP\_AFFINITY**](/windows/desktop/api/WinNT/ns-winnt-group_affinity)<br/>                                                      | Contains a processor group-specific affinity, such as the affinity of a thread.<br/>          |
| [**GROUP\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-group_relationship)<br/>                                              | Contains information about processor groups. <br/>                                            |
| [**NUMA\_NODE\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-numa_node_relationship)<br/>                                     | Contains information about a NUMA node in a processor group. <br/>                            |
| [**PROCESSOR\_GROUP\_INFO**](/windows/desktop/api/WinNT/ns-winnt-processor_group_info)<br/>                                         | Contains the number and affinity of processors in a processor group.<br/>                     |
| [**PROCESSOR\_NUMBER**](/windows/desktop/api/WinNT/ns-winnt-processor_number)<br/>                                                  | Represents a logical processor in a processor group.<br/>                                     |
| [**PROCESSOR\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-processor_relationship)<br/>                                      | Contains information about affinity within a processor group.<br/>                            |
| [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION\_EX**](/windows/desktop/api/WinNT/ns-winnt-system_logical_processor_information_ex)<br/> | Contains information about the relationships of logical processors and related hardware.<br/> |
| [**UMS\_CREATE\_THREAD\_ATTRIBUTES**](/windows/desktop/api/WinNT/ns-winnt-ums_create_thread_attributes)<br/>                        | Specifies attributes for a UMS worker thread. <br/>                                           |
| [**UMS\_SCHEDULER\_STARTUP\_INFO**](/windows/desktop/api/WinBase/ns-winbase-ums_scheduler_startup_info)<br/>                            | Specifies attributes for a UMS scheduler thread<br/>                                          |



 

 

 
