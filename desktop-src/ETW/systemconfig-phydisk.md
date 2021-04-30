---
description: SystemConfig_PhyDisk class - This class is the event type class for physical disk configuration events.
ms.assetid: 850a6b2c-69e6-47ae-95ff-585fcc70c1c8
title: SystemConfig_PhyDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemConfig_PhyDisk
- SystemConfig_PhyDisk.DiskNumber
- SystemConfig_PhyDisk.BytesPerSector
- SystemConfig_PhyDisk.SectorsPerTrack
- SystemConfig_PhyDisk.TracksPerCylinder
- SystemConfig_PhyDisk.Cylinders
- SystemConfig_PhyDisk.SCSIPort
- SystemConfig_PhyDisk.SCSIPath
- SystemConfig_PhyDisk.SCSITarget
- SystemConfig_PhyDisk.SCSILun
- SystemConfig_PhyDisk.Manufacturer
- SystemConfig_PhyDisk.PartitionCount
- SystemConfig_PhyDisk.WriteCacheEnabled
- SystemConfig_PhyDisk.Pad
- SystemConfig_PhyDisk.BootDriveLetter
- SystemConfig_PhyDisk.Spare
api_type: 
- NA
api_location: 
---

# SystemConfig\_PhyDisk class

This class is the event type class for physical disk configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(11), EventTypeName("PhyDisk")]
class SystemConfig_PhyDisk : SystemConfig
{
  uint32 DiskNumber;
  uint32 BytesPerSector;
  uint32 SectorsPerTrack;
  uint32 TracksPerCylinder;
  uint64 Cylinders;
  uint32 SCSIPort;
  uint32 SCSIPath;
  uint32 SCSITarget;
  uint32 SCSILun;
  char16 Manufacturer[];
  uint32 PartitionCount;
  uint8  WriteCacheEnabled;
  uint8  Pad;
  char16 BootDriveLetter[];
  char16 Spare[];
};
```

## Members

The **SystemConfig\_PhyDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **SystemConfig\_PhyDisk** class has these properties.

<dl> <dt>

**BootDriveLetter**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (14), **Max** (3), **Format("s")**
</dt> </dl>

Drive letter of the boot drive in the form, "<letter>:".

</dd> <dt>

**BytesPerSector**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2)
</dt> </dl>

Number of bytes in each sector for the physical disk drive.

</dd> <dt>

**Cylinders**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Total number of cylinders on the physical disk drive. Note: the value for this property is obtained through extended functions of BIOS interrupt 13h. The value may be inaccurate if the drive uses a translation scheme to support high capacity disk sizes. Consult the manufacturer for accurate drive specifications.

</dd> <dt>

**DiskNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

Index number of the disk containing this partition.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10), **Max** (256), **Format("s")**
</dt> </dl>

Name of the disk drive manufacturer.

</dd> <dt>

**Pad**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13)
</dt> </dl>

Not used.

</dd> <dt>

**PartitionCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11)
</dt> </dl>

Number of partitions on this physical disk drive that are recognized by the operating system.

</dd> <dt>

**SCSILun**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9)
</dt> </dl>

SCSI logical unit number (LUN) of the SCSI adapter.

</dd> <dt>

**SCSIPath**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7)
</dt> </dl>

SCSI bus number of the SCSI adapter.

</dd> <dt>

**SCSIPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6)
</dt> </dl>

SCSI number of the SCSI adapter.

</dd> <dt>

**SCSITarget**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8)
</dt> </dl>

Contains the number of the target device.

</dd> <dt>

**SectorsPerTrack**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Number of sectors in each track for this physical disk drive.

</dd> <dt>

**Spare**
</dt> <dd> <dl> <dt>

Data type: **char16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (15), **Max** (2), **Format("s")**
</dt> </dl>

Not used.

</dd> <dt>

**TracksPerCylinder**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Number of tracks in each cylinder on the physical disk drive. Note: the value for this property is obtained through extended functions of BIOS interrupt 13h. The value may be inaccurate if the drive uses a translation scheme to support high capacity disk sizes. Consult the manufacturer for accurate drive specifications.

</dd> <dt>

**WriteCacheEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12)
</dt> </dl>

True if the write cache is enabled.

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

 

 




