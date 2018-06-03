---
Description: The FlushTrace function causes an event tracing session to immediately deliver buffered events for the specified session.
ms.assetid: bc7d0dac-93d9-4614-9cb6-fee99765eb39
title: FlushTrace function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FlushTrace function

The **FlushTrace** function causes an event tracing session to immediately deliver buffered events for the specified session. (An event tracing session does not deliver events until an active buffer is full.)

The [**ControlTrace**](controltrace.md) function supersedes this function.

## Syntax


```C++
ULONG FlushTrace(
  _In_    TRACEHANDLE             SessionHandle,
  _In_    LPCTSTR                 SessionName,
  _Inout_ PEVENT_TRACE_PROPERTIES Properties
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session for whose buffers you want to flush, or **NULL**. You must specify *SessionHandle* if *SessionName* is **NULL**. However, ETW ignores the handle if *SessionName* is not **NULL**. The handle is returned by the [**StartTrace**](starttrace.md) function.

</dd> <dt>

*SessionName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the event tracing session whose buffers you want to flush, or **NULL**. You must specify *SessionName* if *SessionHandle* is **NULL**.

To specify the NT Kernel Logger session, set *SessionName* to **KERNEL\_LOGGER\_NAME**.

</dd> <dt>

*Properties* \[in, out\]
</dt> <dd>

Pointer to an initialized [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure.

If you are using a newly initialized structure, you only need to set the **Wnode.BufferSize**, **Wnode.Guid**, **LoggerNameOffset**, and **LogFileNameOffset** members of the structure. You can use the maximum session name (1024 characters) and maximum log file name (1024 characters) lengths to calculate the buffer size and offsets if not known.

On output, the structure receives the property settings and session statistics of the event tracing session, which reflect the state of the session after the flush.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/windows/desktop/4a3a8feb-a05f-4614-8f04-1f507da7e5b7). The following table includes some common errors and their causes.



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
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true: <br/>
<ul>
<li><em>Properties</em> is <strong>NULL</strong>.</li>
<li><em>SessionName</em> and <em>SessionHandle</em> are both <strong>NULL</strong>.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_BAD_LENGTH</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li>The <strong>Wnode.BufferSize</strong> member of <em>Properties</em> specifies an incorrect size.</li>
<li><em>Properties</em> does not have sufficient space allocated to hold a copy of the session name and log file name (if used).</li>
</ul></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users with administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can control event tracing sessions. To grant a restricted user the ability to control trace sessions, add them to the Performance Log Users group.<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can control a trace session.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Controllers call this function.

Typically, you do not need to flush buffers yourself. However, you may want to flush buffers if the event rate is low and you are delivering events in real time.

Note that it is not safe to flush buffers from DllMain.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **FlushTraceW** (Unicode) and **FlushTraceA** (ANSI)<br/>                         |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> </dl>

 

 




