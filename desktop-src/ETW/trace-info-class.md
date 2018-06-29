---
Description: Determines the type of information to include with the trace.
ms.assetid: b163e120-454a-48ba-93a9-71351fc3f2c2
title: TRACE\_INFO\_CLASS enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRACE_INFO_CLASS,
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# TRACE\_INFO\_CLASS enumeration

Determines the type of information to include with the trace.

## Syntax


```C++
typedef enum  { 
  TraceGuidQueryList,
  TraceGuidQueryInfo,
  TraceGuidQueryProcess,
  TraceStackTracingInfo,
  TraceSystemTraceEnableFlagsInfo,
  TraceSampledProfileIntervalInfo,
  TraceProfileSourceConfigInfo,
  TraceProfileSourceListInfo,
  TracePmcEventListInfo,
  TracePmcCounterListInfo,
  TraceSetDisallowList,
  TraceVersionInfo,
  TraceGroupQueryList,
  TraceGroupQueryInfo,
  TraceDisallowListQuery,
  TracePeriodicCaptureStateListInfo,
  TracePeriodicCaptureStateInfo,
  TraceProviderBinaryTracking,
  TraceMaxLoggersQuery,
  MaxTraceSetInfoClass
} TRACE_INFO_CLASS, TRACE_QUERY_INFO_CLASS;
```



## Constants

<dl> <dt>

<span id="TraceGuidQueryList"></span><span id="traceguidquerylist"></span><span id="TRACEGUIDQUERYLIST"></span>**TraceGuidQueryList**
</dt> <dd>

Query an array of GUIDs of the providers that are registered on the computer.

</dd> <dt>

<span id="TraceGuidQueryInfo"></span><span id="traceguidqueryinfo"></span><span id="TRACEGUIDQUERYINFO"></span>**TraceGuidQueryInfo**
</dt> <dd>

Query information that each session used to enable the provider.

</dd> <dt>

<span id="TraceGuidQueryProcess"></span><span id="traceguidqueryprocess"></span><span id="TRACEGUIDQUERYPROCESS"></span>**TraceGuidQueryProcess**
</dt> <dd>

Query an array of GUIDs of the providers that registered themselves in the same process as the calling process.

</dd> <dt>

<span id="TraceStackTracingInfo"></span><span id="tracestacktracinginfo"></span><span id="TRACESTACKTRACINGINFO"></span>**TraceStackTracingInfo**
</dt> <dd>

Query the setting for call stack tracing for kernel events.

The value is supported on Windows 7, Windows Server 2008 R2, and later.

</dd> <dt>

<span id="TraceSystemTraceEnableFlagsInfo"></span><span id="tracesystemtraceenableflagsinfo"></span><span id="TRACESYSTEMTRACEENABLEFLAGSINFO"></span>**TraceSystemTraceEnableFlagsInfo**
</dt> <dd>

Query the setting for the **EnableFlags** for the system trace provider. For more information, see the [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) structure.

The value is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="TraceSampledProfileIntervalInfo"></span><span id="tracesampledprofileintervalinfo"></span><span id="TRACESAMPLEDPROFILEINTERVALINFO"></span>**TraceSampledProfileIntervalInfo**
</dt> <dd>

Queries the setting for the sampling profile interval for the supplied source.

The value is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="TraceProfileSourceConfigInfo"></span><span id="traceprofilesourceconfiginfo"></span><span id="TRACEPROFILESOURCECONFIGINFO"></span>**TraceProfileSourceConfigInfo**
</dt> <dd>

Query which sources will be traced.

The value is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="TraceProfileSourceListInfo"></span><span id="traceprofilesourcelistinfo"></span><span id="TRACEPROFILESOURCELISTINFO"></span>**TraceProfileSourceListInfo**
</dt> <dd>

Query the setting for sampled profile list information.

The value is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="TracePmcEventListInfo"></span><span id="tracepmceventlistinfo"></span><span id="TRACEPMCEVENTLISTINFO"></span>**TracePmcEventListInfo**
</dt> <dd>

Query the list of system events on which performance monitoring counters will be collected.

The value is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="TracePmcCounterListInfo"></span><span id="tracepmccounterlistinfo"></span><span id="TRACEPMCCOUNTERLISTINFO"></span>**TracePmcCounterListInfo**
</dt> <dd>

Query the list of performance monitoring counters to collect

The value is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="TraceSetDisallowList"></span><span id="tracesetdisallowlist"></span><span id="TRACESETDISALLOWLIST"></span>**TraceSetDisallowList**
</dt> <dd>

Set the list of providers that are disabled for a provider group enable on this session. For more information, see [Provider Traits](provider-traits.md)

The value is supported on Windows 10.

</dd> <dt>

<span id="TraceVersionInfo"></span><span id="traceversioninfo"></span><span id="TRACEVERSIONINFO"></span>**TraceVersionInfo**
</dt> <dd>

Query the trace file version information.

The value is supported on Windows 10.

</dd> <dt>

<span id="TraceGroupQueryList"></span><span id="tracegroupquerylist"></span><span id="TRACEGROUPQUERYLIST"></span>**TraceGroupQueryList**
</dt> <dd>

Query an array of GUIDs of the provider groups that are active on the computer.

</dd> <dt>

<span id="TraceGroupQueryInfo"></span><span id="tracegroupqueryinfo"></span><span id="TRACEGROUPQUERYINFO"></span>**TraceGroupQueryInfo**
</dt> <dd>

Query information that each session used to enable the provider group.

</dd> <dt>

<span id="TraceDisallowListQuery"></span><span id="tracedisallowlistquery"></span><span id="TRACEDISALLOWLISTQUERY"></span>**TraceDisallowListQuery**
</dt> <dd>

Query an array of GUIDs that are disallowed for group enables on this session.

</dd> <dt>

<span id="TracePeriodicCaptureStateListInfo"></span><span id="traceperiodiccapturestatelistinfo"></span><span id="TRACEPERIODICCAPTURESTATELISTINFO"></span>**TracePeriodicCaptureStateListInfo**
</dt> <dd>

Query the list of periodic capture states to collect.

</dd> <dt>

<span id="TracePeriodicCaptureStateInfo"></span><span id="traceperiodiccapturestateinfo"></span><span id="TRACEPERIODICCAPTURESTATEINFO"></span>**TracePeriodicCaptureStateInfo**
</dt> <dd>

Queries the settings used for periodic capture state.

</dd> <dt>

<span id="TraceProviderBinaryTracking"></span><span id="traceproviderbinarytracking"></span><span id="TRACEPROVIDERBINARYTRACKING"></span>**TraceProviderBinaryTracking**
</dt> <dd>

Instructs ETW to begin tracking binaries for all providers that are enabled to the session. The tracking applies retroactively for providers that were enabled to the session prior to the call, as well as for all future providers that are enabled to the session.

ETW fabricates tracking events for these tracked providers that contain a mapping between provider GUID(s). ETW also fabricates the file path that describes where the registered provider is located on disk. If the session is in realtime, the events are provided live in the realtime buffers. If the session is file-based (i.e. trace is saved to an .etl file), the events are aggregated and written to the file header; they will be among some of the first events the ETW runtime provides when the .etl file is played back.

The binary tracking events will come from the EventTraceGuid provider, with an opcode of **WMI\_LOG\_TYPE\_BINARY\_PATH**.

The value is supported on Windows 10, version 1709 and later.

</dd> <dt>

<span id="TraceMaxLoggersQuery"></span><span id="tracemaxloggersquery"></span><span id="TRACEMAXLOGGERSQUERY"></span>**TraceMaxLoggersQuery**
</dt> <dd>

Queries the currently-configured maximum number of system loggers allowed by the operating system. Returns a ULONG. Used with [**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md).

The value is supported on Windows 10, version 1709 and later.

</dd> <dt>

<span id="MaxTraceSetInfoClass"></span><span id="maxtracesetinfoclass"></span><span id="MAXTRACESETINFOCLASS"></span>**MaxTraceSetInfoClass**
</dt> <dd>

Marks the last value in the enumeration. Do not use.

</dd> </dl>

## Remarks

The **TRACE\_INFO\_CLASS** and **TRACE\_QUERY\_INFO\_CLASS** enumerations both define the same values. Use both enumerations with the [**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md) function or the [**TraceSetInformation**](tracesetinformation.md) function.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TraceSetInformation**](tracesetinformation.md)
</dt> <dt>

[**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md)
</dt> </dl>

 

 




