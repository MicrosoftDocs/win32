---
Description: Consumers implement this function to receive statistics about each buffer of events that ETW delivers to an event trace consumer.
ms.assetid: 0cfe2f62-63dc-45a6-96ce-fb4bf458358f
title: PEVENT_TRACE_BUFFER_CALLBACK callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BufferCallback
api_type: 
- UserDefined
api_location: 
- Evntrace.h
---

# PEVENT\_TRACE\_BUFFER\_CALLBACK callback function

Consumers implement this function to receive statistics about each buffer of events that ETW delivers to an event trace consumer. ETW calls this function after the events for each buffer are delivered.

The **PEVENT\_TRACE\_BUFFER\_CALLBACK** type defines a pointer to this callback function. **BufferCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
ULONG WINAPI BufferCallback(
  _In_ PEVENT_TRACE_LOGFILE Buffer
);
```



## Parameters

<dl> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md) structure that contains information about the buffer.

</dd> </dl>

## Return value

To continue processing events, return **TRUE**. Otherwise, return **FALSE**. Returning **FALSE** will terminate the [**ProcessTrace**](processtrace.md) function.

## Remarks

To specify the function that ETW calls to deliver the buffer statistics, set the **BufferCallback** member of the [**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md) structure that you pass to the [**OpenTrace**](opentrace.md) function.

## Examples

For an example implementation of a **BufferCallback** function, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> </dl>

 

 




