---
title: GetSupportedSizeRange method of the MSISCSITARGET\_StoragePool class
description: Retrieves the supported size range for pools that support a range of sizes for volume or pool creation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 70a44635-b58c-4e36-9e31-dc2f5499a9be
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedSizeRange method iSCSI Software Target API
- GetSupportedSizeRange method iSCSI Software Target API , MSISCSITARGET_StoragePool class
- MSISCSITARGET_StoragePool class iSCSI Software Target API , GetSupportedSizeRange method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StoragePool.GetSupportedSizeRange
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedSizeRange method of the MSISCSITARGET\_StoragePool class

Retrieves the supported size range for pools that support a range of sizes for volume or pool creation. The retrieved sizes might change after this method returns due to requests from other clients.

Different implementations might support either or both the [**GetSupportedSizes**](getsupportedsizes-msiscsitarget-storagepool.md) and **GetSupportedSizeRange** methods, depending on pool configuration.

## Syntax


```mof
uint32 GetSupportedSizeRange(
  [in]  uint16                 ElementType,
  [in]  CIM_StorageSetting REF Goal,
  [out] uint64                 MinimumVolumeSize,
  [out] uint64                 MaximumVolumeSize,
  [out] uint64                 VolumeSizeDivisor
);
```



## Parameters

<dl> <dt>

*ElementType* \[in\]
</dt> <dd>

Specifies the requested element type.

<dt>

<span id="Storage_Pool"></span><span id="storage_pool"></span><span id="STORAGE_POOL"></span>

**Storage Pool** (2)


</dt> <dd></dd> <dt>

<span id="Storage_Volume"></span><span id="storage_volume"></span><span id="STORAGE_VOLUME"></span>

**Storage Volume** (3)


</dt> <dd></dd> <dt>

<span id="Logical_Disk"></span><span id="logical_disk"></span><span id="LOGICAL_DISK"></span>

**Logical Disk** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*Goal* \[in\]
</dt> <dd>

Specifies the [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance that describes the requested element type.

</dd> <dt>

*MinimumVolumeSize* \[out\]
</dt> <dd>

On return, indicates the minimum size for a requested element in bytes.

</dd> <dt>

*MaximumVolumeSize* \[out\]
</dt> <dd>

On return, indicates the maximum size for a requested element in bytes.

</dd> <dt>

*VolumeSizeDivisor* \[out\]
</dt> <dd>

On return, indicates the size in bytes of an incremental unit of element size. The size of a volume or pool must be an even multiple of this value.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Use GetSupportedSizes instead** (2)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> </dl>

 

 





