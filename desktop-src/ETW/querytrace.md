---
Description: The QueryTrace function retrieves the property settings and session statistics for the specified event tracing session. The ControlTrace function supersedes this function.
ms.assetid: 8ad0f4f6-902c-490e-b26e-7499dd99fc95
title: QueryTrace function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- QueryTrace
- QueryTraceA
- QueryTraceW
api_type: 
- DllExport
api_location: 
- Advapi32.dll
- API-MS-Win-eventing-Legacy-l1-1-0.dll
- advapi32legacy.dll
---

# QueryTrace function

The **QueryTrace** function retrieves the property settings and session statistics for the specified event tracing session.

The [**ControlTrace**](controltrace.md) function supersedes this function.

## Syntax


```C++
ULONG QueryTrace(
  _In_    TRACEHANDLE             SessionHandle,
  _In_    LPCTSTR                 SessionName,
  _Inout_ PEVENT_TRACE_PROPERTIES Properties
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session for whose properties and statistics you want to query, or **NULL**. You must specify *SessionHandle* if *SessionName* is **NULL**. However, ETW ignores the handle if *SessionName* is not **NULL**. The handle is returned by the [**StartTrace**](starttrace.md) function.

</dd> <dt>

*SessionName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the event tracing session whose properties and statistics you want to query, or **NULL**. You must specify *SessionName* if *SessionHandle* is **NULL**.

To specify the NT Kernel Logger session, set *SessionName* to **KERNEL\_LOGGER\_NAME**.

</dd> <dt>

*Properties* \[in, out\]
</dt> <dd>

Pointer to an initialized [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure.

You only need to set the **Wnode.BufferSize** member of the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure. You can use the maximum session name (1024 characters) and maximum log file name (1024 characters) lengths to calculate the buffer size and offsets if not known.

On output, the structure members contain the property settings and session statistics for the event tracing session.

**Starting with Windows 10, version 1703:** For better performance in cross process scenarios, you can now pass filtering in to **QueryTrace** for system wide private loggers. You will need to pass in the new [**EVENT\_TRACE\_PROPERTIES\_V2**](event-trace-properties-v2.md) structure to include filtering information. See [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md) for more details.

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
<td>One of the following is true:<br/>
<ul>
<li>The <strong>Wnode.BufferSize</strong> member of <em>Properties</em> specifies an incorrect size.</li>
<li><em>Properties</em> does not have sufficient space allocated to hold a copy of the session name and log file name (if used).</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true: <br/>
<ul>
<li><em>Properties</em> is <strong>NULL</strong>.</li>
<li><em>SessionName</em> and <em>SessionHandle</em> are both <strong>NULL</strong>.</li>
</ul></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users running with elevated administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can query event tracing sessions. To grant a restricted user the ability to query trace sessions, add them to the Performance Log Users group or see <a href="/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol"><strong>EventAccessControl</strong></a>.<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can control a trace session.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_WMI_INSTANCE_NOT_FOUND</strong></dt> </dl></td>
<td>The given session is not running.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Controllers call this function.

To update the property settings and session statistics for an event tracing session, call the [**UpdateTrace**](updatetrace.md) function.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **QueryTraceW** (Unicode) and **QueryTraceA** (ANSI)<br/>                         |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> <dt>

[**QueryAllTraces**](queryalltraces.md)
</dt> </dl>

 

 




