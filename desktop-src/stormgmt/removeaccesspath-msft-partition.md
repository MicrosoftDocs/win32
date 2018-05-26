---
title: RemoveAccessPath method of the MSFT\_Partition class
description: Remove the access path from the partition.
ms.assetid: 0238bfe6-2e36-44e2-81ee-04bfa159ef47
keywords:
- RemoveAccessPath method Windows Storage Management API
- RemoveAccessPath method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , RemoveAccessPath method
topic_type:
- apiref
api_name:
- MSFT_Partition.RemoveAccessPath
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

# RemoveAccessPath method of the MSFT\_Partition class

Remove the access path from the partition.

## Syntax


```mof
UInt32 RemoveAccessPath(
  [in]  String AccessPath,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccessPath* \[in\]
</dt> <dd>

Specifies the access path, which is a user-mode path that can be used to open the partition. An access path can be a drive letter (for example, "C:" or "C:\\") or a path to an empty directory on an NTFS volume. The access path string does not require a trailing backslash.

This parameter is required and cannot be **NULL**.

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

**Cannot remove a volume GUID path.** (42005)
</dt> <dt>

**Cannot remove the drive letter of a boot or paging file partition.** (42006)
</dt> <dt>

**The access path is not valid.** (42007)
</dt> </dl>

## Remarks

This method removes the access path from the partition even if the access path is in use.

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

 

 





