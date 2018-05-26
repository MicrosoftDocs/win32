---
Description: This topic describes the process and thread functions.
ms.assetid: 8c8e8af0-bf50-4a4b-945c-83bae1eff7dd
title: Process and Thread Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Process and Thread Functions

This topic describes the process and thread functions.

-   [Dispatch Queue Function](#dispatch-queue-function)
-   [Process Functions](#process-functions)
-   [Process Enumeration Functions](#process-enumeration-functions)
-   [Policy Functions](#policy-functions)
-   [Thread Functions](#process-and-thread-functions)
-   [Process and Thread Extended Attribute Functions](#process-and-thread-extended-attribute-functions)
-   [WOW64 Functions](#wow64-functions)
-   [Job Object Functions](#job-object-functions)
-   [Thread Pool Functions](#thread-pool-functions)
-   [Thread Ordering Service Functions](#thread-ordering-service-functions)
-   [Multimedia Class Scheduler Service Functions](#multimedia-class-scheduler-service-functions)
-   [Fiber Functions](#fiber-functions)
-   [NUMA Support Functions](#numa-support-functions)
-   [Processor Functions](#processor-functions)
-   [User-Mode Scheduling Functions](#user-mode-scheduling-functions)
-   [Obsolete Functions](#obsolete-functions)

## Dispatch Queue Function

The following function creates a [DispatcherQueueController](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueuecontroller).



| Function                                                                   | Description                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDispatcherQueueController**](/windows/win32/DispatcherQueue/nf-dispatcherqueue-createdispatcherqueuecontroller?branch=master) | Creates a [DispatcherQueueController](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueuecontroller) which manages the lifetime of a [DispatcherQueue](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueue) that runs queued tasks in priority order on another thread. |



 

## Process Functions

The following functions are used with [processes](child-processes.md).



| Function                                                                 | Description                                                                                                                                                                                   |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateProcess**](/windows/win32/WinBase/nf-processthreadsapi-createprocessa?branch=master)                                   | Creates a new process and its primary thread.                                                                                                                                                 |
| [**CreateProcessAsUser**](createprocessasuser.md)                       | Creates a new process and its primary thread. The new process runs in the security context of the user represented by the specified token.                                                    |
| [**CreateProcessWithLogonW**](/windows/win32/WinBase/nf-winbase-createprocesswithlogonw?branch=master)               | Creates a new process and its primary thread. The new process then runs the specified executable file in the security context of the specified credentials (user, domain, and password).      |
| [**CreateProcessWithTokenW**](/windows/win32/WinBase/nf-winbase-createprocesswithtokenw?branch=master)               | Creates a new process and its primary thread. The new process runs in the security context of the specified token.                                                                            |
| [**ExitProcess**](/windows/win32/WinBase/nf-processthreadsapi-exitprocess?branch=master)                                       | Ends the calling process and all its threads.                                                                                                                                                 |
| [**FlushProcessWriteBuffers**](/windows/win32/WinBase/nf-processthreadsapi-flushprocesswritebuffers?branch=master)             | Flushes the write queue of each processor that is running a thread of the current process.                                                                                                    |
| [**FreeEnvironmentStrings**](/windows/win32/WinBase/?branch=master)                 | Frees a block of environment strings.                                                                                                                                                         |
| [**GetCommandLine**](/windows/win32/WinBase/?branch=master)                                 | Retrieves the command-line string for the current process.                                                                                                                                    |
| [**GetCurrentProcess**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentprocess?branch=master)                           | Retrieves a pseudo handle for the current process.                                                                                                                                            |
| [**GetCurrentProcessId**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentprocessid?branch=master)                       | Retrieves the process identifier of the calling process.                                                                                                                                      |
| [**GetCurrentProcessorNumber**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentprocessornumber?branch=master)           | Retrieves the number of the processor the current thread was running on during the call to this function.                                                                                     |
| [**GetEnvironmentStrings**](/windows/win32/WinBase/?branch=master)                   | Retrieves the environment block for the current process.                                                                                                                                      |
| [**GetEnvironmentVariable**](/windows/win32/WinBase/nf-winbase-getenvironmentvariable?branch=master)                 | Retrieves the value of the specified variable from the environment block of the calling process.                                                                                              |
| [**GetExitCodeProcess**](/windows/win32/WinBase/nf-processthreadsapi-getexitcodeprocess?branch=master)                         | Retrieves the termination status of the specified process.                                                                                                                                    |
| [**GetGuiResources**](/windows/win32/Winuser/nf-winuser-getguiresources?branch=master)                               | Retrieves the count of handles to graphical user interface (GUI) objects in use by the specified process.                                                                                     |
| [**GetLogicalProcessorInformation**](/windows/win32/WinBase/?branch=master) | Retrieves information about logical processors and related hardware.                                                                                                                          |
| [**GetPriorityClass**](/windows/win32/WinBase/nf-processthreadsapi-getpriorityclass?branch=master)                             | Retrieves the priority class for the specified process.                                                                                                                                       |
| [**GetProcessAffinityMask**](/windows/win32/WinBase/nf-winbase-getprocessaffinitymask?branch=master)                 | Retrieves a process affinity mask for the specified process and the system affinity mask for the system.                                                                                      |
| [**GetProcessGroupAffinity**](/windows/win32/WinBase/?branch=master)               | Retrieves the processor group affinity of the specified process.                                                                                                                              |
| [**GetProcessHandleCount**](/windows/win32/WinBase/nf-processthreadsapi-getprocesshandlecount?branch=master)                   | Retrieves the number of open handles that belong to the specified process.                                                                                                                    |
| [**GetProcessId**](/windows/win32/WinBase/nf-processthreadsapi-getprocessid?branch=master)                                     | Retrieves the process identifier of the specified process.                                                                                                                                    |
| [**GetProcessIdOfThread**](/windows/win32/WinBase/nf-processthreadsapi-getprocessidofthread?branch=master)                     | Retrieves the process identifier of the process associated with the specified thread.                                                                                                         |
| [**GetProcessIoCounters**](/windows/win32/WinBase/nf-winbase-getprocessiocounters?branch=master)                     | Retrieves accounting information for all I/O operations performed by the specified process.                                                                                                   |
| [**GetProcessMitigationPolicy**](/windows/win32/Processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy?branch=master)         | Retrieves mitigation policy settings for the calling process.                                                                                                                                 |
| [**GetProcessPriorityBoost**](getprocesspriorityboost.md)               | Retrieves the priority boost control state of the specified process.                                                                                                                          |
| [**GetProcessShutdownParameters**](getprocessshutdownparameters.md)     | Retrieves shutdown parameters for the currently calling process.                                                                                                                              |
| [**GetProcessTimes**](/windows/win32/WinBase/nf-processthreadsapi-getprocesstimes?branch=master)                               | Retrieves timing information about for the specified process.                                                                                                                                 |
| [**GetProcessVersion**](/windows/win32/WinBase/nf-processthreadsapi-getprocessversion?branch=master)                           | Retrieves the major and minor version numbers of the system on which the specified process expects to run.                                                                                    |
| [**GetProcessWorkingSetSize**](/windows/win32/WinBase/nf-winbase-getprocessworkingsetsize?branch=master)             | Retrieves the minimum and maximum working set sizes of the specified process.                                                                                                                 |
| [**GetProcessWorkingSetSizeEx**](/windows/win32/WinBase/nf-memoryapi-getprocessworkingsetsizeex?branch=master)         | Retrieves the minimum and maximum working set sizes of the specified process.                                                                                                                 |
| [**GetProcessorSystemCycleTime**](/windows/win32/WinBase/?branch=master)       | Retrieves the cycle time each processor in the specified group spent executing deferred procedure calls (DPCs) and interrupt service routines (ISRs).                                         |
| [**GetStartupInfo**](/windows/win32/WinBase/nf-winbase-getstartupinfoa?branch=master)                                 | Retrieves the contents of the [**STARTUPINFO**](/windows/win32/WinBase/ns-processthreadsapi-_startupinfoa?branch=master) structure that was specified when the calling process was created.                                                       |
| [**IsImmersiveProcess**](/windows/win32/Winuser/nf-winuser-isimmersiveprocess?branch=master)                         | Determines whether the process belongs to a Windows Store app.                                                                                                                                |
| [**NeedCurrentDirectoryForExePath**](/windows/win32/WinBase/?branch=master) | Determines whether the current directory should be included in the search path for the specified executable.                                                                                  |
| [**OpenProcess**](/windows/win32/WinBase/nf-processthreadsapi-openprocess?branch=master)                                       | Opens an existing local process object.                                                                                                                                                       |
| [**QueryFullProcessImageName**](/windows/win32/WinBase/nf-winbase-queryfullprocessimagenamea?branch=master)           | Retrieves the full name of the executable image for the specified process.                                                                                                                    |
| [**QueryProcessAffinityUpdateMode**](/windows/win32/WinBase/nf-processthreadsapi-queryprocessaffinityupdatemode?branch=master) | Retrieves the affinity update mode of the specified process.                                                                                                                                  |
| [**QueryProcessCycleTime**](/windows/win32/WinBase/nf-realtimeapiset-queryprocesscycletime?branch=master)                   | Retrieves the sum of the cycle time of all threads of the specified process.                                                                                                                  |
| [**SetEnvironmentVariable**](/windows/win32/WinBase/nf-winbase-setenvironmentvariable?branch=master)                 | Sets the value of an environment variable for the current process.                                                                                                                            |
| [**SetPriorityClass**](/windows/win32/WinBase/nf-processthreadsapi-setpriorityclass?branch=master)                             | Sets the priority class for the specified process.                                                                                                                                            |
| [**SetProcessAffinityMask**](/windows/win32/WinBase/nf-winbase-setprocessaffinitymask?branch=master)                 | Sets a processor affinity mask for the threads of a specified process.                                                                                                                        |
| [**SetProcessAffinityUpdateMode**](/windows/win32/WinBase/nf-processthreadsapi-setprocessaffinityupdatemode?branch=master)     | Sets the affinity update mode of the specified process.                                                                                                                                       |
| [**SetProcessInformation**](setprocessinformation.md)                   | Sets information for the specified process.                                                                                                                                                   |
| [**SetProcessMitigationPolicy**](/windows/win32/Processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy?branch=master)         | Sets the mitigation policy for the calling process.                                                                                                                                           |
| [**SetProcessPriorityBoost**](setprocesspriorityboost.md)               | Disables the ability of the system to temporarily boost the priority of the threads of the specified process.                                                                                 |
| [**SetProcessRestrictionExemption**](/windows/win32/Winuser/nf-winuser-setprocessrestrictionexemption?branch=master) | Exempts the calling process from restrictions preventing desktop processes from interacting with the Windows Store app environment. This function is used by development and debugging tools. |
| [**SetProcessShutdownParameters**](/windows/win32/WinBase/nf-processthreadsapi-setprocessshutdownparameters?branch=master)     | Sets shutdown parameters for the currently calling process.                                                                                                                                   |
| [**SetProcessWorkingSetSize**](/windows/win32/WinBase/nf-winbase-setprocessworkingsetsize?branch=master)             | Sets the minimum and maximum working set sizes for the specified process.                                                                                                                     |
| [**SetProcessWorkingSetSizeEx**](/windows/win32/WinBase/nf-memoryapi-setprocessworkingsetsizeex?branch=master)         | Sets the minimum and maximum working set sizes for the specified process.                                                                                                                     |
| [**TerminateProcess**](/windows/win32/WinBase/nf-processthreadsapi-terminateprocess?branch=master)                             | Terminates the specified process and all of its threads.                                                                                                                                      |



 

## Process Enumeration Functions

The following functions are used to enumerate processes.



| Function                                                    | Description                                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**EnumProcesses**](base.enumprocesses)                     | Retrieves the process identifier for each process object in the system.            |
| [**Process32First**](base.process32first)                   | Retrieves information about the first process encountered in a system snapshot.    |
| [**Process32Next**](base.process32next)                     | Retrieves information about the next process recorded in a system snapshot.        |
| [**WTSEnumerateProcesses**](termserv.wtsenumerateprocesses) | Retrieves information about the active processes on the specified terminal server. |



 

## Policy Functions

The following functions are used with process wide policy.



|                                                      |                                                       |
|------------------------------------------------------|-------------------------------------------------------|
| Function                                             | Description                                           |
| [**QueryProtectedPolicy**](queryprotectedpolicy.md) | Queries the value associated with a protected policy. |
| [**SetProtectedPolicy**](setprotectedpolicy.md)     | Sets a protected policy.                              |



 

## Thread Functions

The following functions are used with [threads](multiple-threads.md).



| Function                                                           | Description                                                                                                                                               |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachThreadInput**](/windows/win32/Winuser/nf-winuser-attachthreadinput?branch=master)                     | Attaches the input processing mechanism of one thread to that of another thread.                                                                          |
| [**CreateRemoteThread**](/windows/win32/WinBase/nf-processthreadsapi-createremotethread?branch=master)                   | Creates a thread that runs in the virtual address space of another process.                                                                               |
| [**CreateRemoteThreadEx**](/windows/win32/WinBase/nf-processthreadsapi-createremotethreadex?branch=master)               | Creates a thread that runs in the virtual address space of another process and optionally specifies extended attributes such as processor group affinity. |
| [**CreateThread**](/windows/win32/WinBase/nf-processthreadsapi-createthread?branch=master)                               | Creates a thread to execute within the virtual address space of the calling process.                                                                      |
| [**ExitThread**](/windows/win32/WinBase/nf-processthreadsapi-exitthread?branch=master)                                   | Ends the calling thread.                                                                                                                                  |
| [**GetCurrentThread**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentthread?branch=master)                       | Retrieves a pseudo handle for the current thread.                                                                                                         |
| [**GetCurrentThreadId**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentthreadid?branch=master)                   | Retrieves the thread identifier of the calling thread.                                                                                                    |
| [**GetExitCodeThread**](/windows/win32/WinBase/nf-processthreadsapi-getexitcodethread?branch=master)                     | Retrieves the termination status of the specified thread.                                                                                                 |
| [**GetThreadDescription**](/windows/win32/ProcessThreadsApi/nf-processthreadsapi-getthreaddescription?branch=master)               | Retrieves the description that was assigned to a thread by calling [**SetThreadDescription**](/windows/win32/ProcessThreadsApi/nf-processthreadsapi-setthreaddescription?branch=master).                                  |
| [**GetThreadGroupAffinity**](/windows/win32/WinBase/?branch=master)           | Retrieves the processor group affinity of the specified thread.                                                                                           |
| [**GetThreadId**](/windows/win32/WinBase/nf-processthreadsapi-getthreadid?branch=master)                                 | Retrieves the thread identifier of the specified thread.                                                                                                  |
| [**GetThreadIdealProcessorEx**](/windows/win32/WinBase/nf-processthreadsapi-getthreadidealprocessorex?branch=master)     | Retrieves the processor number of the ideal processor for the specified thread.                                                                           |
| [**GetThreadInformation**](getthreadinformation.md)               | Retrieves information about the specified thread.                                                                                                         |
| [**GetThreadIOPendingFlag**](getthreadiopendingflag.md)           | Determines whether a specified thread has any I/O requests pending.                                                                                       |
| [**GetThreadPriority**](/windows/win32/WinBase/nf-processthreadsapi-getthreadpriority?branch=master)                     | Retrieves the priority value for the specified thread.                                                                                                    |
| [**GetThreadPriorityBoost**](/windows/win32/WinBase/nf-processthreadsapi-getthreadpriorityboost?branch=master)           | Retrieves the priority boost control state of the specified thread.                                                                                       |
| [**GetThreadTimes**](/windows/win32/WinBase/nf-processthreadsapi-getthreadtimes?branch=master)                           | Retrieves timing information for the specified thread.                                                                                                    |
| [**OpenThread**](/windows/win32/WinBase/nf-processthreadsapi-openthread?branch=master)                                   | Opens an existing thread object.                                                                                                                          |
| [**QueryIdleProcessorCycleTime**](/windows/win32/WinBase/nf-realtimeapiset-queryidleprocessorcycletime?branch=master) | Retrieves the cycle time for the idle thread of each processor in the system.                                                                             |
| [**QueryThreadCycleTime**](/windows/win32/WinBase/nf-realtimeapiset-querythreadcycletime?branch=master)               | Retrieves the cycle time for the specified thread.                                                                                                        |
| [**ResumeThread**](/windows/win32/WinBase/nf-processthreadsapi-resumethread?branch=master)                               | Decrements a thread's suspend count.                                                                                                                      |
| [**SetThreadAffinityMask**](/windows/win32/WinBase/nf-winbase-setthreadaffinitymask?branch=master)             | Sets a processor affinity mask for the specified thread.                                                                                                  |
| [**SetThreadDescription**](/windows/win32/ProcessThreadsApi/nf-processthreadsapi-setthreaddescription?branch=master)               | Assigns a description to a thread.                                                                                                                        |
| [**SetThreadGroupAffinity**](/windows/win32/WinBase/?branch=master)           | Sets the processor group affinity for the specified thread.                                                                                               |
| [**SetThreadIdealProcessor**](setthreadidealprocessor.md)         | Specifies a preferred processor for a thread.                                                                                                             |
| [**SetThreadIdealProcessorEx**](/windows/win32/WinBase/nf-processthreadsapi-setthreadidealprocessorex?branch=master)     | Sets the ideal processor for the specified thread and optionally retrieves the previous ideal processor.                                                  |
| [**SetThreadInformation**](setthreadinformation.md)               | Sets information for the specified thread.                                                                                                                |
| [**SetThreadPriority**](/windows/win32/WinBase/nf-processthreadsapi-setthreadpriority?branch=master)                     | Sets the priority value for the specified thread.                                                                                                         |
| [**SetThreadPriorityBoost**](/windows/win32/WinBase/nf-processthreadsapi-setthreadpriorityboost?branch=master)           | Disables the ability of the system to temporarily boost the priority of a thread.                                                                         |
| [**SetThreadStackGuarantee**](/windows/win32/WinBase/nf-processthreadsapi-setthreadstackguarantee?branch=master)         | Sets the stack guarantee for the calling thread.                                                                                                          |
| [**Sleep**](/windows/win32/WinBase/nf-synchapi-sleep?branch=master)                                             | Suspends the execution of the current thread for a specified interval.                                                                                    |
| [**SleepEx**](/windows/win32/WinBase/nf-synchapi-sleepex?branch=master)                                         | Suspends the current thread until the specified condition is met.                                                                                         |
| [**SuspendThread**](/windows/win32/WinBase/nf-processthreadsapi-suspendthread?branch=master)                             | Suspends the specified thread.                                                                                                                            |
| [**SwitchToThread**](/windows/win32/WinBase/nf-processthreadsapi-switchtothread?branch=master)                           | Causes the calling thread to yield execution to another thread that is ready to run on the current processor.                                             |
| [**TerminateThread**](/windows/win32/WinBase/nf-processthreadsapi-terminatethread?branch=master)                         | Terminates a thread.                                                                                                                                      |
| [**ThreadProc**](/windows/win32/WinBase/?branch=master)                                   | An application-defined function that serves as the starting address for a thread.                                                                         |
| [**TlsAlloc**](/windows/win32/WinBase/nf-processthreadsapi-tlsalloc?branch=master)                                       | Allocates a thread local storage (TLS) index.                                                                                                             |
| [**TlsFree**](/windows/win32/WinBase/nf-processthreadsapi-tlsfree?branch=master)                                         | Releases a TLS index.                                                                                                                                     |
| [**TlsGetValue**](/windows/win32/WinBase/nf-processthreadsapi-tlsgetvalue?branch=master)                                 | Retrieves the value in the calling thread's TLS slot for a specified TLS index.                                                                           |
| [**TlsSetValue**](/windows/win32/WinBase/nf-processthreadsapi-tlssetvalue?branch=master)                                 | Stores a value in the calling thread's TLS slot for a specified TLS index.                                                                                |
| [**WaitForInputIdle**](/windows/win32/Winuser/nf-winuser-waitforinputidle?branch=master)                       | Waits until the specified process is waiting for user input with no input pending, or until the time-out interval has elapsed.                            |



 

## Process and Thread Extended Attribute Functions

The following functions are used to set extended attributes for process and thread creation.



| Function                                                                       | Description                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DeleteProcThreadAttributeList**](/windows/win32/WinBase/nf-processthreadsapi-deleteprocthreadattributelist?branch=master)         | Deletes the specified list of attributes for process and thread creation.                            |
| [**InitializeProcThreadAttributeList**](/windows/win32/WinBase/nf-processthreadsapi-initializeprocthreadattributelist?branch=master) | Initializes the specified list of attributes for process and thread creation.                        |
| [**UpdateProcThreadAttribute**](/windows/win32/WinBase/nf-processthreadsapi-updateprocthreadattribute?branch=master)                 | Updates the specified attribute in the specified list of attributes for process and thread creation. |



 

## WOW64 Functions

The following functions are used with [WOW64](winprog64.running_32_bit_applications).



| Function                                         | Description                                                                                                                            |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**IsWow64Message**](/windows/win32/Winuser/nf-winuser-iswow64message?branch=master)         | Determines whether the last message read from the current thread's queue originated from a WOW64 process.                              |
| [**IsWow64Process**](/windows/win32/WinBase/nf-wow64apiset-iswow64process?branch=master)         | Determines whether the specified process is running under WOW64.                                                                       |
| [**IsWow64Process2**](/windows/win32/wow64apiset/nf-wow64apiset-iswow64process2?branch=master)       | Determines whether the specified process is running under WOW64; also returns additional machine process and architecture information. |
| [**Wow64SuspendThread**](/windows/win32/WinBase/nf-winbase-wow64suspendthread?branch=master) | Suspends the specified WOW64 thread.                                                                                                   |



 

## Job Object Functions

The following functions are used with [job objects](job-objects.md).



| Function                                                       | Description                                                                                          |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**AssignProcessToJobObject**](assignprocesstojobobject.md)   | Associates a process with an existing job object.                                                    |
| [**CreateJobObject**](/windows/win32/WinBase/nf-winbase-createjobobjecta?branch=master)                     | Creates or opens a job object.                                                                       |
| [**IsProcessInJob**](/windows/win32/WinBase/?branch=master)                       | Determines whether the process is running in the specified job.                                      |
| [**OpenJobObject**](/windows/win32/WinBase/nf-winbase-openjobobjecta?branch=master)                         | Opens an existing job object.                                                                        |
| [**QueryInformationJobObject**](queryinformationjobobject.md) | Retrieves limit and job state information from the job object.                                       |
| [**SetInformationJobObject**](setinformationjobobject.md)     | Set limits for a job object.                                                                         |
| [**TerminateJobObject**](terminatejobobject.md)               | Terminates all processes currently associated with the job.                                          |
| [**UserHandleGrantAccess**](/windows/win32/Winuser/nf-winuser-userhandlegrantaccess?branch=master)         | Grants or denies access to a handle to a User object to a job that has a user-interface restriction. |



 

## Thread Pool Functions

The following functions are used with [thread pools](thread-pools.md).



| Function                                                                                   | Description                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallbackMayRunLong**](/windows/win32/WinBase/nf-threadpoolapiset-callbackmayrunlong?branch=master)                                           | Indicates that the callback may not return quickly.                                                                                                                                                                                                 |
| [**CancelThreadpoolIo**](/windows/win32/WinBase/nf-threadpoolapiset-cancelthreadpoolio?branch=master)                                           | Cancels the notification from the [**StartThreadpoolIo**](/windows/win32/WinBase/nf-threadpoolapiset-startthreadpoolio?branch=master) function.                                                                                                                                                          |
| [**CloseThreadpool**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpool?branch=master)                                                 | Closes the specified thread pool.                                                                                                                                                                                                                   |
| [**CloseThreadpoolCleanupGroup**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpoolcleanupgroup?branch=master)                         | Closes the specified cleanup group.                                                                                                                                                                                                                 |
| [**CloseThreadpoolCleanupGroupMembers**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpoolcleanupgroupmembers?branch=master)           | Releases the members of the specified cleanup group, waits for all callback functions to complete, and optionally cancels any outstanding callback functions.                                                                                       |
| [**CloseThreadpoolIo**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpoolio?branch=master)                                             | Releases the specified I/O completion object.                                                                                                                                                                                                       |
| [**CloseThreadpoolTimer**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpooltimer?branch=master)                                       | Releases the specified timer object.                                                                                                                                                                                                                |
| [**CloseThreadpoolWait**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpoolwait?branch=master)                                         | Releases the specified wait object.                                                                                                                                                                                                                 |
| [**CloseThreadpoolWork**](/windows/win32/WinBase/nf-threadpoolapiset-closethreadpoolwork?branch=master)                                         | Releases the specified work object.                                                                                                                                                                                                                 |
| [**CreateThreadpool**](/windows/win32/WinBase/nf-threadpoolapiset-createthreadpool?branch=master)                                               | Allocates a new pool of threads to execute callbacks.                                                                                                                                                                                               |
| [**CreateThreadpoolCleanupGroup**](/windows/win32/WinBase/nf-threadpoolapiset-createthreadpoolcleanupgroup?branch=master)                       | Creates a cleanup group that applications can use to track one or more thread pool callbacks.                                                                                                                                                       |
| [**CreateThreadpoolIo**](/windows/win32/WinBase/nf-threadpoolapiset-createthreadpoolio?branch=master)                                           | Creates a new I/O completion object.                                                                                                                                                                                                                |
| [**CreateThreadpoolTimer**](/windows/win32/WinBase/nf-threadpoolapiset-createthreadpooltimer?branch=master)                                     | Creates a new timer object.                                                                                                                                                                                                                         |
| [**CreateThreadpoolWait**](/windows/win32/WinBase/nf-threadpoolapiset-createthreadpoolwait?branch=master)                                       | Creates a new wait object.                                                                                                                                                                                                                          |
| [**CreateThreadpoolWork**](createthreadpoolwork.md)                                       | Creates a new work object.                                                                                                                                                                                                                          |
| [**DestroyThreadpoolEnvironment**](/windows/win32/WinBase/nf-winbase-destroythreadpoolenvironment?branch=master)                       | Deletes the specified callback environment. Call this function when the callback environment is no longer needed for creating new thread pool objects.                                                                                              |
| [**DisassociateCurrentThreadFromCallback**](/windows/win32/WinBase/nf-threadpoolapiset-disassociatecurrentthreadfromcallback?branch=master)     | Removes the association between the currently executing callback function and the object that initiated the callback. The current thread will no longer count as executing a callback on behalf of the object.                                      |
| [**FreeLibraryWhenCallbackReturns**](/windows/win32/WinBase/nf-threadpoolapiset-freelibrarywhencallbackreturns?branch=master)                   | Specifies the DLL that the thread pool will unload when the current callback completes.                                                                                                                                                             |
| [**InitializeThreadpoolEnvironment**](/windows/win32/WinBase/nf-winbase-initializethreadpoolenvironment?branch=master)                 | Initializes a callback environment.                                                                                                                                                                                                                 |
| [**IsThreadpoolTimerSet**](/windows/win32/WinBase/nf-threadpoolapiset-isthreadpooltimerset?branch=master)                                       | Determines whether the specified timer object is currently set.                                                                                                                                                                                     |
| [**LeaveCriticalSectionWhenCallbackReturns**](/windows/win32/WinBase/nf-threadpoolapiset-leavecriticalsectionwhencallbackreturns?branch=master) | Specifies the critical section that the thread pool will release when the current callback completes.                                                                                                                                               |
| [**QueryThreadpoolStackInformation**](/windows/win32/WinBase/nf-threadpoolapiset-querythreadpoolstackinformation?branch=master)                 | Retrieves the stack reserve and commit sizes for threads in the specified thread pool.                                                                                                                                                              |
| [**ReleaseMutexWhenCallbackReturns**](/windows/win32/WinBase/nf-threadpoolapiset-releasemutexwhencallbackreturns?branch=master)                 | Specifies the mutex that the thread pool will release when the current callback completes.                                                                                                                                                          |
| [**ReleaseSemaphoreWhenCallbackReturns**](/windows/win32/WinBase/nf-threadpoolapiset-releasesemaphorewhencallbackreturns?branch=master)         | Specifies the semaphore that the thread pool will release when the current callback completes.                                                                                                                                                      |
| [**SetEventWhenCallbackReturns**](/windows/win32/WinBase/nf-threadpoolapiset-seteventwhencallbackreturns?branch=master)                         | Specifies the event that the thread pool will set when the current callback completes.                                                                                                                                                              |
| [**SetThreadpoolCallbackCleanupGroup**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackcleanupgroup?branch=master)             | Associates the specified cleanup group with the specified callback environment.                                                                                                                                                                     |
| [**SetThreadpoolCallbackLibrary**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbacklibrary?branch=master)                       | Ensures that the specified DLL remains loaded as long as there are outstanding callbacks.                                                                                                                                                           |
| [**SetThreadpoolCallbackPersistent**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackpersistent?branch=master)                 | Specifies that the callback should run on a persistent thread.                                                                                                                                                                                      |
| [**SetThreadpoolCallbackPool**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackpool?branch=master)                             | Sets the thread pool to be used when generating callbacks.                                                                                                                                                                                          |
| [**SetThreadpoolCallbackPriority**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackpriority?branch=master)                     | Specifies the priority of a callback function relative to other work items in the same thread pool.                                                                                                                                                 |
| [**SetThreadpoolCallbackRunsLong**](/windows/win32/WinBase/nf-winbase-setthreadpoolcallbackrunslong?branch=master)                     | Indicates that callbacks associated with this callback environment may not return quickly.                                                                                                                                                          |
| [**SetThreadpoolStackInformation**](/windows/win32/WinBase/nf-threadpoolapiset-setthreadpoolstackinformation?branch=master)                     | Sets the stack reserve and commit sizes for new threads in the specified thread pool.                                                                                                                                                               |
| [**SetThreadpoolThreadMaximum**](setthreadpoolthreadmaximum.md)                           | Sets the maximum number of threads that the specified thread pool can allocate to process callbacks.                                                                                                                                                |
| [**SetThreadpoolThreadMinimum**](/windows/win32/WinBase/nf-threadpoolapiset-setthreadpoolthreadminimum?branch=master)                           | Sets the minimum number of threads that the specified thread pool must make available to process callbacks.                                                                                                                                         |
| [**SetThreadpoolTimerEx**](/windows/win32/threadpoolapiset/nf-threadpoolapiset-setthreadpooltimerex?branch=master)                                       | Sets the timer object. A worker thread calls the timer object's callback after the specified timeout expires.                                                                                                                                       |
| [**SetThreadpoolTimer**](/windows/win32/WinBase/nf-threadpoolapiset-setthreadpooltimer?branch=master)                                           | Sets the timer object. A worker thread calls the timer object's callback after the specified timeout expires.                                                                                                                                       |
| [**SetThreadpoolWait**](/windows/win32/WinBase/nf-threadpoolapiset-setthreadpoolwait?branch=master)                                             | Sets the wait object. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.                                                                                           |
| [**SetThreadpoolWaitEx**](/windows/win32/threadpoolapiset/nf-threadpoolapiset-setthreadpoolwaitex?branch=master)                                         | Sets the wait object. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.                                                                                           |
| [**StartThreadpoolIo**](/windows/win32/WinBase/nf-threadpoolapiset-startthreadpoolio?branch=master)                                             | Notifies the thread pool that I/O operations may possibly begin for the specified I/O completion object. A worker thread calls the I/O completion object's callback function after the operation completes on the file handle bound to this object. |
| [**SubmitThreadpoolWork**](/windows/win32/WinBase/nf-threadpoolapiset-submitthreadpoolwork?branch=master)                                       | Posts a work object to the thread pool. A worker thread calls the work object's callback function.                                                                                                                                                  |
| [**TpInitializeCallbackEnviron**](/windows/win32/winnt/nf-winnt-tpinitializecallbackenviron?branch=master)                         | Initializes a callback environment for the thread pool.                                                                                                                                                                                             |
| [**TpDestroyCallbackEnviron**](/windows/win32/winnt/nf-winnt-tpdestroycallbackenviron?branch=master)                               | Deletes the specified callback environment. Call this function when the callback environment is no longer needed for creating new thread pool objects.                                                                                              |
| [**TpSetCallbackActivationContext**](/windows/win32/winnt/nf-winnt-tpsetcallbackactivationcontext?branch=master)                   | Assigns an activation context to the callback environment.                                                                                                                                                                                          |
| [**TpSetCallbackCleanupGroup**](/windows/win32/winnt/nf-winnt-tpsetcallbackcleanupgroup?branch=master)                             | Associates the specified cleanup group with the specified callback environment.                                                                                                                                                                     |
| [**TpSetCallbackFinalizationCallback**](/windows/win32/winnt/nf-winnt-tpsetcallbackfinalizationcallback?branch=master)             | Indicates a function to call when the callback environment is finalized.                                                                                                                                                                            |
| [**TpSetCallbackLongFunction**](/windows/win32/winnt/nf-winnt-tpsetcallbacklongfunction?branch=master)                             | Indicates that callbacks associated with this callback environment may not return quickly.                                                                                                                                                          |
| [**TpSetCallbackNoActivationContext**](/windows/win32/winnt/nf-winnt-tpsetcallbacknoactivationcontext?branch=master)               | Indicates that the callback environment has no activation context.                                                                                                                                                                                  |
| [**TpSetCallbackPersistent**](/windows/win32/winnt/nf-winnt-tpsetcallbackpersistent?branch=master)                                 | Specifies that the callback should run on a persistent thread.                                                                                                                                                                                      |
| [**TpSetCallbackPriority**](/windows/win32/winnt/nf-winnt-tpsetcallbackpriority?branch=master)                                     | Specifies the priority of a callback function relative to other work items in the same thread pool.                                                                                                                                                 |
| [**TpSetCallbackRaceWithDll**](/windows/win32/winnt/nf-winnt-tpsetcallbackracewithdll?branch=master)                               | Ensures that the specified DLL remains loaded as long as there are outstanding callbacks.                                                                                                                                                           |
| [**TpSetCallbackThreadpool**](/windows/win32/winnt/nf-winnt-tpsetcallbackthreadpool?branch=master)                                 | Assigns a thread pool to a callback environment.                                                                                                                                                                                                    |
| [**TrySubmitThreadpoolCallback**](/windows/win32/WinBase/nf-threadpoolapiset-trysubmitthreadpoolcallback?branch=master)                         | Requests that a thread pool worker thread call the specified callback function.                                                                                                                                                                     |
| [**WaitForThreadpoolIoCallbacks**](/windows/win32/WinBase/nf-threadpoolapiset-waitforthreadpooliocallbacks?branch=master)                       | Waits for outstanding I/O completion callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                           |
| [**WaitForThreadpoolTimerCallbacks**](/windows/win32/WinBase/nf-threadpoolapiset-waitforthreadpooltimercallbacks?branch=master)                 | Waits for outstanding timer callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                    |
| [**WaitForThreadpoolWaitCallbacks**](/windows/win32/WinBase/nf-threadpoolapiset-waitforthreadpoolwaitcallbacks?branch=master)                   | Waits for outstanding wait callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                     |
| [**WaitForThreadpoolWorkCallbacks**](/windows/win32/WinBase/nf-threadpoolapiset-waitforthreadpoolworkcallbacks?branch=master)                   | Waits for outstanding work callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                     |



 

The following functions are part of the original [thread pooling](thread-pooling.md) API.



| Function                                                            | Description                                                                                                                                                                                                            |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BindIoCompletionCallback**](/windows/win32/WinBase/nf-winbase-bindiocompletioncallback?branch=master)        | Associates the I/O completion port owned by the thread pool with the specified file handle. On completion of an I/O request involving this file, a non-I/O worker thread will execute the specified callback function. |
| [**QueueUserWorkItem**](/windows/win32/WinBase/?branch=master)                      | Queues a work item to a worker thread in the thread pool.                                                                                                                                                              |
| [**RegisterWaitForSingleObject**](base.registerwaitforsingleobject) | Directs a wait thread in the thread pool to wait on the object.                                                                                                                                                        |
| [**UnregisterWaitEx**](base.unregisterwaitex)                       | Waits until one or all of the specified objects are in the signaled state or the time-out interval elapses.                                                                                                            |



 

## Thread Ordering Service Functions

The following functions are used with the [thread ordering service](thread-ordering-service.md).



| Function                                                                   | Description                                                                                 |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**AvQuerySystemResponsiveness**](/windows/win32/Avrt/nf-avrt-avquerysystemresponsiveness?branch=master)         | Retrieves the system responsiveness setting used by the multimedia class scheduler service. |
| [**AvRtCreateThreadOrderingGroup**](/windows/win32/Avrt/nf-avrt-avrtcreatethreadorderinggroup?branch=master)     | Creates a thread ordering group.                                                            |
| [**AvRtCreateThreadOrderingGroupEx**](/windows/win32/Avrt/nf-avrt-avrtcreatethreadorderinggroupexa?branch=master) | Creates a thread ordering group and associates the server thread with a task.               |
| [**AvRtDeleteThreadOrderingGroup**](/windows/win32/Avrt/nf-avrt-avrtdeletethreadorderinggroup?branch=master)     | Deletes the specified thread ordering group created by the caller.                          |
| [**AvRtJoinThreadOrderingGroup**](/windows/win32/Avrt/nf-avrt-avrtjointhreadorderinggroup?branch=master)         | Joins client threads to a thread ordering group.                                            |
| [**AvRtLeaveThreadOrderingGroup**](/windows/win32/Avrt/nf-avrt-avrtleavethreadorderinggroup?branch=master)       | Enables client threads to leave a thread ordering group.                                    |
| [**AvRtWaitOnThreadOrderingGroup**](/windows/win32/Avrt/nf-avrt-avrtwaitonthreadorderinggroup?branch=master)     | Enables client threads of a thread ordering group to wait until they should execute.        |



 

## Multimedia Class Scheduler Service Functions

The following functions are used with the [multimedia class scheduler service](multimedia-class-scheduler-service.md).



| Function                                                                   | Description                                                                                           |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**AvRevertMmThreadCharacteristics**](/windows/win32/Avrt/nf-avrt-avrevertmmthreadcharacteristics?branch=master) | Indicates that a thread is no longer performing work associated with the specified task.              |
| [**AvSetMmMaxThreadCharacteristics**](/windows/win32/Avrt/nf-avrt-avsetmmmaxthreadcharacteristicsa?branch=master) | Associates the calling thread with the specified tasks.                                               |
| [**AvSetMmThreadCharacteristics**](/windows/win32/Avrt/nf-avrt-avsetmmthreadcharacteristicsa?branch=master)       | Associates the calling thread with the specified task.                                                |
| [**AvSetMmThreadPriority**](/windows/win32/Avrt/nf-avrt-avsetmmthreadpriority?branch=master)                     | Adjusts the thread priority of the calling thread relative to other threads performing the same task. |



 

## Fiber Functions

The following functions are used with [fibers](fibers.md).



| Function                                                 | Description                                                                                                  |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ConvertFiberToThread**](/windows/win32/WinBase/nf-winbase-convertfibertothread?branch=master)     | Converts the current fiber into a thread.                                                                    |
| [**ConvertThreadToFiber**](/windows/win32/WinBase/nf-winbase-convertthreadtofiber?branch=master)     | Converts the current thread into a fiber.                                                                    |
| [**ConvertThreadToFiberEx**](/windows/win32/WinBase/nf-winbase-convertthreadtofiberex?branch=master) | Converts the current thread into a fiber.                                                                    |
| [**CreateFiber**](/windows/win32/WinBase/nf-winbase-createfiber?branch=master)                       | Allocates a fiber object, assigns it a stack, and sets up execution to begin at the specified start address. |
| [**CreateFiberEx**](/windows/win32/WinBase/nf-winbase-createfiberex?branch=master)                   | Allocates a fiber object, assigns it a stack, and sets up execution to begin at the specified start address. |
| [**DeleteFiber**](/windows/win32/WinBase/nf-winbase-deletefiber?branch=master)                       | Deletes an existing fiber.                                                                                   |
| [**FiberProc**](fiberproc.md)                           | An application-defined function used with the [**CreateFiber**](/windows/win32/WinBase/nf-winbase-createfiber?branch=master) function.                   |
| [**FlsAlloc**](/windows/win32/WinBase/?branch=master)                             | Allocates a fiber local storage (FLS) index.                                                                 |
| [**FlsFree**](/windows/win32/WinBase/?branch=master)                               | Releases an FLS index.                                                                                       |
| [**FlsGetValue**](/windows/win32/WinBase/?branch=master)                       | Retrieves the value in the calling fiber's FLS slot for a specified FLS index.                               |
| [**FlsSetValue**](/windows/win32/WinBase/?branch=master)                       | Stores a value in the calling fiber's FLS slot for a specified FLS index.                                    |
| [**IsThreadAFiber**](/windows/win32/WinBase/?branch=master)                 | Determines whether the current thread is a fiber.                                                            |
| [**SwitchToFiber**](/windows/win32/WinBase/nf-winbase-switchtofiber?branch=master)                   | Schedules a fiber.                                                                                           |



 

## NUMA Support Functions

The following functions provide [NUMA support](numa-support.md).



| Function                                                                 | Description                                                                                                                                            |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPagesNuma**](base.allocateuserphysicalpagesnuma)  | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |
| [**GetLogicalProcessorInformation**](/windows/win32/WinBase/?branch=master) | Retrieves information about logical processors and related hardware.                                                                                   |
| [**GetNumaAvailableMemoryNode**](/windows/win32/WinBase/nf-winbase-getnumaavailablememorynode?branch=master)         | Retrieves the amount of memory available in the specified node.                                                                                        |
| [**GetNumaAvailableMemoryNodeEx**](/windows/win32/WinBase/nf-winbase-getnumaavailablememorynodeex?branch=master)     | Retrieves the amount of memory that is available in the specified node as a USHORT value.                                                              |
| [**GetNumaHighestNodeNumber**](/windows/win32/WinBase/?branch=master)             | Retrieves the node that currently has the highest number.                                                                                              |
| [**GetNumaNodeNumberFromHandle**](/windows/win32/WinBase/nf-winbase-getnumanodenumberfromhandle?branch=master)       | Retrieves the NUMA node associated with the underlying device for a file handle.                                                                       |
| [**GetNumaNodeProcessorMask**](/windows/win32/WinBase/nf-winbase-getnumanodeprocessormask?branch=master)             | Retrieves the processor mask for the specified node.                                                                                                   |
| [**GetNumaNodeProcessorMaskEx**](/windows/win32/WinBase/?branch=master)         | Retrieves the processor mask for the specified NUMA node as a USHORT value.                                                                            |
| [**GetNumaProcessorNode**](/windows/win32/WinBase/nf-winbase-getnumaprocessornode?branch=master)                     | Retrieves the node number for the specified processor.                                                                                                 |
| [**GetNumaProcessorNodeEx**](/windows/win32/WinBase/nf-winbase-getnumaprocessornodeex?branch=master)                 | Retrieves the node number of the specified logical processor as a USHORT value.                                                                        |
| [**GetNumaProximityNode**](/windows/win32/WinBase/nf-winbase-getnumaproximitynode?branch=master)                     | Retrieves the node number for the specified proximity identifier.                                                                                      |
| [**GetNumaProximityNodeEx**](/windows/win32/WinBase/?branch=master)                 | Retrieves the node number as a USHORT value for the specified proximity identifier.                                                                    |
| [**VirtualAllocExNuma**](base.virtualallocexnuma)                        | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |



 

## Processor Functions

The following functions are used with logical processors and [processor groups](processor-groups.md).



| Function                                                                     | Description                                                                                                          |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**GetActiveProcessorCount**](/windows/win32/WinBase/nf-winbase-getactiveprocessorcount?branch=master)                   | Returns the number of active processors in a processor group or in the system.                                       |
| [**GetActiveProcessorGroupCount**](/windows/win32/WinBase/nf-winbase-getactiveprocessorgroupcount?branch=master)         | Returns the number of active processor groups in the system.                                                         |
| [**GetCurrentProcessorNumber**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentprocessornumber?branch=master)               | Retrieves the number of the processor the current thread was running on during the call to this function.            |
| [**GetCurrentProcessorNumberEx**](/windows/win32/WinBase/nf-processthreadsapi-getcurrentprocessornumberex?branch=master)           | Retrieves the processor group and number of the logical processor in which the calling thread is running.            |
| [**GetLogicalProcessorInformation**](/windows/win32/WinBase/?branch=master)     | Retrieves information about logical processors and related hardware.                                                 |
| [**GetLogicalProcessorInformationEx**](/windows/win32/WinBase/?branch=master) | Retrieves information about the relationships of logical processors and related hardware.                            |
| [**GetMaximumProcessorCount**](/windows/win32/WinBase/nf-winbase-getmaximumprocessorcount?branch=master)                 | Returns the maximum number of logical processors that a processor group or the system can have.                      |
| [**GetMaximumProcessorGroupCount**](/windows/win32/WinBase/nf-winbase-getmaximumprocessorgroupcount?branch=master)       | Returns the maximum number of processor groups that the system can have.                                             |
| [**QueryIdleProcessorCycleTime**](/windows/win32/WinBase/nf-realtimeapiset-queryidleprocessorcycletime?branch=master)           | Retrieves the cycle time for the idle thread of each processor in the system.                                        |
| [**QueryIdleProcessorCycleTimeEx**](/windows/win32/WinBase/nf-realtimeapiset-queryidleprocessorcycletimeex?branch=master)       | Retrieves the accumulated cycle time for the idle thread on each logical processor in the specified processor group. |



 

## User-Mode Scheduling Functions

The following functions are used with user-mode scheduling (UMS).



| Function                                                               | Description                                                                                               |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**CreateUmsCompletionList**](/windows/win32/WinBase/nf-winbase-createumscompletionlist?branch=master)             | Creates a UMS completion list.                                                                            |
| [**CreateUmsThreadContext**](/windows/win32/WinBase/nf-winbase-createumsthreadcontext?branch=master)               | Creates a UMS thread context to represent a UMS worker thread.                                            |
| [**DeleteUmsCompletionList**](/windows/win32/WinBase/nf-winbase-deleteumscompletionlist?branch=master)             | Deletes the specified UMS completion list. The list must be empty.                                        |
| [**DeleteUmsThreadContext**](/windows/win32/WinBase/nf-winbase-deleteumsthreadcontext?branch=master)               | Deletes the specified UMS thread context. The thread must be terminated.                                  |
| [**DequeueUmsCompletionListItems**](/windows/win32/WinBase/nf-winbase-dequeueumscompletionlistitems?branch=master) | Retrieves UMS worker threads from the specified UMS completion list.                                      |
| [**EnterUmsSchedulingMode**](/windows/win32/WinBase/nf-winbase-enterumsschedulingmode?branch=master)               | Converts the calling thread into a UMS scheduler thread.                                                  |
| [**ExecuteUmsThread**](/windows/win32/WinBase/nf-winbase-executeumsthread?branch=master)                           | Runs the specified UMS worker thread.                                                                     |
| [**GetCurrentUmsThread**](/windows/win32/WinBase/nf-winbase-getcurrentumsthread?branch=master)                     | Returns the UMS thread context of the calling UMS thread.                                                 |
| [**GetNextUmsListItem**](/windows/win32/WinBase/nf-winbase-getnextumslistitem?branch=master)                       | Returns the next UMS thread context in a list of UMS thread contexts.                                     |
| [**GetUmsCompletionListEvent**](/windows/win32/WinBase/nf-winbase-getumscompletionlistevent?branch=master)         | Retrieves a handle to the event associated with the specified UMS completion list.                        |
| [**GetUmsSystemThreadInformation**](/windows/win32/WinBase/nf-winbase-getumssystemthreadinformation?branch=master) | Queries whether the specified thread is a UMS scheduler thread, a UMS worker thread, or a non-UMS thread. |
| [**QueryUmsThreadInformation**](/windows/win32/WinBase/nf-winbase-queryumsthreadinformation?branch=master)         | Retrieves information about the specified UMS worker thread.                                              |
| [**SetUmsThreadInformation**](/windows/win32/WinBase/nf-winbase-setumsthreadinformation?branch=master)             | Sets application-specific context information for the specified UMS worker thread.                        |
| [*UmsSchedulerProc*](/windows/win32/WinNT/nc-winnt-rtl_ums_scheduler_entry_point?branch=master)                             | The application-defined UMS scheduler entry point function associated with a UMS completion list.         |
| [**UmsThreadYield**](/windows/win32/WinBase/nf-winbase-umsthreadyield?branch=master)                               | Yields control to the UMS scheduler thread on which the calling UMS worker thread is running.             |



 

## Obsolete Functions

-   [**NtGetCurrentProcessorNumber**](ntgetcurrentprocessornumber.md)
-   [**NtQueryInformationProcess**](/windows/win32/Winternl/nf-winternl-ntqueryinformationprocess?branch=master)
-   [**NtQueryInformationThread**](/windows/win32/Winternl/nf-winternl-ntqueryinformationthread?branch=master)
-   [**WinExec**](/windows/win32/WinBase/nf-winbase-winexec?branch=master)
-   [**ZwQueryInformationProcess**](zwqueryinformationprocess.md)

 

 



