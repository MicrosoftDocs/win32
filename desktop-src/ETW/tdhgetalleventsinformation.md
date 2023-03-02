---
description: Retrieves metadata about all events in the specified namespace.
title: TdhGetAllEventsInformation function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetVersion
api_type: 
- DllExport
api_location: 
- tdh.dll
---

# TdhGetAllEventsInformation function

Retrieves metadata about all events in the specified namespace.

## Syntax


```C++
TdhGetAllEventsInformation(
    __in PEVENT_RECORD pEvent,
    __in_opt PVOID pWbemService,
    __out ULONG *pIndex,
    __out ULONG *pCount,
    __out_bcount_opt(*pBufferSize) PTRACE_EVENT_INFO *ppBuffer,
    __inout ULONG *pBufferSize
    );
```



## Parameters

### pEvent [in]

The event record passed to your [EventRecordCallback](/windows/desktop/ETW/eventrecordcallback) callback. For details, see the [EVENT_RECORD](/windows/desktop/api/evntcons/ns-evntcons-event_record) structure.

### pWbemService [in]

Pointer to namespace for which the diagnostic mode data is retrieved.

### pIndex [out]

The index in the *ppBuffer* buffer of the first **PTRACE_EVENT_INFO**.

### pCount

The number of **PTRACE_EVENT_INFO** entries returned in *ppBuffer*.

### ppBuffer

User-allocated buffer to receive the event information. For details, see the [TRACE_EVENT_INFO](/windows/desktop/api/tdh/ns-tdh-trace_event_info) structure.


### pBufferSize

Size, in bytes, of the *pBuffer* buffer. If the function succeeds, this parameter receives the size of the buffer used. If the buffer is too small, the function returns ERROR_INSUFFICIENT_BUFFER and sets this parameter to the required buffer size. If the buffer size is zero on input, no data is returned in the buffer and this parameter receives the required buffer size.

## Return value

TRUE if a shutdown of the current dll process is in progress; otherwise, FALSE.

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from tdh.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11 |
| Minimum supported server | Windows 11 |
| DLL | tdh.dll |



## See also



 

 
