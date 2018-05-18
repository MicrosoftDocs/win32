---
title: Maintenance method of the MSFT\_PhysicalDisk class
description: Allows a user to perform certain maintenance tasks on the physical disk while it is part of a concrete pool.
ms.assetid: '99730040-46E2-4886-A0FE-4C2D8980DC87'
keywords: ["Maintenance method Windows Storage Management API", "Maintenance method Windows Storage Management API , MSFT_PhysicalDisk class", "MSFT_PhysicalDisk class Windows Storage Management API , Maintenance method"]
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.Maintenance
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Maintenance method of the MSFT\_PhysicalDisk class

Allows a user to perform certain maintenance tasks on the physical disk while it is part of a concrete pool.

## Syntax


```mof
UInt32 Maintenance(
  [in]  Boolean EnableIndication,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*EnableIndication* \[in\]
</dt> <dd>

If **TRUE**, this instructs the physical disk to enable its indication LED. The indication LED should remain enabled until a second call to **Maintenance** is made with this parameter specified as **FALSE**.

This parameter is required and cannot be NULL.

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

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
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

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> </dl>

 

 





