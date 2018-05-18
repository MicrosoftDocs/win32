---
title: SetUsage method of the MSFT\_PhysicalDisk class
description: Set or changes the intended usage for the physical disk within a concrete pool.
ms.assetid: 'E35C3D17-73E1-4319-A993-30BCE01B9B87'
keywords: ["SetUsage method Windows Storage Management API", "SetUsage method Windows Storage Management API , MSFT_PhysicalDisk class", "MSFT_PhysicalDisk class Windows Storage Management API , SetUsage method"]
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.SetUsage
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetUsage method of the MSFT\_PhysicalDisk class

Set or changes the intended usage for the physical disk within a concrete pool.

Storage pools are required to follow the assigned policy for a physical disk.

## Syntax


```mof
UInt32 SetUsage(
  [in]  UInt16 Usage,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Usage* \[in\]
</dt> <dd>

The intended usage for the physical disk. This parameter is required and cannot be NULL.



| Value                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Data_Store"></span><span id="data_store"></span><span id="DATA_STORE"></span><dl> <dt>**Data Store**</dt> <dt>1</dt> </dl>             | This physical disk should only be used for data storage.<br/>                                                                                                                                                                                                                       |
| <span id="Manual-Select"></span><span id="manual-select"></span><span id="MANUAL-SELECT"></span><dl> <dt>**Manual-Select**</dt> <dt>2</dt> </dl> | This physical disk should only be used if manually selected by an administrator at the time of virtual disk creation. A manual-select disk is selected using the *PhysicalDisksToUse* parameter of the [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method.<br/> |
| <span id="Hot_Spare"></span><span id="hot_spare"></span><span id="HOT_SPARE"></span><dl> <dt>**Hot Spare**</dt> <dt>3</dt> </dl>                 | This physical disk should be used as a hot spare.<br/>                                                                                                                                                                                                                              |
| <span id="Retired"></span><span id="retired"></span><span id="RETIRED"></span><dl> <dt>**Retired**</dt> <dt>4</dt> </dl>                         | This physical disk should be retired from use. At a minimum, no new allocations should go to this disk. If the virtual disks that reside on this disk are repaired, the data should be moved to another active physical disk.<br/>                                                  |
| <span id="Journal"></span><span id="journal"></span><span id="JOURNAL"></span><dl> <dt>**Journal**</dt> <dt>5</dt> </dl>                         | This physical disk should be used as a cache for other devices comprising a virtual disk. It will back a virtual disk’s write-back cache, if configured.<br/>                                                                                                                       |



 

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

 

 





