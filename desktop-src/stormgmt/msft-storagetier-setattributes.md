---
title: SetAttributes method of the MSFT\_StorageTier class
description: Updates or sets various attributes on the storage tier.
ms.assetid: C949619B-0197-45C0-B3A1-9E7ECCE6D272
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StorageTier class
- MSFT_StorageTier class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StorageTier.SetAttributes
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

# SetAttributes method of the MSFT\_StorageTier class

Updates or sets various attributes on the storage tier. Note that not all parameters need be specified, and only those given will be updated.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  UInt16 MediaType,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*MediaType* \[in\]
</dt> <dd>

The media type of the storage tier.



| Value                                                                                                | Meaning        |
|------------------------------------------------------------------------------------------------------|----------------|
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | HDD<br/> |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | SSD<br/> |



 

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

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
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

 

 





