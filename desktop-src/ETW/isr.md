---
description: This class is the event type class for interrupt service routine (ISR) events. The following syntax is simplified from MOF code.
ms.assetid: 2c7ccace-3384-43f4-905e-e7eeeee6f87b
title: ISR class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISR
- ISR.InitialTime
- ISR.Routine
- ISR.ReturnValue
- ISR.Vector
- ISR.Reserved
api_type: 
- NA
api_location: 
---

# ISR class

This class is the event type class for interrupt service routine (ISR) events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{67}, EventTypeName{"ISR"}]
class ISR : PerfInfo
{
  object InitialTime;
  uint32 Routine;
  uint8  ReturnValue;
  uint8  Vector;
  uint16 Reserved;
};
```

## Members

The **ISR** class has these types of members:

-   [Properties](#properties)

### Properties

The **ISR** class has these properties.

<dl> <dt>

**InitialTime**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Extension("WmiTime")
</dt> </dl>

ISR entry time.

</dd> <dt>

**Reserved**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), Pointer
</dt> </dl>

Reserved.

</dd> <dt>

**ReturnValue**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Boolean indicating if the interrupt was claimed (is True if the interrupt was claimed).

</dd> <dt>

**Routine**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Address of ISR routine. Use the address with the Image events to find which image started.

</dd> <dt>

**Vector**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Vector from interrupt descriptor table to which ISR routine is assigned.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




