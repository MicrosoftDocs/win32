---
title: MSFT\_Disk class
description: Represents a Windows disk.
ms.assetid: 'a3703b30-5e32-4bcf-9abd-fd3fb67fa6b6'
keywords: ["MSFT_Disk class Windows Storage Management API", "MSFT_Disk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_Disk
- MSFT_Disk.Path
- MSFT_Disk.Location
- MSFT_Disk.FriendlyName
- MSFT_Disk.UniqueId
- MSFT_Disk.UniqueIdFormat
- MSFT_Disk.Number
- MSFT_Disk.SerialNumber
- MSFT_Disk.FirmwareVersion
- MSFT_Disk.Manufacturer
- MSFT_Disk.Model
- MSFT_Disk.Size
- MSFT_Disk.AllocatedSize
- MSFT_Disk.LogicalSectorSize
- MSFT_Disk.PhysicalSectorSize
- MSFT_Disk.LargestFreeExtent
- MSFT_Disk.NumberOfPartitions
- MSFT_Disk.ProvisioningType
- MSFT_Disk.OperationalStatus
- MSFT_Disk.HealthStatus
- MSFT_Disk.BusType
- MSFT_Disk.PartitionStyle
- MSFT_Disk.Signature
- MSFT_Disk.Guid
- MSFT_Disk.IsOffline
- MSFT_Disk.OfflineReason
- MSFT_Disk.IsReadOnly
- MSFT_Disk.IsSystem
- MSFT_Disk.IsClustered
- MSFT_Disk.IsBoot
- MSFT_Disk.BootFromDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_Disk class

Represents a Windows disk.

A **MSFT\_Disk** object models the Windows operating system's concept of a disk device. The disk may be directly attached to the computer system, or it may be a virtual disk exposed to the system through the use of a Storage Management Provider.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_Disk : MSFT_StorageObject
{
  String  Path;
  String  Location;
  String  FriendlyName;
  String  UniqueId;
  UInt16  UniqueIdFormat;
  UInt32  Number;
  String  SerialNumber;
  String  FirmwareVersion;
  String  Manufacturer;
  String  Model;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt32  LogicalSectorSize;
  UInt32  PhysicalSectorSize;
  UInt64  LargestFreeExtent;
  UInt32  NumberOfPartitions;
  UInt16  ProvisioningType;
  UInt16  OperationalStatus;
  UInt16  HealthStatus;
  UInt16  BusType;
  UInt16  PartitionStyle;
  UInt32  Signature;
  String  Guid;
  Boolean IsOffline;
  UInt16  OfflineReason;
  Boolean IsReadOnly;
  Boolean IsSystem;
  Boolean IsClustered;
  Boolean IsBoot;
  Boolean BootFromDisk;
};
```

## Members

The **MSFT\_Disk** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Disk** class has these methods.



| Method                                               | Description                                                                                     |
|:-----------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Clear**](clear-msft-disk.md)                     | Removes partition information and uninitializes a disk, returning it to a RAW state.<br/> |
| [**ConvertStyle**](msft-disk-convertstyle.md)       | Converts the partition style of an already initialized disk.<br/>                         |
| [**CreatePartition**](createpartition-msft-disk.md) | Creates a partition on a disk.<br/>                                                       |
| [**Initialize**](initialize-msft-disk.md)           | Initializes a RAW disk with a particular partition style.<br/>                            |
| [**Offline**](msft-disk-offline.md)                 | Takes the disk offline.<br/>                                                              |
| [**Online**](msft-disk-online.md)                   | Brings the disk online.<br/>                                                              |
| [**Refresh**](msft-disk-refresh.md)                 | Refreshes the cached disk layout information.<br/>                                        |
| [**SetAttributes**](msft-disk-setattributes.md)     | Sets the disk's attributes and properties.<br/>                                           |



 

### Properties

The **MSFT\_Disk** class has these properties.

<dl> <dt>

**AllocatedSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

The amount of space, in bytes, that is currently used on the disk.

</dd> <dt>

**BootFromDisk**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the computer is configured to start from this disk. On computers with BIOS firmware, this is the first disk that the firmware detects during startup. On computers that use EFI firmware, this is the disk that contains the EFI System Partition (ESP). If there are no disks, or if there are multiple disks with an ESP partition, this property is not set for any disk.

</dd> <dt>

**BusType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The I/O bus type used by the disk.



| Value                                                                                                                                                                                                                                                                             | Meaning                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                       | The bus type is unknown.<br/>               |
| <span id="SCSI"></span><span id="scsi"></span><dl> <dt>**SCSI**</dt> <dt>1</dt> </dl>                                                                                          | SCSI<br/>                                   |
| <span id="ATAPI"></span><span id="atapi"></span><dl> <dt>**ATAPI**</dt> <dt>2</dt> </dl>                                                                                       | ATAPI<br/>                                  |
| <span id="ATA"></span><span id="ata"></span><dl> <dt>**ATA**</dt> <dt>3</dt> </dl>                                                                                             | ATA<br/>                                    |
| <span id="1394"></span><dl> <dt>**1394**</dt> <dt>4</dt> </dl>                                                                                                                 | IEEE 1394<br/>                              |
| <span id="SSA"></span><span id="ssa"></span><dl> <dt>**SSA**</dt> <dt>5</dt> </dl>                                                                                             | SSA<br/>                                    |
| <span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span><dl> <dt>**Fibre Channel**</dt> <dt>6</dt> </dl>                               | Fibre Channel<br/>                          |
| <span id="USB"></span><span id="usb"></span><dl> <dt>**USB**</dt> <dt>7</dt> </dl>                                                                                             | USB<br/>                                    |
| <span id="RAID"></span><span id="raid"></span><dl> <dt>**RAID**</dt> <dt>8</dt> </dl>                                                                                          | RAID<br/>                                   |
| <span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span><dl> <dt>**iSCSI**</dt> <dt>9</dt> </dl>                                                               | iSCSI<br/>                                  |
| <span id="SAS"></span><span id="sas"></span><dl> <dt>**SAS**</dt> <dt>10</dt> </dl>                                                                                            | Serial Attached SCSI (SAS)<br/>             |
| <span id="SATA"></span><span id="sata"></span><dl> <dt>**SATA**</dt> <dt>11</dt> </dl>                                                                                         | Serial ATA (SATA)<br/>                      |
| <span id="SD"></span><span id="sd"></span><dl> <dt>**SD**</dt> <dt>12</dt> </dl>                                                                                               | Secure Digital (SD)<br/>                    |
| <span id="MMC"></span><span id="mmc"></span><dl> <dt>**MMC**</dt> <dt>13</dt> </dl>                                                                                            | Multimedia Card (MMC)<br/>                  |
| <span id="Virtual"></span><span id="virtual"></span><span id="VIRTUAL"></span><dl> <dt>**Virtual**</dt> <dt>14</dt> </dl>                                                      | This value is reserved for system use.<br/> |
| <span id="File_Backed_Virtual_"></span><span id="file_backed_virtual_"></span><span id="FILE_BACKED_VIRTUAL_"></span><dl> <dt>**File Backed Virtual** </dt> <dt>15 </dt> </dl> | File-Backed Virtual<br/>                    |
| <span id="Storage_Spaces_"></span><span id="storage_spaces_"></span><span id="STORAGE_SPACES_"></span><dl> <dt>**Storage Spaces** </dt> <dt>16 </dt> </dl>                     | Storage spaces<br/>                         |
| <span id="NVMe"></span><span id="nvme"></span><span id="NVME"></span><dl> <dt>**NVMe**</dt> <dt>17 </dt> </dl>                                                                 | NVMe<br/>                                   |



 

</dd> <dt>

**FirmwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the disk's firmware version.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly, display-oriented string to identify the disk.

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **PartitionStyle** is GPT, this property contains the GUID for the disk. This property will be NULL for all other disk types.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the disk device.



| Value                                                                                                                                                                                                                               | Meaning                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span><dl> <dt>**Healthy**</dt> <dt>0</dt> </dl>         | The disk is functioning normally.<br/>                                                                                     |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span><dl> <dt>**Warning**</dt> <dt>1</dt> </dl>         | The disk is still functioning, but has detected errors or issues that require administrator intervention.<br/>             |
| <span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span><dl> <dt>**Unhealthy**</dt> <dt>2</dt> </dl> | The volume is not functioning, due to errors or failures. The volume needs immediate attention from an administrator.<br/> |



 

</dd> <dt>

**IsBoot**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the disk contains the boot partition.

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the disk is used in a clustered environment, or **FALSE** otherwise.

</dd> <dt>

**IsOffline**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the disk is offline, or **FALSE** otherwise.

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the disk is read-only, or **FALSE** if it is read/write.

</dd> <dt>

**IsSystem**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if this disk contains the system partition, or **FALSE** otherwise.

</dd> <dt>

**LargestFreeExtent**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

The largest contiguous block of free space on the disk. This is also the largest size of a partition that can be created on the disk.

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that contains the PnP location path of the disk. The format of this string depends on the bus type. If the bus type is SCSI, SAS, or PCI RAID, the format is *AdapterPnpLocationPath*\#*BusType*(P*PathId*T*TargetId*L*LunId*). If the bus type is IDE, ATA, PATA, or SATA, the format is *AdapterPnpLocationPath*\#*BusType*(C*PathId*T*TargetId*L*LunId*). See the following Remarks section for a table that lists the parts of this string.

> [!Note]  
> For Hyper-V and VHD images, this property is **NULL**, because the virtual controller does not return the location path.

 

For more information about this property, see the following Remarks section.

</dd> <dt>

**LogicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

The logical sector size of the disk, in bytes. For example, a 4K native disk will report 4096, while a 512 emulated disk will report 512.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the disk's hardware manufacturer.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the disk's model number.

</dd> <dt>

**Number**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operating system's number for the disk. Disk 0 is typically the boot device. Disk numbers may not necessarily remain the same across restarts.

</dd> <dt>

**NumberOfPartitions**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of partitions that have been created on the disk.

</dd> <dt>

**OfflineReason**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **IsOffline** is **TRUE**, this property contains the reason for the disk being offline.

One of the following values.



| Value                                                                                                                                                                                                                                                                                                           | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="Policy"></span><span id="policy"></span><span id="POLICY"></span><dl> <dt>**Policy**</dt> <dt>1</dt> </dl>                                                                                         | The user requested the disk to be offline.<br/>                       |
| <span id="Redundant_Path"></span><span id="redundant_path"></span><span id="REDUNDANT_PATH"></span><dl> <dt>**Redundant Path**</dt> <dt>2</dt> </dl>                                                         | The disk is used for multi-path I/O.<br/>                             |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span><dl> <dt>**Snapshot**</dt> <dt>3</dt> </dl>                                                                                 | The disk is a snapshot disk.<br/>                                     |
| <span id="Collision"></span><span id="collision"></span><span id="COLLISION"></span><dl> <dt>**Collision**</dt> <dt>4</dt> </dl>                                                                             | There was a signature or identifier collision with another disk.<br/> |
| <span id="Resource_Exhaustion"></span><span id="resource_exhaustion"></span><span id="RESOURCE_EXHAUSTION"></span><dl> <dt>**Resource Exhaustion**</dt> <dt>5</dt> </dl>                                     | There were insufficient resources to bring the disk online.<br/>      |
| <span id="Critical_Write_Failures"></span><span id="critical_write_failures"></span><span id="CRITICAL_WRITE_FAILURES"></span><dl> <dt>**Critical Write Failures**</dt> <dt>6</dt> </dl>                     | There were critical write failures on the disk.<br/>                  |
| <span id="Data_Integrity_Scan_Required"></span><span id="data_integrity_scan_required"></span><span id="DATA_INTEGRITY_SCAN_REQUIRED"></span><dl> <dt>**Data Integrity Scan Required**</dt> <dt>7</dt> </dl> | A data integrity scan is required.<br/>                               |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operational status of the disk device.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                              | The operational status is unknown.<br/>                                                                                                                                         |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                      | A vendor-specific *OperationalStatus* has been specified by setting the *OtherOperationalStatusDescription* property.<br/>                                                      |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                                       | The disk is responding to commands and is in a normal operating state.<br/>                                                                                                     |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                                          | The disk is responding to commands, but is not running in an optimal operating state.<br/>                                                                                      |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>4</dt> </dl>                                                                          | The disk is functioning, but needs attention. For example, the disk might be overloaded or overheated.<br/>                                                                     |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>5</dt> </dl>                                  | The disk is functioning, but a failure is likely to occur in the near future.<br/>                                                                                              |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                                      | An error has occurred.<br/>                                                                                                                                                     |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl>                      | A non-recoverable error has occurred.<br/>                                                                                                                                      |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>8</dt> </dl>                                                                          | The disk is in the process of starting.<br/>                                                                                                                                    |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>9</dt> </dl>                                                                          | The disk is in the process of stopping.<br/>                                                                                                                                    |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>10</dt> </dl>                                                                             | The disk was stopped or shut down in a clean and orderly fashion.<br/>                                                                                                          |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>11</dt> </dl>                                                                 | The disk is being configured, maintained, cleaned, or otherwise administered.<br/>                                                                                              |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>12</dt> </dl>                                                                 | The storage provider has knowledge of the disk, but has never been able to establish communication with it.<br/>                                                                |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>13</dt> </dl>                                 | The storage provider has knowledge of the disk and has contacted it successfully in the past, but the disk is currently unreachable.<br/>                                       |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>14</dt> </dl>                                                                             | Similar to **Stopped**, except that the disk stopped abruptly and may require configuration or maintenance.<br/>                                                                |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>15</dt> </dl>                                                                             | The disk is reachable, but it is inactive.<br/>                                                                                                                                 |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>16</dt> </dl> | This status value does not necessarily indicate trouble with the disk, but it does indicate that another device or connection that the disk depends on may need attention.<br/> |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>17</dt> </dl>                                                                     | The disk has completed an operation. This status value should be combined with OK, Error, or Degraded, depending on the outcome of the operation.<br/>                          |
| <span id="Online"></span><span id="online"></span><span id="ONLINE"></span><dl> <dt>**Online**</dt> <dt>0xD010</dt> </dl>                                                                             | In Windows-based storage subsystems, this indicates that the object is online.<br/>                                                                                             |
| <span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span><dl> <dt>**Not Ready**</dt> <dt>0xD011</dt> </dl>                                                                 | In Windows-based storage subsystems, this indicates that the object is not ready.<br/>                                                                                          |
| <span id="No_Media"></span><span id="no_media"></span><span id="NO_MEDIA"></span><dl> <dt>**No Media**</dt> <dt>0xD012</dt> </dl>                                                                     | In Windows-based storage subsystems, this indicates that the object has no media present.<br/>                                                                                  |
| <span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span><dl> <dt>**Offline**</dt> <dt>0xD013</dt> </dl>                                                                         | In Windows-based storage subsystems, this indicates that the object is offline.<br/>                                                                                            |
| <span id="Failed"></span><span id="failed"></span><span id="FAILED"></span><dl> <dt>**Failed**</dt> <dt>0xD014</dt> </dl>                                                                             | In Windows-based storage subsystems, this indicates that the object is in a failed state.<br/>                                                                                  |



 

</dd> <dt>

**PartitionStyle**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The partition style used by the disk.



| Value                                                                                                                                                                                                                       | Meaning                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl> | The partition style is unknown.<br/> |
| <span id="MBR"></span><span id="mbr"></span><dl> <dt>**MBR**</dt> <dt>1</dt> </dl>                                       | Master Boot Record (MBR)<br/>        |
| <span id="GPT_"></span><span id="gpt_"></span><dl> <dt>**GPT** </dt> <dt>2 </dt> </dl>                                   | GUID Partition Table (GPT)<br/>      |



 

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A path that can be used to open an operating system handle to the disk device.

</dd> <dt>

**PhysicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

The physical sector size of the disk, in bytes. For example, both 4K native disks and 512 emulated disks will report 4096.

</dd> <dt>

**ProvisioningType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The provisioning type of the disk device.



| Value                                                                                                                                                                                                                       | Meaning                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl> | The provisioning scheme is unspecified.<br/>            |
| <span id="Thin"></span><span id="thin"></span><span id="THIN"></span><dl> <dt>**Thin**</dt> <dt>1</dt> </dl>             | The storage for the disk is allocated on-demand.<br/>   |
| <span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span><dl> <dt>**Fixed**</dt> <dt>2 </dt> </dl>        | The storage is allocated when the disk is created.<br/> |



 

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the disk's serial number.

</dd> <dt>

**Signature**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the **PartitionStyle** is MBR, this property contains the MBR partition signature. This property will be NULL for all other disk types.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Total size of the disk, in bytes.

</dd> <dt>

**UniqueId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The disk identifier. This contains the VPD Page 0x83 information that uniquely identifies this disk. The following types are accepted (in order of precedence):

-   8 (SCSI Name String)
-   3 (FCPH Name)
-   2 (EUI64)
-   1 (Vendor Id)
-   0 (Vendor Specific)

If the disk is an exposed virtual disk, the **UniqueId** is used to map the association between the two objects.

</dd> <dt>

**UniqueIdFormat**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Values**](https://msdn.microsoft.com/library/aa393650) ( "Vendor Specific", "Vendor Id", "EUI64", "FCPH Name", "SCSI Name String" ), [**ValueMap**](https://msdn.microsoft.com/library/aa393650) ("0", "1", "2", "3", "8")
</dt> </dl>

The format of the disk identifier. This property contains the VPD Page 0x83 descriptor type that was used to set the **UniqueId** property.

</dd> </dl>

## Remarks

The following table lists the parts of the location path string used in the **Location** property.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Location path part</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>AdapterPnpLocationPath</em></td>
<td>The adapter's PnP location path. This is retrieved by calling the [<strong>SetupDiGetDeviceProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551963) function, passing &amp;DEVPKEY_Device_LocationPaths for the <em>PropertyKey</em> parameter.</td>
</tr>
<tr class="even">
<td><em>BusType</em></td>
<td>The bus type: ATA, RAID, SAS, or SCSI.
<blockquote>
[!Note]<br />
If the bus type is IDE, PATA, or SATA, it appears as ATA in the location path string. If it is PCI RAID, it appears as RAID.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><em>PathId</em></td>
<td>The number of the bus. This is the value of the <strong>PathId</strong> member of the [<strong>SCSI_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565299) structure that is returned by the [<strong>IOCTL_SCSI_GET_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560500) control code.</td>
</tr>
<tr class="even">
<td><em>TargetId</em></td>
<td>The number of the target device. This is the value of the <strong>TargetId</strong> member of the [<strong>SCSI_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565299) structure that is returned by the [<strong>IOCTL_SCSI_GET_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560500) control code.</td>
</tr>
<tr class="odd">
<td><em>LunId</em></td>
<td>The number of the LUN. This is the value of the <strong>Lun</strong> member of the [<strong>SCSI_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565299) structure that is returned by the [<strong>IOCTL_SCSI_GET_ADDRESS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560500) control code.</td>
</tr>
</tbody>
</table>



 

The following table contains examples of location paths.



| Bus type | Example location path                                        |
|----------|--------------------------------------------------------------|
| ATA      | PCIROOT(0)\#PCI(0100)\#ATA(C01T03L00)                        |
| RAID     | PCIROOT(0)\#PCI(0200)\#PCI(0003)\#PCI(0100)\#RAID(P02T00L00) |
| SAS      | PCIROOT(1)\#PCI(0300)\#SAS(P00T03L00)                        |
| SCSI     | PCIROOT(0)\#PCI(1C00)\#PCI(0000)\#SCSI(P00T01L01)            |



 

**Starting in Windows 10:** **MSFT\_Disk** derives from [**MSFT\_StorageObject**](msft-storageobject.md). It now inherits the property *ObjectId*, which was formerly a property of **MSFT\_Disk**.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





