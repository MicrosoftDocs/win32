---
Description: The StartTrace function registers and starts an event tracing session.
ms.assetid: c040514a-733d-44b9-8300-a8341d2630b3
title: StartTrace function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StartTrace
- StartTraceA
- StartTraceW
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

# StartTrace function

The **StartTrace** function registers and starts an event tracing session.

## Syntax


```C++
ULONG StartTrace(
  _Out_   PTRACEHANDLE            SessionHandle,
  _In_    LPCTSTR                 SessionName,
  _Inout_ PEVENT_TRACE_PROPERTIES Properties
);
```



## Parameters

<dl> <dt>

*SessionHandle* \[out\]
</dt> <dd>

Handle to the event tracing session.

Do not use this handle if the function fails. Do not compare the session handle to INVALID\_HANDLE\_VALUE; the session handle is 0 if the handle is not valid.

</dd> <dt>

*SessionName* \[in\]
</dt> <dd>

Null-terminated string that contains the name of the event tracing session. The session name is limited to 1,024 characters, is case-insensitive, and must be unique.

**Windows 2000:** Session names are case-sensitive. As a result, duplicate session names are allowed. However, to reduce confusion, you should make sure your session names are unique.

This function copies the session name that you provide to the offset that the **LoggerNameOffset** member of *Properties* points to.

</dd> <dt>

*Properties* \[in, out\]
</dt> <dd>

Pointer to an [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure that specifies the behavior of the session. The following are key members of the structure to set:

-   **Wnode.BufferSize**
-   **Wnode.Guid**
-   **Wnode.ClientContext**
-   **Wnode.Flags**
-   **LogFileMode**
-   **LogFileNameOffset**
-   **LoggerNameOffset**

Depending on the type of log file you choose to create, you may also need to specify a value for **MaximumFileSize**. See the Remarks section for more information on setting the *Properties* parameter and the behavior of the session.

**Starting with Windows 10, version 1703:** For better performance in cross process scenarios, you can now pass filtering in to **StartTrace** when starting system wide private loggers. You will need to pass in the new [**EVENT\_TRACE\_PROPERTIES\_V2**](event-trace-properties-v2.md) structure to include filtering information. See [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md) for more details.

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
<li><em>Properties</em> does not have sufficient space allocated to hold a copy of <em>SessionName</em>.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true:<br/>
<ul>
<li><em>Properties</em> is <strong>NULL</strong>.</li>
<li><em>SessionHandle</em> is <strong>NULL</strong>.</li>
<li>The <strong>LogFileNameOffset</strong> member of <em>Properties</em> is not valid.</li>
<li>The <strong>LoggerNameOffset</strong> member of <em>Properties</em> is not valid.</li>
<li>The <strong>LogFileMode</strong> member of <em>Properties</em> specifies a combination of flags that is not valid.</li>
<li>The <strong>Wnode.Guid</strong> member is <strong>SystemTraceControlGuid</strong>, but the <em>SessionName</em> parameter is not <strong>KERNEL_LOGGER_NAME</strong>.<strong>Windows 2000:</strong> This case does not return an error.<br/></li>
</ul></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ALREADY_EXISTS</strong></dt> </dl></td>
<td>A session with the same name or GUID is already running.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_BAD_PATHNAME</strong></dt> </dl></td>
<td>You can receive this error for one of the following reasons:<br/>
<ul>
<li>Another session is already using the file name specified by the <strong>LogFileNameOffset</strong> member of the <em>Properties</em> structure.</li>
<li>Both <strong>LogFileMode</strong> and <strong>LogFileNameOffset</strong> are zero.</li>
</ul></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_DISK_FULL</strong></dt> </dl></td>
<td>There is not enough free space on the drive for the log file. This occurs if:<br/>
<ul>
<li><strong>MaximumFileSize</strong> is nonzero and there is not <strong>MaximumFileSize</strong> bytes available for the log file</li>
<li>the drive is a system drive and there is not an additional 200 MB available</li>
<li><strong>MaximumFileSize</strong> is zero and there is not an additional 200 MB available</li>
</ul>
Choose a drive with more space, or decrease the size specified in <strong>MaximumFileSize</strong> (if used).<br/> <strong>Windows 2000:</strong> Does not require an additional 200 MB available disk space. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users with administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can control event tracing sessions. To grant a restricted user the ability to control trace sessions, add them to the Performance Log Users group. Only users with administrative privileges and services running as LocalSystem can control an NT Kernel Logger session.<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can control a trace session.<br/> If the user is a member of the Performance Log Users group, they may not have permission to create the log file in the specified folder.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_NO_SYSTEM_RESOURCES</strong></dt> </dl></td>
<td>The maximum number of logging sessions on the system has been reached. No new loggers can be created until a logging session has been stopped. This value defaults to 64 on most systems.<br/> You can change this value by editing the <strong>REG_DWORD</strong> key at <strong>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\EtwMaxLoggers</strong>. Permissible values are 32 through 256, inclusive. A reboot is required for any change to take effect. <br/> Note that Loggers use system resources. Increasing the number of loggers on the system will come at a performance cost if those slots are filled. <br/> Prior to Windows 10, version 1709, this is a fixed cap of 64 loggers for non-private loggers.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

The session remains active until you stop the session, the computer is restarted or the maximum file size is reached for non-circular logs. To stop an event tracing session, call the [**ControlTrace**](controltrace.md) function and set the *ControlCode* parameter to **EVENT\_TRACE\_CONTROL\_STOP**.

You cannot start more than one session with the same session GUID.

**Windows Server 2003:** You can start more than one session with the same session GUID.

For the logger to be a system logger and receive events from [SystemTraceProvider](configuring-and-starting-a-systemtraceprovider-session.md), any of the following must be true:

-   The *Properties* member **Wnode.Guid** is set to **SystemTraceControlGuid** or **GlobalLoggerGuid**.
-   The *Properties* member **LogFileMode** includes the **EVENT\_TRACE\_SYSTEM\_LOGGER\_MODE** flag.
-   *SessionName* is set to **KERNEL\_LOGGER\_NAME**.

> [!Note]  
> A system logger must set the **EnableFlags** member of the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure to indicate which [SystemTraceProvider](configuring-and-starting-a-systemtraceprovider-session.md) events should be included in the trace.

 

Because system loggers receive special kernel events, they are subject to additional restrictions:

-   There can be no more than 8 system loggers active on the same system.
-   System loggers cannot be created within a Windows Server container.
-   System loggers cannot use the **EVENT\_TRACE\_USE\_PAGED\_MEMORY** flag.
-   Prior to Windows 10, version 1703, no more than 2 distinct clock types can be used simultaneously by any system loggers. For example, if one active system logger is using the "CPU cycle counter" clock type, and another active system logger is using the "Query performance counter" clock type, then any attempt to start a system logger using the "System time" clock type will fail because it would require the activation of a third clock type. Because of this limitation, Microsoft strongly recommends that system loggers do not use the "System time" clock type.
-   Starting with Windows 10, version 1703, the clock type restriction has been removed. All three clock types can now be used simultaneously by system loggers.

To specify an NT Kernel Logger session, set *SessionName* to **KERNEL\_LOGGER\_NAME** and the **Wnode.Guid** member of *Properties* to **SystemTraceControlGuid**. If you do not specify the GUID as **SystemTraceControlGuid**, ETW will override the GUID value and set it to **SystemTraceControlGuid**.

**Windows 2000:** To start the kernel session, the session name must be **KERNEL\_LOGGER\_NAME** and the GUID must be **SystemTraceControlGuid**.

To specify a private logger session, set **Wnode.Guid** member of *Properties* to the provider's control GUID, not the private logger session's control GUID. The provider must have registered the GUID before you call **StartTrace**.

You do not use this function to start a global logger session. For details on starting a global logger session, see [Configuring and Starting the Global Logger Session](configuring-and-starting-the-global-logger-session.md).

## Examples

For an example that uses **StartTrace**, see [Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md).

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                                  |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                                                                                                                                                                                                                                 |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Server 2008, Windows Vista and Windows XP</dt> </dl> |
| Unicode and ANSI names<br/>   | **StartTraceW** (Unicode) and **StartTraceA** (ANSI)<br/>                                                                                                                                                                                                                                                              |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> <dt>

[**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md)
</dt> </dl>

 

 




