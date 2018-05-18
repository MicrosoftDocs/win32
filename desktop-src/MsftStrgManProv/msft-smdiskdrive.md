---
title: MSFT\_SMDiskDrive class
description: Represents a disk device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'aa92c094-0777-4724-bbde-957065133d7f'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMDiskDrive class", "MSFT_SMDiskDrive class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMDiskDrive
- MSFT_SMDiskDrive.ObjectId
- MSFT_SMDiskDrive.Identifier
- MSFT_SMDiskDrive.Name
- MSFT_SMDiskDrive.DeviceId
- MSFT_SMDiskDrive.SystemName
- MSFT_SMDiskDrive.DisplayName
- MSFT_SMDiskDrive.Description
- MSFT_SMDiskDrive.Manufacturer
- MSFT_SMDiskDrive.Model
- MSFT_SMDiskDrive.SerialNumber
- MSFT_SMDiskDrive.PartNumber
- MSFT_SMDiskDrive.FirmwareVersion
- MSFT_SMDiskDrive.SoftwareVersion
- MSFT_SMDiskDrive.PhysicalLocation
- MSFT_SMDiskDrive.OperationalStatus
- MSFT_SMDiskDrive.StatusDescription
- MSFT_SMDiskDrive.HealthStatus
- MSFT_SMDiskDrive.HealthStatusDescription
- MSFT_SMDiskDrive.TotalSize
- MSFT_SMDiskDrive.AllocatedSize
- MSFT_SMDiskDrive.BusType
- MSFT_SMDiskDrive.BytesPerPhysicalSector
- MSFT_SMDiskDrive.BytesPerLogicalSector
- MSFT_SMDiskDrive.SpindleSpeed
- MSFT_SMDiskDrive.IsIndicationEnabled
- MSFT_SMDiskDrive.IsAvailable
- MSFT_SMDiskDrive.IsSpare
- MSFT_SMDiskDrive.DiskType
- MSFT_SMDiskDrive.Encryption
- MSFT_SMDiskDrive.CompressionMethod
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMDiskDrive class

Represents a disk device. The disk may be directly attached to the computer system, or it may be a virtual disk exposed to the system through the use of a Storage Management Provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[Dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMDiskDrive : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  String  Name;
  String  DeviceId;
  String  SystemName;
  String  DisplayName;
  String  Description;
  String  Manufacturer;
  String  Model;
  String  SerialNumber;
  String  PartNumber;
  String  FirmwareVersion;
  String  SoftwareVersion;
  String  PhysicalLocation;
  uint16  OperationalStatus[];
  String  StatusDescription;
  uInt16  HealthStatus;
  string  HealthStatusDescription;
  Uint64  TotalSize;
  Uint64  AllocatedSize;
  UInt16  BusType;
  UInt64  BytesPerPhysicalSector;
  UInt64  BytesPerLogicalSector;
  UInt64  SpindleSpeed;
  Boolean IsIndicationEnabled;
  Boolean IsAvailable;
  Boolean IsSpare;
  Uint16  DiskType;
  Uint16  Encryption;
  String  CompressionMethod;
};
```

## Members

The **MSFT\_SMDiskDrive** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMDiskDrive** class has these properties.

<dl> <dt>

**AllocatedSize**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.ConsumableBlocks \* CIM\_StorageExtent.BlockSize")
</dt> </dl>

Consumable size of the disk drive.

</dd> <dt>

**BusType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bus type of the disk drive.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="SCSI"></span><span id="scsi"></span>

**SCSI** (1)


</dt> <dd></dd> <dt>

<span id="ATAPI"></span><span id="atapi"></span>

**ATAPI** (2)


</dt> <dd></dd> <dt>

<span id="ATA"></span><span id="ata"></span>

**ATA** (3)


</dt> <dd></dd> <dt>

<span id="1394"></span>

**1394** (4)


</dt> <dd></dd> <dt>

<span id="SSA"></span><span id="ssa"></span>

**SSA** (5)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>

**Fibre Channel** (6)


</dt> <dd></dd> <dt>

<span id="USB"></span><span id="usb"></span>

**USB** (7)


</dt> <dd></dd> <dt>

<span id="RAID"></span><span id="raid"></span>

**RAID** (8)


</dt> <dd></dd> <dt>

<span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span>

**iSCSI** (9)


</dt> <dd></dd> <dt>

<span id="SAS"></span><span id="sas"></span>

**SAS** (10)


</dt> <dd></dd> <dt>

<span id="SATA"></span><span id="sata"></span>

**SATA** (11)


</dt> <dd></dd> <dt>

<span id="SD"></span><span id="sd"></span>

**SD** (12)


</dt> <dd></dd> <dt>

<span id="MMC"></span><span id="mmc"></span>

**MMC** (13)


</dt> <dd></dd> <dt>

<span id="MAX"></span><span id="max"></span>

**MAX** (14)


</dt> <dd></dd> <dt>

<span id="File_Backed_Virtual"></span><span id="file_backed_virtual"></span><span id="FILE_BACKED_VIRTUAL"></span>

**File Backed Virtual** (15)


</dt> <dd></dd> </dl>

</dd> <dt>

**BytesPerLogicalSector**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Punit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

Logical block size, in bytes, for this disk drive.

</dd> <dt>

**BytesPerPhysicalSector**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Punit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

Physical block size, in bytes, for this disk drive.

</dd> <dt>

**CompressionMethod**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("SNIA\_DiskDrive.CompressionMethod")
</dt> </dl>

Describes the algorithm or tool used by the device to support compression.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_DiskDrive.Description")
</dt> </dl>

A textual description of the disk drive.

</dd> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_DiskDrive.DeviceID")
</dt> </dl>

An address or other identifying information used to uniquely name the disk drive.

</dd> <dt>

**DiskType**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("SNIA\_DiskDrive.DiskType")
</dt> </dl>

The technology employed to store data.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Hard_Disk_Drive"></span><span id="hard_disk_drive"></span><span id="HARD_DISK_DRIVE"></span>

**Hard Disk Drive** (2)


</dt> <dd></dd> <dt>

<span id="Solid_State_Drive"></span><span id="solid_state_drive"></span><span id="SOLID_STATE_DRIVE"></span>

**Solid State Drive** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_DiskDrive.ElementName")
</dt> </dl>

A user-friendly name for the disk drive.

</dd> <dt>

**Encryption**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("SNIA\_DiskDrive.Encryption")
</dt> </dl>

The state of the encryption feature implemented by some disk drives.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

**Not Supported** (1)


</dt> <dd></dd> <dt>

<span id="Unlocked"></span><span id="unlocked"></span><span id="UNLOCKED"></span>

**Unlocked** (2)


</dt> <dd></dd> <dt>

<span id="Locked"></span><span id="locked"></span><span id="LOCKED"></span>

**Locked** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**FirmwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.VersionString")
</dt> </dl>

The complete firmware version information.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the disk drive.

The possible values are.

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the pool in text.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**IsAvailable**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the disk drive is available for the creation of a concrete pool.

</dd> <dt>

**IsIndicationEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the disk drive identification LEDs are enabled; otherwise, **False**.

</dd> <dt>

**IsSpare**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the disk drive is reserved as a hot spare.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalPackage.Manufacturer")
</dt> </dl>

The name of the manufacturer.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalPackage.Model")
</dt> </dl>

The name for the group of disk drives from the manufacturer.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_DiskDrive.Name")
</dt> </dl>

The label by which the disk drive is known.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_DiskDrive.OperationalStatus")
</dt> </dl>

The current SMIS status of the disk drive.

The possible values are.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

**Predictive Failure** (5)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (10)


</dt> <dd></dd> </dl>

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalPackage.PartNumber")
</dt> </dl>

The part number assigned by the manufacturer.

</dd> <dt>

**PhysicalLocation**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Location.PhysicalPosition")
</dt> </dl>

A free-form string that indicates the physical placement of the disk drive.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalPackage.Model")
</dt> </dl>

A manufacturer-allocated number used to identify this disk drive.

</dd> <dt>

**SoftwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.VersionString")
</dt> </dl>

The complete software version information.

</dd> <dt>

**SpindleSpeed**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rotational speed of the disk drive spindle, in RPMs.

</dd> <dt>

**StatusDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current SMIS status of the disk drive in text.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("CIM\_System.Name"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_DiskDrive.SystemName")
</dt> </dl>

The name of the scoping system.

</dd> <dt>

**TotalSize**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.NumberOfBlocks \* CIM\_StorageExtent.BlockSize")
</dt> </dl>

Total size of the disk drive.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





