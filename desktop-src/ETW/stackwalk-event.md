---
description: This class is the event type class for stack tracing events.
ms.assetid: 05117bd6-a39c-42f3-8aed-c6f758f946c6
title: StackWalk_Event class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StackWalk_Event
- StackWalk_Event.EventTimeStamp
- StackWalk_Event.StackProcess
- StackWalk_Event.StackThread
- StackWalk_Event.Stack1
- StackWalk_Event.Stack192
api_type: 
- NA
api_location: 
---

# StackWalk\_Event class

This class is the event type class for stack tracing events.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[EventType{32}, EventTypeName{"Stack"}]
class StackWalk_Event : StackWalk
{
  uint64 EventTimeStamp;
  uint32 StackProcess;
  uint32 StackThread;
  uint32 Stack1;
  uint32 Stack192;
};
```

## Members

The **StackWalk\_Event** class has these types of members:

-   [Properties](#properties)

### Properties

The **StackWalk\_Event** class has these properties.

<dl> <dt>

**EventTimeStamp**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

Original event time stamp from the event header. Use this time stamp to match the stack to an event.

</dd> <dt>

**Stack1**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), pointer
</dt> </dl>

Address of the call.

</dd> <dt>

**Stack192**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(195), pointer
</dt> </dl>

Address of the call.

</dd> <dt>

**StackProcess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), format("x")
</dt> </dl>

The process identifier of the original event.

</dd> <dt>

**StackThread**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

The thread identifier of the original event.

</dd> </dl>

## Remarks

Note that the class does not show all of the **Stack*n*** properties that exist between **Stack1** and **Stack192**. Use the size of the event to determine how many **Stack*n*** properties contain valid addresses.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 




