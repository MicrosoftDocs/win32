---
title: Reset method of the MSFT\_PhysicalDisk class
description: Resets the health and operational status of the physical disk.
ms.assetid: 0330F04C-1FAE-40BA-8FFD-B4BEDB3B4D9C
keywords:
- Reset method Windows Storage Management API
- Reset method Windows Storage Management API , MSFT_PhysicalDisk class
- MSFT_PhysicalDisk class Windows Storage Management API , Reset method
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.Reset
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

# Reset method of the MSFT\_PhysicalDisk class

Resets the health and operational status of the physical disk.

## Syntax


```mof
UInt32 Reset(
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

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

## Remarks

The exact behavior of this method depends on whether this physical disk belongs to a concrete pool.

If it is a member of a concrete pool, the **HealthStatus** property should be set to **Healthy**, and the **OperationalStatus** property should be set to **OK**. If any additional errors are detected after **Reset**, the health and operational statuses should reflect these new errors.

If the physical disk is not a member of a concrete pool, then this method should not only reset the health and operational statuses, but it should return the disk into a state where it is usable as storage for a concrete pool. For example, if a physical disk is missing and then reappears (after it has been replaced), this physical disk is expected to be in the primordial pool only with an operational status indicating its data is either split or corrupt. Calling **Reset** should clear the physical disk of any data, remove any remaining ties to its former concrete pool, and return the disk to a healthy, usable state.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
</dt> </dl>

 

 





