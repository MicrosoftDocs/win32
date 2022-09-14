---
description: The HWConfig\_PhyDisk class is the event type class for physical disk configuration events. The following syntax is simplified from MOF code.
ms.assetid: b134ab45-b161-452f-be84-ccbdfa3fe4af
title: HWConfig_PhyDisk class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HWConfig_PhyDisk
- HWConfig_PhyDisk.DiskNumber
- HWConfig_PhyDisk.BytesPerSector
- HWConfig_PhyDisk.SectorsPerTrack
- HWConfig_PhyDisk.TracksPerCylinder
- HWConfig_PhyDisk.Cylinders
- HWConfig_PhyDisk.SCSIPort
- HWConfig_PhyDisk.SCSIPath
- HWConfig_PhyDisk.SCSITarget
- HWConfig_PhyDisk.SCSILun
- HWConfig_PhyDisk.Manufacturer
api_type: 
- NA
api_location: 
---

# HWConfig\_PhyDisk class

The **HWConfig\_PhyDisk** class is the event type class for physical disk configuration events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(11), EventTypeName("PhyDisk")]
class HWConfig_PhyDisk : HWConfig
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
  string Manufacturer;
};
```

## Members

The **HWConfig\_PhyDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **HWConfig\_PhyDisk** class has these properties.

<dl> <dt>

BytesPerSector
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2)
</dt> </dl>

Number of bytes in each sector for the physical disk drive.

</dd> <dt>

Cylinders
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(5)
</dt> </dl>

Total number of cylinders on the physical disk drive. Note: the value for this property is obtained through extended functions of BIOS interrupt 13h. The value may be inaccurate if the drive uses a translation scheme to support high capacity disk sizes. Consult the manufacturer for accurate drive specifications.

</dd> <dt>

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

Manufacturer
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(10), StringTermination("NullTerminated"), Format("w")
</dt> </dl>

Name of the disk drive manufacturer.

</dd> <dt>

SCSILun
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(9)
</dt> </dl>

SCSI logical unit number (LUN) of the SCSI adapter.

</dd> <dt>

SCSIPath
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(7)
</dt> </dl>

SCSI bus number of the SCSI adapter.

</dd> <dt>

SCSIPort
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(6)
</dt> </dl>

SCSI number of the SCSI adapter.

</dd> <dt>

SCSITarget
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(8)
</dt> </dl>

Contains the number of the target device.

</dd> <dt>

SectorsPerTrack
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(3)
</dt> </dl>

Number of sectors in each track for this physical disk drive.

</dd> <dt>

TracksPerCylinder
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(4)
</dt> </dl>

Number of tracks in each cylinder on the physical disk drive. Note: the value for this property is obtained through extended functions of BIOS interrupt 13h. The value may be inaccurate if the drive uses a translation scheme to support high capacity disk sizes. Consult the manufacturer for accurate drive specifications.

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

 

 




