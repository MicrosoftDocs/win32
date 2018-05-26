---
title: SetAttributes method of the MSFT\_StoragePool class
description: Sets or changes attribute values for the storage pool object.
ms.assetid: 01D081C7-349A-4344-AF11-123872887AE4
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetAttributes
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

# SetAttributes method of the MSFT\_StoragePool class

Sets or changes attribute values for the storage pool object.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsReadOnly,
  [in]  Boolean ClearOnDeallocate,
  [in]  Boolean IsPowerProtected,
  [in]  UInt16  RepairPolicy,
  [in]  UInt16  RetireMissingPhysicalDisks,
  [in]  UInt16  ThinProvisioningAlertThresholds[],
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*IsReadOnly* \[in\]
</dt> <dd>

Indicates whether or not the storage pool's configuration is read only. If **TRUE**, the storage pool will not allow modification to its properties or any of its associated elements.

</dd> <dt>

*ClearOnDeallocate* \[in\]
</dt> <dd>

If **TRUE**, physical disks should be zeroed (cleared of all data) when unmapped or removed from the storage pool. If **FALSE**, the behavior is subsystem defined.

</dd> <dt>

*IsPowerProtected* \[in\]
</dt> <dd>

If **TRUE**, the disks in this pool are able to tolerate power loss without data loss. For example, they automatically flush volatile buffers to non-volatile media after external power is disconnected.

</dd> <dt>

*RepairPolicy* \[in\]
</dt> <dd>

How the operating system repairs virtual disks for this storage pool.



| Value                                                                                                | Meaning                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Sequential - processes one allocation slab at a time. Repairs take longer, but with less impact on the I/O load.<br/>                            |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Parallel - processes as many allocation slabs as it can in parallel. Repair time is minimized, but with significant impact on the I/O load.<br/> |



 

</dd> <dt>

*RetireMissingPhysicalDisks* \[in\]
</dt> <dd>

Specifies whether the storage subsystem will automatically retire physical disks that are missing from this storage pool and replace them with hot spares or other physical disks that are available in the storage pool.

<dl> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>**Auto** (1)
</dt> <dt>

<span id="Always"></span><span id="always"></span><span id="ALWAYS"></span>**Always** (2)
</dt> <dt>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>**Never** (3)
</dt> </dl> </dd> <dt>

*ThinProvisioningAlertThresholds* \[in\]
</dt> <dd>

An array of percentage values that represent various sparse (thin provisioning) thresholds. The minimum value for each value is 1; the maximum value is 100. When the virtual disk space usage crosses one of these thresholds, a notification will be broadcasted to all subscribed clients.

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

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> <dt>

**The number of thin provisioning alert thresholds specified exceeds the limit for this storage pool.** (48009)
</dt> </dl>

## Remarks

Not all parameters must be specified, and only those that are specified will be updated.

When you set the **IsReadOnly** property to **TRUE**, it must be set alone and must be the last attribute set.

If you want to set the **IsReadOnly**, **ClearOnDeallocate**, and **IsPowerProtected** properties:

1.  Call this method and specify appropriate values for the *ClearOnDeallocate* and *IsPowerProtected* parameter and **FALSE** for the *IsReadOnly* parameter.
2.  If the **IsReadOnly** property should be **TRUE**, call this method again and specify **TRUE** for the *IsReadOnly* parameter.

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

 

 





