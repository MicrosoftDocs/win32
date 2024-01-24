---
description: The HWConfig\_LogDisk class is the event type class for logical disk configuration events. The following syntax is simplified from MOF code.
ms.assetid: 2b7038fa-2f20-4bb5-bac1-76b272b3421c
title: HWConfig_LogDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HWConfig_LogDisk
- HWConfig_LogDisk.DiskNumber
- HWConfig_LogDisk.Pad
- HWConfig_LogDisk.StartOffset
- HWConfig_LogDisk.PartitionSize
api_type: 
- NA
api_location: 
---

# HWConfig\_LogDisk class

The **HWConfig\_LogDisk** class is the event type class for logical disk configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(12), EventTypeName("LogDisk")]
class HWConfig_LogDisk : HWConfig
{
  uint32 DiskNumber;
  uint32 Pad;
  uint64 StartOffset;
  uint64 PartitionSize;
};
```

## Members

The **HWConfig\_LogDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **HWConfig\_LogDisk** class has these properties.

<dl> <dt>

DiskNumber
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1)
</dt> </dl>

Index number of the disk containing this partition.

</dd> <dt>

Pad
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Reserved.

</dd> <dt>

PartitionSize
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Total size of the partition, in bytes.

</dd> <dt>

StartOffset
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Starting offset (in bytes) of the partition from the beginning of the disk.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                   |



## See also

<dl> <dt>

[**HWConfig**](hwconfig.md)
</dt> </dl>

 

 




