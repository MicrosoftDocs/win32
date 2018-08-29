---
Description: The ControlTrace function flushes, queries, updates, or stops the specified event tracing session.
ms.assetid: c39f669c-ff40-40ed-ba47-798474ec2de4
title: ControlTrace function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ControlTrace
- ControlTraceA
- ControlTraceW
api_type: 
- DllExport
api_location: 
- Sechost.dll
- Advapi32.dll
- API-MS-Win-DownLevel-AdvAPI32-l2-1-1.dll
- API-MS-Win-Eventing-Controller-l1-1-0.dll
- API-MS-Win-Eventing-Legacy-l1-1-0.dll
- AdvApi32Legacy.dll
- KernelBase.dll
---

# ControlTrace function

The **ControlTrace** function flushes, queries, updates, or stops the specified event tracing session.

## Syntax


```C++
ULONG ControlTrace(
  _In_    TRACEHANDLE             SessionHandle,
  _In_    LPCTSTR                 SessionName,
  _Inout_ PEVENT_TRACE_PROPERTIES Properties,
  _In_    ULONG                   ControlCode
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to an event tracing session, or **NULL**. You must specify *SessionHandle* if *SessionName* is **NULL**. However, ETW ignores the handle if *SessionName* is not **NULL**. The handle is returned by the [**StartTrace**](starttrace.md) function.

</dd> <dt>

*SessionName* \[in\]
</dt> <dd>

Name of an event tracing session, or **NULL**. You must specify *SessionName* if *SessionHandle* is **NULL**.

To specify the NT Kernel Logger session, set *SessionName* to **KERNEL\_LOGGER\_NAME**.

</dd> <dt>

*Properties* \[in, out\]
</dt> <dd>

Pointer to an initialized [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure. This structure should be zeroed out before it is used.

If *ControlCode* specifies **EVENT\_TRACE\_CONTROL\_STOP**, **EVENT\_TRACE\_CONTROL\_QUERY** or **EVENT\_TRACE\_CONTROL\_FLUSH**, you only need to set the **Wnode.BufferSize**, **Wnode.Guid**, **LoggerNameOffset**, and **LogFileNameOffset** members of the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure. If the session is a private session, you also need to set **LogFileMode**. You can use the maximum session name (1024 characters) and maximum log file name (1024 characters) lengths to calculate the buffer size and offsets if not known.

If *ControlCode* specifies **EVENT\_TRACE\_CONTROL\_UPDATE**, on input, the members must specify the new values for the properties to update. On output, *Properties* contains the properties and statistics for the event tracing session. You can update the following properties.



| Member                | Use                                                                                                                                                                                                                                                                         |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EnableFlags**       | Set this member to 0 to disable all kernel providers. Otherwise, you must specify the kernel providers that you want to enable or keep enabled. Applies only to NT Kernel Logger sessions.                                                                                  |
| **FlushTimer**        | Set this member if you want to change the time to wait before flushing buffers. If this member is 0, the member is not updated.                                                                                                                                             |
| **LogFileNameOffset** | Set this member if you want to switch to another log file. If this member is 0, the file name is not updated. If the offset is not zero and you do not change the log file name, the function returns an error.                                                             |
| **LogFileMode**       | Set this member if you want to turn **EVENT\_TRACE\_REAL\_TIME\_MODE** on and off. To turn real time consuming off, set this member to 0. To turn real time consuming on, set this member to **EVENT\_TRACE\_REAL\_TIME\_MODE** and it will be OR'd with the current modes. |
| **MaximumBuffers**    | Set this member if you want to change the maximum number of buffers that ETW uses. If this member is 0, the member is not updated.                                                                                                                                          |



 

For private logger sessions, you can update only the **LogFileNameOffset** and **FlushTimer** members.

If you are using a newly initialized [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure, the only members you need to specify, other than the members you are updating, are **Wnode.BufferSize**, **Wnode.Guid**, and **Wnode.Flags**.

If you use the property structure you passed to [**StartTrace**](starttrace.md), make sure the **LogFileNameOffset** member is 0 unless you are changing the log file name.

If you call the **ControlTrace** function to query the current session properties and then update those properties to update the session, make sure you set **LogFileNameOffset** to 0 (unless you are changing the log file name) and set [**EVENT\_TRACE\_PROPERTIES.Wnode.Flags**](event-trace-properties.md) to **WNODE\_FLAG\_TRACED\_GUID**.

**Starting with Windows 10, version 1703:** For better performance in cross process scenarios, you can now pass filtering in to **ControlTrace** for system wide private loggers. You will need to pass in the new [**EVENT\_TRACE\_PROPERTIES\_V2**](event-trace-properties-v2.md) structure to include filtering information. See [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md) for more details.

</dd> <dt>

*ControlCode* \[in\]
</dt> <dd>

Requested control function. You can specify one of the following values.



| Value                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_TRACE_CONTROL_FLUSH"></span><span id="event_trace_control_flush"></span><dl> <dt>****EVENT\_TRACE\_CONTROL\_FLUSH****</dt> </dl>    | Flushes the session's active buffers. Typically, you do not need to flush buffers yourself. However, you may want to flush buffers if the event rate is low and you are delivering events in real time.<br/> **Windows 2000:** This value is not supported.<br/> |
| <span id="EVENT_TRACE_CONTROL_QUERY"></span><span id="event_trace_control_query"></span><dl> <dt>****EVENT\_TRACE\_CONTROL\_QUERY****</dt> </dl>    | Retrieves session properties and statistics.<br/>                                                                                                                                                                                                                      |
| <span id="EVENT_TRACE_CONTROL_STOP"></span><span id="event_trace_control_stop"></span><dl> <dt>****EVENT\_TRACE\_CONTROL\_STOP****</dt> </dl>       | Stops the session. The session handle is no longer valid.<br/>                                                                                                                                                                                                         |
| <span id="EVENT_TRACE_CONTROL_UPDATE"></span><span id="event_trace_control_update"></span><dl> <dt>****EVENT\_TRACE\_CONTROL\_UPDATE****</dt> </dl> | Updates the session properties.<br/>                                                                                                                                                                                                                                   |



 

Note that it is not safe to flush buffers or stop a trace session from DllMain.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381). The following table includes some common errors and their causes.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>ERROR_BAD_LENGTH</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li>The <strong>Wnode.BufferSize</strong> member of <em>Properties</em> specifies an incorrect size.</li>
<li><em>Properties</em> does not have sufficient space allocated to hold a copy of the session name and log file name (if used).</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>Properties</em> is <strong>NULL</strong>.</li>
<li><em>SessionName</em> and <em>SessionHandle</em> are both <strong>NULL</strong>.</li>
<li>The <strong>LogFileNameOffset</strong> member of <em>Properties</em> is not valid.</li>
<li>The <strong>LoggerNameOffset</strong> member of <em>Properties</em> is not valid.</li>
<li>The <strong>LogFileMode</strong> member of <em>Properties</em> specifies a combination of flags that is not valid.</li>
<li>The <strong>Wnode.Guid</strong> member of <em>Properties</em> is <strong>SystemTraceControlGuid</strong>, but the <em>SessionName</em> parameter is not KERNEL_LOGGER_NAME.</li>
</ul></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_BAD_PATHNAME</strong></dt> </dl></td>
<td>Another session is already using the file name specified by the <strong>LogFileNameOffset</strong> member of the <em>Properties</em> structure. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_MORE_DATA</strong></dt> </dl></td>
<td>The buffer for <a href="event-trace-properties"><strong>EVENT_TRACE_PROPERTIES</strong></a> is too small to hold all the information for the session. If you do not need the session's property information, you can ignore this error. If you receive this error when stopping the session, ETW will have already stopped the session before generating this error.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users running with elevated administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can control event tracing sessions. To grant a restricted user the ability to control trace sessions, add them to the Performance Log Users group. Only users with administrative privileges and services running as LocalSystem can control an NT Kernel Logger session.<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can control a trace session.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_WMI_INSTANCE_NOT_FOUND</strong></dt> </dl></td>
<td>The given session is not running.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

This function supersedes the [**FlushTrace**](flushtrace.md), [**QueryTrace**](querytrace.md), [**StopTrace**](stoptrace.md), and [**UpdateTrace**](updatetrace.md) functions.

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                                                                                                                                                                                                                                 |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl>    |
| Unicode and ANSI names<br/>   | **ControlTraceW** (Unicode) and **ControlTraceA** (ANSI)<br/>                                                                                                                                                                                                                                                          |



## See also

<dl> <dt>

[**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md)
</dt> <dt>

[**QueryAllTraces**](queryalltraces.md)
</dt> <dt>

[**StartTrace**](starttrace.md)
</dt> </dl>

 

 




