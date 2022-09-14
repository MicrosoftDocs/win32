---
description: This class is the event type class for IDE channel events. The following syntax is simplified from MOF code.
ms.assetid: 2265a4a6-4377-4aa9-926a-def6e8eda998
title: SystemConfig_IDEChannel class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_IDEChannel
- SystemConfig_IDEChannel.TargetId
- SystemConfig_IDEChannel.DeviceType
- SystemConfig_IDEChannel.DeviceTimingMode
- SystemConfig_IDEChannel.LocationInformationLen
- SystemConfig_IDEChannel.LocationInformation
api_type: 
- NA
api_location: 
---

# SystemConfig\_IDEChannel class

This class is the event type class for IDE channel events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(23), EventTypeName("IDEChannel")]
class SystemConfig_IDEChannel : SystemConfig
{
  uint32 TargetId;
  uint32 DeviceType;
  uint32 DeviceTimingMode;
  uint32 LocationInformationLen;
  string LocationInformation;
};
```

## Members

The **SystemConfig\_IDEChannel** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_IDEChannel** class has these properties.

<dl> <dt>

**DeviceTimingMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3), Format("x")
</dt> </dl>

The mode in which the IDE could function. The following are the possible values:

-   PIO\_MODE0 (0x1)
-   PIO\_MODE1 (0x2)
-   PIO\_MODE2 (0x4)
-   PIO\_MODE3 (0x8)
-   PIO\_MODE4 (0x10)
-   SWDMA\_MODE0 (0x20)
-   SWDMA\_MODE1 (0x40)
-   SWDMA\_MODE2 (0x80)
-   MWDMA\_MODE0 (0x100)
-   MWDMA\_MODE2 (0x200)
-   MWDMA\_MODE3 (0x400)
-   UDMA\_MODE0 (0x800)
-   UDMA\_MODE1 (0x1000)
-   UDMA\_MODE2 (0x2000)
-   UDMA\_MODE3 (0x4000)
-   UDMA\_MODE4 (0x8000)
-   UDMA\_MODE5 (0x10000)

</dd> <dt>

**DeviceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Format("x")
</dt> </dl>

The device type. The following are the possible values:

-   ATA (1)
-   ATAPI (2)

</dd> <dt>

**LocationInformation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

The IDE channel (for example, Primary Channel, Secondary Channel, and so on).

</dd> <dt>

**LocationInformationLen**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Length of the **LocationInformation** string.

</dd> <dt>

**TargetId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

The identifier of the disk.

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

 

 




