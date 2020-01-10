---
Description: Enables or disables the specified event trace provider. The EnableTraceEx2 function supersedes this function.
ms.assetid: 1c675bf7-f292-49b1-8b60-720499a497fd
title: EnableTraceEx function (Evntrace.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EnableTraceEx
api_type:
- DllExport
api_location:
- Advapi32.dll
- API-MS-Win-eventing-Legacy-l1-1-0.dll
- advapi32legacy.dll
---

# EnableTraceEx function

Enables or disables the specified event trace provider.

The [**EnableTraceEx2**](enabletraceex2.md) function supersedes this function.

## Syntax


```C++
ULONG EnableTraceEx(
  _In_     LPCGUID                  ProviderId,
  _In_opt_ LPCGUID                  SourceId,
  _In_     TRACEHANDLE              TraceHandle,
  _In_     ULONG                    IsEnabled,
  _In_     UCHAR                    Level,
  _In_     ULONGLONG                MatchAnyKeyword,
  _In_     ULONGLONG                MatchAllKeyword,
  _In_     ULONG                    EnableProperty,
  _In_opt_ PEVENT_FILTER_DESCRIPTOR EnableFilterDesc
);
```



## Parameters

<dl> <dt>

*ProviderId* \[in\]
</dt> <dd>

GUID of the event trace provider that you want to enable or disable.

</dd> <dt>

*SourceId* \[in, optional\]
</dt> <dd>

GUID that uniquely identifies the session that is enabling or disabling the provider. Can be **NULL**. If the provider does not implement [**EnableCallback**](/windows/desktop/api/Evntprov/nc-evntprov-penablecallback), the GUID is not used.

</dd> <dt>

*TraceHandle* \[in\]
</dt> <dd>

Handle of the event tracing session to which you want to enable or disable the provider. The [**StartTrace**](starttrace.md) function returns this handle.

</dd> <dt>

*IsEnabled* \[in\]
</dt> <dd>

Set to 1 to receive events when the provider is registered; otherwise, set to 0 to no longer receive events from the provider.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

Provider-defined value that specifies the level of detail included in the event. Specify one of the following levels that are defined in Winmeta.h. Higher numbers imply that you get lower levels as well. For example, if you specify TRACE\_LEVEL\_WARNING, you also receive all warning, error, and critical events.



| Value                                                                                                                                                                                                                                               | Meaning                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <span id="TRACE_LEVEL_CRITICAL"></span><span id="trace_level_critical"></span><dl> <dt>**TRACE\_LEVEL\_CRITICAL**</dt> <dt>1</dt> </dl>          | Abnormal exit or termination events<br/>           |
| <span id="TRACE_LEVEL_ERROR"></span><span id="trace_level_error"></span><dl> <dt>**TRACE\_LEVEL\_ERROR**</dt> <dt>2</dt> </dl>                   | Severe error events<br/>                           |
| <span id="TRACE_LEVEL_WARNING"></span><span id="trace_level_warning"></span><dl> <dt>**TRACE\_LEVEL\_WARNING**</dt> <dt>3</dt> </dl>             | Warning events such as allocation failures<br/>    |
| <span id="TRACE_LEVEL_INFORMATION"></span><span id="trace_level_information"></span><dl> <dt>**TRACE\_LEVEL\_INFORMATION**</dt> <dt>4</dt> </dl> | Non-error events such as entry or exit events<br/> |
| <span id="TRACE_LEVEL_VERBOSE"></span><span id="trace_level_verbose"></span><dl> <dt>**TRACE\_LEVEL\_VERBOSE**</dt> <dt>5</dt> </dl>             | Detailed trace events<br/>                         |



 

</dd> <dt>

*MatchAnyKeyword* \[in\]
</dt> <dd>

Bitmask of keywords that determine the category of events that you want the provider to write. The provider writes the event if any of the event's keyword bits match any of the bits set in this mask. See Remarks.

</dd> <dt>

*MatchAllKeyword* \[in\]
</dt> <dd>

This bitmask is optional. This mask further restricts the category of events that you want the provider to write. If the event's keyword meets the *MatchAnyKeyword* condition, the provider will write the event only if all of the bits in this mask exist in the event's keyword. This mask is not used if *MatchAnyKeyword* is zero. See Remarks.

</dd> <dt>

*EnableProperty* \[in\]
</dt> <dd>

Optional information that ETW can include when writing the event. The data is written to the [**extended data item**](https://msdn.microsoft.com/library/Aa363760(v=VS.85).aspx) section of the event. To include the optional information, specify one or more of the following flags; otherwise, set to zero.



| Value                                                                                                                                                                                                      | Meaning                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="EVENT_ENABLE_PROPERTY_SID"></span><span id="event_enable_property_sid"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_SID**</dt> </dl>        | Include the security identifier (SID) of the user in the extended data.<br/> |
| <span id="EVENT_ENABLE_PROPERTY_TS_ID"></span><span id="event_enable_property_ts_id"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_TS\_ID**</dt> </dl> | Include the terminal session identifier in the extended data.<br/>           |



 

</dd> <dt>

*EnableFilterDesc* \[in, optional\]
</dt> <dd>

An [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor) structure that points to the filter data. The provider uses to filter data to prevent events that match the filter criteria from being written to the session; the provider determines the layout of the data and how it applies the filter to the event's data. A session can pass only one filter to the provider.

A session can call the [**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters) function to determine the filters that it can pass to the provider.

</dd> </dl>

## Return value

If the function is successful, the return value is ERROR\_SUCCESS.

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
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>One of the following is true: <br/>
<ul>
<li><em>ProviderId</em> is <strong>NULL</strong>.</li>
<li><em>TraceHandle</em> is <strong>NULL</strong>.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_INVALID_FUNCTION</strong></dt> </dl></td>
<td>You cannot update the level when the provider is not registered.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_NO_SYSTEM_RESOURCES</strong> </dt> </dl></td>
<td>Exceeded the number of trace sessions that can enable the provider.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users with administrative privileges, users in the Performance Log Users group, and services running as LocalSystem, LocalService, NetworkService can enable trace providers. To grant a restricted user the ability to enable a trace provider, add them to the Performance Log Users group or see <a href="/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol"><strong>EventAccessControl</strong></a>.<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can enable a trace provider.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

The provider defines its interpretation of being enabled or disabled. Typically, if a provider has been enabled, it generates events, but while it is disabled, it does not.

To include all events that a provider provides, set *MatchAnyKeyword* to zero (for a [manifest-based](about-event-tracing.md) provider and 0xFFFFFFFF for a [classic](about-event-tracing.md) provider). To include specific events, set the *MatchAnyKeyword* mask to those specific events. For example, if the provider defines an event for its initialization and cleanup routines (set keyword bit 0), an event for its file operations (set keyword bit 1), and an event for its calculation operations (set keyword bit 2), you can set *MatchAnyKeyword* to 5 to receive initialization and cleanup events and calculation events.

If the provider defines more complex event keywords, for example, the provider defines an event that sets bit 0 for read and bit 1 for local access and a second event that sets bit 0 for read and bit 2 for remote access, you could set MatchAnyKeyword to 1 to receive all read events, or you could set MatchAnykeyword to 1 and MatchAllKeywords to 3 to receive local reads only.

If an event's keyword is zero, the provider will write the event to the session, regardless of the *MatchAnyKeyword* and *MatchAllKeyword* masks.

When you call **EnableTraceEx** the provider may or may not be registered. If the provider is registered, ETW calls the provider's callback function, if it implements one, and the session begins receiving events. If the provider is not registered, ETW will call the provider's callback function when it registers itself, if it implements one, and the session will begin receiving events. If the provider is not registered, the provider's callback function will not receive the source ID or filter data. You can call **EnableTraceEx** one time to enable a provider before the provider registers itself.

If the provider is registered and already enabled to your session, you can also use this function to update the *Level*, *MatchAnyKeyword*, *MatchAllKeyword*, *EnableProperty* and *EnableFilterDesc* parameters that determine which events the provider writes.

You do not call **EnableTraceEx** to enable kernel providers. To enable kernel providers, set the **EnableFlags** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) which you then pass to [**StartTrace**](starttrace.md). The **StartTrace** function enables the selected kernel providers.

Up to eight trace sessions can enable and receive events from the same [manifest-based](about-event-tracing.md) provider; however, only one trace session can enable a [classic](about-event-tracing.md) provider. If more than one session tried to enable a classic provider, the first session would stop receiving events when the second session enabled the same provider. For example, if Session A enabled Provider 1 and then Session B enabled Provider 1, only Session B would receive events from Provider 1.

The provider remains enabled for the session until the session disables the provider. If the application that started the session ends without disabling the provider, the provider remains enabled.

To determine the level and keywords used to enable a manifest-based provider, use one of the following commands:

-   Logman query providers <provider-name>
-   Wevtutil gp <provider-name>

For classic providers, it is up to the provider to document and make available to potential controllers the severity levels or enable flags that it supports. If the provider wants to be enabled by any controller, the provider should accept 0 for the severity level and enable flags and interpret 0 as a request to perform default logging (whatever that may be).

If you use **EnableTraceEx** to enable a classic provider, the following translation occurs:

-   The *Level* parameter is the same as setting the *EnableLevel* parameter in [**EnableTrace**](enabletrace.md).
-   The *MatchAnyKeyword* is the same as setting the *EnableFlag* parameter in [**EnableTrace**](enabletrace.md) except that the keyword value is truncated from a ULONGLONG to a ULONG value.
-   In the [*ControlCallback*](controlcallback.md) callback, the provider can call [**GetTraceEnableLevel**](gettraceenablelevel.md) to get the level and [**GetTraceEnableFlags**](gettraceenableflags.md) to get the enable flag.
-   The other parameter are not used.

A provider can define filters that a session uses to filter events based on event data. With the level and keywords that you provide, ETW determines whether the event is written to the session but with filters, the provider uses the filter data to determine whether it writes the event to the session. For example, if the provider generates process events, it could define a data filter that filters process events based on the process identifier. If the identifier of the process did not match the identifier that you passed as filter data, the provider would prevent event from being written to your session.

On Windows 8.1,Windows Server 2012 R2, and later, payload filters can be used by the [**EnableTraceEx2**](enabletraceex2.md) function to filter on specific conditions in a logger session.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                             |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Advapi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Advapi32.dll</dt> </dl> |



## See also

<dl> <dt>

[**EnableTraceEx2**](enabletraceex2.md)
</dt> </dl>

 

 




