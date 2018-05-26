---
title: Clear method of the MSFT\_Disk class
description: Removes partition information and uninitializes a disk, returning it to a RAW state.
ms.assetid: a3703b30-5e32-4bcf-9abd-fd3fb67fa6b6
keywords:
- Clear method Windows Storage Management API
- Clear method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , Clear method
topic_type:
- apiref
api_name:
- MSFT_Disk.Clear
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

# Clear method of the MSFT\_Disk class

Removes partition information and uninitializes a disk, returning it to a RAW state.

## Syntax


```mof
UInt32 Clear(
  [in]  Boolean RemoveData,
  [in]  Boolean RemoveOEM,
  [in]  Boolean ZeroOutEntireDisk,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*RemoveData* \[in\]
</dt> <dd>

**TRUE** if it is okay to remove data partitions from the disk. If this parameter is **FALSE** or **NULL**, this method will fail in the presence of a data partition.

</dd> <dt>

*RemoveOEM* \[in\]
</dt> <dd>

**TRUE** if it is okay to remove OEM and other special partitions. If this parameter is **FALSE** or not specified, this method will fail in the presence of these types of partitions.

</dd> <dt>

*ZeroOutEntireDisk* \[in\]
</dt> <dd>

**TRUE** if this parameter instructs this method to zero out the entire disk in addition to removing all partition information. If this parameter is **FALSE** or **NULL**, only the first and last megabytes of the disk are zeroed.

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

**Disk is in use** (6)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**The disk has not been initialized.** (41000)
</dt> <dt>

**The disk is read only.** (41002)
</dt> <dt>

**The disk is offline.** (41003)
</dt> <dt>

**Cannot clear with OEM partitions present. To clear OEM partitions, use the RemoveOEM flag.** (41007)
</dt> <dt>

**Cannot clear with data partitions present. To clear data partitions, use the RemoveData flag.** (41008)
</dt> <dt>

**Operation not supported on a critical disk.** (41009)
</dt> <dt>

**There is no media in the device.** (41015)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be removed from the cluster to perform this operation.** (41019)
</dt> </dl>

## Remarks

The caller must specify *RemoveData*, *RemoveOEM*, or both, unless it first deletes all data partitions, known OEM partitions, and ESP partitions on the disk. This requirement excludes metadata partitions such as the MSR, the LDM metadata partition, and unknown OEM partitions.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](msft-disk.md)
</dt> </dl>

 

 





