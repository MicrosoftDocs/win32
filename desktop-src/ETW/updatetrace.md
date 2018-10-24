---
Description: The UpdateTrace function updates the property setting of the specified event tracing session. The ControlTrace function supersedes this function.
ms.assetid: 40e6deaf-7363-45eb-80d0-bc3f33760875
title: UpdateTrace function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UpdateTrace
- UpdateTraceA
- UpdateTraceW
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- API-MS-Win-eventing-Legacy-l1-1-0.dll
- advapi32legacy.dll
---

# UpdateTrace function

The **UpdateTrace** function updates the property setting of the specified event tracing session.

The [**ControlTrace**](controltrace.md) function supersedes this function.

## Syntax


```C++
ULONG UpdateTrace(
  _In_    TRACEHANDLE             SessionHandle,
  _In_    LPCTSTR                 SessionName,
  _Inout_ PEVENT_TRACE_PROPERTIES Properties
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session to update, or **NULL**. You must specify *SessionHandle* if *SessionName* is **NULL**. However, ETW ignores the handle if *SessionName* is not **NULL**. The handle is returned by the [**StartTrace**](starttrace.md) function.

</dd> <dt>

*SessionName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the event tracing session to update, or **NULL**. You must specify *SessionName* if *SessionHandle* is **NULL**.

To specify the NT Kernel Logger session, set *SessionName* to **KERNEL\_LOGGER\_NAME**.

</dd> <dt>

*Properties* \[in, out\]
</dt> <dd>

Pointer to an initialized [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure.

On input, the members must specify the new values for the properties to update. For information on which properties you can update, see Remarks.

On output, the structure members contains the updated settings and statistics for the event tracing session.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/en-us/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



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
<td>The <strong>BufferSize</strong> member of the <strong>Wnode</strong> member of <em>Properties</em> specifies an incorrect size.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>SessionName</em> and <em>SessionHandle</em> are both <strong>NULL</strong>.</li>
<li><em>Properties</em> is <strong>NULL</strong>.</li>
<li>The <strong>LogFileNameOffset</strong> member of <em>Properties</em> is not valid.</li>
<li>The <strong>LoggerNameOffset</strong> member of <em>Properties</em> is not valid.</li>
</ul>
<strong>Windows Server 2003 and Windows XP:</strong> The <strong>Guid</strong> member of the <strong>Wnode</strong> structure is SystemTraceControlGuid, but the <em>SessionName</em> parameter is not KERNEL_LOGGER_NAME.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users with administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can control event tracing sessions. To grant a restricted user the ability to control trace sessions, add them to the Performance Log Users group.<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can control a trace session.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Controllers call this function.

On input, the members must specify the new values for the properties to update. You can update the following properties.



| Member                | Use                                                                                                                                                                                                                                                                         |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EnableFlags**       | Set this member to 0 to disable all kernel providers. Otherwise, you must specify the kernel providers that you want to enable or keep enabled. Applies only to NT Kernel Logger sessions.                                                                                  |
| **FlushTimer**        | Set this member if you want to change the time to wait before flushing buffers. If this member is 0, the member is not updated.                                                                                                                                             |
| **LogFileNameOffset** | Set this member if you want to switch to another log file. If this member is 0, the file name is not updated. If the offset is not zero and you do not change the log file name, the function returns an error.                                                             |
| **LogFileMode**       | Set this member if you want to turn **EVENT\_TRACE\_REAL\_TIME\_MODE** on and off. To turn real time consuming off, set this member to 0. To turn real time consuming on, set this member to **EVENT\_TRACE\_REAL\_TIME\_MODE** and it will be OR'd with the current modes. |
| **MaximumBuffers**    | Set set this member if you want to change the maximum number of buffers that ETW uses. If this member is 0, the member is not updated.                                                                                                                                      |



 

For private logger sessions, you can only update **LogFileNameOffset** and **FlushTimer**.

If you are using a newly initialized [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure, the only members you need to specify, other than the members you are updating, are **Wnode.BufferSize**, **Wnode.Guid**, and **Wnode.Flags**.

If you use the property structure you passed to [**StartTrace**](starttrace.md), make sure the **LogFileNameOffset** member is 0 unless you are changing the log file name.

If you call the [**ControlTrace**](controltrace.md) function to query the current session properties and then update those properties to update the session, make sure you set **LogFileNameOffset** to 0 (unless you are changing the log file name) and set [**EVENT\_TRACE\_PROPERTIES.Wnode.Flags**](event-trace-properties.md) to **WNODE\_FLAG\_TRACED\_GUID**.

To obtain the property settings and session statistics for an event tracing session, call the [**ControlTrace**](controltrace.md) function.

## Examples

For an example that uses **UpdateTrace**, see [Updating an Event Tracing Session](updating-an-event-tracing-session.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **UpdateTraceW** (Unicode) and **UpdateTraceA** (ANSI)<br/>                       |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> </dl>

 

 




