---
Description: This topic describes the process and thread functions.
ms.assetid: 8c8e8af0-bf50-4a4b-945c-83bae1eff7dd
title: Process and Thread Functions
ms.topic: article
ms.date: 05/31/2018
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
| [**CreateDispatcherQueueController**](/windows/desktop/api/DispatcherQueue/nf-dispatcherqueue-createdispatcherqueuecontroller) | Creates a [DispatcherQueueController](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueuecontroller) which manages the lifetime of a [DispatcherQueue](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueue) that runs queued tasks in priority order on another thread. |



 

## Process Functions

The following functions are used with [processes](child-processes.md).



| Function                                                                 | Description                                                                                                                                                                                   |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateProcess**](https://msdn.microsoft.com/library/ms682425(v=VS.85).aspx)                                   | Creates a new process and its primary thread.                                                                                                                                                 |
| [**CreateProcessAsUser**](https://msdn.microsoft.com/library/ms682429(v=VS.85).aspx)                       | Creates a new process and its primary thread. The new process runs in the security context of the user represented by the specified token.                                                    |
| [**CreateProcessWithLogonW**](/windows/desktop/api/WinBase/nf-winbase-createprocesswithlogonw)               | Creates a new process and its primary thread. The new process then runs the specified executable file in the security context of the specified credentials (user, domain, and password).      |
| [**CreateProcessWithTokenW**](/windows/desktop/api/WinBase/nf-winbase-createprocesswithtokenw)               | Creates a new process and its primary thread. The new process runs in the security context of the specified token.                                                                            |
| [**ExitProcess**](https://msdn.microsoft.com/library/ms682658(v=VS.85).aspx)                                       | Ends the calling process and all its threads.                                                                                                                                                 |
| [**FlushProcessWriteBuffers**](https://msdn.microsoft.com/library/ms683148(v=VS.85).aspx)             | Flushes the write queue of each processor that is running a thread of the current process.                                                                                                    |
| [**FreeEnvironmentStrings**](https://msdn.microsoft.com/library/ms683151(v=VS.85).aspx)                 | Frees a block of environment strings.                                                                                                                                                         |
| [**GetCommandLine**](https://msdn.microsoft.com/library/ms683156(v=VS.85).aspx)                                 | Retrieves the command-line string for the current process.                                                                                                                                    |
| [**GetCurrentProcess**](https://msdn.microsoft.com/library/ms683179(v=VS.85).aspx)                           | Retrieves a pseudo handle for the current process.                                                                                                                                            |
| [**GetCurrentProcessId**](https://msdn.microsoft.com/library/ms683180(v=VS.85).aspx)                       | Retrieves the process identifier of the calling process.                                                                                                                                      |
| [**GetCurrentProcessorNumber**](https://msdn.microsoft.com/library/ms683181(v=VS.85).aspx)           | Retrieves the number of the processor the current thread was running on during the call to this function.                                                                                     |
| [**GetEnvironmentStrings**](https://msdn.microsoft.com/library/ms683187(v=VS.85).aspx)                   | Retrieves the environment block for the current process.                                                                                                                                      |
| [**GetEnvironmentVariable**](/windows/desktop/api/WinBase/nf-winbase-getenvironmentvariable)                 | Retrieves the value of the specified variable from the environment block of the calling process.                                                                                              |
| [**GetExitCodeProcess**](https://msdn.microsoft.com/library/ms683189(v=VS.85).aspx)                         | Retrieves the termination status of the specified process.                                                                                                                                    |
| [**GetGuiResources**](/windows/desktop/api/Winuser/nf-winuser-getguiresources)                               | Retrieves the count of handles to graphical user interface (GUI) objects in use by the specified process.                                                                                     |
| [**GetLogicalProcessorInformation**](https://msdn.microsoft.com/library/ms683194(v=VS.85).aspx) | Retrieves information about logical processors and related hardware.                                                                                                                          |
| [**GetPriorityClass**](https://msdn.microsoft.com/library/ms683211(v=VS.85).aspx)                             | Retrieves the priority class for the specified process.                                                                                                                                       |
| [**GetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-getprocessaffinitymask)                 | Retrieves a process affinity mask for the specified process and the system affinity mask for the system.                                                                                      |
| [**GetProcessGroupAffinity**](https://msdn.microsoft.com/library/Dd405496(v=VS.85).aspx)               | Retrieves the processor group affinity of the specified process.                                                                                                                              |
| [**GetProcessHandleCount**](https://msdn.microsoft.com/library/ms683214(v=VS.85).aspx)                   | Retrieves the number of open handles that belong to the specified process.                                                                                                                    |
| [**GetProcessId**](https://msdn.microsoft.com/library/ms683215(v=VS.85).aspx)                                     | Retrieves the process identifier of the specified process.                                                                                                                                    |
| [**GetProcessIdOfThread**](https://msdn.microsoft.com/library/ms683216(v=VS.85).aspx)                     | Retrieves the process identifier of the process associated with the specified thread.                                                                                                         |
| [**GetProcessIoCounters**](/windows/desktop/api/WinBase/nf-winbase-getprocessiocounters)                     | Retrieves accounting information for all I/O operations performed by the specified process.                                                                                                   |
| [**GetProcessMitigationPolicy**](/windows/desktop/api/Processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy)         | Retrieves mitigation policy settings for the calling process.                                                                                                                                 |
| [**GetProcessPriorityBoost**](https://msdn.microsoft.com/library/ms683220(v=VS.85).aspx)               | Retrieves the priority boost control state of the specified process.                                                                                                                          |
| [**GetProcessShutdownParameters**](https://msdn.microsoft.com/library/ms683221(v=VS.85).aspx)     | Retrieves shutdown parameters for the currently calling process.                                                                                                                              |
| [**GetProcessTimes**](https://msdn.microsoft.com/library/ms683223(v=VS.85).aspx)                               | Retrieves timing information about for the specified process.                                                                                                                                 |
| [**GetProcessVersion**](https://msdn.microsoft.com/library/ms683224(v=VS.85).aspx)                           | Retrieves the major and minor version numbers of the system on which the specified process expects to run.                                                                                    |
| [**GetProcessWorkingSetSize**](/windows/desktop/api/WinBase/nf-winbase-getprocessworkingsetsize)             | Retrieves the minimum and maximum working set sizes of the specified process.                                                                                                                 |
| [**GetProcessWorkingSetSizeEx**](https://msdn.microsoft.com/library/ms683227(v=VS.85).aspx)         | Retrieves the minimum and maximum working set sizes of the specified process.                                                                                                                 |
| [**GetProcessorSystemCycleTime**](https://msdn.microsoft.com/library/Dd405497(v=VS.85).aspx)       | Retrieves the cycle time each processor in the specified group spent executing deferred procedure calls (DPCs) and interrupt service routines (ISRs).                                         |
| [**GetStartupInfo**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getstartupinfow)                                 | Retrieves the contents of the [**STARTUPINFO**](https://msdn.microsoft.com/library/ms686331(v=VS.85).aspx) structure that was specified when the calling process was created.                                                       |
| [**IsImmersiveProcess**](/windows/desktop/api/Winuser/nf-winuser-isimmersiveprocess)                         | Determines whether the process belongs to a Windows Store app.                                                                                                                                |
| [**NeedCurrentDirectoryForExePath**](https://msdn.microsoft.com/library/ms684269(v=VS.85).aspx) | Determines whether the current directory should be included in the search path for the specified executable.                                                                                  |
| [**OpenProcess**](https://msdn.microsoft.com/library/ms684320(v=VS.85).aspx)                                       | Opens an existing local process object.                                                                                                                                                       |
| [**QueryFullProcessImageName**](/windows/desktop/api/WinBase/nf-winbase-queryfullprocessimagenamea)           | Retrieves the full name of the executable image for the specified process.                                                                                                                    |
| [**QueryProcessAffinityUpdateMode**](https://msdn.microsoft.com/library/Bb309062(v=VS.85).aspx) | Retrieves the affinity update mode of the specified process.                                                                                                                                  |
| [**QueryProcessCycleTime**](https://msdn.microsoft.com/library/ms684929(v=VS.85).aspx)                   | Retrieves the sum of the cycle time of all threads of the specified process.                                                                                                                  |
| [**SetEnvironmentVariable**](/windows/desktop/api/WinBase/nf-winbase-setenvironmentvariable)                 | Sets the value of an environment variable for the current process.                                                                                                                            |
| [**SetPriorityClass**](https://msdn.microsoft.com/library/ms686219(v=VS.85).aspx)                             | Sets the priority class for the specified process.                                                                                                                                            |
| [**SetProcessAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setprocessaffinitymask)                 | Sets a processor affinity mask for the threads of a specified process.                                                                                                                        |
| [**SetProcessAffinityUpdateMode**](https://msdn.microsoft.com/library/Bb309063(v=VS.85).aspx)     | Sets the affinity update mode of the specified process.                                                                                                                                       |
| [**SetProcessInformation**](https://msdn.microsoft.com/library/Hh448389(v=VS.85).aspx)                   | Sets information for the specified process.                                                                                                                                                   |
| [**SetProcessMitigationPolicy**](/windows/desktop/api/Processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy)         | Sets the mitigation policy for the calling process.                                                                                                                                           |
| [**SetProcessPriorityBoost**](https://msdn.microsoft.com/library/ms686225(v=VS.85).aspx)               | Disables the ability of the system to temporarily boost the priority of the threads of the specified process.                                                                                 |
| [**SetProcessRestrictionExemption**](/windows/desktop/api/Winuser/nf-winuser-setprocessrestrictionexemption) | Exempts the calling process from restrictions preventing desktop processes from interacting with the Windows Store app environment. This function is used by development and debugging tools. |
| [**SetProcessShutdownParameters**](https://msdn.microsoft.com/library/ms686227(v=VS.85).aspx)     | Sets shutdown parameters for the currently calling process.                                                                                                                                   |
| [**SetProcessWorkingSetSize**](/windows/desktop/api/WinBase/nf-winbase-setprocessworkingsetsize)             | Sets the minimum and maximum working set sizes for the specified process.                                                                                                                     |
| [**SetProcessWorkingSetSizeEx**](https://msdn.microsoft.com/library/ms686237(v=VS.85).aspx)         | Sets the minimum and maximum working set sizes for the specified process.                                                                                                                     |
| [**TerminateProcess**](https://msdn.microsoft.com/library/ms686714(v=VS.85).aspx)                             | Terminates the specified process and all of its threads.                                                                                                                                      |



 

## Process Enumeration Functions

The following functions are used to enumerate processes.



| Function                                                    | Description                                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**EnumProcesses**](https://msdn.microsoft.com/library/ms682629(v=VS.85).aspx)                     | Retrieves the process identifier for each process object in the system.            |
| [**Process32First**](https://msdn.microsoft.com/library/ms684834(v=VS.85).aspx)                   | Retrieves information about the first process encountered in a system snapshot.    |
| [**Process32Next**](https://msdn.microsoft.com/library/ms684836(v=VS.85).aspx)                     | Retrieves information about the next process recorded in a system snapshot.        |
| [**WTSEnumerateProcesses**](https://msdn.microsoft.com/library/Aa383831(v=VS.85).aspx) | Retrieves information about the active processes on the specified terminal server. |



 

## Policy Functions

The following functions are used with process wide policy.



|                                                      |                                                       |
|------------------------------------------------------|-------------------------------------------------------|
| Function                                             | Description                                           |
| [**QueryProtectedPolicy**](https://msdn.microsoft.com/library/Dn893591(v=VS.85).aspx) | Queries the value associated with a protected policy. |
| [**SetProtectedPolicy**](https://msdn.microsoft.com/library/Dn893592(v=VS.85).aspx)     | Sets a protected policy.                              |



 

## Thread Functions

The following functions are used with [threads](multiple-threads.md).



| Function                                                           | Description                                                                                                                                               |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AttachThreadInput**](/windows/desktop/api/Winuser/nf-winuser-attachthreadinput)                     | Attaches the input processing mechanism of one thread to that of another thread.                                                                          |
| [**CreateRemoteThread**](https://msdn.microsoft.com/library/ms682437(v=VS.85).aspx)                   | Creates a thread that runs in the virtual address space of another process.                                                                               |
| [**CreateRemoteThreadEx**](https://msdn.microsoft.com/library/Dd405484(v=VS.85).aspx)               | Creates a thread that runs in the virtual address space of another process and optionally specifies extended attributes such as processor group affinity. |
| [**CreateThread**](https://msdn.microsoft.com/library/ms682453(v=VS.85).aspx)                               | Creates a thread to execute within the virtual address space of the calling process.                                                                      |
| [**ExitThread**](https://msdn.microsoft.com/library/ms682659(v=VS.85).aspx)                                   | Ends the calling thread.                                                                                                                                  |
| [**GetCurrentThread**](https://msdn.microsoft.com/library/ms683182(v=VS.85).aspx)                       | Retrieves a pseudo handle for the current thread.                                                                                                         |
| [**GetCurrentThreadId**](https://msdn.microsoft.com/library/ms683183(v=VS.85).aspx)                   | Retrieves the thread identifier of the calling thread.                                                                                                    |
| [**GetExitCodeThread**](https://msdn.microsoft.com/library/ms683190(v=VS.85).aspx)                     | Retrieves the termination status of the specified thread.                                                                                                 |
| [**GetThreadDescription**](/windows/desktop/api/ProcessThreadsApi/nf-processthreadsapi-getthreaddescription)               | Retrieves the description that was assigned to a thread by calling [**SetThreadDescription**](/windows/desktop/api/ProcessThreadsApi/nf-processthreadsapi-setthreaddescription).                                  |
| [**GetThreadGroupAffinity**](https://msdn.microsoft.com/library/Dd405498(v=VS.85).aspx)           | Retrieves the processor group affinity of the specified thread.                                                                                           |
| [**GetThreadId**](https://msdn.microsoft.com/library/ms683233(v=VS.85).aspx)                                 | Retrieves the thread identifier of the specified thread.                                                                                                  |
| [**GetThreadIdealProcessorEx**](https://msdn.microsoft.com/library/Dd405499(v=VS.85).aspx)     | Retrieves the processor number of the ideal processor for the specified thread.                                                                           |
| [**GetThreadInformation**](https://msdn.microsoft.com/library/Hh448382(v=VS.85).aspx)               | Retrieves information about the specified thread.                                                                                                         |
| [**GetThreadIOPendingFlag**](https://msdn.microsoft.com/library/ms683234(v=VS.85).aspx)           | Determines whether a specified thread has any I/O requests pending.                                                                                       |
| [**GetThreadPriority**](https://msdn.microsoft.com/library/ms683235(v=VS.85).aspx)                     | Retrieves the priority value for the specified thread.                                                                                                    |
| [**GetThreadPriorityBoost**](https://msdn.microsoft.com/library/ms683236(v=VS.85).aspx)           | Retrieves the priority boost control state of the specified thread.                                                                                       |
| [**GetThreadTimes**](https://msdn.microsoft.com/library/ms683237(v=VS.85).aspx)                           | Retrieves timing information for the specified thread.                                                                                                    |
| [**OpenThread**](https://msdn.microsoft.com/library/ms684335(v=VS.85).aspx)                                   | Opens an existing thread object.                                                                                                                          |
| [**QueryIdleProcessorCycleTime**](https://msdn.microsoft.com/library/ms684922(v=VS.85).aspx) | Retrieves the cycle time for the idle thread of each processor in the system.                                                                             |
| [**QueryThreadCycleTime**](https://msdn.microsoft.com/library/ms684943(v=VS.85).aspx)               | Retrieves the cycle time for the specified thread.                                                                                                        |
| [**ResumeThread**](https://msdn.microsoft.com/library/ms685086(v=VS.85).aspx)                               | Decrements a thread's suspend count.                                                                                                                      |
| [**SetThreadAffinityMask**](/windows/desktop/api/WinBase/nf-winbase-setthreadaffinitymask)             | Sets a processor affinity mask for the specified thread.                                                                                                  |
| [**SetThreadDescription**](/windows/desktop/api/ProcessThreadsApi/nf-processthreadsapi-setthreaddescription)               | Assigns a description to a thread.                                                                                                                        |
| [**SetThreadGroupAffinity**](https://msdn.microsoft.com/library/Dd405516(v=VS.85).aspx)           | Sets the processor group affinity for the specified thread.                                                                                               |
| [**SetThreadIdealProcessor**](https://msdn.microsoft.com/library/ms686253(v=VS.85).aspx)         | Specifies a preferred processor for a thread.                                                                                                             |
| [**SetThreadIdealProcessorEx**](https://msdn.microsoft.com/library/Dd405517(v=VS.85).aspx)     | Sets the ideal processor for the specified thread and optionally retrieves the previous ideal processor.                                                  |
| [**SetThreadInformation**](https://msdn.microsoft.com/library/Hh448390(v=VS.85).aspx)               | Sets information for the specified thread.                                                                                                                |
| [**SetThreadPriority**](https://msdn.microsoft.com/library/ms686277(v=VS.85).aspx)                     | Sets the priority value for the specified thread.                                                                                                         |
| [**SetThreadPriorityBoost**](https://msdn.microsoft.com/library/ms686280(v=VS.85).aspx)           | Disables the ability of the system to temporarily boost the priority of a thread.                                                                         |
| [**SetThreadStackGuarantee**](https://msdn.microsoft.com/library/ms686283(v=VS.85).aspx)         | Sets the stack guarantee for the calling thread.                                                                                                          |
| [**Sleep**](https://msdn.microsoft.com/library/ms686298(v=VS.85).aspx)                                             | Suspends the execution of the current thread for a specified interval.                                                                                    |
| [**SleepEx**](https://msdn.microsoft.com/library/ms686307(v=VS.85).aspx)                                         | Suspends the current thread until the specified condition is met.                                                                                         |
| [**SuspendThread**](https://msdn.microsoft.com/library/ms686345(v=VS.85).aspx)                             | Suspends the specified thread.                                                                                                                            |
| [**SwitchToThread**](https://msdn.microsoft.com/library/ms686352(v=VS.85).aspx)                           | Causes the calling thread to yield execution to another thread that is ready to run on the current processor.                                             |
| [**TerminateThread**](https://msdn.microsoft.com/library/ms686717(v=VS.85).aspx)                         | Terminates a thread.                                                                                                                                      |
| [**ThreadProc**](https://msdn.microsoft.com/library/ms686736(v=VS.85).aspx)                                   | An application-defined function that serves as the starting address for a thread.                                                                         |
| [**TlsAlloc**](https://msdn.microsoft.com/library/ms686801(v=VS.85).aspx)                                       | Allocates a thread local storage (TLS) index.                                                                                                             |
| [**TlsFree**](https://msdn.microsoft.com/library/ms686804(v=VS.85).aspx)                                         | Releases a TLS index.                                                                                                                                     |
| [**TlsGetValue**](https://msdn.microsoft.com/library/ms686812(v=VS.85).aspx)                                 | Retrieves the value in the calling thread's TLS slot for a specified TLS index.                                                                           |
| [**TlsSetValue**](https://msdn.microsoft.com/library/ms686818(v=VS.85).aspx)                                 | Stores a value in the calling thread's TLS slot for a specified TLS index.                                                                                |
| [**WaitForInputIdle**](/windows/desktop/api/Winuser/nf-winuser-waitforinputidle)                       | Waits until the specified process is waiting for user input with no input pending, or until the time-out interval has elapsed.                            |



 

## Process and Thread Extended Attribute Functions

The following functions are used to set extended attributes for process and thread creation.



| Function                                                                       | Description                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DeleteProcThreadAttributeList**](https://msdn.microsoft.com/library/ms682559(v=VS.85).aspx)         | Deletes the specified list of attributes for process and thread creation.                            |
| [**InitializeProcThreadAttributeList**](https://msdn.microsoft.com/library/ms683481(v=VS.85).aspx) | Initializes the specified list of attributes for process and thread creation.                        |
| [**UpdateProcThreadAttribute**](https://msdn.microsoft.com/library/ms686880(v=VS.85).aspx)                 | Updates the specified attribute in the specified list of attributes for process and thread creation. |



 

## WOW64 Functions

The following functions are used with [WOW64](https://msdn.microsoft.com/library/Aa384249(v=VS.85).aspx).



| Function                                         | Description                                                                                                                            |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**IsWow64Message**](/windows/desktop/api/Winuser/nf-winuser-iswow64message)         | Determines whether the last message read from the current thread's queue originated from a WOW64 process.                              |
| [**IsWow64Process**](https://msdn.microsoft.com/library/ms684139(v=VS.85).aspx)         | Determines whether the specified process is running under WOW64.                                                                       |
| [**IsWow64Process2**](/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64process2)       | Determines whether the specified process is running under WOW64; also returns additional machine process and architecture information. |
| [**Wow64SuspendThread**](/windows/desktop/api/WinBase/nf-winbase-wow64suspendthread) | Suspends the specified WOW64 thread.                                                                                                   |



 

## Job Object Functions

The following functions are used with [job objects](job-objects.md).



| Function                                                       | Description                                                                                          |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**AssignProcessToJobObject**](https://msdn.microsoft.com/library/ms681949(v=VS.85).aspx)   | Associates a process with an existing job object.                                                    |
| [**CreateJobObject**](/windows/desktop/api/WinBase/nf-winbase-createjobobjecta)                     | Creates or opens a job object.                                                                       |
| [**IsProcessInJob**](https://msdn.microsoft.com/library/ms684127(v=VS.85).aspx)                       | Determines whether the process is running in the specified job.                                      |
| [**OpenJobObject**](/windows/desktop/api/WinBase/nf-winbase-openjobobjecta)                         | Opens an existing job object.                                                                        |
| [**QueryInformationJobObject**](https://msdn.microsoft.com/library/ms684925(v=VS.85).aspx) | Retrieves limit and job state information from the job object.                                       |
| [**SetInformationJobObject**](https://msdn.microsoft.com/library/ms686216(v=VS.85).aspx)     | Set limits for a job object.                                                                         |
| [**TerminateJobObject**](https://msdn.microsoft.com/library/ms686709(v=VS.85).aspx)               | Terminates all processes currently associated with the job.                                          |
| [**UserHandleGrantAccess**](/windows/desktop/api/Winuser/nf-winuser-userhandlegrantaccess)         | Grants or denies access to a handle to a User object to a job that has a user-interface restriction. |



 

## Thread Pool Functions

The following functions are used with [thread pools](thread-pools.md).



| Function                                                                                   | Description                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallbackMayRunLong**](https://msdn.microsoft.com/library/ms681981(v=VS.85).aspx)                                           | Indicates that the callback may not return quickly.                                                                                                                                                                                                 |
| [**CancelThreadpoolIo**](https://msdn.microsoft.com/library/ms681983(v=VS.85).aspx)                                           | Cancels the notification from the [**StartThreadpoolIo**](https://msdn.microsoft.com/library/ms686326(v=VS.85).aspx) function.                                                                                                                                                          |
| [**CloseThreadpool**](https://msdn.microsoft.com/library/ms682030(v=VS.85).aspx)                                                 | Closes the specified thread pool.                                                                                                                                                                                                                   |
| [**CloseThreadpoolCleanupGroup**](https://msdn.microsoft.com/library/ms682033(v=VS.85).aspx)                         | Closes the specified cleanup group.                                                                                                                                                                                                                 |
| [**CloseThreadpoolCleanupGroupMembers**](https://msdn.microsoft.com/library/ms682036(v=VS.85).aspx)           | Releases the members of the specified cleanup group, waits for all callback functions to complete, and optionally cancels any outstanding callback functions.                                                                                       |
| [**CloseThreadpoolIo**](https://msdn.microsoft.com/library/ms682038(v=VS.85).aspx)                                             | Releases the specified I/O completion object.                                                                                                                                                                                                       |
| [**CloseThreadpoolTimer**](https://msdn.microsoft.com/library/ms682040(v=VS.85).aspx)                                       | Releases the specified timer object.                                                                                                                                                                                                                |
| [**CloseThreadpoolWait**](https://msdn.microsoft.com/library/ms682042(v=VS.85).aspx)                                         | Releases the specified wait object.                                                                                                                                                                                                                 |
| [**CloseThreadpoolWork**](https://msdn.microsoft.com/library/ms682043(v=VS.85).aspx)                                         | Releases the specified work object.                                                                                                                                                                                                                 |
| [**CreateThreadpool**](https://msdn.microsoft.com/library/ms682456(v=VS.85).aspx)                                               | Allocates a new pool of threads to execute callbacks.                                                                                                                                                                                               |
| [**CreateThreadpoolCleanupGroup**](https://msdn.microsoft.com/library/ms682462(v=VS.85).aspx)                       | Creates a cleanup group that applications can use to track one or more thread pool callbacks.                                                                                                                                                       |
| [**CreateThreadpoolIo**](https://msdn.microsoft.com/library/ms682464(v=VS.85).aspx)                                           | Creates a new I/O completion object.                                                                                                                                                                                                                |
| [**CreateThreadpoolTimer**](https://msdn.microsoft.com/library/ms682466(v=VS.85).aspx)                                     | Creates a new timer object.                                                                                                                                                                                                                         |
| [**CreateThreadpoolWait**](https://msdn.microsoft.com/library/ms682474(v=VS.85).aspx)                                       | Creates a new wait object.                                                                                                                                                                                                                          |
| [**CreateThreadpoolWork**](https://msdn.microsoft.com/library/ms682478(v=VS.85).aspx)                                       | Creates a new work object.                                                                                                                                                                                                                          |
| [**DestroyThreadpoolEnvironment**](/windows/desktop/api/WinBase/nf-winbase-destroythreadpoolenvironment)                       | Deletes the specified callback environment. Call this function when the callback environment is no longer needed for creating new thread pool objects.                                                                                              |
| [**DisassociateCurrentThreadFromCallback**](https://msdn.microsoft.com/library/ms682581(v=VS.85).aspx)     | Removes the association between the currently executing callback function and the object that initiated the callback. The current thread will no longer count as executing a callback on behalf of the object.                                      |
| [**FreeLibraryWhenCallbackReturns**](https://msdn.microsoft.com/library/ms683154(v=VS.85).aspx)                   | Specifies the DLL that the thread pool will unload when the current callback completes.                                                                                                                                                             |
| [**InitializeThreadpoolEnvironment**](/windows/desktop/api/WinBase/nf-winbase-initializethreadpoolenvironment)                 | Initializes a callback environment.                                                                                                                                                                                                                 |
| [**IsThreadpoolTimerSet**](https://msdn.microsoft.com/library/ms684133(v=VS.85).aspx)                                       | Determines whether the specified timer object is currently set.                                                                                                                                                                                     |
| [**LeaveCriticalSectionWhenCallbackReturns**](https://msdn.microsoft.com/library/ms684171(v=VS.85).aspx) | Specifies the critical section that the thread pool will release when the current callback completes.                                                                                                                                               |
| [**QueryThreadpoolStackInformation**](https://msdn.microsoft.com/library/Dd405508(v=VS.85).aspx)                 | Retrieves the stack reserve and commit sizes for threads in the specified thread pool.                                                                                                                                                              |
| [**ReleaseMutexWhenCallbackReturns**](https://msdn.microsoft.com/library/ms685070(v=VS.85).aspx)                 | Specifies the mutex that the thread pool will release when the current callback completes.                                                                                                                                                          |
| [**ReleaseSemaphoreWhenCallbackReturns**](https://msdn.microsoft.com/library/ms685073(v=VS.85).aspx)         | Specifies the semaphore that the thread pool will release when the current callback completes.                                                                                                                                                      |
| [**SetEventWhenCallbackReturns**](https://msdn.microsoft.com/library/ms686214(v=VS.85).aspx)                         | Specifies the event that the thread pool will set when the current callback completes.                                                                                                                                                              |
| [**SetThreadpoolCallbackCleanupGroup**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackcleanupgroup)             | Associates the specified cleanup group with the specified callback environment.                                                                                                                                                                     |
| [**SetThreadpoolCallbackLibrary**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbacklibrary)                       | Ensures that the specified DLL remains loaded as long as there are outstanding callbacks.                                                                                                                                                           |
| [**SetThreadpoolCallbackPersistent**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackpersistent)                 | Specifies that the callback should run on a persistent thread.                                                                                                                                                                                      |
| [**SetThreadpoolCallbackPool**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackpool)                             | Sets the thread pool to be used when generating callbacks.                                                                                                                                                                                          |
| [**SetThreadpoolCallbackPriority**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackpriority)                     | Specifies the priority of a callback function relative to other work items in the same thread pool.                                                                                                                                                 |
| [**SetThreadpoolCallbackRunsLong**](/windows/desktop/api/WinBase/nf-winbase-setthreadpoolcallbackrunslong)                     | Indicates that callbacks associated with this callback environment may not return quickly.                                                                                                                                                          |
| [**SetThreadpoolStackInformation**](https://msdn.microsoft.com/library/Dd405520(v=VS.85).aspx)                     | Sets the stack reserve and commit sizes for new threads in the specified thread pool.                                                                                                                                                               |
| [**SetThreadpoolThreadMaximum**](https://msdn.microsoft.com/library/ms686266(v=VS.85).aspx)                           | Sets the maximum number of threads that the specified thread pool can allocate to process callbacks.                                                                                                                                                |
| [**SetThreadpoolThreadMinimum**](https://msdn.microsoft.com/library/ms686268(v=VS.85).aspx)                           | Sets the minimum number of threads that the specified thread pool must make available to process callbacks.                                                                                                                                         |
| [**SetThreadpoolTimerEx**](/windows/desktop/api/threadpoolapiset/nf-threadpoolapiset-setthreadpooltimerex)                                       | Sets the timer object. A worker thread calls the timer object's callback after the specified timeout expires.                                                                                                                                       |
| [**SetThreadpoolTimer**](https://msdn.microsoft.com/library/ms686271(v=VS.85).aspx)                                           | Sets the timer object. A worker thread calls the timer object's callback after the specified timeout expires.                                                                                                                                       |
| [**SetThreadpoolWait**](https://msdn.microsoft.com/library/ms686273(v=VS.85).aspx)                                             | Sets the wait object. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.                                                                                           |
| [**SetThreadpoolWaitEx**](/windows/desktop/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolwaitex)                                         | Sets the wait object. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.                                                                                           |
| [**StartThreadpoolIo**](https://msdn.microsoft.com/library/ms686326(v=VS.85).aspx)                                             | Notifies the thread pool that I/O operations may possibly begin for the specified I/O completion object. A worker thread calls the I/O completion object's callback function after the operation completes on the file handle bound to this object. |
| [**SubmitThreadpoolWork**](https://msdn.microsoft.com/library/ms686338(v=VS.85).aspx)                                       | Posts a work object to the thread pool. A worker thread calls the work object's callback function.                                                                                                                                                  |
| [**TpInitializeCallbackEnviron**](/windows/desktop/api/winnt/nf-winnt-tpinitializecallbackenviron)                         | Initializes a callback environment for the thread pool.                                                                                                                                                                                             |
| [**TpDestroyCallbackEnviron**](/windows/desktop/api/winnt/nf-winnt-tpdestroycallbackenviron)                               | Deletes the specified callback environment. Call this function when the callback environment is no longer needed for creating new thread pool objects.                                                                                              |
| [**TpSetCallbackActivationContext**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackactivationcontext)                   | Assigns an activation context to the callback environment.                                                                                                                                                                                          |
| [**TpSetCallbackCleanupGroup**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackcleanupgroup)                             | Associates the specified cleanup group with the specified callback environment.                                                                                                                                                                     |
| [**TpSetCallbackFinalizationCallback**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackfinalizationcallback)             | Indicates a function to call when the callback environment is finalized.                                                                                                                                                                            |
| [**TpSetCallbackLongFunction**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbacklongfunction)                             | Indicates that callbacks associated with this callback environment may not return quickly.                                                                                                                                                          |
| [**TpSetCallbackNoActivationContext**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbacknoactivationcontext)               | Indicates that the callback environment has no activation context.                                                                                                                                                                                  |
| [**TpSetCallbackPersistent**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackpersistent)                                 | Specifies that the callback should run on a persistent thread.                                                                                                                                                                                      |
| [**TpSetCallbackPriority**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackpriority)                                     | Specifies the priority of a callback function relative to other work items in the same thread pool.                                                                                                                                                 |
| [**TpSetCallbackRaceWithDll**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackracewithdll)                               | Ensures that the specified DLL remains loaded as long as there are outstanding callbacks.                                                                                                                                                           |
| [**TpSetCallbackThreadpool**](/windows/desktop/api/winnt/nf-winnt-tpsetcallbackthreadpool)                                 | Assigns a thread pool to a callback environment.                                                                                                                                                                                                    |
| [**TrySubmitThreadpoolCallback**](https://msdn.microsoft.com/library/ms686862(v=VS.85).aspx)                         | Requests that a thread pool worker thread call the specified callback function.                                                                                                                                                                     |
| [**WaitForThreadpoolIoCallbacks**](https://msdn.microsoft.com/library/ms687038(v=VS.85).aspx)                       | Waits for outstanding I/O completion callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                           |
| [**WaitForThreadpoolTimerCallbacks**](https://msdn.microsoft.com/library/ms687042(v=VS.85).aspx)                 | Waits for outstanding timer callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                    |
| [**WaitForThreadpoolWaitCallbacks**](https://msdn.microsoft.com/library/ms687047(v=VS.85).aspx)                   | Waits for outstanding wait callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                     |
| [**WaitForThreadpoolWorkCallbacks**](https://msdn.microsoft.com/library/ms687053(v=VS.85).aspx)                   | Waits for outstanding work callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                     |



 

The following functions are part of the original [thread pooling](thread-pooling.md) API.



| Function                                                            | Description                                                                                                                                                                                                            |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BindIoCompletionCallback**](/windows/desktop/api/WinBase/nf-winbase-bindiocompletioncallback)        | Associates the I/O completion port owned by the thread pool with the specified file handle. On completion of an I/O request involving this file, a non-I/O worker thread will execute the specified callback function. |
| [**QueueUserWorkItem**](https://msdn.microsoft.com/library/ms684957(v=VS.85).aspx)                      | Queues a work item to a worker thread in the thread pool.                                                                                                                                                              |
| [**RegisterWaitForSingleObject**](https://msdn.microsoft.com/library/ms685061(v=VS.85).aspx) | Directs a wait thread in the thread pool to wait on the object.                                                                                                                                                        |
| [**UnregisterWaitEx**](https://msdn.microsoft.com/library/ms686876(v=VS.85).aspx)                       | Waits until one or all of the specified objects are in the signaled state or the time-out interval elapses.                                                                                                            |



 

## Thread Ordering Service Functions

The following functions are used with the [thread ordering service](thread-ordering-service.md).



| Function                                                                   | Description                                                                                 |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**AvQuerySystemResponsiveness**](/windows/desktop/api/Avrt/nf-avrt-avquerysystemresponsiveness)         | Retrieves the system responsiveness setting used by the multimedia class scheduler service. |
| [**AvRtCreateThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtcreatethreadorderinggroup)     | Creates a thread ordering group.                                                            |
| [**AvRtCreateThreadOrderingGroupEx**](/windows/desktop/api/Avrt/nf-avrt-avrtcreatethreadorderinggroupexa) | Creates a thread ordering group and associates the server thread with a task.               |
| [**AvRtDeleteThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtdeletethreadorderinggroup)     | Deletes the specified thread ordering group created by the caller.                          |
| [**AvRtJoinThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtjointhreadorderinggroup)         | Joins client threads to a thread ordering group.                                            |
| [**AvRtLeaveThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtleavethreadorderinggroup)       | Enables client threads to leave a thread ordering group.                                    |
| [**AvRtWaitOnThreadOrderingGroup**](/windows/desktop/api/Avrt/nf-avrt-avrtwaitonthreadorderinggroup)     | Enables client threads of a thread ordering group to wait until they should execute.        |



 

## Multimedia Class Scheduler Service Functions

The following functions are used with the [multimedia class scheduler service](multimedia-class-scheduler-service.md).



| Function                                                                   | Description                                                                                           |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**AvRevertMmThreadCharacteristics**](/windows/desktop/api/Avrt/nf-avrt-avrevertmmthreadcharacteristics) | Indicates that a thread is no longer performing work associated with the specified task.              |
| [**AvSetMmMaxThreadCharacteristics**](/windows/desktop/api/Avrt/nf-avrt-avsetmmmaxthreadcharacteristicsa) | Associates the calling thread with the specified tasks.                                               |
| [**AvSetMmThreadCharacteristics**](/windows/desktop/api/Avrt/nf-avrt-avsetmmthreadcharacteristicsa)       | Associates the calling thread with the specified task.                                                |
| [**AvSetMmThreadPriority**](/windows/desktop/api/Avrt/nf-avrt-avsetmmthreadpriority)                     | Adjusts the thread priority of the calling thread relative to other threads performing the same task. |



 

## Fiber Functions

The following functions are used with [fibers](fibers.md).



| Function                                                 | Description                                                                                                  |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ConvertFiberToThread**](/windows/desktop/api/WinBase/nf-winbase-convertfibertothread)     | Converts the current fiber into a thread.                                                                    |
| [**ConvertThreadToFiber**](/windows/desktop/api/WinBase/nf-winbase-convertthreadtofiber)     | Converts the current thread into a fiber.                                                                    |
| [**ConvertThreadToFiberEx**](/windows/desktop/api/WinBase/nf-winbase-convertthreadtofiberex) | Converts the current thread into a fiber.                                                                    |
| [**CreateFiber**](/windows/desktop/api/WinBase/nf-winbase-createfiber)                       | Allocates a fiber object, assigns it a stack, and sets up execution to begin at the specified start address. |
| [**CreateFiberEx**](/windows/desktop/api/WinBase/nf-winbase-createfiberex)                   | Allocates a fiber object, assigns it a stack, and sets up execution to begin at the specified start address. |
| [**DeleteFiber**](/windows/desktop/api/WinBase/nf-winbase-deletefiber)                       | Deletes an existing fiber.                                                                                   |
| [**FiberProc**](https://msdn.microsoft.com/library/ms682660(v=VS.85).aspx)                           | An application-defined function used with the [**CreateFiber**](/windows/desktop/api/WinBase/nf-winbase-createfiber) function.                   |
| [**FlsAlloc**](https://msdn.microsoft.com/library/ms682664(v=VS.85).aspx)                             | Allocates a fiber local storage (FLS) index.                                                                 |
| [**FlsFree**](https://msdn.microsoft.com/library/ms682667(v=VS.85).aspx)                               | Releases an FLS index.                                                                                       |
| [**FlsGetValue**](https://msdn.microsoft.com/library/ms683141(v=VS.85).aspx)                       | Retrieves the value in the calling fiber's FLS slot for a specified FLS index.                               |
| [**FlsSetValue**](https://msdn.microsoft.com/library/ms683146(v=VS.85).aspx)                       | Stores a value in the calling fiber's FLS slot for a specified FLS index.                                    |
| [**IsThreadAFiber**](https://msdn.microsoft.com/library/ms684131(v=VS.85).aspx)                 | Determines whether the current thread is a fiber.                                                            |
| [**SwitchToFiber**](/windows/desktop/api/WinBase/nf-winbase-switchtofiber)                   | Schedules a fiber.                                                                                           |



 

## NUMA Support Functions

The following functions provide [NUMA support](numa-support.md).



| Function                                                                 | Description                                                                                                                                            |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPagesNuma**](https://msdn.microsoft.com/library/Aa366529(v=VS.85).aspx)  | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |
| [**GetLogicalProcessorInformation**](https://msdn.microsoft.com/library/ms683194(v=VS.85).aspx) | Retrieves information about logical processors and related hardware.                                                                                   |
| [**GetNumaAvailableMemoryNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynode)         | Retrieves the amount of memory available in the specified node.                                                                                        |
| [**GetNumaAvailableMemoryNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaavailablememorynodeex)     | Retrieves the amount of memory that is available in the specified node as a USHORT value.                                                              |
| [**GetNumaHighestNodeNumber**](https://msdn.microsoft.com/library/ms683203(v=VS.85).aspx)             | Retrieves the node that currently has the highest number.                                                                                              |
| [**GetNumaNodeNumberFromHandle**](/windows/desktop/api/WinBase/nf-winbase-getnumanodenumberfromhandle)       | Retrieves the NUMA node associated with the underlying device for a file handle.                                                                       |
| [**GetNumaNodeProcessorMask**](/windows/desktop/api/WinBase/nf-winbase-getnumanodeprocessormask)             | Retrieves the processor mask for the specified node.                                                                                                   |
| [**GetNumaNodeProcessorMaskEx**](https://msdn.microsoft.com/library/Dd405493(v=VS.85).aspx)         | Retrieves the processor mask for the specified NUMA node as a USHORT value.                                                                            |
| [**GetNumaProcessorNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornode)                     | Retrieves the node number for the specified processor.                                                                                                 |
| [**GetNumaProcessorNodeEx**](/windows/desktop/api/WinBase/nf-winbase-getnumaprocessornodeex)                 | Retrieves the node number of the specified logical processor as a USHORT value.                                                                        |
| [**GetNumaProximityNode**](/windows/desktop/api/WinBase/nf-winbase-getnumaproximitynode)                     | Retrieves the node number for the specified proximity identifier.                                                                                      |
| [**GetNumaProximityNodeEx**](https://msdn.microsoft.com/library/Dd405495(v=VS.85).aspx)                 | Retrieves the node number as a USHORT value for the specified proximity identifier.                                                                    |
| [**VirtualAllocExNuma**](https://msdn.microsoft.com/library/Aa366891(v=VS.85).aspx)                        | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |



 

## Processor Functions

The following functions are used with logical processors and [processor groups](processor-groups.md).



| Function                                                                     | Description                                                                                                          |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**GetActiveProcessorCount**](/windows/desktop/api/WinBase/nf-winbase-getactiveprocessorcount)                   | Returns the number of active processors in a processor group or in the system.                                       |
| [**GetActiveProcessorGroupCount**](/windows/desktop/api/WinBase/nf-winbase-getactiveprocessorgroupcount)         | Returns the number of active processor groups in the system.                                                         |
| [**GetCurrentProcessorNumber**](https://msdn.microsoft.com/library/ms683181(v=VS.85).aspx)               | Retrieves the number of the processor the current thread was running on during the call to this function.            |
| [**GetCurrentProcessorNumberEx**](https://msdn.microsoft.com/library/Dd405487(v=VS.85).aspx)           | Retrieves the processor group and number of the logical processor in which the calling thread is running.            |
| [**GetLogicalProcessorInformation**](https://msdn.microsoft.com/library/ms683194(v=VS.85).aspx)     | Retrieves information about logical processors and related hardware.                                                 |
| [**GetLogicalProcessorInformationEx**](https://msdn.microsoft.com/library/Dd405488(v=VS.85).aspx) | Retrieves information about the relationships of logical processors and related hardware.                            |
| [**GetMaximumProcessorCount**](/windows/desktop/api/WinBase/nf-winbase-getmaximumprocessorcount)                 | Returns the maximum number of logical processors that a processor group or the system can have.                      |
| [**GetMaximumProcessorGroupCount**](/windows/desktop/api/WinBase/nf-winbase-getmaximumprocessorgroupcount)       | Returns the maximum number of processor groups that the system can have.                                             |
| [**QueryIdleProcessorCycleTime**](https://msdn.microsoft.com/library/ms684922(v=VS.85).aspx)           | Retrieves the cycle time for the idle thread of each processor in the system.                                        |
| [**QueryIdleProcessorCycleTimeEx**](https://msdn.microsoft.com/library/Dd405507(v=VS.85).aspx)       | Retrieves the accumulated cycle time for the idle thread on each logical processor in the specified processor group. |



 

## User-Mode Scheduling Functions

The following functions are used with user-mode scheduling (UMS).



| Function                                                               | Description                                                                                               |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**CreateUmsCompletionList**](/windows/desktop/api/WinBase/nf-winbase-createumscompletionlist)             | Creates a UMS completion list.                                                                            |
| [**CreateUmsThreadContext**](/windows/desktop/api/WinBase/nf-winbase-createumsthreadcontext)               | Creates a UMS thread context to represent a UMS worker thread.                                            |
| [**DeleteUmsCompletionList**](/windows/desktop/api/WinBase/nf-winbase-deleteumscompletionlist)             | Deletes the specified UMS completion list. The list must be empty.                                        |
| [**DeleteUmsThreadContext**](/windows/desktop/api/WinBase/nf-winbase-deleteumsthreadcontext)               | Deletes the specified UMS thread context. The thread must be terminated.                                  |
| [**DequeueUmsCompletionListItems**](/windows/desktop/api/WinBase/nf-winbase-dequeueumscompletionlistitems) | Retrieves UMS worker threads from the specified UMS completion list.                                      |
| [**EnterUmsSchedulingMode**](/windows/desktop/api/WinBase/nf-winbase-enterumsschedulingmode)               | Converts the calling thread into a UMS scheduler thread.                                                  |
| [**ExecuteUmsThread**](/windows/desktop/api/WinBase/nf-winbase-executeumsthread)                           | Runs the specified UMS worker thread.                                                                     |
| [**GetCurrentUmsThread**](/windows/desktop/api/WinBase/nf-winbase-getcurrentumsthread)                     | Returns the UMS thread context of the calling UMS thread.                                                 |
| [**GetNextUmsListItem**](/windows/desktop/api/WinBase/nf-winbase-getnextumslistitem)                       | Returns the next UMS thread context in a list of UMS thread contexts.                                     |
| [**GetUmsCompletionListEvent**](/windows/desktop/api/WinBase/nf-winbase-getumscompletionlistevent)         | Retrieves a handle to the event associated with the specified UMS completion list.                        |
| [**GetUmsSystemThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-getumssystemthreadinformation) | Queries whether the specified thread is a UMS scheduler thread, a UMS worker thread, or a non-UMS thread. |
| [**QueryUmsThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-queryumsthreadinformation)         | Retrieves information about the specified UMS worker thread.                                              |
| [**SetUmsThreadInformation**](/windows/desktop/api/WinBase/nf-winbase-setumsthreadinformation)             | Sets application-specific context information for the specified UMS worker thread.                        |
| [*UmsSchedulerProc*](/windows/desktop/api/WinNT/nc-winnt-rtl_ums_scheduler_entry_point)                             | The application-defined UMS scheduler entry point function associated with a UMS completion list.         |
| [**UmsThreadYield**](/windows/desktop/api/WinBase/nf-winbase-umsthreadyield)                               | Yields control to the UMS scheduler thread on which the calling UMS worker thread is running.             |



 

## Obsolete Functions

-   [**NtGetCurrentProcessorNumber**](ntgetcurrentprocessornumber.md)
-   [**NtQueryInformationProcess**](/windows/desktop/api/Winternl/nf-winternl-ntqueryinformationprocess)
-   [**NtQueryInformationThread**](/windows/desktop/api/Winternl/nf-winternl-ntqueryinformationthread)
-   [**WinExec**](/windows/desktop/api/WinBase/nf-winbase-winexec)
-   [**ZwQueryInformationProcess**](zwqueryinformationprocess.md)

 

 



