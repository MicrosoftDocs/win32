---
description: SystemConfig_V0_LogDisk class - This class is the event type class for logical disk configuration events.
ms.assetid: 3fa5f2e4-f6fa-4c10-9634-04908783cd28
title: SystemConfig_V0_LogDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_V0_LogDisk
- SystemConfig_V0_LogDisk.StartOffset
- SystemConfig_V0_LogDisk.PartitionSize
- SystemConfig_V0_LogDisk.DiskNumber
- SystemConfig_V0_LogDisk.Size
- SystemConfig_V0_LogDisk.DriveType
- SystemConfig_V0_LogDisk.DriveLetterString
- SystemConfig_V0_LogDisk.Pad
- SystemConfig_V0_LogDisk.PartitionNumber
- SystemConfig_V0_LogDisk.SectorsPerCluster
- SystemConfig_V0_LogDisk.BytesPerSector
- SystemConfig_V0_LogDisk.NumberOfFreeClusters
- SystemConfig_V0_LogDisk.TotalNumberOfClusters
- SystemConfig_V0_LogDisk.FileSystem
- SystemConfig_V0_LogDisk.VolumeExt
api_type: 
- NA
api_location: 
---

# SystemConfig\_V0\_LogDisk class

This class is the event type class for logical disk configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(12), EventTypeName("LogDisk")]
class SystemConfig_V0_LogDisk : SystemConfig_V0
{
  uint64 StartOffset;
  uint64 PartitionSize;
  uint32 DiskNumber;
  uint32 Size;
  uint32 DriveType;
  char16 DriveLetterString[];
  uint32 Pad;
  uint32 PartitionNumber;
  uint32 SectorsPerCluster;
  uint32 BytesPerSector;
  sint64 NumberOfFreeClusters;
  sint64 TotalNumberOfClusters;
  char16 FileSystem;
  uint32 VolumeExt;
};
```

## Members

The **SystemConfig\_V0\_LogDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_V0\_LogDisk** class has these properties.

<dl> <dt>

**BytesPerSector**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10)
</dt> </dl>

Number of bytes in each sector for the physical disk drive.

</dd> <dt>

**DiskNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Index number of the disk containing this partition.

</dd> <dt>

**DriveLetterString**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6), **Max** (4)
</dt> </dl>

Drive letter of the disk in the form, "&lt;letter&gt;:".

</dd> <dt>

**DriveType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Type of disk drive. Possible values are:



| Value                                                                        | Meaning                                         |
|------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>1</dt> </dl> | Partition<br/>                            |
| <dl> <dt>2</dt> </dl> | Volume<br/>                               |
| <dl> <dt>3</dt> </dl> | Extended partition on multiple disks<br/> |



 

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **char16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13), **Max** (16)
</dt> </dl>

File system on the logical disk, for example, NTFS.

</dd> <dt>

**NumberOfFreeClusters**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11)
</dt> </dl>

Number of free clusters in the specified volume.

</dd> <dt>

**Pad**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7)
</dt> </dl>

Reserved.

</dd> <dt>

**PartitionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8)
</dt> </dl>

Index number of the partition.

</dd> <dt>

**PartitionSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2)
</dt> </dl>

Total size of the partition, in bytes.

</dd> <dt>

**SectorsPerCluster**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9)
</dt> </dl>

Number of sectors in the volume.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Size of the disk drive, in bytes.

</dd> <dt>

**StartOffset**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

Starting offset (in bytes) of the partition from the beginning of the disk.

</dd> <dt>

**TotalNumberOfClusters**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12)
</dt> </dl>

Number of used and free clusters in the volume.

</dd> <dt>

**VolumeExt**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (14)
</dt> </dl>

Reserved.

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

 

 




