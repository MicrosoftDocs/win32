---
description: This class is the event type class for device deferred procedure call (DPC) events. The following syntax is simplified from MOF code.
ms.assetid: 46010179-7f0a-47dd-95fd-04d30fc597ba
title: DPC class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DPC
- DPC.InitialTime
- DPC.Routine
api_type: 
- NA
api_location: 
---

# DPC class

This class is the event type class for device deferred procedure call (DPC) events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{66, 68, 69}, EventTypeName{"ThreadDPC", "DPC", "TimerDPC"}]
class DPC : PerfInfo
{
  object InitialTime;
  uint32 Routine;
};
```

## Members

The **DPC** class has these types of members:

-   [Properties](#properties)

### Properties

The **DPC** class has these properties.

<dl> <dt>

**InitialTime**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Extension("WmiTime")
</dt> </dl>

DPC entry time.

</dd> <dt>

**Routine**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Address of DPC routine. Use the address with the Image events to find which image started.

</dd> </dl>

## Remarks

These events are logged when a DPC is entered. You use these events to monitor and verify the behavior of drivers and kernel-mode components. For example, you can use DPC, ISR, and Image events to determine those components that spend too much time at high interrupt levels. DPC and ISR events have an entry time stamp which is used to compute the duration of the routines. The image events are read to construct the memory regions that map to certain modules. You can use the mapping to locate the module that contains the interrupt routine.

The TimerDPC event records when a DPC fires as a result of a timer expiration and the ThreadDPC event records when a threaded DPC executes.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




