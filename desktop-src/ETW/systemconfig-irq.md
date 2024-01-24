---
description: This class is the event type class for interrupt request (IRQ) events. The following syntax is simplified from MOF code.
ms.assetid: 9d4692e8-f19f-478c-a003-396722e426c3
title: SystemConfig_IRQ class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_IRQ
- SystemConfig_IRQ.IRQAffinity
- SystemConfig_IRQ.IRQNum
- SystemConfig_IRQ.DeviceDescriptionLen
- SystemConfig_IRQ.DeviceDescription
api_type: 
- NA
api_location: 
---

# SystemConfig\_IRQ class

This class is the event type class for interrupt request (IRQ) events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(21), EventTypeName("IRQ")]
class SystemConfig_IRQ : SystemConfig
{
  uint64 IRQAffinity;
  uint32 IRQNum;
  uint32 DeviceDescriptionLen;
  string DeviceDescription;
};
```

## Members

The **SystemConfig\_IRQ** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_IRQ** class has these properties.

<dl> <dt>

**DeviceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Description of the device or software making the request.

</dd> <dt>

**DeviceDescriptionLen**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Length, in characters, of the string in **DeviceDescription**.

</dd> <dt>

**IRQAffinity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Format("x")
</dt> </dl>

IRQ affinity mask. The affinity mask identifies the specific processors (or groups of processors) that can receive the IRQ.

</dd> <dt>

**IRQNum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Interrupt request line number.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SystemConfig**](systemconfig.md)
</dt> </dl>

 

 




