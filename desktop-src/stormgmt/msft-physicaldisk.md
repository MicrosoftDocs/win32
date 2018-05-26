---
title: MSFT\_PhysicalDisk class
description: Represents a subsystem drive or spindle.
ms.assetid: 01eeb68b-c8b0-4f91-9072-3a03b20b9636
keywords:
- MSFT_PhysicalDisk class Windows Storage Management API
- MSFT_PhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk
- MSFT_PhysicalDisk.UniqueIdFormat
- MSFT_PhysicalDisk.DeviceId
- MSFT_PhysicalDisk.FriendlyName
- MSFT_PhysicalDisk.HealthStatus
- MSFT_PhysicalDisk.OperationalStatus
- MSFT_PhysicalDisk.OperationalDetails
- MSFT_PhysicalDisk.PhysicalLocation
- MSFT_PhysicalDisk.VirtualDiskFootprint
- MSFT_PhysicalDisk.Usage
- MSFT_PhysicalDisk.SupportedUsages
- MSFT_PhysicalDisk.Description
- MSFT_PhysicalDisk.PartNumber
- MSFT_PhysicalDisk.FirmwareVersion
- MSFT_PhysicalDisk.SoftwareVersion
- MSFT_PhysicalDisk.Size
- MSFT_PhysicalDisk.AllocatedSize
- MSFT_PhysicalDisk.BusType
- MSFT_PhysicalDisk.IsWriteCacheEnabled
- MSFT_PhysicalDisk.IsPowerProtected
- MSFT_PhysicalDisk.PhysicalSectorSize
- MSFT_PhysicalDisk.LogicalSectorSize
- MSFT_PhysicalDisk.SpindleSpeed
- MSFT_PhysicalDisk.IsIndicationEnabled
- MSFT_PhysicalDisk.EnclosureNumber
- MSFT_PhysicalDisk.SlotNumber
- MSFT_PhysicalDisk.CanPool
- MSFT_PhysicalDisk.CannotPoolReason
- MSFT_PhysicalDisk.OtherCannotPoolReasonDescription
- MSFT_PhysicalDisk.IsPartial
- MSFT_PhysicalDisk.MediaType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_PhysicalDisk class

Represents a subsystem drive or spindle.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_PhysicalDisk : MSFT_StorageFaultDomain
{
  UInt16  UniqueIdFormat;
  String  DeviceId;
  String  FriendlyName;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OperationalDetails[];
  String  PhysicalLocation;
  UInt16  VirtualDiskFootprint;
  UInt16  Usage;
  UInt16  SupportedUsages[];
  String  Description;
  String  PartNumber;
  String  FirmwareVersion;
  String  SoftwareVersion;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt16  BusType;
  Boolean IsWriteCacheEnabled;
  Boolean IsPowerProtected;
  UInt64  PhysicalSectorSize;
  UInt64  LogicalSectorSize;
  UInt32  SpindleSpeed;
  Boolean IsIndicationEnabled;
  UInt16  EnclosureNumber;
  UInt16  SlotNumber;
  Boolean CanPool;
  UInt16  CannotPoolReason[];
  String  OtherCannotPoolReasonDescription;
  Boolean IsPartial;
  UInt16  MediaType;
};
```

## Members

The **MSFT\_PhysicalDisk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_PhysicalDisk** class has these methods.



| Method                                                       | Description                                                                                                                       |
|:-------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**Maintenance**](msft-physicaldisk-maintenance.md)         | Allows maintenance operations to be performed on the physical disk while in a concrete pool, such as firmware updates.<br/> |
| [**Reset**](msft-physicaldisk-reset.md)                     | Resets the physical disk.<br/>                                                                                              |
| [**SetAttributes**](msft-physicaldisk-setattributes.md)     | Updates the attributes of the physical disk.<br/>                                                                           |
| [**SetDescription**](msft-physicaldisk-setdescription.md)   | Sets or changes the description for the physical disk.<br/>                                                                 |
| [**SetFriendlyName**](msft-physicaldisk-setfriendlyname.md) | Sets or changes the friendly name for the physical disk.<br/>                                                               |
| [**SetUsage**](msft-physicaldisk-setusage.md)               | Sets or changes the intended usage for the physical disk within a concrete pool.<br/>                                       |
| [**SetWriteCache**](msft-physicaldisk-setwritecache.md)     | Allows the physical disk's write cache to be enabled or disabled.<br/>                                                      |



 

### Properties

The **MSFT\_PhysicalDisk** class has these properties.

<dl> <dt>

**AllocatedSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The total amount of used space on this physical disk. This should include usage from all storage pools and other data stored on the disk.

</dd> <dt>

**BusType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The storage bus type of the physical disk.



| Value                                                                                                                                                                                                                                                                        | Meaning                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                  | The bus type is unknown.<br/>               |
| <span id="SCSI"></span><span id="scsi"></span><dl> <dt>**SCSI**</dt> <dt>1</dt> </dl>                                                                                     | SCSI<br/>                                   |
| <span id="ATAPI"></span><span id="atapi"></span><dl> <dt>**ATAPI**</dt> <dt>2</dt> </dl>                                                                                  | ATAPI<br/>                                  |
| <span id="ATA"></span><span id="ata"></span><dl> <dt>**ATA**</dt> <dt>3</dt> </dl>                                                                                        | ATA<br/>                                    |
| <span id="1394"></span><dl> <dt>**1394**</dt> <dt>4</dt> </dl>                                                                                                            | IEEE 1394<br/>                              |
| <span id="SSA"></span><span id="ssa"></span><dl> <dt>**SSA**</dt> <dt>5</dt> </dl>                                                                                        | SSA<br/>                                    |
| <span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span><dl> <dt>**Fibre Channel**</dt> <dt>6</dt> </dl>                          | Fibre Channel<br/>                          |
| <span id="USB"></span><span id="usb"></span><dl> <dt>**USB**</dt> <dt>7</dt> </dl>                                                                                        | USB<br/>                                    |
| <span id="RAID"></span><span id="raid"></span><dl> <dt>**RAID**</dt> <dt>8</dt> </dl>                                                                                     | RAID<br/>                                   |
| <span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span><dl> <dt>**iSCSI**</dt> <dt>9</dt> </dl>                                                          | iSCSI<br/>                                  |
| <span id="SAS"></span><span id="sas"></span><dl> <dt>**SAS**</dt> <dt>10</dt> </dl>                                                                                       | Serial Attached SCSI (SAS)<br/>             |
| <span id="SATA"></span><span id="sata"></span><dl> <dt>**SATA**</dt> <dt>11</dt> </dl>                                                                                    | Serial ATA (SATA)<br/>                      |
| <span id="SD"></span><span id="sd"></span><dl> <dt>**SD**</dt> <dt>12</dt> </dl>                                                                                          | Secure Digital (SD)<br/>                    |
| <span id="MMC"></span><span id="mmc"></span><dl> <dt>**MMC**</dt> <dt>13</dt> </dl>                                                                                       | Multimedia Card (MMC)<br/>                  |
| <span id="MAX"></span><span id="max"></span><dl> <dt>**MAX**</dt> <dt>14</dt> </dl>                                                                                       | This value is reserved for system use.<br/> |
| <span id="File_Backed_Virtual"></span><span id="file_backed_virtual"></span><span id="FILE_BACKED_VIRTUAL"></span><dl> <dt>**File Backed Virtual**</dt> <dt>15</dt> </dl> | File-Backed Virtual<br/>                    |
| <span id="Storage_Spaces"></span><span id="storage_spaces"></span><span id="STORAGE_SPACES"></span><dl> <dt>**Storage Spaces**</dt> <dt>16</dt> </dl>                     | Storage Spaces<br/>                         |
| <span id="NVMe"></span><span id="nvme"></span><span id="NVME"></span><dl> <dt>**NVMe**</dt> <dt>17</dt> </dl>                                                             |                                                   |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>18..</dt> </dl>   | This value is reserved for system use.<br/> |



 

</dd> <dt>

**CannotPoolReason**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array of values specifying the reasons why this physical disk cannot be added to a concrete pool. This property is valid only if the **CanPool** property is **FALSE**.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="In_a_Pool"></span><span id="in_a_pool"></span><span id="IN_A_POOL"></span>**In a Pool** (2)
</dt> <dt>

<span id="Not_Healthy"></span><span id="not_healthy"></span><span id="NOT_HEALTHY"></span>**Not Healthy** (3)
</dt> <dt>

<span id="Removable_Media"></span><span id="removable_media"></span><span id="REMOVABLE_MEDIA"></span>**Removable Media** (4)
</dt> <dt>

<span id="In_Use_by_Cluster"></span><span id="in_use_by_cluster"></span><span id="IN_USE_BY_CLUSTER"></span>**In Use by Cluster** (5)
</dt> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (6)
</dt> <dt>

<span id="Insufficient_Capacity"></span><span id="insufficient_capacity"></span><span id="INSUFFICIENT_CAPACITY"></span>**Insufficient Capacity** (7)
</dt> <dt>

<span id="Spare_Disk"></span><span id="spare_disk"></span><span id="SPARE_DISK"></span>**Spare Disk** (8)
</dt> <dt>

<span id="Reserved_by_subsystem"></span><span id="reserved_by_subsystem"></span><span id="RESERVED_BY_SUBSYSTEM"></span>**Reserved by subsystem** (9)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (10)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (0x8000..)
</dt> </dl>

</dd> <dt>

**CanPool**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this physical disk can be added to a concrete pool.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-settable description of the physical disk.

</dd> <dt>

**DeviceId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An address or other identifier that uniquely names the physical disk.

</dd> <dt>

**EnclosureNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of the enclosure in which the disk physically resides.

</dd> <dt>

**FirmwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A string representation of the firmware revision.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly display name for the physical disk. The initial value should be set by the storage provider or subsystem, and can be modified by the user at any point in the object's lifetime.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A high-level indication of device health.



| Value                                                                        | Meaning              |
|------------------------------------------------------------------------------|----------------------|
| <dl> <dt>0</dt> </dl> | Healthy<br/>   |
| <dl> <dt>1</dt> </dl> | Warning<br/>   |
| <dl> <dt>2</dt> </dl> | Unhealthy<br/> |
| <dl> <dt>5</dt> </dl> | Unknown<br/>   |



 

</dd> <dt>

**IsIndicationEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the physical disk's identification LEDs are active or not. This is typically used in maintenance operations.

</dd> <dt>

**IsPartial**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if this physical disk is partially consumed by a system or service outside of normal storage pool operations.

</dd> <dt>

**IsPowerProtected**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this physical disk is equipped to tolerate a power loss without loss of data.

</dd> <dt>

**IsWriteCacheEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether write caching is enabled on this physical disk or not.

</dd> <dt>

**LogicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The logical sector size of the physical disk, in bytes. For example: a 4K native disk should report 4096, while a 512-byte emulated disk should report 512.

</dd> <dt>

**MediaType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The media type of the physical disk.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unspecified<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | HDD<br/>         |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | SSD<br/>         |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | SCM<br/>         |



 

</dd> <dt>

**OperationalDetails**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings providing further information on a given operational status.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of operational status values further explaining a given health status.

</dd> <dt>

**OtherCannotPoolReasonDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string containing the vendor-defined reason why this physical disk cannot be added to a concrete pool. This property must be **NULL** if the value of the **CannotPoolReason** property is not **Other**.

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A string representation of the physical disk's part number or SKU.

</dd> <dt>

**PhysicalLocation**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is a free-form string indicating where the hardware is located.

</dd> <dt>

**PhysicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The physical sector size of the physical disk, in bytes. For example: for 4K native and 512-byte emulated disks, the value of this property should be 4096.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

Total physical storage size of the disk, in bytes.

</dd> <dt>

**SlotNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of the enclosure slot in which the disk physically resides.

</dd> <dt>

**SoftwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A string representation of the software version number.

</dd> <dt>

**SpindleSpeed**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Units**](https://msdn.microsoft.com/library/aa393650) ("RPM")
</dt> </dl>

The rotational speed of spindle-based physical disks. For solid state devices (SSDs) or other non-rotational media, this member should be set to 0. For rotating media that has an unknown speed, this member should be set to 0xFFFFFFFF (**UINT32\_MAX**).

</dd> <dt>

**SupportedUsages**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array of values that specify the supported usages for this physical disk.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                         | The intended usage is not specified.<br/>                                                                                                                                                                                                                                |
| <span id="Auto-Select"></span><span id="auto-select"></span><span id="AUTO-SELECT"></span><dl> <dt>**Auto-Select**</dt> <dt>1</dt> </dl>         | This physical disk should only be used for data storage.<br/>                                                                                                                                                                                                            |
| <span id="Manual-Select"></span><span id="manual-select"></span><span id="MANUAL-SELECT"></span><dl> <dt>**Manual-Select**</dt> <dt>2</dt> </dl> | This physical disk should only be used if manually selected by an administrator at the time of virtual disk creation. A manual-select disk is selected using the *PhysicalDisksToUse* parameter to [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md).<br/> |
| <span id="Hot_Spare"></span><span id="hot_spare"></span><span id="HOT_SPARE"></span><dl> <dt>**Hot Spare**</dt> <dt>3</dt> </dl>                 | This physical disk should be used as a hot spare.<br/>                                                                                                                                                                                                                   |
| <span id="Retired"></span><span id="retired"></span><span id="RETIRED"></span><dl> <dt>**Retired**</dt> <dt>4</dt> </dl>                         | This physical disk should be retired from use. At a minimum, no new allocations should go to this disk. If the virtual disks that reside on this disk are repaired, the data should be moved to another active physical disk.<br/>                                       |
| <span id="Journal"></span><span id="journal"></span><span id="JOURNAL"></span><dl> <dt>**Journal**</dt> <dt>5</dt> </dl>                         | This physical disk should be used as a cache for other devices comprising a virtual disk. It will back a virtual disk s write-back cache, if configured.<br/>                                                                                                            |



 

</dd> <dt>

**UniqueIdFormat**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Indicates the type of identifier used in the *UniqueId* field (inherited from [**MSFT\_StorageObject**](msft-storageobject.md)). The identifier used in *UniqueId* must be the highest available identifier using the following order of preference: 8 (highest), 3, 2, 1, 0 (lowest). For example, if the physical disk device exposes identifiers of type 0, 1, and 3, *UniqueId* must be the identifier of type 3, and *UniqueIdFormat* should be set to 3.

<dl> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0)
</dt> <dt>

<span id="Vendor_Id"></span><span id="vendor_id"></span><span id="VENDOR_ID"></span>**Vendor Id** (1)
</dt> <dt>

<span id="EUI64"></span><span id="eui64"></span>**EUI64** (2)
</dt> <dt>

<span id="FCPH_Name"></span><span id="fcph_name"></span><span id="FCPH_NAME"></span>**FCPH Name** (3)
</dt> <dt>

<span id="SCSI_Name_String"></span><span id="scsi_name_string"></span><span id="SCSI_NAME_STRING"></span>**SCSI Name String** (8)
</dt> </dl>

</dd> <dt>

**Usage**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The intended usage of this physical disk within a concrete pool.

Storage pools are required to follow the assigned policy for a physical disk.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                         | The intended usage is not specified.<br/>                                                                                                                                                                                                                                |
| <span id="Auto-Select"></span><span id="auto-select"></span><span id="AUTO-SELECT"></span><dl> <dt>**Auto-Select**</dt> <dt>1</dt> </dl>         | This physical disk should only be used for data storage.<br/>                                                                                                                                                                                                            |
| <span id="Manual-Select"></span><span id="manual-select"></span><span id="MANUAL-SELECT"></span><dl> <dt>**Manual-Select**</dt> <dt>2</dt> </dl> | This physical disk should only be used if manually selected by an administrator at the time of virtual disk creation. A manual-select disk is selected using the *PhysicalDisksToUse* parameter to [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md).<br/> |
| <span id="Hot_Spare"></span><span id="hot_spare"></span><span id="HOT_SPARE"></span><dl> <dt>**Hot Spare**</dt> <dt>3</dt> </dl>                 | This physical disk should be used as a hot spare.<br/>                                                                                                                                                                                                                   |
| <span id="Retired"></span><span id="retired"></span><span id="RETIRED"></span><dl> <dt>**Retired**</dt> <dt>4</dt> </dl>                         | This physical disk should be retired from use. At a minimum, no new allocations should go to this disk. If the virtual disks that reside on this disk are repaired, the data should be moved to another active physical disk.<br/>                                       |
| <span id="Journal"></span><span id="journal"></span><span id="JOURNAL"></span><dl> <dt>**Journal**</dt> <dt>5</dt> </dl>                         | This physical disk should be used as a cache for other devices comprising a virtual disk. It will back a virtual disk s write-back cache, if configured.<br/>                                                                                                            |



 

</dd> <dt>

**VirtualDiskFootprint**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field indicates the size in bytes of the user data footprint from virtual disks on this physical disk.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





