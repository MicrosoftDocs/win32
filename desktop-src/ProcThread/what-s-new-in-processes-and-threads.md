---
Description: 'Windows 7 and Windows Server 2008 R2 include the following new programming elements for processes and threads.'
ms.assetid: '69cd8713-b40c-4fec-a256-9c2ee3d73da5'
title: 'What''s New in Processes and Threads'
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
| [**CreateRemoteThreadEx**](createremotethreadex.md)<br/>                         | Creates a thread that runs in the virtual address space of another process and optionally specifies extended attributes such as processor group affinity.<br/> |
| [**GetActiveProcessorCount**](getactiveprocessorcount.md)<br/>                   | Returns the number of active processors in a processor group or in the system.<br/>                                                                            |
| [**GetActiveProcessorGroupCount**](getactiveprocessorgroupcount.md)<br/>         | Returns the number of active processor groups in the system.<br/>                                                                                              |
| [**GetCurrentProcessorNumberEx**](getcurrentprocessornumberex.md)<br/>           | Retrieves the processor group and number of the logical processor in which the calling thread is running.<br/>                                                 |
| [**GetLogicalProcessorInformationEx**](getlogicalprocessorinformationex.md)<br/> | Retrieves information about the relationships of logical processors and related hardware.<br/>                                                                 |
| [**GetMaximumProcessorCount**](getmaximumprocessorcount.md)<br/>                 | Returns the maximum number of logical processors that a processor group or the system can have.<br/>                                                           |
| [**GetMaximumProcessorGroupCount**](getmaximumprocessorgroupcount.md)<br/>       | Returns the maximum number of processor groups that the system can have. <br/>                                                                                 |
| [**GetNumaAvailableMemoryNodeEx**](getnumaavailablememorynodeex.md)<br/>         | Retrieves the amount of memory that is available in the specified node as a USHORT value.<br/>                                                                 |
| [**GetNumaNodeNumberFromHandle**](getnumanodenumberfromhandle.md)<br/>           | Retrieves the NUMA node associated with the underlying device for a file handle.<br/>                                                                          |
| [**GetNumaNodeProcessorMaskEx**](getnumanodeprocessormaskex.md)<br/>             | Retrieves the processor mask for the specified NUMA node as a USHORT value.<br/>                                                                               |
| [**GetNumaProcessorNodeEx**](getnumaprocessornodeex.md)<br/>                     | Retrieves the node number of the specified logical processor as a USHORT value.<br/>                                                                           |
| [**GetNumaProximityNodeEx**](getnumaproximitynodeex.md)<br/>                     | Retrieves the node number as a USHORT value for the specified proximity identifier.<br/>                                                                       |
| [**GetProcessGroupAffinity**](getprocessgroupaffinity.md)<br/>                   | Retrieves the processor group affinity of the specified process.<br/>                                                                                          |
| [**GetProcessorSystemCycleTime**](getprocessorsystemcycletime.md)<br/>           | Retrieves the cycle time each processor in the specified group spent executing deferred procedure calls (DPCs) and interrupt service routines (ISRs).<br/>     |
| [**GetThreadGroupAffinity**](getthreadgroupaffinity.md)<br/>                     | Retrieves the processor group affinity of the specified thread.<br/>                                                                                           |
| [**GetThreadIdealProcessorEx**](getthreadidealprocessorex.md)<br/>               | Retrieves the processor number of the ideal processor for the specified thread.<br/>                                                                           |
| [**QueryIdleProcessorCycleTimeEx**](queryidleprocessorcycletimeex.md)<br/>       | Retrieves the accumulated cycle time for the idle thread on each logical processor in the specified processor group. <br/>                                     |
| [**SetThreadGroupAffinity**](setthreadgroupaffinity.md)<br/>                     | Sets the processor group affinity for the specified thread.<br/>                                                                                               |
| [**SetThreadIdealProcessorEx**](setthreadidealprocessorex.md)<br/>               | Sets the ideal processor for the specified thread and optionally retrieves the previous ideal processor.<br/>                                                  |



 

The following new functions are used with thread pools.



| Function                                                                              | Description                                                                                                    |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**QueryThreadpoolStackInformation**](querythreadpoolstackinformation.md)<br/> | Retrieves the stack reserve and commit sizes for threads in the specified thread pool.<br/>              |
| [**SetThreadpoolCallbackPersistent**](setthreadpoolcallbackpersistent.md)<br/> | Specifies that the callback should run on a persistent thread.<br/>                                      |
| [**SetThreadpoolCallbackPriority**](setthreadpoolcallbackpriority.md)<br/>     | Specifies the priority of a callback function relative to other work items in the same thread pool.<br/> |
| [**SetThreadpoolStackInformation**](setthreadpoolstackinformation.md)<br/>     | Sets the stack reserve and commit sizes for new threads in the specified thread pool. <br/>              |



 

The following new functions are used with UMS.



| Function                                                                          | Description                                                                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**CreateUmsCompletionList**](createumscompletionlist.md)<br/>             | Creates a UMS completion list.<br/>                                                                     |
| [**CreateUmsThreadContext**](createumsthreadcontext.md)<br/>               | Creates a UMS thread context to represent a UMS worker thread.<br/>                                     |
| [**DeleteUmsCompletionList**](deleteumscompletionlist.md)<br/>             | Deletes the specified UMS completion list. The list must be empty.<br/>                                 |
| [**DeleteUmsThreadContext**](deleteumsthreadcontext.md)<br/>               | Deletes the specified UMS thread context. The thread must be terminated.<br/>                           |
| [**DequeueUmsCompletionListItems**](dequeueumscompletionlistitems.md)<br/> | Retrieves UMS worker threads from the specified UMS completion list.<br/>                               |
| [**EnterUmsSchedulingMode**](enterumsschedulingmode.md)<br/>               | Converts the calling thread into a UMS scheduler thread.<br/>                                           |
| [**ExecuteUmsThread**](executeumsthread.md)<br/>                           | Runs the specified UMS worker thread.<br/>                                                              |
| [**GetCurrentUmsThread**](getcurrentumsthread.md)<br/>                     | Returns the UMS thread context of the calling UMS thread.<br/>                                          |
| [**GetNextUmsListItem**](getnextumslistitem.md)<br/>                       | Returns the next UMS thread context in a list of UMS thread contexts.<br/>                              |
| [**GetUmsCompletionListEvent**](getumscompletionlistevent.md)<br/>         | Retrieves a handle to the event associated with the specified UMS completion list.<br/>                 |
| [**QueryUmsThreadInformation**](queryumsthreadinformation.md)<br/>         | Retrieves information about the specified UMS worker thread.<br/>                                       |
| [**SetUmsThreadInformation**](setumsthreadinformation.md)<br/>             | Sets application-specific context information for the specified UMS worker thread.<br/>                 |
| [*UmsSchedulerProc*](umsschedulerproc.md)<br/>                             | The application-defined UMS scheduler entry point function associated with a UMS completion list. <br/> |
| [**UmsThreadYield**](umsthreadyield.md)<br/>                               | Yields control to the UMS scheduler thread on which the calling UMS worker thread is running.<br/>      |



 

## New Structures



| Structure                                                                                                 | Description                                                                                         |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**CACHE\_RELATIONSHIP**](cache-relationship.md)<br/>                                              | Describes cache attributes. <br/>                                                             |
| [**GROUP\_AFFINITY**](group-affinity.md)<br/>                                                      | Contains a processor group-specific affinity, such as the affinity of a thread.<br/>          |
| [**GROUP\_RELATIONSHIP**](group-relationship.md)<br/>                                              | Contains information about processor groups. <br/>                                            |
| [**NUMA\_NODE\_RELATIONSHIP**](numa-node-relationship.md)<br/>                                     | Contains information about a NUMA node in a processor group. <br/>                            |
| [**PROCESSOR\_GROUP\_INFO**](processor-group-info.md)<br/>                                         | Contains the number and affinity of processors in a processor group.<br/>                     |
| [**PROCESSOR\_NUMBER**](processor-number.md)<br/>                                                  | Represents a logical processor in a processor group.<br/>                                     |
| [**PROCESSOR\_RELATIONSHIP**](processor-relationship.md)<br/>                                      | Contains information about affinity within a processor group.<br/>                            |
| [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION\_EX**](system-logical-processor-information-ex.md)<br/> | Contains information about the relationships of logical processors and related hardware.<br/> |
| [**UMS\_CREATE\_THREAD\_ATTRIBUTES**](ums-create-thread-attributes.md)<br/>                        | Specifies attributes for a UMS worker thread. <br/>                                           |
| [**UMS\_SCHEDULER\_STARTUP\_INFO**](ums-scheduler-startup-info.md)<br/>                            | Specifies attributes for a UMS scheduler thread<br/>                                          |



 

 

 




