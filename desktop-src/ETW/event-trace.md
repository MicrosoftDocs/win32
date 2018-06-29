---
Description: The EVENT\_TRACE structure is used to deliver event information to an event trace consumer.
ms.assetid: d8a6b63e-0cd4-4d19-b0b3-16bb0d33e4c0
title: EVENT\_TRACE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EVENT_TRACE
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# EVENT\_TRACE structure

The **EVENT\_TRACE** structure is used to deliver event information to an event trace consumer.

## Syntax


```C++
typedef struct _EVENT_TRACE {
  EVENT_TRACE_HEADER Header;
  ULONG              InstanceId;
  ULONG              ParentInstanceId;
  GUID               ParentGuid;
  PVOID              MofData;
  ULONG              MofLength;
  union {
    ULONG              ClientContext;
    ETW_BUFFER_CONTEXT BufferContext;
  };
} EVENT_TRACE, *PEVENT_TRACE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

An [**EVENT\_TRACE\_HEADER**](event-trace-header.md) structure that contains standard event tracing information.

</dd> <dt>

**InstanceId**
</dt> <dd>

Instance identifier. Contains valid data when the provider calls the [**TraceEventInstance**](traceeventinstance.md) function to generate the event. Otherwise, the value is zero.

</dd> <dt>

**ParentInstanceId**
</dt> <dd>

Instance identifier for a parent event. Contains valid data when the provider calls the [**TraceEventInstance**](traceeventinstance.md) function to generate the event. Otherwise, the value is zero.

</dd> <dt>

**ParentGuid**
</dt> <dd>

Class GUID of the parent event. Contains valid data when the provider calls the [**TraceEventInstance**](traceeventinstance.md) function to generate the event. Otherwise, the value is zero.

</dd> <dt>

**MofData**
</dt> <dd>

Pointer to the beginning of the event-specific data for this event.

</dd> <dt>

**MofLength**
</dt> <dd>

Number of bytes to which **MofData** points.

</dd> <dt>

**ClientContext**
</dt> <dd>

Reserved.

</dd> <dt>

**BufferContext**
</dt> <dd>

Provides information about the event such as the session identifier and processor number of the CPU on which the provider process ran. For details, see the [**ETW\_BUFFER\_CONTEXT**](/windows/desktop/api/relogger/ns-relogger-_etw_buffer_context) structure.

**Prior to Windows Vista:** Not supported.

</dd> </dl>

## Remarks

ETW passes this structure to the consumer's [**EventCallback**](eventcallback.md) callback function.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EventCallback**](eventcallback.md)
</dt> <dt>

[**EventClassCallback**](eventclasscallback.md)
</dt> </dl>

 

 




