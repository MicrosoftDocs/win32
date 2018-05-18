---
title: GetSupportedSize method of the MSFT\_StoragePool class
description: Retrieves the supported virtual disk sizes that can be created in the storage pool.
ms.assetid: 'C993C168-910B-4151-9B24-7A72807939F0'
keywords: ["GetSupportedSize method Windows Storage Management API", "GetSupportedSize method Windows Storage Management API , MSFT_StoragePool class", "MSFT_StoragePool class Windows Storage Management API , GetSupportedSize method"]
topic_type:
- apiref
api_name:
- MSFT_StoragePool.GetSupportedSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetSupportedSize method of the MSFT\_StoragePool class

Retrieves the supported virtual disk sizes that can be created in the storage pool.

These sizes can be returned in either or both of the following ways:

-   As an array of all supported sizes in the *SupportedSizes* parameter.
-   As a range defined by the *VirtualDiskSizeMin*, *VirtualDiskSizeMax*, and *VirtualDiskSizeDivisor* parameters.

## Syntax


```mof
UInt32 GetSupportedSize(
  [in]  String ResiliencySettingName,
  [out] UInt64 SupportedSizes[],
  [out] UInt64 VirtualDiskSizeMin,
  [out] UInt64 VirtualDiskSizeMax,
  [out] UInt64 VirtualDiskSizeDivisor,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ResiliencySettingName* \[in\]
</dt> <dd>

The name of the resiliency setting that should be used when determining the supported sizes. Note that the sizes returned may be different depending on the resiliency setting.

</dd> <dt>

*SupportedSizes* \[out\]
</dt> <dd>

An array of all of the supported sizes, in bytes, that are supported by the storage pool. This parameter can be **NULL** if the number of supported sizes is large, but is useful for storage pools that only support a select number of virtual disk sizes.

</dd> <dt>

*VirtualDiskSizeMin* \[out\]
</dt> <dd>

The minimum virtual disk size, in bytes, for a virtual disk created in the storage pool.

</dd> <dt>

*VirtualDiskSizeMax* \[out\]
</dt> <dd>

The maximum virtual disk size, in bytes, for a virtual disk created in the storage pool.

</dd> <dt>

*VirtualDiskSizeDivisor* \[out\]
</dt> <dd>

Specifies the multiplier that must be used when determining a virtual disk size. Any size specified in a creation or modification operation must be a multiple of this value.

For example: If the minimum supported size is 10 GB, and this parameter is 2 GB, the supported sizes for this pool would be 10 GB, 12 GB, 14 GB, and so on, until the maximum supported size is reached.

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

**Cache out of date** (40003)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> </dl>

## Remarks

The values that this method returns should reflect the current state of the storage pool and its available storage capacity. All values returned in *SupportedSizes* must be multiples of *VirtualDiskSizeDivisor*.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





