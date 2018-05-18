---
title: CreatePartition method of the MSFT\_Disk class
description: Creates a partition on a disk.
ms.assetid: '4356352c-462e-4283-97e1-fcf7fe173b19'
keywords: ["CreatePartition method Windows Storage Management API", "CreatePartition method Windows Storage Management API , MSFT_Disk class", "MSFT_Disk class Windows Storage Management API , CreatePartition method"]
topic_type:
- apiref
api_name:
- MSFT_Disk.CreatePartition
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# CreatePartition method of the MSFT\_Disk class

Creates a partition on a disk.

## Syntax


```mof
UInt32 CreatePartition(
  [in]  UInt64  Size,
  [in]  Boolean UseMaximumSize,
  [in]  UInt64  Offset,
  [in]  UInt32  Alignment,
  [in]  Char16  DriveLetter,
  [in]  Boolean AssignDriveLetter,
  [in]  UInt16  MbrType,
  [in]  String  GptType,
  [in]  Boolean IsHidden,
  [in]  Boolean IsActive,
  [out] String  CreatedPartition,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Size* \[in\]
</dt> <dd>

The desired size, in bytes, for the partition. This must be equal to or less than the size specified by the disk's **LargestFreeExtent** property. This parameter cannot be used with *UseMaximumSize*.

</dd> <dt>

*UseMaximumSize* \[in\]
</dt> <dd>

If **TRUE**, the partition will fill the largest free extent on the disk. This parameter cannot be used with the *Size* parameter.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

The partition offset, in bytes. If the offset is not aligned and the *Alignment* parameter is not specified, the offset is rounded up or down to the closest alignment boundary, depending on the size of the disk on which the partition is created.

</dd> <dt>

*Alignment* \[in\]
</dt> <dd>

The alignment of the partition, in bytes.

</dd> <dt>

*DriveLetter* \[in\]
</dt> <dd>

The drive letter to be assigned to the partition at the time of creation. This parameter cannot be used with *AssignDriveLetter*. If both parameters are specified, an Invalid Parameter error will be returned. If the drive letter is not available, the partition will be created, but error '42002' will be returned.

</dd> <dt>

*AssignDriveLetter* \[in\]
</dt> <dd>

If **TRUE**, the next available drive letter will be assigned to the created partition. If no more drive letters are available, the partition will be created with no drive letter. This parameter cannot be used with *DriveLetter*. If both parameters are specified, an Invalid Parameter error will be returned.

</dd> <dt>

*MbrType* \[in\]
</dt> <dd>

Specifies the MBR partition type. This parameter can only be set if the disk's **PartitionStyle** property is **MBR**, otherwise an error will be returned. The default value of this parameter is **Huge**.



| Value                                                                                                                                                                                                                           | Meaning                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FAT12"></span><span id="fat12"></span><dl> <dt>**FAT12**</dt> <dt>1</dt> </dl>                                     | A FAT12 file system partition.<br/>                                                                                                               |
| <span id="FAT16"></span><span id="fat16"></span><dl> <dt>**FAT16**</dt> <dt>4</dt> </dl>                                     | A FAT16 file system partition.<br/>                                                                                                               |
| <span id="Extended"></span><span id="extended"></span><span id="EXTENDED"></span><dl> <dt>**Extended**</dt> <dt>5</dt> </dl> | An extended partition.<br/>                                                                                                                       |
| <span id="Huge"></span><span id="huge"></span><span id="HUGE"></span><dl> <dt>**Huge**</dt> <dt>6</dt> </dl>                 | A huge partition. This value indicates that there is no Windows file system on the partition. Use this value when creating a logical volume.<br/> |
| <span id="IFS"></span><span id="ifs"></span><dl> <dt>**IFS**</dt> <dt>7</dt> </dl>                                           | An NTFS or ExFAT partition.<br/>                                                                                                                  |
| <span id="FAT32"></span><span id="fat32"></span><dl> <dt>**FAT32**</dt> <dt>12</dt> </dl>                                    | A FAT32 partition.<br/>                                                                                                                           |



 

</dd> <dt>

*GptType* \[in\]
</dt> <dd>

The GPT type of the partition. This parameter is only valid if the disk's **PartitionStyle** property is **GPT**, otherwise an error will be returned. The default value for this parameter is **Basic data**.



| Value                                                                                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="System_Partition"></span><span id="system_partition"></span><span id="SYSTEM_PARTITION"></span><dl> <dt>**System Partition**</dt> <dt>c12a7328-f81f-11d2-ba4b-00a0c93ec93b</dt> </dl>         | An EFI system partition.<br/>                                                                                                                                                                                                                                                                                                                                                         |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>e3c9e316-0b5c-4db8-817d-f92df00215ae</dt> </dl> | A Microsoft reserved partition.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| <span id="Basic_data"></span><span id="basic_data"></span><span id="BASIC_DATA"></span><dl> <dt>**Basic data**</dt> <dt>ebd0a0a2-b9e5-4433-87c0-68b6b72699c7</dt> </dl>                                 | A basic data partition. This is the data partition type that is created and recognized by Windows.<br/> Only partitions of this type can be assigned drive letters, receive volume GUID paths, host mounted folders (also called volume mount points) and be enumerated by calls to [**FindFirstVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364425) and [**FindNextVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364431).<br/> |
| <span id="LDM_Metadata"></span><span id="ldm_metadata"></span><span id="LDM_METADATA"></span><dl> <dt>**LDM Metadata**</dt> <dt>5808c8aa-7e8f-42e0-85d2-e1e90434cfb3</dt> </dl>                         | A Logical Disk Manager (LDM) metadata partition on a dynamic disk.<br/>                                                                                                                                                                                                                                                                                                               |
| <span id="LDM_Data"></span><span id="ldm_data"></span><span id="LDM_DATA"></span><dl> <dt>**LDM Data**</dt> <dt>af9b60a0-1431-4f62-bc68-3311714a69ad</dt> </dl>                                         | The partition is an LDM data partition on a dynamic disk.<br/>                                                                                                                                                                                                                                                                                                                        |
| <span id="Microsoft_Recovery"></span><span id="microsoft_recovery"></span><span id="MICROSOFT_RECOVERY"></span><dl> <dt>**Microsoft Recovery**</dt> <dt>de94bba4-06d1-4d40-a16a-bfd50179d6ac</dt> </dl> | A Microsoft recovery partition.<br/>                                                                                                                                                                                                                                                                                                                                                  |



 

</dd> <dt>

*IsHidden* \[in\]
</dt> <dd>

If **TRUE**, the partition will not be able to receive a drive letter assignment, nor will the mount manager assign a volume GUID name. The partition will not be enumerated by the [**FindFirstVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364425) and [**FindNextVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364431) functions. The partition can be opened by its associated volume device name (for example, "\\\\?GLOBALROOT\\Device\\HarddiskVolumeX").

</dd> <dt>

*IsActive* \[in\]
</dt> <dd>

If **TRUE**, the partition's MBR active bit will be set, and the partition will become bootable. This parameter is only valid for MBR disks.

</dd> <dt>

*CreatedPartition* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_Partition**](msft-partition.md) object that represents the partition that was created.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Disk is in use** (6)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Not enough free space** (40000)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time.** (40005)
</dt> <dt>

**The disk has not been initialized.** (41000)
</dt> <dt>

**The disk is read only.** (41002)
</dt> <dt>

**The disk is offline.** (41003)
</dt> <dt>

**The disk's partition limit has been reached.** (41004)
</dt> <dt>

**The specified partition alignment is not valid. It must be a multiple of the disk's sector size.** (41005)
</dt> <dt>

**A parameter is not valid for this type of partition.** (41006)
</dt> <dt>

**The specified partition type is not valid.** (41010)
</dt> <dt>

**Only the first 2 TB are usable on MBR disks.** (41011)
</dt> <dt>

**The specified offset is not valid.** (41012)
</dt> <dt>

**There is no media in the device.** (41015)
</dt> <dt>

**The specified offset is not valid.** (41016)
</dt> <dt>

**The specified partition layout is invalid.** (41017)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
</dt> <dt>

**The requested access path is already in use.** (42002)
</dt> <dt>

**Cannot assign access paths to hidden partitions.** (42004)
</dt> <dt>

**The access path is not valid.** (42007)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](msft-disk.md)
</dt> </dl>

 

 





