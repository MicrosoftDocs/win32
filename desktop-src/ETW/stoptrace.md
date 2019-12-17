---
Description: The StopTrace function stops the specified event tracing session. The ControlTrace function supersedes this function.
ms.assetid: 604274a1-c4ed-4746-b69a-e18969f969db
title: StopTrace function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StopTrace
- StopTraceA
- StopTraceW
api_type: 
- DllExport
api_location: 
- Sechost.dll
- Advapi32.dll
- AdvApi32Legacy.dll
- API-MS-Win-DownLevel-AdvAPI32-l2-1-1.dll
- API-MS-Win-Eventing-Controller-l1-1-0.dll
- API-MS-Win-Eventing-Legacy-l1-1-0.dll
- KernelBase.dll
---

# StopTrace function

The **StopTrace** function stops the specified event tracing session.

The [**ControlTrace**](controltrace.md) function supersedes this function.

## Syntax


```C++
ULONG StopTrace(
  _In_  TRACEHANDLE             SessionHandle,
  _In_  LPCTSTR                 SessionName,
  _Out_ PEVENT_TRACE_PROPERTIES Properties
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle to the event tracing session that you want to stop, or **NULL**. You must specify *SessionHandle* if *SessionName* is **NULL**. However, ETW ignores the handle if *SessionName* is not **NULL**. The handle is returned by the [**StartTrace**](starttrace.md) function.

</dd> <dt>

*SessionName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the event tracing session that you want to stop, or **NULL**. You must specify *SessionName* if *SessionHandle* is **NULL**.

To specify the NT Kernel Logger session, set *SessionName* to **KERNEL\_LOGGER\_NAME**.

</dd> <dt>

*Properties* \[out\]
</dt> <dd>

Pointer to an [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure that receives the final properties and statistics for the session.

If you are using a newly initialized structure, you only need to set the **Wnode.BufferSize**, **Wnode.Guid**, **LoggerNameOffset**, and **LogFileNameOffset** members of the structure. You can use the maximum session name (1024 characters) and maximum log file name (1024 characters) lengths to calculate the buffer size and offsets if not known.

**Starting with Windows 10, version 1703:** For better performance in cross process scenarios, you can now pass filtering in to **StopTrace** for system wide private loggers. You will need to pass in the new [**EVENT\_TRACE\_PROPERTIES\_V2**](event-trace-properties-v2.md) structure to include filtering information. See [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md) for more details.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/library/ms681381(v=VS.85).aspx). The following table includes some common errors and their causes.



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

If **LogFileMode** contains **EVENT\_TRACE\_FILE\_MODE\_PREALLOCATE**, [**StartTrace**](starttrace.md) extends the log file to **MaximumFileSize** bytes. The file occupies the entire space during logging, for both circular and sequential logs. When you stop the logger, the log file is reduced to the size needed.

Note that it is not safe to stop a trace session from DllMain.

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                                                                                                                                                                                                                                 |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| Unicode and ANSI names<br/>   | **StopTraceW** (Unicode) and **StopTraceA** (ANSI)<br/>                                                                                                                                                                                                                                                                |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> <dt>

[**StartTrace**](starttrace.md)
</dt> </dl>

 

 




