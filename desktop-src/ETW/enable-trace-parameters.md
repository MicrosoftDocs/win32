---
Description: Defines the information used to enable a provider.
ms.assetid: bc7cf886-f763-428a-9e75-031e8df26554
title: ENABLE\_TRACE\_PARAMETERS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ENABLE_TRACE_PARAMETERS
api_type:
- HeaderDef
api_location:
- Evntrace.h
---

# ENABLE\_TRACE\_PARAMETERS structure

The **ENABLE\_TRACE\_PARAMETERS** structure defines the information used to enable a provider.

## Syntax


```C++
typedef struct _ENABLE_TRACE_PARAMETERS {
  ULONG                    Version;
  ULONG                    EnableProperty;
  ULONG                    ControlFlags;
  GUID                     SourceId;
  PEVENT_FILTER_DESCRIPTOR EnableFilterDesc;
  ULONG                    FilterDescCount;
} ENABLE_TRACE_PARAMETERS, *PENABLE_TRACE_PARAMETERS;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Set to **ENABLE\_TRACE\_PARAMETERS\_VERSION\_2**.

</dd> <dt>

**EnableProperty**
</dt> <dd>

Optional settings that ETW can include when writing the event. Some settings write extra data to the [**extended data item**](https://msdn.microsoft.com/en-us/library/Aa363760(v=VS.85).aspx) section of each event. Other settings refine which events will be included. To use these optional settings, specify one or more of the following flags; otherwise, set to zero.



| Value                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0"></span><span id="event_enable_property_ignore_keyword_0"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_IGNORE\_KEYWORD\_0**</dt> </dl>    | Filters out all events that do not have a non-zero keyword specified.<br/> Supported on Windows 10, version 1507 and later. This is also supported on Windows 8.1 and Windows 7 with SP1 via a patch.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="EVENT_ENABLE_PROPERTY_PROVIDER_GROUP"></span><span id="event_enable_property_provider_group"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_PROVIDER\_GROUP**</dt> </dl>           | Indicates that this call to [**EnableTraceEx2**](enabletraceex2.md) should enable a [Provider Group](provider-traits.md) rather than an individual Event Provider.<br/> Supported on Windows 10, version 1507 and later. This is also supported on Windows 8.1 and Windows 7 with SP1 via a patch.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="EVENT_ENABLE_PROPERTY_PROCESS_START_KEY"></span><span id="event_enable_property_process_start_key"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_PROCESS\_START\_KEY**</dt> </dl> | Include the Process Start Key in the extended data.<br/> The Process Start Key is a sequence number that identifies the process. While the Process ID may be reused within a session, the Process Start Key is guaranteed uniqueness in the current boot session.<br/> Supported on Windows 10, version 1507 and later. This is also supported on Windows 8.1 and Windows 7 with SP1 via a patch.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="EVENT_ENABLE_PROPERTY_EVENT_KEY"></span><span id="event_enable_property_event_key"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_EVENT\_KEY**</dt> </dl>                          | Include the Event Key in the extended data.<br/> The Event Key is a unique identifier for the event instance that will be constant across multiple trace sessions listening to this event. It can be used to correlate simultaneous trace sessions.<br/> Supported on Windows 10, version 1507 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE"></span><span id="event_enable_property_exclude_inprivate"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_EXCLUDE\_INPRIVATE**</dt> </dl>  | Filters out all events that are either marked as an InPrivate event or come from a process that is marked as InPrivate.<br/> InPrivate implies that the event or process contains some data that would be considered private or personal. It is up to the process or event to designate itself as InPrivate for this to work.<br/> Supported on Windows 10, version 1507 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="EVENT_ENABLE_PROPERTY_SID"></span><span id="event_enable_property_sid"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_SID**</dt> </dl>                                             | Include in the extended data the security identifier (SID) of the user.<br/> Supported on Windows Vista and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="EVENT_ENABLE_PROPERTY_TS_ID"></span><span id="event_enable_property_ts_id"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_TS\_ID**</dt> </dl>                                      | Include in the extended data the terminal session identifier.<br/> Supported on Windows Vista and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="EVENT_ENABLE_PROPERTY_STACK_TRACE"></span><span id="event_enable_property_stack_trace"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE**</dt> </dl>                    | Include in the extended data a call stack trace for events written using [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite).<br/> If you set **EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE**, ETW will drop the event if the total event size exceeds 64K. If the provider is logging events close in size to 64K maximum, it is possible that enabling stack capture will cause the event to be lost.<br/> If the stack is longer than the maximum number of frames (192), the frames will be cut from the bottom of the stack.<br/> For consumers, the events will include the [**EVENT\_EXTENDED\_ITEM\_STACK\_TRACE32**](/windows/desktop/api/Evntcons/ns-evntcons-_event_extended_item_stack_trace32) or [**EVENT\_EXTENDED\_ITEM\_STACK\_TRACE64**](/windows/desktop/api/Evntcons/ns-evntcons-_event_extended_item_stack_trace64) extended item. Note that on 64-bit computers, 32-bit processes will receive 64-bit stack traces.<br/> Supported on Windows 7 and later.<br/> |



 

</dd> <dt>

**ControlFlags**
</dt> <dd>

Reserved. Set to 0.

</dd> <dt>

**SourceId**
</dt> <dd>

A GUID that uniquely identifies the session that is enabling or disabling the provider. If the provider does not implement [**EnableCallback**](/windows/desktop/api/Evntprov/nc-evntprov-penablecallback), the GUID is not used.

</dd> <dt>

**EnableFilterDesc**
</dt> <dd>

A pointer to an array of [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) structures that points to the filter data. The number of elements in the array is specified in the **FilterDescCount** member. There can only be one filter for a specific filter type as specified by the **Type** member of the **EVENT\_FILTER\_DESCRIPTOR** structure.

For a schematized filter (a **Type** member equal to **EVENT\_FILTER\_TYPE\_SCHEMATIZED**), the provider uses filter data to prevent events that match the filter criteria from being written to the session. The provider determines the layout of the data and how it applies the filter to the event's data. A session can pass only one schematized filter to the provider.

A session can call the [**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters) function to determine the schematized filters that it can pass to the provider.

</dd> <dt>

**FilterDescCount**
</dt> <dd>

The number of elements (filters) in the [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) array pointed to by **EnableFilterDesc** member.

The **FilterDescCount** member should match the number of [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) structures in the array pointed to by the **EnableFilterDesc** member.

.

</dd> </dl>

## Remarks

The **ENABLE\_TRACE\_PARAMETERS** structure is a version 2 structure and replaces the [**ENABLE\_TRACE\_PARAMETERS\_V1**](enable-trace-parameters-v1.md) structure for use with the [**EnableTraceEx2**](enabletraceex2.md) function.

On Windows 8.1,Windows Server 2012 R2, and later, event payload , scope, and stack walk filters can be used by the [**EnableTraceEx2**](enabletraceex2.md) function and the **ENABLE\_TRACE\_PARAMETERS** and [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) structures to filter on specific conditions in a logger session. For more information on event payload filters, see the **EnableTraceEx2**, [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter), and [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) functions and the **EVENT\_FILTER\_DESCRIPTOR** and [**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-_payload_filter_predicate) structures.

Typically, on 64-bit computers, you cannot capture the kernel stack in certain contexts when page faults are not allowed. To enable walking the kernel stack on x64, set the **DisablePagingExecutive** Memory Management registry value to 1. The **DisablePagingExecutive** registry value is located under the following registry key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Memory Management**

You should consider the cost of setting this registry value before doing so.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EnableTraceEx2**](enabletraceex2.md)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS\_V1**](enable-trace-parameters-v1.md)
</dt> <dt>

[**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor)
</dt> <dt>

[**EVENT\_FILTER\_EVENT\_ID**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_event_id)
</dt> <dt>

[**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-_payload_filter_predicate)
</dt> <dt>

[**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters)
</dt> <dt>

[**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter)
</dt> <dt>

[**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters)
</dt> </dl>

 

 




