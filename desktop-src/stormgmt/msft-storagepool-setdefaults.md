---
title: SetDefaults method of the MSFT\_StoragePool class
description: Sets or changes the default values for properties of the storage pool object.
ms.assetid: F9435AA1-B102-4628-B664-251D35AD40F1
keywords:
- SetDefaults method Windows Storage Management API
- SetDefaults method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetDefaults method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetDefaults
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDefaults method of the MSFT\_StoragePool class

Sets or changes the default values for properties of the storage pool object.

Note that not all parameters must be specified, and only those that are specified will be updated.

## Syntax


```mof
UInt32 SetDefaults(
  [in]  UInt16  ProvisioningTypeDefault,
  [in]  String  ResiliencySettingNameDefault,
  [in]  Boolean EnclosureAwareDefault,
  [in]  UInt64  WriteCacheSizeDefault,
  [in]  Boolean AutoWriteCacheSize,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ProvisioningTypeDefault* \[in\]
</dt> <dd>

The default provisioning type for virtual disks in the storage pool.



| Value                                                                                                                                                                                                               | Meaning                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <span id="Thin"></span><span id="thin"></span><span id="THIN"></span><dl> <dt>**Thin**</dt> <dt>1</dt> </dl>     | Storage for the virtual disk is allocated on demand.<br/>                            |
| <span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span><dl> <dt>**Fixed**</dt> <dt>2</dt> </dl> | Storage for the virtual disk is allocated at the time of virtual disk creation.<br/> |



 

</dd> <dt>

*ResiliencySettingNameDefault* \[in\]
</dt> <dd>

The new default resiliency setting for the storage pool. The resiliency setting specified must already be associated with this storage pool.

</dd> <dt>

*EnclosureAwareDefault* \[in\]
</dt> <dd>

**TRUE** if the storage pool is enclosure aware by default. This parameter determines the default allocation policy for virtual disks created in an enclosure aware storage pool. For example, an enclosure aware subsystem could balance each data copy of the virtual disk across multiple physical enclosures such that each enclosure contains a full data copy of the virtual disk.

</dd> <dt>

*WriteCacheSizeDefault* \[in\]
</dt> <dd>

The new default size of the write cache for virtual disk creation.

</dd> <dt>

*AutoWriteCacheSize* \[in\]
</dt> <dd>

**TRUE** if the provider should pick up the auto write cache size; otherwise, **FALSE**.

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

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**This operation is not supported on primordial storage pools.** (48000)
</dt> <dt>

**The specified resiliency setting is not supported by this storage pool.** (48002)
</dt> <dt>

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> <dt>

**No resiliency setting with that name exists.** (49000)
</dt> <dt>

**The value for WriteCacheSize is outside of the supported range of values.** (50005)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





