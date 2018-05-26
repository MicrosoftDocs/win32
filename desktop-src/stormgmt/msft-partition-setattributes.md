---
title: SetAttributes method of the MSFT\_Partition class
description: Sets various attributes and properties of the partition.
ms.assetid: 203396F7-2F2B-4121-B415-21BFE036074F
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_Partition.SetAttributes
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

# SetAttributes method of the MSFT\_Partition class

Sets various attributes and properties of the partition.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsReadOnly,
  [in]  Boolean NoDefaultDriveLetter,
  [in]  Boolean IsActive,
  [in]  Boolean IsHidden,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*IsReadOnly* \[in\]
</dt> <dd>

If **TRUE**, the partition will be made read-only. If **FALSE**, the partition will be made writable.

</dd> <dt>

*NoDefaultDriveLetter* \[in\]
</dt> <dd>

If **TRUE**, the operating system does not assign a drive letter automatically when the partition is discovered. This is only honored for GPT disks and is assumed to be **FALSE** for MBR disks. This attribute is useful in storage area network (SAN) environments.

</dd> <dt>

*IsActive* \[in\]
</dt> <dd>

**TRUE** if the partition is an MBR partition that is active and can be used to start the system. This parameter is only relevant for MBR disks.

</dd> <dt>

*IsHidden* \[in\]
</dt> <dd>

**TRUE** if the partition is not detected by the mount manager. As a result, the partition does not receive a drive letter, does not receive a volume GUID path, does not host volume mount points, and is not enumerated by calls to [**FindFirstVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364425) and [**FindNextVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364431). This ensures that applications such as disk defragmenter do not access the partition. The Volume Shadow Copy Service (VSS) uses this attribute on its shadow copies.

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

**In Use** (6)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**The disk has not been initialized.** (41000)
</dt> <dt>

**The disk is offline.** (41003)
</dt> <dt>

**A parameter is not valid for this type of partition.** (41006)
</dt> <dt>

**The operation is not allowed on a system or critical partition.** (42010)
</dt> </dl>

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

 

 





