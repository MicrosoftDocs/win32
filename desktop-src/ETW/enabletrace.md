---
Description: Enables or disables the specified classic event trace provider. On Windows Vista and later, call the EnableTraceEx function to enable or disable a provider.
ms.assetid: d75f18e1-e5fa-4039-bb74-76dea334b0fd
title: EnableTrace function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableTrace function

Enables or disables the specified classic event trace provider.

On Windows Vista and later, call the [**EnableTraceEx**](enabletraceex-func.md) function to enable or disable a provider.

## Syntax


```C++
ULONG EnableTrace(
  _In_ ULONG       Enable,
  _In_ ULONG       EnableFlag,
  _In_ ULONG       EnableLevel,
  _In_ LPCGUID     ControlGuid,
  _In_ TRACEHANDLE SessionHandle
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

If **TRUE**, the provider is enabled; otherwise, the provider is disabled.

</dd> <dt>

*EnableFlag* \[in\]
</dt> <dd>

Provider-defined value that specifies the class of events for which the provider generates events. A provider that generates only one class of events will typically ignore this flag. If the provider is more complex, the provider could use the *TraceGuidReg* parameter of [**RegisterTraceGuids**](registertraceguids.md) to register more than one class of events. For example, if the provider has a database component, a UI component, and a general processing component, the provider could register separate event classes for these components. This would then allow the controller the ability to turn on tracing in only the database component.

The provider calls [**GetTraceEnableFlags**](gettraceenableflags.md) from its [*ControlCallback*](controlcallback.md) function to obtain the enable flags.

</dd> <dt>

*EnableLevel* \[in\]
</dt> <dd>

Provider-defined value that specifies the level of information the event generates. For example, you can use this value to indicate the severity level of the events (informational, warning, error) you want the provider to generate.

Specify a value from zero to 255. ETW defines the following severity levels that you can use. Higher numbers imply that you get lower levels as well. For example, if you specify TRACE\_LEVEL\_WARNING, you also receive all warning, error, and fatal events.



| Value                                                                                                                                                                                                                                               | Meaning                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <span id="TRACE_LEVEL_CRITICAL"></span><span id="trace_level_critical"></span><dl> <dt>**TRACE\_LEVEL\_CRITICAL**</dt> <dt>1</dt> </dl>          | Abnormal exit or termination events<br/>           |
| <span id="TRACE_LEVEL_ERROR"></span><span id="trace_level_error"></span><dl> <dt>**TRACE\_LEVEL\_ERROR**</dt> <dt>2</dt> </dl>                   | Severe error events<br/>                           |
| <span id="TRACE_LEVEL_WARNING"></span><span id="trace_level_warning"></span><dl> <dt>**TRACE\_LEVEL\_WARNING**</dt> <dt>3</dt> </dl>             | Warning events such as allocation failures<br/>    |
| <span id="TRACE_LEVEL_INFORMATION"></span><span id="trace_level_information"></span><dl> <dt>**TRACE\_LEVEL\_INFORMATION**</dt> <dt>4</dt> </dl> | Non-error events such as entry or exit events<br/> |
| <span id="TRACE_LEVEL_VERBOSE"></span><span id="trace_level_verbose"></span><dl> <dt>**TRACE\_LEVEL\_VERBOSE**</dt> <dt>5</dt> </dl>             | Detailed trace events<br/>                         |



 

</dd> <dt>

*ControlGuid* \[in\]
</dt> <dd>

GUID of the event trace provider that you want to enable or disable.

</dd> <dt>

*SessionHandle* \[in\]
</dt> <dd>

Handle of the event tracing session to which you want to enable, disable, or change the logging level of the provider. The [**StartTrace**](starttrace.md) function returns this handle.

</dd> </dl>

## Return value

If the function is successful, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/4a3a8feb-a05f-4614-8f04-1f507da7e5b7). The following table includes some common errors and their causes.



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
<li><em>ControlGuid</em> is <strong>NULL</strong>.</li>
<li><em>SessionHandle</em> is <strong>NULL</strong>.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_FUNCTION</strong></dt> </dl></td>
<td>You cannot change the enable flags and level when the provider is not registered.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_WMI_GUID_NOT_FOUND</strong></dt> </dl></td>
<td>The provider is not registered. Occurs when [KB307331](Http://go.microsoft.com/fwlink/p/?linkid=83987) or Windows 2000 Service Pack 4 is installed and the provider is not registered. To avoid this error, the provider must first be registered. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_NO_SYSTEM_RESOURCES</strong> </dt> </dl></td>
<td>Exceeded the number of trace sessions that can enable the provider.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users with administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can enable trace providers. To grant a restricted user the ability to enable a trace provider, add them to the Performance Log Users group or see [<strong>EventAccessControl</strong>](/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol).<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can enable a trace provider.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

Up to eight trace sessions can enable and receive events from the same [manifest-based](about-event-tracing.md#providers) provider; however, only one trace session can enable a [classic](about-event-tracing.md#providers) provider. If more than one session tried to enable a classic provider, the first session would stop receiving events when the second session enabled the same provider. For example, if Session A enabled Provider 1 and then Session B enabled Provider 1, only Session B would receive events from Provider 1.

The provider remains enabled for the session until the session disables the provider. If the application that started the session ends without disabling the provider, the provider remains enabled.

The **EnableTrace** function calls the [**ControlCallback**](controlcallback.md) function implemented by the event trace provider, if defined. The provider defines its interpretation of being enabled or disabled. Typically, if a provider has been enabled, it generates events, but while it is disabled, it does not. The **ControlCallback** function can call the [**GetTraceEnableFlags**](gettraceenableflags.md), [**GetTraceEnableLevel**](gettraceenablelevel.md), and [**GetTraceLoggerHandle**](gettraceloggerhandle.md) functions to obtain the values specified for the *EnableFlag*, *EnableLevel*, and *SessionHandle* parameters, respectively.

You can call this function one time to enable a provider before the provider registers itself. After the provider registers itself, ETW calls the provider's [**ControlCallback**](controlcallback.md) function. If you try to enable the provider for multiple sessions before the provider registers itself, ETW will only enable the provider for the last session. For example, if you enable the provider to Session A and then enable the provider to Session B, when the provider registers itself, the provider is only enabled for Session B.

You do not call **EnableTrace** to enable kernel providers. To enable kernel providers, set the **EnableFlags** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) which you then pass to [**StartTrace**](starttrace.md). The **StartTrace** function enables the selected kernel providers.

To determine the level and keywords used to enable a manifest-based provider, use one of the following commands:

-   Logman query providers &lt;provider-name&gt;
-   Wevtutil gp &lt;provider-name&gt;

For classic providers, it is up to the provider to document and make available to potential controllers the severity levels or enable flags that it supports. If the provider wants to be enabled by any controller, the provider should accept 0 for the severity level and enable flags and interpret 0 as a request to perform default logging (whatever that may be).

If you use **EnableTrace** to enable a manifest-based provider, the following translation occurs:

-   The *EnableLevel* parameter is the same as setting the *Level* parameter in [**EnableTraceEx**](enabletraceex-func.md).
-   The *EnableFlag* is the same as setting the *MatchAnyKeyword* parameter in [**EnableTraceEx**](enabletraceex-func.md).
-   In the [**EnableCallback**](/windows/desktop/api/Evntprov/nc-evntprov-penablecallback) callback, the *SourceId* parameter will be **NULL**, *Level* will be set to the value in **EnableTrace**, *MatchAnyKeyword* will be set to the value of *EnableFlag* in [**EventTrace**](eventtrace.md), *MatchAllKeyword* will be 0, and *FilterData* will be **NULL**.

On Windows 8.1,Windows Server 2012 R2, and later, payload filters can be used by the [**EnableTraceEx2**](enabletraceex2.md) function to filter on specific conditions in a logger session.

## Examples

For an example that uses **EnableTrace**, see [Example that Creates a Session and Enables a manifest-based provider](example-that-creates-a-session-and-enables-a-manifest-based-provider.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**ControlCallback**](controlcallback.md)
</dt> <dt>

[**EnableTraceEx**](enabletraceex-func.md)
</dt> <dt>

[**EnableTraceEx2**](enabletraceex2.md)
</dt> <dt>

[**GetTraceEnableFlags**](gettraceenableflags.md)
</dt> <dt>

[**GetTraceEnableLevel**](gettraceenablelevel.md)
</dt> <dt>

[**GetTraceLoggerHandle**](gettraceloggerhandle.md)
</dt> <dt>

[**StartTrace**](starttrace.md)
</dt> </dl>

 

 




