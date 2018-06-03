---
title: GetSupportedSize method of the MSFT\_StorageTier class
description: Returns the supported sizes for a new storage tier.
ms.assetid: 6D88653E-0F32-42A3-9B14-7E13CBABE1D7
keywords:
- GetSupportedSize method Windows Storage Management API
- GetSupportedSize method Windows Storage Management API , MSFT_StorageTier class
- MSFT_StorageTier class Windows Storage Management API , GetSupportedSize method
topic_type:
- apiref
api_name:
- MSFT_StorageTier.GetSupportedSize
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

# GetSupportedSize method of the MSFT\_StorageTier class

Returns the supported sizes for a new storage tier. These sizes can be returned in one or both of the following ways: in an array of all supported sizes; or through a minimum, increment, and maximum.

## Syntax


```mof
UInt32 GetSupportedSize(
  [in]  String ResiliencySettingName,
  [out] UInt64 SupportedSizes[],
  [out] UInt64 TierSizeMin,
  [out] UInt64 TierSizeMax,
  [out] UInt64 TierSizeDivisor,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ResiliencySettingName* \[in\]
</dt> <dd>

The name of the resiliency setting to use to determine the supported sizes. Note that the sizes returned may vary depending on the resiliency setting.

</dd> <dt>

*SupportedSizes* \[out\]
</dt> <dd>

The supported sizes for the storage tier, one size per array element. This parameter may be NULL if the number of supported sizes is large, but is useful for storage tiers that only support a small number of tier sizes.

</dd> <dt>

*TierSizeMin* \[out\]
</dt> <dd>

The minimum supported size of a sequence of sizes specified by the minimum, increment and maximum.

</dd> <dt>

*TierSizeMax* \[out\]
</dt> <dd>

The maximum supported size of a sequence of sizes specified by the minimum, increment and maximum.

</dd> <dt>

*TierSizeDivisor* \[out\]
</dt> <dd>

The increment, in bytes, between support sizes. For example: if the minimum supported size is 10 GB, the maximum is 20 GB, and this parameter is 2 GB, then the supported sizes for this pool would be 10 GB, 12 GB, 14 GB, 16 GB, 18 GB, and 20 GB.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

Extended error information from the storage provider in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

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

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageTier**](msft-storagetier.md)
</dt> </dl>

 

 





