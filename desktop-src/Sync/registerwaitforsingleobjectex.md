---
description: Directs a wait thread in the thread pool to wait on the object. (RegisterWaitForSingleObjectEx)
title: RegisterWaitForSingleObjectEx function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RegisterWaitForSingleObjectEx
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# RegisterWaitForSingleObjectEx function

Directs a wait thread in the <a href="/windows/desktop/ProcThread/thread-pooling">thread pool</a> to wait on the object. The wait thread queues the specified callback function to the thread pool when one of the following occurs:

- The specified object is in the signaled state.
- The time-out interval elapses.

## Syntax


```C++
WINBASEAPI
__out
HANDLE
WINAPI
RegisterWaitForSingleObjectEx(
    __in     HANDLE hObject,
    __in     WAITORTIMERCALLBACK Callback,
    __in_opt PVOID Context,
    __in     ULONG dwMilliseconds,
    __in     ULONG dwFlags
    );
```



## Parameters

### hObject [in]

A handle to the object. For a list of the object types whose handles can be specified, see the **Remarks** section. 

If this handle is closed while the wait is still pending, the function's behavior is undefined.

The handles must have the <b>SYNCHRONIZE</b> access right. For more information, see [Standard Access Rights](/windows/desktop/SecAuthZ/standard-access-rights).

### Callback [in]

A pointer to the application-defined function of type **WAITORTIMERCALLBACK** to be executed when *hObject* is in the signaled state, or *dwMilliseconds* elapses. For more information, see [WaitOrTimerCallback](/previous-versions/windows/desktop/legacy/ms687066(v=vs.85)).

### Context [in, optional]

A single value that is passed to the callback function.

### dwMiliseconds [in]

The time-out interval, in milliseconds. The function returns if the interval elapses, even if the object's state is nonsignaled. If <i>dwMilliseconds</i> is zero, the function tests the object's state and returns immediately. If <i>dwMilliseconds</i> is <b>INFINITE</b>, the function's time-out interval never elapses.

### dwFlags [in]

This parameter can be one or more of the following values. 

For information about using these values with objects that remain signaled, see the Remarks section.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="WT_EXECUTEDEFAULT"></a><a id="wt_executedefault"></a><dl>
<dt><b>WT_EXECUTEDEFAULT</b></dt>
<dt>0x00000000</dt>
</dl>
</td>
<td width="60%">
By default, the callback function is queued to a non-I/O worker thread.

</td>
</tr>
<tr>
<td width="40%"><a id="WT_EXECUTEINIOTHREAD"></a><a id="wt_executeiniothread"></a><dl>
<dt><b>WT_EXECUTEINIOTHREAD</b></dt>
<dt>0x00000001</dt>
</dl>
</td>
<td width="60%">
This flag is not used.

<b>Windows Server 2003 and Windows XP:  </b>The callback function is queued to an I/O worker thread. This flag should be used if the function should be executed in a thread that waits in an alertable state. 


I/O worker threads were removed starting with Windows Vista and Windows Server 2008.

</td>
</tr>
<tr>
<td width="40%"><a id="WT_EXECUTEINPERSISTENTTHREAD"></a><a id="wt_executeinpersistentthread"></a><dl>
<dt><b>WT_EXECUTEINPERSISTENTTHREAD</b></dt>
<dt>0x00000080</dt>
</dl>
</td>
<td width="60%">
The callback function is queued to a thread that never terminates. It does not guarantee that the same thread is used each time. This flag should be used only for short tasks or it could affect other wait operations. 


This flag must be set if the thread calls functions that use APCs. For more information, see <a href="/windows/desktop/Sync/asynchronous-procedure-calls">Asynchronous Procedure Calls</a>.

Note that currently no worker thread is truly persistent, although no worker thread will terminate if there are any pending I/O requests.

</td>
</tr>
<tr>
<td width="40%"><a id="WT_EXECUTEINWAITTHREAD"></a><a id="wt_executeinwaitthread"></a><dl>
<dt><b>WT_EXECUTEINWAITTHREAD</b></dt>
<dt>0x00000004</dt>
</dl>
</td>
<td width="60%">
The callback function is invoked by the wait thread itself. This flag should be used only for short tasks or it could affect other wait operations. 




Deadlocks can occur if some other thread acquires an exclusive lock and calls the 
<a href="/windows/desktop/api/winbase/nf-winbase-unregisterwait">UnregisterWait</a> or 
<a href="/windows/desktop/Sync/unregisterwaitex">UnregisterWaitEx</a> function while the callback function is trying to acquire the same lock.

</td>
</tr>
<tr>
<td width="40%"><a id="WT_EXECUTELONGFUNCTION"></a><a id="wt_executelongfunction"></a><dl>
<dt><b>WT_EXECUTELONGFUNCTION</b></dt>
<dt>0x00000010</dt>
</dl>
</td>
<td width="60%">
The callback function can perform a long wait. This flag helps the system to decide if it should create a new thread.

</td>
</tr>
<tr>
<td width="40%"><a id="WT_EXECUTEONLYONCE"></a><a id="wt_executeonlyonce"></a><dl>
<dt><b>WT_EXECUTEONLYONCE</b></dt>
<dt>0x00000008</dt>
</dl>
</td>
<td width="60%">
The thread will no longer wait on the handle after the callback function has been called once. Otherwise, the timer is reset every time the wait operation completes until the wait operation is canceled.

</td>
</tr>
<tr>
<td width="40%"><a id="WT_TRANSFER_IMPERSONATION"></a><a id="wt_transfer_impersonation"></a><dl>
<dt><b>WT_TRANSFER_IMPERSONATION</b></dt>
<dt>0x00000100</dt>
</dl>
</td>
<td width="60%">
Callback functions will use the current access token, whether it is a process or impersonation token. If this flag is not specified, callback functions execute only with the process token.

<b>Windows XP:  </b>This flag is not supported until Windows XP with SP2 and Windows Server 2003.

</td>
</tr>
</table>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call  
[GetLastError](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from kernel32.dll.

New wait threads are created automatically when required. The wait operation is performed by a wait thread from the thread pool. The callback routine is executed by a worker thread when the object's state becomes signaled or the time-out interval elapses. If <i>dwFlags</i> is not <b>WT_EXECUTEONLYONCE</b>, the timer is reset every time the event is signaled or the time-out interval elapses.

When the wait is completed, you must call the 
<a href="/windows/desktop/api/winbase/nf-winbase-unregisterwait">UnregisterWait</a> or 
<a href="/windows/desktop/Sync/unregisterwaitex">UnregisterWaitEx</a> function to cancel the wait operation. (Even wait operations that use <b>WT_EXECUTEONLYONCE</b> must be canceled.) Do not make a blocking call to either of these functions from within the callback function.

Note that you should not pulse an event object passed to 
<b>RegisterWaitForSingleObjectEx</b>, because the wait thread might not detect that the event is signaled before it is reset. You should not register an object that remains signaled (such as a manual reset event or terminated process) unless you set the <b>WT_EXECUTEONLYONCE</b> or <b>WT_EXECUTEINWAITTHREAD</b> flag. For other flags,  the callback function might be called too many times before the event is reset.

The function modifies the state of some types of synchronization objects. Modification occurs only for the object whose signaled state caused the wait condition to be satisfied. For example, the count of a semaphore object is decreased by one.

The 
<b>RegisterWaitForSingleObjectEx</b> function can wait for the following objects:

<ul>
<li>Change notification</li>
<li>Console input</li>
<li>Event</li>
<li>Memory resource notification</li>
<li>Mutex</li>
<li>Process</li>
<li>Semaphore</li>
<li>Thread</li>
<li>Waitable timer</li>
</ul>
For more information, see 
<a href="/windows/desktop/Sync/synchronization-objects">Synchronization Objects</a>.

By default, the thread pool has a maximum of 500 threads. To raise this limit, use the <b>WT_SET_MAX_THREADPOOL_THREAD</b> macro defined in WinNT.h.


``` syntax
#define WT_SET_MAX_THREADPOOL_THREADS(Flags,Limit) \
    ((Flags)|=(Limit)&lt;&lt;16)
```

Use this macro when specifying the <i>dwFlags</i> parameter. The macro parameters are the desired flags and the new limit (up to (2&lt;&lt;16)-1 threads). However, note that your application can improve its performance by keeping the number of worker threads low.

The work item and all functions it calls must be thread-pool safe. Therefore, you cannot call an asynchronous call that requires a persistent thread, such as the 
<a href="/windows/desktop/api/winreg/nf-winreg-regnotifychangekeyvalue">RegNotifyChangeKeyValue</a> function, from the default callback environment. Instead, set the thread pool maximum equal to the thread pool minimum using the <a href="/windows/desktop/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolthreadmaximum">SetThreadpoolThreadMaximum</a> and <a href="/windows/desktop/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolthreadminimum">SetThreadpoolThreadMinimum</a> functions, or create your own thread using the <a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createthread">CreateThread</a> function. (For the original thread pool API, specify <b>WT_EXECUTEINPERSISTENTTHREAD</b> using the <a href="/windows/desktop/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-queueuserworkitem">QueueUserWorkItem</a> function.)

To compile an application that uses this function, define <b>_WIN32_WINNT</b> as 0x0500 or later. For more information, see 
<a href="/windows/desktop/WinProg/using-the-windows-headers">Using the Windows Headers</a>.





## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows 10 |
| DLL | wldp.dll |



## See also



 

 
