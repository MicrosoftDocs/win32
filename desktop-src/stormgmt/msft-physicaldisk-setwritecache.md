---
title: SetWriteCache method of the MSFT\_PhysicalDisk class
description: Allows the physical disk's write cache to be enabled or disabled.
ms.assetid: '1DBA8B0E-0C31-471C-B90B-89C1B07CF7F3'
keywords: ["SetWriteCache method Windows Storage Management API", "SetWriteCache method Windows Storage Management API , MSFT_PhysicalDisk class", "MSFT_PhysicalDisk class Windows Storage Management API , SetWriteCache method"]
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.SetWriteCache
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetWriteCache method of the MSFT\_PhysicalDisk class

Allows the physical disk's write cache to be enabled or disabled.

## Syntax


```mof
UInt32 SetWriteCache(
  [in]  Boolean WriteCacheEnabled,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*WriteCacheEnabled* \[in\]
</dt> <dd>

Specifies whether the physical disk's write cache should be enabled or disabled.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

Contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

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

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> </dl>

 

 





