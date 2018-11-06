---
Description: Defines the information used to enable a provider.
ms.assetid: 6FC5EF54-2D05-4246-A8E8-7FDA0ABA0D4B
title: ENABLE_TRACE_PARAMETERS_V1 structure
ms.topic: structure
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ENABLE_TRACE_PARAMETERS_V1
api_type:
- HeaderDef
api_location:
- Evntrace.h
---

# ENABLE\_TRACE\_PARAMETERS\_V1 structure

The **ENABLE\_TRACE\_PARAMETERS\_V1** structure defines the information used to enable a provider.

## Syntax


```C++
typedef struct _ENABLE_TRACE_PARAMETERS_V1 {
  ULONG                    Version;
  ULONG                    EnableProperty;
  ULONG                    ControlFlags;
  GUID                     SourceId;
  PEVENT_FILTER_DESCRIPTOR EnableFilterDesc;
} ENABLE_TRACE_PARAMETERS_V1, *PENABLE_TRACE_PARAMETERS_V1;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Set to **ENABLE\_TRACE\_PARAMETERS\_VERSION**.

</dd> <dt>

**EnableProperty**
</dt> <dd>

Optional information that ETW can include when writing the event. The data is written to the [**extended data item**](https://msdn.microsoft.com/en-us/library/Aa363760(v=VS.85).aspx) section of the event. To include the optional information, specify one or more of the following flags; otherwise, set to zero.



| Value                                                                                                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_ENABLE_PROPERTY_SID"></span><span id="event_enable_property_sid"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_SID**</dt> </dl>                          | Include in the extended data the security identifier (SID) of the user.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="EVENT_ENABLE_PROPERTY_TS_ID"></span><span id="event_enable_property_ts_id"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_TS\_ID**</dt> </dl>                   | Include in the extended data the terminal session identifier.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="EVENT_ENABLE_PROPERTY_STACK_TRACE"></span><span id="event_enable_property_stack_trace"></span><dl> <dt>**EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE**</dt> </dl> | Include in the extended data a call stack trace for events written using [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite).<br/> If you set **EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE**, ETW will drop the event if the total event size exceeds 64K. If the provider is logging events close in size to 64K maximum, it is possible that enabling stack capture will cause the event to be lost.<br/> If the stack is longer than the maximum number of frames (192), the frames will be cut from the bottom of the stack.<br/> For consumers, the events will include the [**EVENT\_EXTENDED\_ITEM\_STACK\_TRACE32**](/windows/desktop/api/Evntcons/ns-evntcons-_event_extended_item_stack_trace32) or [**EVENT\_EXTENDED\_ITEM\_STACK\_TRACE64**](/windows/desktop/api/Evntcons/ns-evntcons-_event_extended_item_stack_trace64) extended item. Note that on 64-bit computers, 32-bit processes will receive 64-bit stack traces.<br/> |



 

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

An [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) structure that points to the filter data. The provider uses filter data to prevent events that match the filter criteria from being written to the session. The provider determines the layout of the data and how it applies the filter to the event's data. A session can pass only one filter to the provider.

A session can call the [**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters) function to determine the schematized filters that it can pass to the provider.

</dd> </dl>

## Remarks

The **ENABLE\_TRACE\_PARAMETERS\_V1** structure is used with the [**EnableTrace**](enabletrace.md) and [**EnableTraceEx**](enabletraceex-func.md) functions. The [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) structure is a version 2 structure and replaces the **ENABLE\_TRACE\_PARAMETERS\_V1** structure for use with the [**EnableTraceEx2**](enabletraceex2.md) function.

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

[**EnableTrace**](enabletrace.md)
</dt> <dt>

[**EnableTraceEx**](enabletraceex-func.md)
</dt> <dt>

[**EnableTraceEx2**](enabletraceex2.md)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md)
</dt> <dt>

[**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor)
</dt> </dl>

 

 




