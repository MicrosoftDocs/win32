---
description: Logs an event.
title: EtwLogTraceEvent
ms.topic: reference
ms.date: 03/01/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EtwLogTraceEvent
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# EtwLogTraceEvent function

Logs an event.

## Syntax

```C++
ULONG EtwLogTraceEvent (
    _In_ TRACEHANDLE LoggerHandle,
    _In_ PEVENT_TRACE_HEADER EventTrace
)
```

## Parameters

### LoggerHandle [in]

Handle to an event tracing session, or 0. You must specify a non-zero
_SessionHandle_ if _SessionName_ is **NULL**. ETW ignores the handle if
_SessionName_ is not **NULL**.


### EventDescriptor [in]

An [EVENT_TRACE_HEADER](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure containing standard event tracing information common to all events written by [TraceEvent](/windows/win32/api/evntrace/nf-evntrace-traceevent).


## Return value

A Win32 error code.


## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from ntdll.dll.
