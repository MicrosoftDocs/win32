---
description: This event type class is used to indicate that events were lost in a real-time session. The following syntax is simplified from MOF code.
ms.assetid: 19c747c0-2d9f-49c5-81e4-06a870371bac
title: RT_LostEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RT_LostEvent
api_type: 
- NA
api_location: 
---

# RT\_LostEvent class

This event type class is used to indicate that events were lost in a real-time session.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{32, 33, 34}, EventTypeName{"RTLostEvent", "RTLostBuffer", "RTLostFile"}]
class RT_LostEvent : Lost_Event
{
};
```

## Members

The **RT\_LostEvent** class does not define any members.

## Remarks

The RTLostEvent event type indicates that one or more events were lost. The RTLostBuffer event type indicates that one or more buffers were lost. The RTLostEvent and RTLostBuffer event types are delivered before processing events from the buffer.

The RTLostFile indicates that the backing file used by the AutoLogger to capture events was lost.

Loosing events depends on the frequency with which the events are logged and how much time the consumer spends processing the events.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                      |



## See also

<dl> <dt>

[**Lost\_Event**](lost-event.md)
</dt> </dl>

 

 




