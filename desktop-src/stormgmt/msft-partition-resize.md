---
title: Resize method of the MSFT\_Partition class
description: Resizes the partition and any associated file system volume to the size specified by the Size parameter.
ms.assetid: 89343280-F14E-47B2-A8F6-28F85B525804
keywords:
- Resize method Windows Storage Management API
- Resize method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , Resize method
topic_type:
- apiref
api_name:
- MSFT_Partition.Resize
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

# Resize method of the MSFT\_Partition class

Resizes the partition and any associated file system volume to the size specified by the *Size* parameter.

## Syntax


```mof
UInt32 Resize(
  [in]  UInt64 Size,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Size* \[in\]
</dt> <dd>

The new size for the disk. This parameter is required and cannot be zero.

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

**Size Not Supported** (4097)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot shrink a partition containing a volume with errors.** (42008)
</dt> <dt>

**Cannot resize a partition containing an unknown file system.** (42009)
</dt> </dl>

## Remarks

This method resizes the partition and any associated file system to the size specified by the *Size* parameter. If the size is outside the bounds returned by the [**GetSupportedSize**](msft-partition-getsupportedsizes.md) method, then this method will fail with a well-defined error code. The resize operation is supported only on NTFS-formatted partitions and RAW partitions.

If the specified size is smaller than the original size, this method will move files so that they are as close as possible to the beginning of the partition, to consolidate free space at the end of the partition. It then truncates the file system volume, reducing its size, and then truncates the partition.

In almost all cases, there will be some files that are immovable (that is, cannot be moved). For example, file system and storage driver metadata files are likely to be immovable. For this reason, the amount by which a partition can be shrunk is usually less than the total amount of free space on the partition.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Partition**](msft-partition.md)
</dt> </dl>

 

 





