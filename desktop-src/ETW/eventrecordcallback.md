---
Description: Consumers implement this callback to receive events from a session. The PEVENT\_RECORD\_CALLBACK type defines a pointer to this callback function. EventRecordCallback is a placeholder for the application-defined function name.
ms.assetid: 80a30faf-af1f-4440-8a17-9df44bdb2291
title: PEVENT_RECORD_CALLBACK callback function
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EventRecordCallback
api_type:
- UserDefined
api_location:
- Evntrace.h
---

# PEVENT\_RECORD\_CALLBACK callback function

Consumers implement this callback to receive events from a session.

The **PEVENT\_RECORD\_CALLBACK** type defines a pointer to this callback function. **EventRecordCallback** is a placeholder for the application-defined function name.

## Syntax


```C++
VOID WINAPI EventRecordCallback(
  _In_ PEVENT_RECORD EventRecord
);
```



## Parameters

<dl> <dt>

*EventRecord* \[in\]
</dt> <dd>

Pointer to an [**EVENT\_RECORD**](https://msdn.microsoft.com/en-us/library/Aa363769(v=VS.85).aspx) structure that contains the event information.

</dd> </dl>

## Return value

The function does not return a value.

## Remarks

To specify the function that ETW calls to deliver events, set the **EventRecordCallback** member of the [**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md) structure (you pass this structure to the [**OpenTrace**](opentrace.md) function). You must also set the **ProcessTraceMode** member to PROCESS\_TRACE\_MODE\_EVENT\_RECORD.

This callback receives all events that the session generates from the time you call the [**OpenTrace**](opentrace.md) function. Call the [**ProcessTrace**](processtrace.md) function to begin receiving the events.

For information on parsing the event data, see [Retrieving Event Data Using TDH](retrieving-event-data-using-tdh.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[*BufferCallback*](buffercallback.md)
</dt> <dt>

[**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md)
</dt> <dt>

[**ProcessTrace**](processtrace.md)
</dt> </dl>

 

 




