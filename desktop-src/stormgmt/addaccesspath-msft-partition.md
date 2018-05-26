---
title: AddAccessPath method of the MSFT\_Partition class
description: Adds a mount path or drive letter assignment to the partition.
ms.assetid: d692d4f5-c912-48ec-98a6-9c72ac6e75f6
keywords:
- AddAccessPath method Windows Storage Management API
- AddAccessPath method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , AddAccessPath method
topic_type:
- apiref
api_name:
- MSFT_Partition.AddAccessPath
api_location:
- vds.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AddAccessPath method of the MSFT\_Partition class

Adds a mount path or drive letter assignment to the partition.

## Syntax


```mof
UInt32 AddAccessPath(
  [in]  String  AccessPath,
  [in]  Boolean AssignDriveLetter,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccessPath* \[in\]
</dt> <dd>

Specifies the access path, which is a user-mode path that can be used to open the partition. An access path can be a drive letter (for example, "C:" or "C:\\") or a path to an empty directory on an NTFS volume. The access path string does not require a trailing backslash.

</dd> <dt>

*AssignDriveLetter* \[in\]
</dt> <dd>

If **TRUE**, the next available drive letter will be assigned to the partition.

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

**The requested access path is already in use.** (42002)
</dt> <dt>

**Cannot assign access paths to hidden partitions.** (42004)
</dt> <dt>

**The access path is not valid.** (42007)
</dt> </dl>

## Remarks

This method adds a mount path or drive letter assignment to the partition. The *AccessPath* and *AssignDriveLetter* parameters are mutually exclusive, and will result in an Invalid Parameter error if both are specified at once. This method adds the access path by creating a mounted folder (also called a volume mount point). Note that mounted folders are supported only on NTFS formatted partitions. This method returns an error if the path specified in *AccessPath* is a folder that is already in use (even if the directory is empty) or if it contains a path to a non-empty directory.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| Header<br/>                   | <dl> <dt>Vds.h</dt> </dl>          |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Partition**](msft-partition.md)
</dt> </dl>

 

 





