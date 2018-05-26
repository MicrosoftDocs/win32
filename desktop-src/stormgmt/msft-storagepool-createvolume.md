---
title: CreateVolume method of the MSFT\_StoragePool class
description: Creates a virtual disk and single volume using the resources of the storage pool.
ms.assetid: 35FFE851-F9A4-43D6-BBB6-975836E79105
keywords:
- CreateVolume method Windows Storage Management API
- CreateVolume method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , CreateVolume method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.CreateVolume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateVolume method of the MSFT\_StoragePool class

Creates a virtual disk and single volume using the resources of the storage pool.

## Syntax


```mof
UInt32 CreateVolume(
  [in]  String              FriendlyName,
  [in]  UInt64              Size,
  [in]  String              StorageTiers[],
  [in]  UInt64              StorageTierSizes[],
  [in]  UInt16              ProvisioningType,
  [in]  String              ResiliencySettingName,
  [in]  UInt16              PhysicalDiskRedundancy,
  [in]  UInt16              NumberOfColumns,
  [in]  UInt16              FileSystem,
  [in]  String              AccessPath,
  [in]  String              FileServer,
  [out] String              CreatedVolume,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name of the volume. The friendly name should describe the volume. It need not be unique. The label of the file system will also be set to this name.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*Size* \[in\]
</dt> <dd>

The size of the virtual disk. Note that some storage subsystems will round the size up or down to a multiple of its allocation unit size. The size of the created volume will be as large as this virtual disk size allows.

</dd> <dt>

*StorageTiers* \[in\]
</dt> <dd>

The storage tiers on the virtual disk. Each array element is an [**MSFT\_StorageTier**](msft-storagetier.md) object.

</dd> <dt>

*StorageTierSizes* \[in\]
</dt> <dd>

The sizes of the tiers.

</dd> <dt>

*ProvisioningType* \[in\]
</dt> <dd>

The provisioning type of the volume.



| Value                                                                                                | Meaning                                                                                             |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Thin provisioning - the storage for the volume is allocated on-demand.<br/>                   |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Fixed provisioning - the storage for the volume is allocated when the volume is created.<br/> |



 

</dd> <dt>

*ResiliencySettingName* \[in\]
</dt> <dd>

The name of the resiliency setting to use as a template for this the volume. It is the same as the **Name** property of the resiliency setting instance. Only resiliency settings associated with this storage pool may be used.

</dd> <dt>

*PhysicalDiskRedundancy* \[in\]
</dt> <dd>

The number of physical disk failures that the virtual disk can withstand without data loss. If not specified, the value used is the **PhysicalDiskRedundancyDefault** member of the resiliency setting specified by *ResiliencySettingName*.

</dd> <dt>

*NumberOfColumns* \[in\]
</dt> <dd>

The number of physical disks to use to stripe the data. If not specified, the value used is the **NumberOfColumnsDefault** member of the resiliency setting specified by *ResiliencySettingName*.

</dd> <dt>

*FileSystem* \[in\]
</dt> <dd>

The type of file system to use on the created volume. A CSV file system is only supported on a storage spaces subsystem. For CSV the pool must be clusterable and the volume created will be a cluster shared volume.

This parameter is required and cannot be **NULL**.



| Value                                                                                                                                   | Meaning                |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| <span id="14"></span><dl> <dt>**14**</dt> </dl>                                  | NTFS<br/>        |
| <span id="15"></span><dl> <dt>**15**</dt> </dl>                                  | ReFS<br/>        |
| <span id="0x8000"></span><span id="0X8000"></span><dl> <dt>**0x8000**</dt> </dl> | CSVFS\_NTFS<br/> |
| <span id="0x8001"></span><span id="0X8001"></span><dl> <dt>**0x8001**</dt> </dl> | CSVFS\_ReFS<br/> |



 

</dd> <dt>

*AccessPath* \[in\]
</dt> <dd>

A local access path to the volume. If the access path could not be set, or this parameter is **NULL**, a new access path will be assigned.

</dd> <dt>

*FileServer* \[in\]
</dt> <dd>

**Starting in Windows 10:** A string that contains an embedded [**MSFT\_FileServer**](msft-fileserver.md) object, representing the file server that will own this volume.

</dd> <dt>

*CreatedVolume* \[out\]
</dt> <dd>

The created volume, a [**MSFT\_Volume**](msft-volume.md) object.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Returns a reference to the storage job object used to track the long-running operation.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

Extended error information in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Not enough free space** (40000)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**An unexpected I/O error has occurred.** (40004)
</dt> <dt>

**You must specify a size by using either the *Size* or the *UseMaximumSize* parameter. You can specify only one of these parameters at a time.** (40005)
</dt> <dt>

**The requested access path is already in use.** (42002)
</dt> <dt>

**The access path is not valid.** (42007)
</dt> <dt>

**The specified file system is not supported.** (43001)
</dt> <dt>

**The volume cannot be quick formatted.** (43002)
</dt> <dt>

**Cannot perform the requested operation when the drive is read only.** (43006)
</dt> <dt>

**You must specify a name for this volume.** (43017)
</dt> <dt>

**You must specify a file server to expose this volume to.** (43018)
</dt> <dt>

**The volume is not exposed to the specified file server.** (43019)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**Failover clustering could not be enabled for this storage object.** (46008)
</dt> <dt>

**This operation is not supported on primordial storage pools.** (48000)
</dt> <dt>

**The storage pool is reserved for special usage only.** (48001)
</dt> <dt>

**The specified resiliency setting is not supported by this storage pool.** (48002)
</dt> <dt>

**There are not enough physical disks in the storage pool to create the specified virtual disk configuration.** (48004)
</dt> <dt>

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> <dt>

**You must specify the size info (either the *Size* or *UseMaximumSize* parameter) or the tier info (the *StorageTiers* and *StorageTierSizes* parameters), but not both size info and tier info.** (48010)
</dt> <dt>

**No resiliency setting with that name exists.** (49000)
</dt> <dt>

**The value for *NoSinglePointOfFailure* is not supported.** (49001)
</dt> <dt>

**The value for *PhysicalDiskRedundancy* is outside of the supported range of values.** (49002)
</dt> <dt>

**The value for *NumberOfDataCopies* is outside of the supported range of values.** (49003)
</dt> <dt>

**The value for *ParityLayout* is outside of the supported range of values.** (49004)
</dt> <dt>

**The value for *Interleave* is outside of the supported range of values.** (49005)
</dt> <dt>

**The value for *NumberOfColumns* is outside of the supported range of values.** (49006)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





