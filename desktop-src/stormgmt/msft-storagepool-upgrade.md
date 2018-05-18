---
title: Upgrade method of the MSFT\_StoragePool class
description: Upgrades the metadata on the storage pool.
ms.assetid: 'FE6ADA25-70F4-49EF-AC2B-799AFCECFBBC'
keywords: ["Upgrade method Windows Storage Management API", "Upgrade method Windows Storage Management API , MSFT_StoragePool class", "MSFT_StoragePool class Windows Storage Management API , Upgrade method"]
topic_type:
- apiref
api_name:
- MSFT_StoragePool.Upgrade
api_location:
- netcfgn.h
api_type:
- COM
---

# Upgrade method of the MSFT\_StoragePool class

Upgrades the metadata on the storage pool. On Windows 8.1 or later, if a Windows 8 pool is present then this method can be used to upgrade the pool metadata so that it now becomes a Windows 8.1 pool and has new Windows 8.1 features (such as tiering) available.

## Syntax


```mof
UInt32 Upgrade(
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

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
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| Header<br/>                   | <dl> <dt>Netcfgn.h</dt> </dl>      |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





