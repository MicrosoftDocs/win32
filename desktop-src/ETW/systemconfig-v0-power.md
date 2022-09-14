---
description: SystemConfig_V0_Power class - This class is the event type class for power configuration events. The following syntax is simplified from MOF code.
ms.assetid: b3391435-dac0-4c48-b788-eb4d4a7aa635
title: SystemConfig_V0_Power class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_V0_Power
- SystemConfig_V0_Power.s1
- SystemConfig_V0_Power.s2
- SystemConfig_V0_Power.s3
- SystemConfig_V0_Power.s4
- SystemConfig_V0_Power.s5
- SystemConfig_V0_Power.Pad1
- SystemConfig_V0_Power.Pad2
- SystemConfig_V0_Power.Pad3
api_type: 
- NA
api_location: 
---

# SystemConfig\_V0\_Power class

This class is the event type class for power configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(16), EventTypeName("Power")]
class SystemConfig_V0_Power : SystemConfig_V0
{
  boolean s1;
  boolean s2;
  boolean s3;
  boolean s4;
  boolean s5;
  uint8   Pad1;
  uint8   Pad2;
  uint8   Pad3;
};
```

## Members

The **SystemConfig\_V0\_Power** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_V0\_Power** class has these properties.

<dl> <dt>

Pad1
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6)
</dt> </dl>

Reserved.

</dd> <dt>

Pad2
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

Reserved.

</dd> <dt>

Pad3
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8)
</dt> </dl>

Reserved.

</dd> <dt>

s1
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

True indicates the system supports sleep state S1.

</dd> <dt>

s2
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

True indicates the system supports sleep state S2.

</dd> <dt>

s3
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

True indicates the system supports sleep state S3.

</dd> <dt>

s4
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

True indicates the system supports sleep state S4.

</dd> <dt>

s5
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

True indicates the system supports sleep state S5.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SystemConfig\_V0**](systemconfig-v0.md)
</dt> </dl>

 

 




