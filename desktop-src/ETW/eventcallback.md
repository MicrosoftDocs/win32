---
Description: Consumers implement this function to receive events from a session. The PEVENT\_CALLBACK type defines a pointer to this callback function. EventCallback is a placeholder for the application-defined function name.
ms.assetid: 9312eaed-2997-4d44-952a-fcae3b262947
title: PEVENT\_CALLBACK callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EventCallback
api_type: 
- UserDefined
api_location: 
- Evntrace.h
---

# PEVENT\_CALLBACK callback function

Consumers implement this function to receive events from a session.

The **PEVENT\_CALLBACK** type defines a pointer to this callback function. **EventCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
VOID WINAPI EventCallback(
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

To specify the function that ETW calls to deliver the events, set the **EventCallback** member of the [**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md) structure that you pass to the [**OpenTrace**](opentrace.md) function.

This callback receives all events that the session generates from the time you call the [**OpenTrace**](opentrace.md) function to open the trace. Call the [**ProcessTrace**](processtrace.md) function to begin receiving the events.

The event data for the first event you always receive contains the [**TRACE\_LOGFILE\_HEADER**](trace-logfile-header.md) information.

All the other events you receive contain provider-specific event data. You use the **Header.Guid** and **Header.Class.Type** members of [**EVENT\_TRACE**](event-trace.md) to determine the type of event you received. If you are consuming events from your own provider and know the layout of the data, this is not an issue. Otherwise, to interpret the event, the provider must have published their event schema in the \\\\root\\wmi namespace. For information on using an event's MOF schema to interpret the event, see [Consuming Events](consuming-events.md).

## Examples

For an example implementation of an **EventCallback** function, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[*BufferCallback*](buffercallback.md)
</dt> <dt>

[**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md)
</dt> <dt>

[**EventClassCallback**](eventclasscallback.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> </dl>

 

 




