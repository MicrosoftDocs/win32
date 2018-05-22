---
Description: 'This topic describes the process and thread functions.'
ms.assetid: '8c8e8af0-bf50-4a4b-945c-83bae1eff7dd'
title: Process and Thread Functions
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
| [**CreateDispatcherQueueController**](createdispatcherqueuecontroller.md) | Creates a [DispatcherQueueController](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueuecontroller) which manages the lifetime of a [DispatcherQueue](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueue) that runs queued tasks in priority order on another thread. |



 

## Process Functions

The following functions are used with [processes](child-processes.md).



| Function                                                                 | Description                                                                                                                                                                                   |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateProcess**](createprocess.md)                                   | Creates a new process and its primary thread.                                                                                                                                                 |
| [**CreateProcessAsUser**](createprocessasuser.md)                       | Creates a new process and its primary thread. The new process runs in the security context of the user represented by the specified token.                                                    |
| [**CreateProcessWithLogonW**](createprocesswithlogonw.md)               | Creates a new process and its primary thread. The new process then runs the specified executable file in the security context of the specified credentials (user, domain, and password).      |
| [**CreateProcessWithTokenW**](createprocesswithtokenw.md)               | Creates a new process and its primary thread. The new process runs in the security context of the specified token.                                                                            |
| [**ExitProcess**](exitprocess.md)                                       | Ends the calling process and all its threads.                                                                                                                                                 |
| [**FlushProcessWriteBuffers**](flushprocesswritebuffers.md)             | Flushes the write queue of each processor that is running a thread of the current process.                                                                                                    |
| [**FreeEnvironmentStrings**](freeenvironmentstrings.md)                 | Frees a block of environment strings.                                                                                                                                                         |
| [**GetCommandLine**](getcommandline.md)                                 | Retrieves the command-line string for the current process.                                                                                                                                    |
| [**GetCurrentProcess**](getcurrentprocess.md)                           | Retrieves a pseudo handle for the current process.                                                                                                                                            |
| [**GetCurrentProcessId**](getcurrentprocessid.md)                       | Retrieves the process identifier of the calling process.                                                                                                                                      |
| [**GetCurrentProcessorNumber**](getcurrentprocessornumber.md)           | Retrieves the number of the processor the current thread was running on during the call to this function.                                                                                     |
| [**GetEnvironmentStrings**](getenvironmentstrings.md)                   | Retrieves the environment block for the current process.                                                                                                                                      |
| [**GetEnvironmentVariable**](getenvironmentvariable.md)                 | Retrieves the value of the specified variable from the environment block of the calling process.                                                                                              |
| [**GetExitCodeProcess**](getexitcodeprocess.md)                         | Retrieves the termination status of the specified process.                                                                                                                                    |
| [**GetGuiResources**](getguiresources.md)                               | Retrieves the count of handles to graphical user interface (GUI) objects in use by the specified process.                                                                                     |
| [**GetLogicalProcessorInformation**](getlogicalprocessorinformation.md) | Retrieves information about logical processors and related hardware.                                                                                                                          |
| [**GetPriorityClass**](getpriorityclass.md)                             | Retrieves the priority class for the specified process.                                                                                                                                       |
| [**GetProcessAffinityMask**](getprocessaffinitymask.md)                 | Retrieves a process affinity mask for the specified process and the system affinity mask for the system.                                                                                      |
| [**GetProcessGroupAffinity**](getprocessgroupaffinity.md)               | Retrieves the processor group affinity of the specified process.                                                                                                                              |
| [**GetProcessHandleCount**](getprocesshandlecount.md)                   | Retrieves the number of open handles that belong to the specified process.                                                                                                                    |
| [**GetProcessId**](getprocessid.md)                                     | Retrieves the process identifier of the specified process.                                                                                                                                    |
| [**GetProcessIdOfThread**](getprocessidofthread.md)                     | Retrieves the process identifier of the process associated with the specified thread.                                                                                                         |
| [**GetProcessIoCounters**](getprocessiocounters.md)                     | Retrieves accounting information for all I/O operations performed by the specified process.                                                                                                   |
| [**GetProcessMitigationPolicy**](getprocessmitigationpolicy.md)         | Retrieves mitigation policy settings for the calling process.                                                                                                                                 |
| [**GetProcessPriorityBoost**](getprocesspriorityboost.md)               | Retrieves the priority boost control state of the specified process.                                                                                                                          |
| [**GetProcessShutdownParameters**](getprocessshutdownparameters.md)     | Retrieves shutdown parameters for the currently calling process.                                                                                                                              |
| [**GetProcessTimes**](getprocesstimes.md)                               | Retrieves timing information about for the specified process.                                                                                                                                 |
| [**GetProcessVersion**](getprocessversion.md)                           | Retrieves the major and minor version numbers of the system on which the specified process expects to run.                                                                                    |
| [**GetProcessWorkingSetSize**](getprocessworkingsetsize.md)             | Retrieves the minimum and maximum working set sizes of the specified process.                                                                                                                 |
| [**GetProcessWorkingSetSizeEx**](getprocessworkingsetsizeex.md)         | Retrieves the minimum and maximum working set sizes of the specified process.                                                                                                                 |
| [**GetProcessorSystemCycleTime**](getprocessorsystemcycletime.md)       | Retrieves the cycle time each processor in the specified group spent executing deferred procedure calls (DPCs) and interrupt service routines (ISRs).                                         |
| [**GetStartupInfo**](getstartupinfo.md)                                 | Retrieves the contents of the [**STARTUPINFO**](startupinfo-str.md) structure that was specified when the calling process was created.                                                       |
| [**IsImmersiveProcess**](isimmersiveprocess.md)                         | Determines whether the process belongs to a Windows Store app.                                                                                                                                |
| [**NeedCurrentDirectoryForExePath**](needcurrentdirectoryforexepath.md) | Determines whether the current directory should be included in the search path for the specified executable.                                                                                  |
| [**OpenProcess**](openprocess.md)                                       | Opens an existing local process object.                                                                                                                                                       |
| [**QueryFullProcessImageName**](queryfullprocessimagename.md)           | Retrieves the full name of the executable image for the specified process.                                                                                                                    |
| [**QueryProcessAffinityUpdateMode**](queryprocessaffinityupdatemode.md) | Retrieves the affinity update mode of the specified process.                                                                                                                                  |
| [**QueryProcessCycleTime**](queryprocesscycletime.md)                   | Retrieves the sum of the cycle time of all threads of the specified process.                                                                                                                  |
| [**SetEnvironmentVariable**](setenvironmentvariable.md)                 | Sets the value of an environment variable for the current process.                                                                                                                            |
| [**SetPriorityClass**](setpriorityclass.md)                             | Sets the priority class for the specified process.                                                                                                                                            |
| [**SetProcessAffinityMask**](setprocessaffinitymask.md)                 | Sets a processor affinity mask for the threads of a specified process.                                                                                                                        |
| [**SetProcessAffinityUpdateMode**](setprocessaffinityupdatemode.md)     | Sets the affinity update mode of the specified process.                                                                                                                                       |
| [**SetProcessInformation**](setprocessinformation.md)                   | Sets information for the specified process.                                                                                                                                                   |
| [**SetProcessMitigationPolicy**](setprocessmitigationpolicy.md)         | Sets the mitigation policy for the calling process.                                                                                                                                           |
| [**SetProcessPriorityBoost**](setprocesspriorityboost.md)               | Disables the ability of the system to temporarily boost the priority of the threads of the specified process.                                                                                 |
| [**SetProcessRestrictionExemption**](setprocessrestrictionexemption.md) | Exempts the calling process from restrictions preventing desktop processes from interacting with the Windows Store app environment. This function is used by development and debugging tools. |
| [**SetProcessShutdownParameters**](setprocessshutdownparameters.md)     | Sets shutdown parameters for the currently calling process.                                                                                                                                   |
| [**SetProcessWorkingSetSize**](setprocessworkingsetsize.md)             | Sets the minimum and maximum working set sizes for the specified process.                                                                                                                     |
| [**SetProcessWorkingSetSizeEx**](setprocessworkingsetsizeex.md)         | Sets the minimum and maximum working set sizes for the specified process.                                                                                                                     |
| [**TerminateProcess**](terminateprocess.md)                             | Terminates the specified process and all of its threads.                                                                                                                                      |



 

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
| [**AttachThreadInput**](attachthreadinput.md)                     | Attaches the input processing mechanism of one thread to that of another thread.                                                                          |
| [**CreateRemoteThread**](createremotethread.md)                   | Creates a thread that runs in the virtual address space of another process.                                                                               |
| [**CreateRemoteThreadEx**](createremotethreadex.md)               | Creates a thread that runs in the virtual address space of another process and optionally specifies extended attributes such as processor group affinity. |
| [**CreateThread**](createthread.md)                               | Creates a thread to execute within the virtual address space of the calling process.                                                                      |
| [**ExitThread**](exitthread.md)                                   | Ends the calling thread.                                                                                                                                  |
| [**GetCurrentThread**](getcurrentthread.md)                       | Retrieves a pseudo handle for the current thread.                                                                                                         |
| [**GetCurrentThreadId**](getcurrentthreadid.md)                   | Retrieves the thread identifier of the calling thread.                                                                                                    |
| [**GetExitCodeThread**](getexitcodethread.md)                     | Retrieves the termination status of the specified thread.                                                                                                 |
| [**GetThreadDescription**](getthreaddescription.md)               | Retrieves the description that was assigned to a thread by calling [**SetThreadDescription**](setthreaddescription.md).                                  |
| [**GetThreadGroupAffinity**](getthreadgroupaffinity.md)           | Retrieves the processor group affinity of the specified thread.                                                                                           |
| [**GetThreadId**](getthreadid.md)                                 | Retrieves the thread identifier of the specified thread.                                                                                                  |
| [**GetThreadIdealProcessorEx**](getthreadidealprocessorex.md)     | Retrieves the processor number of the ideal processor for the specified thread.                                                                           |
| [**GetThreadInformation**](getthreadinformation.md)               | Retrieves information about the specified thread.                                                                                                         |
| [**GetThreadIOPendingFlag**](getthreadiopendingflag.md)           | Determines whether a specified thread has any I/O requests pending.                                                                                       |
| [**GetThreadPriority**](getthreadpriority.md)                     | Retrieves the priority value for the specified thread.                                                                                                    |
| [**GetThreadPriorityBoost**](getthreadpriorityboost.md)           | Retrieves the priority boost control state of the specified thread.                                                                                       |
| [**GetThreadTimes**](getthreadtimes.md)                           | Retrieves timing information for the specified thread.                                                                                                    |
| [**OpenThread**](openthread.md)                                   | Opens an existing thread object.                                                                                                                          |
| [**QueryIdleProcessorCycleTime**](queryidleprocessorcycletime.md) | Retrieves the cycle time for the idle thread of each processor in the system.                                                                             |
| [**QueryThreadCycleTime**](querythreadcycletime.md)               | Retrieves the cycle time for the specified thread.                                                                                                        |
| [**ResumeThread**](resumethread.md)                               | Decrements a thread's suspend count.                                                                                                                      |
| [**SetThreadAffinityMask**](setthreadaffinitymask.md)             | Sets a processor affinity mask for the specified thread.                                                                                                  |
| [**SetThreadDescription**](setthreaddescription.md)               | Assigns a description to a thread.                                                                                                                        |
| [**SetThreadGroupAffinity**](setthreadgroupaffinity.md)           | Sets the processor group affinity for the specified thread.                                                                                               |
| [**SetThreadIdealProcessor**](setthreadidealprocessor.md)         | Specifies a preferred processor for a thread.                                                                                                             |
| [**SetThreadIdealProcessorEx**](setthreadidealprocessorex.md)     | Sets the ideal processor for the specified thread and optionally retrieves the previous ideal processor.                                                  |
| [**SetThreadInformation**](setthreadinformation.md)               | Sets information for the specified thread.                                                                                                                |
| [**SetThreadPriority**](setthreadpriority.md)                     | Sets the priority value for the specified thread.                                                                                                         |
| [**SetThreadPriorityBoost**](setthreadpriorityboost.md)           | Disables the ability of the system to temporarily boost the priority of a thread.                                                                         |
| [**SetThreadStackGuarantee**](setthreadstackguarantee.md)         | Sets the stack guarantee for the calling thread.                                                                                                          |
| [**Sleep**](sleep.md)                                             | Suspends the execution of the current thread for a specified interval.                                                                                    |
| [**SleepEx**](sleepex.md)                                         | Suspends the current thread until the specified condition is met.                                                                                         |
| [**SuspendThread**](suspendthread.md)                             | Suspends the specified thread.                                                                                                                            |
| [**SwitchToThread**](switchtothread.md)                           | Causes the calling thread to yield execution to another thread that is ready to run on the current processor.                                             |
| [**TerminateThread**](terminatethread.md)                         | Terminates a thread.                                                                                                                                      |
| [**ThreadProc**](threadproc.md)                                   | An application-defined function that serves as the starting address for a thread.                                                                         |
| [**TlsAlloc**](tlsalloc.md)                                       | Allocates a thread local storage (TLS) index.                                                                                                             |
| [**TlsFree**](tlsfree.md)                                         | Releases a TLS index.                                                                                                                                     |
| [**TlsGetValue**](tlsgetvalue.md)                                 | Retrieves the value in the calling thread's TLS slot for a specified TLS index.                                                                           |
| [**TlsSetValue**](tlssetvalue.md)                                 | Stores a value in the calling thread's TLS slot for a specified TLS index.                                                                                |
| [**WaitForInputIdle**](waitforinputidle.md)                       | Waits until the specified process is waiting for user input with no input pending, or until the time-out interval has elapsed.                            |



 

## Process and Thread Extended Attribute Functions

The following functions are used to set extended attributes for process and thread creation.



| Function                                                                       | Description                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DeleteProcThreadAttributeList**](deleteprocthreadattributelist.md)         | Deletes the specified list of attributes for process and thread creation.                            |
| [**InitializeProcThreadAttributeList**](initializeprocthreadattributelist.md) | Initializes the specified list of attributes for process and thread creation.                        |
| [**UpdateProcThreadAttribute**](updateprocthreadattribute.md)                 | Updates the specified attribute in the specified list of attributes for process and thread creation. |



 

## WOW64 Functions

The following functions are used with [WOW64](winprog64.running_32_bit_applications).



| Function                                         | Description                                                                                                                            |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**IsWow64Message**](iswow64message.md)         | Determines whether the last message read from the current thread's queue originated from a WOW64 process.                              |
| [**IsWow64Process**](iswow64process.md)         | Determines whether the specified process is running under WOW64.                                                                       |
| [**IsWow64Process2**](iswow64process2.md)       | Determines whether the specified process is running under WOW64; also returns additional machine process and architecture information. |
| [**Wow64SuspendThread**](wow64suspendthread.md) | Suspends the specified WOW64 thread.                                                                                                   |



 

## Job Object Functions

The following functions are used with [job objects](job-objects.md).



| Function                                                       | Description                                                                                          |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**AssignProcessToJobObject**](assignprocesstojobobject.md)   | Associates a process with an existing job object.                                                    |
| [**CreateJobObject**](createjobobject.md)                     | Creates or opens a job object.                                                                       |
| [**IsProcessInJob**](isprocessinjob.md)                       | Determines whether the process is running in the specified job.                                      |
| [**OpenJobObject**](openjobobject.md)                         | Opens an existing job object.                                                                        |
| [**QueryInformationJobObject**](queryinformationjobobject.md) | Retrieves limit and job state information from the job object.                                       |
| [**SetInformationJobObject**](setinformationjobobject.md)     | Set limits for a job object.                                                                         |
| [**TerminateJobObject**](terminatejobobject.md)               | Terminates all processes currently associated with the job.                                          |
| [**UserHandleGrantAccess**](userhandlegrantaccess.md)         | Grants or denies access to a handle to a User object to a job that has a user-interface restriction. |



 

## Thread Pool Functions

The following functions are used with [thread pools](thread-pools.md).



| Function                                                                                   | Description                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallbackMayRunLong**](callbackmayrunlong.md)                                           | Indicates that the callback may not return quickly.                                                                                                                                                                                                 |
| [**CancelThreadpoolIo**](cancelthreadpoolio.md)                                           | Cancels the notification from the [**StartThreadpoolIo**](startthreadpoolio.md) function.                                                                                                                                                          |
| [**CloseThreadpool**](closethreadpool.md)                                                 | Closes the specified thread pool.                                                                                                                                                                                                                   |
| [**CloseThreadpoolCleanupGroup**](closethreadpoolcleanupgroup.md)                         | Closes the specified cleanup group.                                                                                                                                                                                                                 |
| [**CloseThreadpoolCleanupGroupMembers**](closethreadpoolcleanupgroupmembers.md)           | Releases the members of the specified cleanup group, waits for all callback functions to complete, and optionally cancels any outstanding callback functions.                                                                                       |
| [**CloseThreadpoolIo**](closethreadpoolio.md)                                             | Releases the specified I/O completion object.                                                                                                                                                                                                       |
| [**CloseThreadpoolTimer**](closethreadpooltimer.md)                                       | Releases the specified timer object.                                                                                                                                                                                                                |
| [**CloseThreadpoolWait**](closethreadpoolwait.md)                                         | Releases the specified wait object.                                                                                                                                                                                                                 |
| [**CloseThreadpoolWork**](closethreadpoolwork.md)                                         | Releases the specified work object.                                                                                                                                                                                                                 |
| [**CreateThreadpool**](createthreadpool.md)                                               | Allocates a new pool of threads to execute callbacks.                                                                                                                                                                                               |
| [**CreateThreadpoolCleanupGroup**](createthreadpoolcleanupgroup.md)                       | Creates a cleanup group that applications can use to track one or more thread pool callbacks.                                                                                                                                                       |
| [**CreateThreadpoolIo**](createthreadpoolio.md)                                           | Creates a new I/O completion object.                                                                                                                                                                                                                |
| [**CreateThreadpoolTimer**](createthreadpooltimer.md)                                     | Creates a new timer object.                                                                                                                                                                                                                         |
| [**CreateThreadpoolWait**](createthreadpoolwait.md)                                       | Creates a new wait object.                                                                                                                                                                                                                          |
| [**CreateThreadpoolWork**](createthreadpoolwork.md)                                       | Creates a new work object.                                                                                                                                                                                                                          |
| [**DestroyThreadpoolEnvironment**](destroythreadpoolenvironment.md)                       | Deletes the specified callback environment. Call this function when the callback environment is no longer needed for creating new thread pool objects.                                                                                              |
| [**DisassociateCurrentThreadFromCallback**](disassociatecurrentthreadfromcallback.md)     | Removes the association between the currently executing callback function and the object that initiated the callback. The current thread will no longer count as executing a callback on behalf of the object.                                      |
| [**FreeLibraryWhenCallbackReturns**](freelibrarywhencallbackreturns.md)                   | Specifies the DLL that the thread pool will unload when the current callback completes.                                                                                                                                                             |
| [**InitializeThreadpoolEnvironment**](initializethreadpoolenvironment.md)                 | Initializes a callback environment.                                                                                                                                                                                                                 |
| [**IsThreadpoolTimerSet**](isthreadpooltimerset.md)                                       | Determines whether the specified timer object is currently set.                                                                                                                                                                                     |
| [**LeaveCriticalSectionWhenCallbackReturns**](leavecriticalsectionwhencallbackreturns.md) | Specifies the critical section that the thread pool will release when the current callback completes.                                                                                                                                               |
| [**QueryThreadpoolStackInformation**](querythreadpoolstackinformation.md)                 | Retrieves the stack reserve and commit sizes for threads in the specified thread pool.                                                                                                                                                              |
| [**ReleaseMutexWhenCallbackReturns**](releasemutexwhencallbackreturns.md)                 | Specifies the mutex that the thread pool will release when the current callback completes.                                                                                                                                                          |
| [**ReleaseSemaphoreWhenCallbackReturns**](releasesemaphorewhencallbackreturns.md)         | Specifies the semaphore that the thread pool will release when the current callback completes.                                                                                                                                                      |
| [**SetEventWhenCallbackReturns**](seteventwhencallbackreturns.md)                         | Specifies the event that the thread pool will set when the current callback completes.                                                                                                                                                              |
| [**SetThreadpoolCallbackCleanupGroup**](setthreadpoolcallbackcleanupgroup.md)             | Associates the specified cleanup group with the specified callback environment.                                                                                                                                                                     |
| [**SetThreadpoolCallbackLibrary**](setthreadpoolcallbacklibrary.md)                       | Ensures that the specified DLL remains loaded as long as there are outstanding callbacks.                                                                                                                                                           |
| [**SetThreadpoolCallbackPersistent**](setthreadpoolcallbackpersistent.md)                 | Specifies that the callback should run on a persistent thread.                                                                                                                                                                                      |
| [**SetThreadpoolCallbackPool**](setthreadpoolcallbackpool.md)                             | Sets the thread pool to be used when generating callbacks.                                                                                                                                                                                          |
| [**SetThreadpoolCallbackPriority**](setthreadpoolcallbackpriority.md)                     | Specifies the priority of a callback function relative to other work items in the same thread pool.                                                                                                                                                 |
| [**SetThreadpoolCallbackRunsLong**](setthreadpoolcallbackrunslong.md)                     | Indicates that callbacks associated with this callback environment may not return quickly.                                                                                                                                                          |
| [**SetThreadpoolStackInformation**](setthreadpoolstackinformation.md)                     | Sets the stack reserve and commit sizes for new threads in the specified thread pool.                                                                                                                                                               |
| [**SetThreadpoolThreadMaximum**](setthreadpoolthreadmaximum.md)                           | Sets the maximum number of threads that the specified thread pool can allocate to process callbacks.                                                                                                                                                |
| [**SetThreadpoolThreadMinimum**](setthreadpoolthreadminimum.md)                           | Sets the minimum number of threads that the specified thread pool must make available to process callbacks.                                                                                                                                         |
| [**SetThreadpoolTimerEx**](setthreadpooltimerex.md)                                       | Sets the timer object. A worker thread calls the timer object's callback after the specified timeout expires.                                                                                                                                       |
| [**SetThreadpoolTimer**](setthreadpooltimer.md)                                           | Sets the timer object. A worker thread calls the timer object's callback after the specified timeout expires.                                                                                                                                       |
| [**SetThreadpoolWait**](setthreadpoolwait.md)                                             | Sets the wait object. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.                                                                                           |
| [**SetThreadpoolWaitEx**](setthreadpoolwaitex.md)                                         | Sets the wait object. A worker thread calls the wait object's callback function after the handle becomes signaled or after the specified timeout expires.                                                                                           |
| [**StartThreadpoolIo**](startthreadpoolio.md)                                             | Notifies the thread pool that I/O operations may possibly begin for the specified I/O completion object. A worker thread calls the I/O completion object's callback function after the operation completes on the file handle bound to this object. |
| [**SubmitThreadpoolWork**](submitthreadpoolwork.md)                                       | Posts a work object to the thread pool. A worker thread calls the work object's callback function.                                                                                                                                                  |
| [**TpInitializeCallbackEnviron**](tpinitializecallbackenviron.md)                         | Initializes a callback environment for the thread pool.                                                                                                                                                                                             |
| [**TpDestroyCallbackEnviron**](tpdestroycallbackenviron.md)                               | Deletes the specified callback environment. Call this function when the callback environment is no longer needed for creating new thread pool objects.                                                                                              |
| [**TpSetCallbackActivationContext**](tpsetcallbackactivationcontext.md)                   | Assigns an activation context to the callback environment.                                                                                                                                                                                          |
| [**TpSetCallbackCleanupGroup**](tpsetcallbackcleanupgroup.md)                             | Associates the specified cleanup group with the specified callback environment.                                                                                                                                                                     |
| [**TpSetCallbackFinalizationCallback**](tpsetcallbackfinalizationcallback.md)             | Indicates a function to call when the callback environment is finalized.                                                                                                                                                                            |
| [**TpSetCallbackLongFunction**](tpsetcallbacklongfunction.md)                             | Indicates that callbacks associated with this callback environment may not return quickly.                                                                                                                                                          |
| [**TpSetCallbackNoActivationContext**](tpsetcallbacknoactivationcontext.md)               | Indicates that the callback environment has no activation context.                                                                                                                                                                                  |
| [**TpSetCallbackPersistent**](tpsetcallbackpersistent.md)                                 | Specifies that the callback should run on a persistent thread.                                                                                                                                                                                      |
| [**TpSetCallbackPriority**](tpsetcallbackpriority.md)                                     | Specifies the priority of a callback function relative to other work items in the same thread pool.                                                                                                                                                 |
| [**TpSetCallbackRaceWithDll**](tpsetcallbackracewithdll.md)                               | Ensures that the specified DLL remains loaded as long as there are outstanding callbacks.                                                                                                                                                           |
| [**TpSetCallbackThreadpool**](tpsetcallbackthreadpool.md)                                 | Assigns a thread pool to a callback environment.                                                                                                                                                                                                    |
| [**TrySubmitThreadpoolCallback**](trysubmitthreadpoolcallback.md)                         | Requests that a thread pool worker thread call the specified callback function.                                                                                                                                                                     |
| [**WaitForThreadpoolIoCallbacks**](waitforthreadpooliocallbacks.md)                       | Waits for outstanding I/O completion callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                           |
| [**WaitForThreadpoolTimerCallbacks**](waitforthreadpooltimercallbacks.md)                 | Waits for outstanding timer callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                    |
| [**WaitForThreadpoolWaitCallbacks**](waitforthreadpoolwaitcallbacks.md)                   | Waits for outstanding wait callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                     |
| [**WaitForThreadpoolWorkCallbacks**](waitforthreadpoolworkcallbacks.md)                   | Waits for outstanding work callbacks to complete and optionally cancels pending callbacks that have not yet started to execute.                                                                                                                     |



 

The following functions are part of the original [thread pooling](thread-pooling.md) API.



| Function                                                            | Description                                                                                                                                                                                                            |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BindIoCompletionCallback**](bindiocompletioncallback.md)        | Associates the I/O completion port owned by the thread pool with the specified file handle. On completion of an I/O request involving this file, a non-I/O worker thread will execute the specified callback function. |
| [**QueueUserWorkItem**](queueuserworkitem.md)                      | Queues a work item to a worker thread in the thread pool.                                                                                                                                                              |
| [**RegisterWaitForSingleObject**](base.registerwaitforsingleobject) | Directs a wait thread in the thread pool to wait on the object.                                                                                                                                                        |
| [**UnregisterWaitEx**](base.unregisterwaitex)                       | Waits until one or all of the specified objects are in the signaled state or the time-out interval elapses.                                                                                                            |



 

## Thread Ordering Service Functions

The following functions are used with the [thread ordering service](thread-ordering-service.md).



| Function                                                                   | Description                                                                                 |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**AvQuerySystemResponsiveness**](avquerysystemresponsiveness.md)         | Retrieves the system responsiveness setting used by the multimedia class scheduler service. |
| [**AvRtCreateThreadOrderingGroup**](avrtcreatethreadorderinggroup.md)     | Creates a thread ordering group.                                                            |
| [**AvRtCreateThreadOrderingGroupEx**](avrtcreatethreadorderinggroupex.md) | Creates a thread ordering group and associates the server thread with a task.               |
| [**AvRtDeleteThreadOrderingGroup**](avrtdeletethreadorderinggroup.md)     | Deletes the specified thread ordering group created by the caller.                          |
| [**AvRtJoinThreadOrderingGroup**](avrtjointhreadorderinggroup.md)         | Joins client threads to a thread ordering group.                                            |
| [**AvRtLeaveThreadOrderingGroup**](avrtleavethreadorderinggroup.md)       | Enables client threads to leave a thread ordering group.                                    |
| [**AvRtWaitOnThreadOrderingGroup**](avrtwaitonthreadorderinggroup.md)     | Enables client threads of a thread ordering group to wait until they should execute.        |



 

## Multimedia Class Scheduler Service Functions

The following functions are used with the [multimedia class scheduler service](multimedia-class-scheduler-service.md).



| Function                                                                   | Description                                                                                           |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**AvRevertMmThreadCharacteristics**](avrevertmmthreadcharacteristics.md) | Indicates that a thread is no longer performing work associated with the specified task.              |
| [**AvSetMmMaxThreadCharacteristics**](avsetmmmaxthreadcharacteristics.md) | Associates the calling thread with the specified tasks.                                               |
| [**AvSetMmThreadCharacteristics**](avsetmmthreadcharacteristics.md)       | Associates the calling thread with the specified task.                                                |
| [**AvSetMmThreadPriority**](avsetmmthreadpriority.md)                     | Adjusts the thread priority of the calling thread relative to other threads performing the same task. |



 

## Fiber Functions

The following functions are used with [fibers](fibers.md).



| Function                                                 | Description                                                                                                  |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ConvertFiberToThread**](convertfibertothread.md)     | Converts the current fiber into a thread.                                                                    |
| [**ConvertThreadToFiber**](convertthreadtofiber.md)     | Converts the current thread into a fiber.                                                                    |
| [**ConvertThreadToFiberEx**](convertthreadtofiberex.md) | Converts the current thread into a fiber.                                                                    |
| [**CreateFiber**](createfiber.md)                       | Allocates a fiber object, assigns it a stack, and sets up execution to begin at the specified start address. |
| [**CreateFiberEx**](createfiberex.md)                   | Allocates a fiber object, assigns it a stack, and sets up execution to begin at the specified start address. |
| [**DeleteFiber**](deletefiber.md)                       | Deletes an existing fiber.                                                                                   |
| [**FiberProc**](fiberproc.md)                           | An application-defined function used with the [**CreateFiber**](createfiber.md) function.                   |
| [**FlsAlloc**](flsalloc.md)                             | Allocates a fiber local storage (FLS) index.                                                                 |
| [**FlsFree**](flsfree.md)                               | Releases an FLS index.                                                                                       |
| [**FlsGetValue**](flsgetvalue.md)                       | Retrieves the value in the calling fiber's FLS slot for a specified FLS index.                               |
| [**FlsSetValue**](flssetvalue.md)                       | Stores a value in the calling fiber's FLS slot for a specified FLS index.                                    |
| [**IsThreadAFiber**](isthreadafiber.md)                 | Determines whether the current thread is a fiber.                                                            |
| [**SwitchToFiber**](switchtofiber.md)                   | Schedules a fiber.                                                                                           |



 

## NUMA Support Functions

The following functions provide [NUMA support](numa-support.md).



| Function                                                                 | Description                                                                                                                                            |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPagesNuma**](base.allocateuserphysicalpagesnuma)  | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |
| [**GetLogicalProcessorInformation**](getlogicalprocessorinformation.md) | Retrieves information about logical processors and related hardware.                                                                                   |
| [**GetNumaAvailableMemoryNode**](getnumaavailablememorynode.md)         | Retrieves the amount of memory available in the specified node.                                                                                        |
| [**GetNumaAvailableMemoryNodeEx**](getnumaavailablememorynodeex.md)     | Retrieves the amount of memory that is available in the specified node as a USHORT value.                                                              |
| [**GetNumaHighestNodeNumber**](getnumahighestnodenumber.md)             | Retrieves the node that currently has the highest number.                                                                                              |
| [**GetNumaNodeNumberFromHandle**](getnumanodenumberfromhandle.md)       | Retrieves the NUMA node associated with the underlying device for a file handle.                                                                       |
| [**GetNumaNodeProcessorMask**](getnumanodeprocessormask.md)             | Retrieves the processor mask for the specified node.                                                                                                   |
| [**GetNumaNodeProcessorMaskEx**](getnumanodeprocessormaskex.md)         | Retrieves the processor mask for the specified NUMA node as a USHORT value.                                                                            |
| [**GetNumaProcessorNode**](getnumaprocessornode.md)                     | Retrieves the node number for the specified processor.                                                                                                 |
| [**GetNumaProcessorNodeEx**](getnumaprocessornodeex.md)                 | Retrieves the node number of the specified logical processor as a USHORT value.                                                                        |
| [**GetNumaProximityNode**](getnumaproximitynode.md)                     | Retrieves the node number for the specified proximity identifier.                                                                                      |
| [**GetNumaProximityNodeEx**](getnumaproximitynodeex.md)                 | Retrieves the node number as a USHORT value for the specified proximity identifier.                                                                    |
| [**VirtualAllocExNuma**](base.virtualallocexnuma)                        | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |



 

## Processor Functions

The following functions are used with logical processors and [processor groups](processor-groups.md).



| Function                                                                     | Description                                                                                                          |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**GetActiveProcessorCount**](getactiveprocessorcount.md)                   | Returns the number of active processors in a processor group or in the system.                                       |
| [**GetActiveProcessorGroupCount**](getactiveprocessorgroupcount.md)         | Returns the number of active processor groups in the system.                                                         |
| [**GetCurrentProcessorNumber**](getcurrentprocessornumber.md)               | Retrieves the number of the processor the current thread was running on during the call to this function.            |
| [**GetCurrentProcessorNumberEx**](getcurrentprocessornumberex.md)           | Retrieves the processor group and number of the logical processor in which the calling thread is running.            |
| [**GetLogicalProcessorInformation**](getlogicalprocessorinformation.md)     | Retrieves information about logical processors and related hardware.                                                 |
| [**GetLogicalProcessorInformationEx**](getlogicalprocessorinformationex.md) | Retrieves information about the relationships of logical processors and related hardware.                            |
| [**GetMaximumProcessorCount**](getmaximumprocessorcount.md)                 | Returns the maximum number of logical processors that a processor group or the system can have.                      |
| [**GetMaximumProcessorGroupCount**](getmaximumprocessorgroupcount.md)       | Returns the maximum number of processor groups that the system can have.                                             |
| [**QueryIdleProcessorCycleTime**](queryidleprocessorcycletime.md)           | Retrieves the cycle time for the idle thread of each processor in the system.                                        |
| [**QueryIdleProcessorCycleTimeEx**](queryidleprocessorcycletimeex.md)       | Retrieves the accumulated cycle time for the idle thread on each logical processor in the specified processor group. |



 

## User-Mode Scheduling Functions

The following functions are used with user-mode scheduling (UMS).



| Function                                                               | Description                                                                                               |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**CreateUmsCompletionList**](createumscompletionlist.md)             | Creates a UMS completion list.                                                                            |
| [**CreateUmsThreadContext**](createumsthreadcontext.md)               | Creates a UMS thread context to represent a UMS worker thread.                                            |
| [**DeleteUmsCompletionList**](deleteumscompletionlist.md)             | Deletes the specified UMS completion list. The list must be empty.                                        |
| [**DeleteUmsThreadContext**](deleteumsthreadcontext.md)               | Deletes the specified UMS thread context. The thread must be terminated.                                  |
| [**DequeueUmsCompletionListItems**](dequeueumscompletionlistitems.md) | Retrieves UMS worker threads from the specified UMS completion list.                                      |
| [**EnterUmsSchedulingMode**](enterumsschedulingmode.md)               | Converts the calling thread into a UMS scheduler thread.                                                  |
| [**ExecuteUmsThread**](executeumsthread.md)                           | Runs the specified UMS worker thread.                                                                     |
| [**GetCurrentUmsThread**](getcurrentumsthread.md)                     | Returns the UMS thread context of the calling UMS thread.                                                 |
| [**GetNextUmsListItem**](getnextumslistitem.md)                       | Returns the next UMS thread context in a list of UMS thread contexts.                                     |
| [**GetUmsCompletionListEvent**](getumscompletionlistevent.md)         | Retrieves a handle to the event associated with the specified UMS completion list.                        |
| [**GetUmsSystemThreadInformation**](getumssystemthreadinformation.md) | Queries whether the specified thread is a UMS scheduler thread, a UMS worker thread, or a non-UMS thread. |
| [**QueryUmsThreadInformation**](queryumsthreadinformation.md)         | Retrieves information about the specified UMS worker thread.                                              |
| [**SetUmsThreadInformation**](setumsthreadinformation.md)             | Sets application-specific context information for the specified UMS worker thread.                        |
| [*UmsSchedulerProc*](umsschedulerproc.md)                             | The application-defined UMS scheduler entry point function associated with a UMS completion list.         |
| [**UmsThreadYield**](umsthreadyield.md)                               | Yields control to the UMS scheduler thread on which the calling UMS worker thread is running.             |



 

## Obsolete Functions

-   [**NtGetCurrentProcessorNumber**](ntgetcurrentprocessornumber.md)
-   [**NtQueryInformationProcess**](ntqueryinformationprocess.md)
-   [**NtQueryInformationThread**](ntqueryinformationthread.md)
-   [**WinExec**](winexec.md)
-   [**ZwQueryInformationProcess**](zwqueryinformationprocess.md)

 

 



