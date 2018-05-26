---
Description: Windows 7 and Windows Server 2008 R2 include the following new programming elements for processes and threads.
ms.assetid: 69cd8713-b40c-4fec-a256-9c2ee3d73da5
title: Whats New in Processes and Threads
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**CreateRemoteThreadEx**](/windows/win32/WinBase/nf-processthreadsapi-createremotethreadex?branch=master)<br/>                         | Creates a thread that runs in the virtual address space of another process and optionally specifies extended attributes such as processor group affinity.<br/> |
| [**GetActiveProcessorCount**](/windows/win32/WinBase/nf-winbase-getactiveprocessorcount?branch=master)<br/>                   | Returns the number of active processors in a processor group or in the system.<br/>                                                                            |
| [**GetActiveProcessorGroupCount**](/windows/win32/WinBase/nf-winbase-getactiveprocessorgroupcount?branch=master)<br/>         | Returns the number of active processor groups in the system.<br/>                                                                                              |
| [**GetCurrentProcessorNumberEx**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentprocessornumberex?branch=master)<br/>           | Retrieves the processor group and number of the logical processor in which the calling thread is running.<br/>                                                 |
| [**GetLogicalProcessorInformationEx**](/windows/win32/WinBase/?branch=master)<br/> | Retrieves information about the relationships of logical processors and related hardware.<br/>                                                                 |
| [**GetMaximumProcessorCount**](/windows/win32/WinBase/nf-winbase-getmaximumprocessorcount?branch=master)<br/>                 | Returns the maximum number of logical processors that a processor group or the system can have.<br/>                                                           |
| [**GetMaximumProcessorGroupCount**](/windows/win32/WinBase/nf-winbase-getmaximumprocessorgroupcount?branch=master)<br/>       | Returns the maximum number of processor groups that the system can have. <br/>                                                                                 |
| [**GetNumaAvailableMemoryNodeEx**](/windows/win32/WinBase/nf-winbase-getnumaavailablememorynodeex?branch=master)<br/>         | Retrieves the amount of memory that is available in the specified node as a USHORT value.<br/>                                                                 |
| [**GetNumaNodeNumberFromHandle**](/windows/win32/WinBase/nf-winbase-getnumanodenumberfromhandle?branch=master)<br/>           | Retrieves the NUMA node associated with the underlying device for a file handle.<br/>                                                                          |
| [**GetNumaNodeProcessorMaskEx**](/windows/win32/WinBase/?branch=master)<br/>             | Retrieves the processor mask for the specified NUMA node as a USHORT value.<br/>                                                                               |
| [**GetNumaProcessorNodeEx**](/windows/win32/WinBase/nf-winbase-getnumaprocessornodeex?branch=master)<br/>                     | Retrieves the node number of the specified logical processor as a USHORT value.<br/>                                                                           |
| [**GetNumaProximityNodeEx**](/windows/win32/WinBase/?branch=master)<br/>                     | Retrieves the node number as a USHORT value for the specified proximity identifier.<br/>                                                                       |
| [**GetProcessGroupAffinity**](/windows/win32/WinBase/?branch=master)<br/>                   | Retrieves the processor group affinity of the specified process.<br/>                                                                                          |
| [**GetProcessorSystemCycleTime**](/windows/win32/WinBase/?branch=master)<br/>           | Retrieves the cycle time each processor in the specified group spent executing deferred procedure calls (DPCs) and interrupt service routines (ISRs).<br/>     |
| [**GetThreadGroupAffinity**](/windows/win32/WinBase/?branch=master)<br/>                     | Retrieves the processor group affinity of the specified thread.<br/>                                                                                           |
| [**GetThreadIdealProcessorEx**](/windows/win32/WinBase/nf-processthreadsapi-getthreadidealprocessorex?branch=master)<br/>               | Retrieves the processor number of the ideal processor for the specified thread.<br/>                                                                           |
| [**QueryIdleProcessorCycleTimeEx**](/windows/win32/WinBase/nf-realtimeapiset-queryidleprocessorcycletimeex?branch=master)<br/>       | Retrieves the accumulated cycle time for the idle thread on each logical processor in the specified processor group. <br/>                                     |
| [**SetThreadGroupAffinity**](/windows/win32/WinBase/?branch=master)<br/>                     | Sets the processor group affinity for the specified thread.<br/>                                                                                               |
| [**SetThreadIdealProcessorEx**](/windows/win32/WinBase/nf-processthreadsapi-setthreadidealprocessorex?branch=master)<br/>               | Sets the ideal processor for the specified thread and optionally retrieves the previous ideal processor.<br/>                                                  |



 

The following new functions are used with thread pools.



| Function                                                                              | Description                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**QueryThreadpoolStackInformation**](/windows/win32/WinBase/nf-threadpoolapiset-querythreadpoolstackinformation?branch=master)<br/> | Retrieves the stack reserve and commit sizes for threads in the specified thread pool.<br/>              |
| [**SetThreadpoolCallbackPersistent**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackpersistent?branch=master)<br/> | Specifies that the callback should run on a persistent thread.<br/>                                      |
| [**SetThreadpoolCallbackPriority**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackpriority?branch=master)<br/>     | Specifies the priority of a callback function relative to other work items in the same thread pool.<br/> |
| [**SetThreadpoolStackInformation**](/windows/win32/WinBase/nf-threadpoolapiset-setthreadpoolstackinformation?branch=master)<br/>     | Sets the stack reserve and commit sizes for new threads in the specified thread pool. <br/>              |



 

The following new functions are used with UMS.



| Function                                                                          | Description                                                                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**CreateUmsCompletionList**](/windows/win32/WinBase/nf-winbase-createumscompletionlist?branch=master)<br/>             | Creates a UMS completion list.<br/>                                                                     |
| [**CreateUmsThreadContext**](/windows/win32/WinBase/nf-winbase-createumsthreadcontext?branch=master)<br/>               | Creates a UMS thread context to represent a UMS worker thread.<br/>                                     |
| [**DeleteUmsCompletionList**](/windows/win32/WinBase/nf-winbase-deleteumscompletionlist?branch=master)<br/>             | Deletes the specified UMS completion list. The list must be empty.<br/>                                 |
| [**DeleteUmsThreadContext**](/windows/win32/WinBase/nf-winbase-deleteumsthreadcontext?branch=master)<br/>               | Deletes the specified UMS thread context. The thread must be terminated.<br/>                           |
| [**DequeueUmsCompletionListItems**](/windows/win32/WinBase/nf-winbase-dequeueumscompletionlistitems?branch=master)<br/> | Retrieves UMS worker threads from the specified UMS completion list.<br/>                               |
| [**EnterUmsSchedulingMode**](/windows/win32/WinBase/nf-winbase-enterumsschedulingmode?branch=master)<br/>               | Converts the calling thread into a UMS scheduler thread.<br/>                                           |
| [**ExecuteUmsThread**](/windows/win32/WinBase/nf-winbase-executeumsthread?branch=master)<br/>                           | Runs the specified UMS worker thread.<br/>                                                              |
| [**GetCurrentUmsThread**](/windows/win32/WinBase/nf-winbase-getcurrentumsthread?branch=master)<br/>                     | Returns the UMS thread context of the calling UMS thread.<br/>                                          |
| [**GetNextUmsListItem**](/windows/win32/WinBase/nf-winbase-getnextumslistitem?branch=master)<br/>                       | Returns the next UMS thread context in a list of UMS thread contexts.<br/>                              |
| [**GetUmsCompletionListEvent**](/windows/win32/WinBase/nf-winbase-getumscompletionlistevent?branch=master)<br/>         | Retrieves a handle to the event associated with the specified UMS completion list.<br/>                 |
| [**QueryUmsThreadInformation**](/windows/win32/WinBase/nf-winbase-queryumsthreadinformation?branch=master)<br/>         | Retrieves information about the specified UMS worker thread.<br/>                                       |
| [**SetUmsThreadInformation**](/windows/win32/WinBase/nf-winbase-setumsthreadinformation?branch=master)<br/>             | Sets application-specific context information for the specified UMS worker thread.<br/>                 |
| [*UmsSchedulerProc*](/windows/win32/WinNT/nc-winnt-rtl_ums_scheduler_entry_point?branch=master)<br/>                             | The application-defined UMS scheduler entry point function associated with a UMS completion list. <br/> |
| [**UmsThreadYield**](/windows/win32/WinBase/nf-winbase-umsthreadyield?branch=master)<br/>                               | Yields control to the UMS scheduler thread on which the calling UMS worker thread is running.<br/>      |



 

## New Structures



| Structure                                                                                                 | Description                                                                                         |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**CACHE\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_cache_relationship?branch=master)<br/>                                              | Describes cache attributes. <br/>                                                             |
| [**GROUP\_AFFINITY**](/windows/win32/WinNT/ns-winnt-_group_affinity?branch=master)<br/>                                                      | Contains a processor group-specific affinity, such as the affinity of a thread.<br/>          |
| [**GROUP\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_group_relationship?branch=master)<br/>                                              | Contains information about processor groups. <br/>                                            |
| [**NUMA\_NODE\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_numa_node_relationship?branch=master)<br/>                                     | Contains information about a NUMA node in a processor group. <br/>                            |
| [**PROCESSOR\_GROUP\_INFO**](/windows/win32/WinNT/ns-winnt-_processor_group_info?branch=master)<br/>                                         | Contains the number and affinity of processors in a processor group.<br/>                     |
| [**PROCESSOR\_NUMBER**](/windows/win32/WinNT/ns-winnt-_processor_number?branch=master)<br/>                                                  | Represents a logical processor in a processor group.<br/>                                     |
| [**PROCESSOR\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_processor_relationship?branch=master)<br/>                                      | Contains information about affinity within a processor group.<br/>                            |
| [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION\_EX**](/windows/win32/WinNT/ns-winnt-_system_logical_processor_information_ex?branch=master)<br/> | Contains information about the relationships of logical processors and related hardware.<br/> |
| [**UMS\_CREATE\_THREAD\_ATTRIBUTES**](/windows/win32/WinNT/ns-winnt-_ums_create_thread_attributes?branch=master)<br/>                        | Specifies attributes for a UMS worker thread. <br/>                                           |
| [**UMS\_SCHEDULER\_STARTUP\_INFO**](/windows/win32/WinBase/ns-winbase-_ums_scheduler_startup_info?branch=master)<br/>                            | Specifies attributes for a UMS scheduler thread<br/>                                          |



 

 

 




