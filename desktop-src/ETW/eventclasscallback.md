---
Description: Consumers implement this function to receive events for a specific event trace class from a session.
ms.assetid: 32e94f58-b8b6-4e0a-b53b-716a534ac374
title: EventClassCallback callback function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EventClassCallback
api_type: 
- UserDefined
api_location: 
- Evntrace.h
---

# EventClassCallback callback function

\[Do not implement this function; it may be unavailable in subsequent versions.\]

Consumers implement this function to receive events for a specific event trace class from a session. ETW calls this function every time the [**ProcessTrace**](processtrace.md) function process an event belonging to the event trace class.

The **PEVENT\_CALLBACK** type defines a pointer to this callback function. **EventClassCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
VOID WINAPI EventClassCallback(
  _In_ PEVENT_TRACE pEvent
);
```



## Parameters

<dl> <dt>

*pEvent* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_TRACE**](event-trace.md) structure that contains the event information.

</dd> </dl>

## Return value

The function does not return a value.

## Remarks

To associate each **EventClassCallback** function with the class GUID of the event trace class it processes, use the [**SetTraceCallback**](settracecallback.md) function.

To stop the **EventClassCallback** from receiving events, call the [**RemoveTraceCallback**](removetracecallback.md) function.

To processes all events that the session generates, see the [**EventCallback**](eventcallback.md) function.

If you use both [**EventCallback**](eventcallback.md) and **EventClassCallback** to receive events, the event is always sent to **EventCallback** and is only sent to **EventClassCallback** if the event matches the class GUID associated with the callback.

You use the **Header.Class.Type** member of [**EVENT\_TRACE**](event-trace.md) to determine the type of event you received. If you are consuming events from your own provider and know the layout of the data, this is not an issue. Otherwise, to interpret the event, the provider must have published their event schema in the \\\\root\\wmi namespace. For information on using an event's MOF schema to interpret the event, see [Consuming Events](consuming-events.md).

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

[**ProcessTrace**](processtrace.md)
</dt> <dt>

[**RemoveTraceCallback**](removetracecallback.md)
</dt> <dt>

[**SetTraceCallback**](settracecallback.md)
</dt> </dl>

 

 




