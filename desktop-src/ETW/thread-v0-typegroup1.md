---
description: This class is the event type class for thread events. The following syntax is simplified from MOF code.
ms.assetid: cc668fef-48fe-4948-8fe5-4351f7a033d1
title: Thread_V0_TypeGroup1 class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Thread_V0_TypeGroup1
- Thread_V0_TypeGroup1.TThreadId
- Thread_V0_TypeGroup1.ProcessId
api_type: 
- NA
api_location: 
---

# Thread\_V0\_TypeGroup1 class

This class is the event type class for thread events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{1, 2, 3, 4}, EventTypeName{"Start", "End", "DCStart", "DCEnd"}]
class Thread_V0_TypeGroup1 : Thread_V0
{
  uint32 TThreadId;
  uint32 ProcessId;
};
```

## Members

The **Thread\_V0\_TypeGroup1** class has these types of members:

-   [Properties](#properties)

### Properties

The **Thread\_V0\_TypeGroup1** class has these properties.

<dl> <dt>

ProcessId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

Process identifier of the thread involved in the event.

</dd> <dt>

TThreadId
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

Thread identifier of the thread involved in the event.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**Thread\_V0**](thread-v0.md)
</dt> </dl>

 

 




