---
title: GetSupportedSize method of the MSFT\_Partition class
description: Retrieves the minimum and maximum sizes that the partition can be resized to using the Resize method.
ms.assetid: 8BE1F2BF-AFA8-4AC3-BFB0-54723F605E95
keywords:
- GetSupportedSize method Windows Storage Management API
- GetSupportedSize method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , GetSupportedSize method
topic_type:
- apiref
api_name:
- MSFT_Partition.GetSupportedSize
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

# GetSupportedSize method of the MSFT\_Partition class

Retrieves the minimum and maximum sizes that the partition can be resized to using the [**Resize**](msft-partition-resize.md) method.

## Syntax


```mof
UInt32 GetSupportedSize(
  [out] UInt64 SizeMin,
  [out] UInt64 SizeMax,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*SizeMin* \[out\]
</dt> <dd>

The minimum size that this partition can become, in bytes. If this method is run multiple times, this value can change slightly depending on the placement of various temporary files.

</dd> <dt>

*SizeMax* \[out\]
</dt> <dd>

The maximum partition size that this partition can become, in bytes.

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

The minimum size is determined by Disk Defragmenter and takes into account the location of immovable files (that is, files that cannot be moved). The maximum size is determined by adding the size of any free extents immediately after the current partition.

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

 

 





