---
title: MSFT\_Partition class
description: Represents a partition on a disk.
ms.assetid: d692d4f5-c912-48ec-98a6-9c72ac6e75f6
keywords:
- MSFT_Partition class Windows Storage Management API
- MSFT_Partition class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_Partition
- MSFT_Partition.DiskNumber
- MSFT_Partition.PartitionNumber
- MSFT_Partition.DriveLetter
- MSFT_Partition.AccessPaths
- MSFT_Partition.OperationalStatus
- MSFT_Partition.TransitionState
- MSFT_Partition.Size
- MSFT_Partition.MbrType
- MSFT_Partition.GptType
- MSFT_Partition.Guid
- MSFT_Partition.IsReadOnly
- MSFT_Partition.IsOffline
- MSFT_Partition.IsSystem
- MSFT_Partition.IsBoot
- MSFT_Partition.IsActive
- MSFT_Partition.IsHidden
- MSFT_Partition.IsShadowCopy
- MSFT_Partition.NoDefaultDriveLetter
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

# MSFT\_Partition class

Represents a partition on a disk.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_Partition : MSFT_StorageObject
{
  UInt32  DiskNumber;
  UInt32  PartitionNumber;
  Char16  DriveLetter;
  String  AccessPaths[];
  UInt16  OperationalStatus;
  UInt16  TransitionState;
  UInt64  Size;
  UInt16  MbrType;
  String  GptType;
  String  Guid;
  Boolean IsReadOnly;
  Boolean IsOffline;
  Boolean IsSystem;
  Boolean IsBoot;
  Boolean IsActive;
  Boolean IsHidden;
  Boolean IsShadowCopy;
  Boolean NoDefaultDriveLetter;
};
```

## Members

The **MSFT\_Partition** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Partition** class has these methods.



| Method                                                       | Description                                                                                                                                       |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddAccessPath**](addaccesspath-msft-partition.md)        | Adds a mount path or drive letter assignment to the partition.<br/>                                                                         |
| [**DeleteObject**](msft-partition-deleteobject.md)          | Deletes the partition and corresponding volume.<br/>                                                                                        |
| [**GetAccessPaths**](getaccesspaths-msft-partition.md)      | Retrieves all mount points and drive letters that can be used to access the partition.<br/>                                                 |
| [**GetSupportedSize**](msft-partition-getsupportedsizes.md) | Retrieves the minimum and maximum sizes that the partition can be resized to using the [**Resize**](msft-partition-resize.md) method.<br/> |
| [**Offline**](msft-partition-offline.md)                    | Takes the partition offline by dismounting the associated volume (if one exists).<br/>                                                      |
| [**Online**](msft-partition-online.md)                      | Brings the partition online by mounting the associated volume (if one exists).<br/>                                                         |
| [**RemoveAccessPath**](removeaccesspath-msft-partition.md)  | Remove an access path from the partition.<br/>                                                                                              |
| [**Resize**](msft-partition-resize.md)                      | Resizes the partition and any associated file system volume to the size specified by the *Size* parameter.<br/>                             |
| [**SetAttributes**](msft-partition-setattributes.md)        | Sets various attributes and properties of the partition.<br/>                                                                               |



 

### Properties

The **MSFT\_Partition** class has these properties.

<dl> <dt>

**AccessPaths**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings containing the various mount points for the partition. This list includes drive letters, in addition to mounted folders.

</dd> <dt>

**DiskNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence {"MSFT\_Disk.Number"}**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The operating system's number for the disk that contains this partition. Disk numbers may not necessarily remain the same across restarts.

</dd> <dt>

**DriveLetter**
</dt> <dd> <dl> <dt>

Data type: **Char16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The currently assigned drive letter for the partition. This property is **NULL** if no drive letter has been assigned.

</dd> <dt>

**GptType**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The partition's GPT type. This property is only valid when the disk's **PartitionStyle** property is **GPT** and will be **NULL** for all other partition styles.



| Value                                                                                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="System_Partition"></span><span id="system_partition"></span><span id="SYSTEM_PARTITION"></span><dl> <dt>**System Partition**</dt> <dt>c12a7328-f81f-11d2-ba4b-00a0c93ec93b</dt> </dl>         | An EFI system partition.<br/>                                                                                                                                                                                                                                                                                                                                                         |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>e3c9e316-0b5c-4db8-817d-f92df00215ae</dt> </dl> | A Microsoft reserved partition.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| <span id="Basic_data"></span><span id="basic_data"></span><span id="BASIC_DATA"></span><dl> <dt>**Basic data**</dt> <dt>ebd0a0a2-b9e5-4433-87c0-68b6b72699c7</dt> </dl>                                 | A basic data partition. This is the data partition type that is created and recognized by Windows.<br/> Only partitions of this type can be assigned drive letters, receive volume GUID paths, host mounted folders (also called volume mount points) and be enumerated by calls to [**FindFirstVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364425) and [**FindNextVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364431).<br/> |
| <span id="LDM_Metadata"></span><span id="ldm_metadata"></span><span id="LDM_METADATA"></span><dl> <dt>**LDM Metadata**</dt> <dt>5808c8aa-7e8f-42e0-85d2-e1e90434cfb3</dt> </dl>                         | A Logical Disk Manager (LDM) metadata partition on a dynamic disk.<br/>                                                                                                                                                                                                                                                                                                               |
| <span id="LDM_Data"></span><span id="ldm_data"></span><span id="LDM_DATA"></span><dl> <dt>**LDM Data**</dt> <dt>af9b60a0-1431-4f62-bc68-3311714a69ad</dt> </dl>                                         | The partition is an LDM data partition on a dynamic disk.<br/>                                                                                                                                                                                                                                                                                                                        |
| <span id="Microsoft_Recovery"></span><span id="microsoft_recovery"></span><span id="MICROSOFT_RECOVERY"></span><dl> <dt>**Microsoft Recovery**</dt> <dt>de94bba4-06d1-4d40-a16a-bfd50179d6ac</dt> </dl> | A Microsoft recovery partition.<br/>                                                                                                                                                                                                                                                                                                                                                  |



 

</dd> <dt>

**Guid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The partition's GPT GUID. This property is only valid when the disk's **PartitionStyle** property is **GPT** and will be **NULL** for all other partition styles.

</dd> <dt>

**IsActive**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the partition is active and can be used to start the system. This property is only valid when the disk's **PartitionStyle** property is **MBR** and will be **NULL** for all other partition styles.

</dd> <dt>

**IsBoot**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the partition is the current boot partition.

</dd> <dt>

**IsHidden**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the partition is not detected by the mount manager. As a result, the partition does not receive a drive letter, does not receive a volume GUID path, does not host volume mount points, and is not enumerated by calls to [**FindFirstVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364425) and [**FindNextVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364431). This ensures that applications such as Disk Defragmenter do not access the partition. The [Volume Shadow Copy Service (VSS)](https://msdn.microsoft.com/library/windows/desktop/bb968832) uses this attribute on its shadow copies.

</dd> <dt>

**IsOffline**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this partition is currently offline.

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this is a read-only partition.

</dd> <dt>

**IsShadowCopy**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the partition is a shadow copy of another partition. This attribute is used by VSS. This attribute is an indication for file system filter driver-based software (such as antivirus programs) to avoid attaching to the volume. An application can use this attribute to differentiate a shadow copy partition from a production partition. For example, an application that performs a fast recovery will break a shadow copy virtual disk by clearing the read-only and hidden attributes and this attribute. This attribute is set when the shadow copy is created and cleared when the shadow copy is broken.

</dd> <dt>

**IsSystem**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this is a system partition.

</dd> <dt>

**MbrType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The partition's MBR type. This property is only valid when the disk's **PartitionStyle** property is **MBR** and will be **NULL** for all other partition styles.

<dl> <dt>

<span id="FAT12"></span><span id="fat12"></span>**FAT12** (1)
</dt> <dt>

<span id="FAT16"></span><span id="fat16"></span>**FAT16** (4)
</dt> <dt>

<span id="Extended"></span><span id="extended"></span><span id="EXTENDED"></span>**Extended** (5)
</dt> <dt>

<span id="Huge"></span><span id="huge"></span><span id="HUGE"></span>**Huge** (6)
</dt> <dt>

<span id="IFS"></span><span id="ifs"></span>**IFS** (7)
</dt> <dt>

<span id="FAT32"></span><span id="fat32"></span>**FAT32** (12)
</dt> </dl>

</dd> <dt>

**NoDefaultDriveLetter**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the operating system does not assign a drive letter automatically when the partition is discovered. This is only honored for GPT disks and is assumed to be **FALSE** for MBR disks. This attribute is useful in storage area network (SAN) environments.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Values**](https://msdn.microsoft.com/library/aa393650) ( "Unknown", "Online", "No Media", "Failed", "Offline" ), [**ValueMap**](https://msdn.microsoft.com/library/aa393650) ( "0", "1", "3", "5", "4" )
</dt> </dl>

The operational status of the partition.

</dd> <dt>

**PartitionNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The operating system's number for the partition. Ordering is based on the partition's offset, relative to other partitions. This means that the value for this property may change based off of the partition configuration in the offset range preceding this partition.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total size of the partition, measured in bytes.

</dd> <dt>

**TransitionState**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The transition state of the partition. One of the following values.



| Value                                                                        | Meaning                                                                                 |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | This value is reserved for system use.<br/>                                       |
| <dl> <dt>1</dt> </dl> | The partition is stable. No configuration activity is currently in progress.<br/> |
| <dl> <dt>2</dt> </dl> | The partition is being extended.<br/>                                             |
| <dl> <dt>3</dt> </dl> | The partition is being shrunk. <br/>                                              |
| <dl> <dt>4</dt> </dl> | The partition is being automagically reconfigured.<br/>                           |
| <dl> <dt>8</dt> </dl> | The partition is being restriped.<br/>                                            |



 

</dd> </dl>

## Remarks

**Starting in Windows 10:** **MSFT\_Partition** derives from [**MSFT\_StorageObject**](msft-storageobject.md).

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





