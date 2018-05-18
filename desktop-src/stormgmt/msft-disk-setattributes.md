---
title: SetAttributes method of the MSFT\_Disk class
description: Sets the disk's attributes and properties.
ms.assetid: '71D7E14B-8E03-479A-BA80-821EE019B8CB'
keywords: ["SetAttributes method Windows Storage Management API", "SetAttributes method Windows Storage Management API , MSFT_Disk class", "MSFT_Disk class Windows Storage Management API , SetAttributes method"]
topic_type:
- apiref
api_name:
- MSFT_Disk.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# SetAttributes method of the MSFT\_Disk class

Sets the disk's attributes and properties. The disk must be online for most attributes to be set.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsReadOnly,
  [in]  UInt32  Signature,
  [in]  String  Guid,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*IsReadOnly* \[in\]
</dt> <dd>

If **TRUE**, the disk will be made read-only. If **FALSE**, the disk will become writable.

</dd> <dt>

*Signature* \[in\]
</dt> <dd>

Sets the MBR signature of the disk. This parameter is only valid when the disk's **PartitionStyle** property is **MBR**. An error will be returned if the disk is any other partition style.

</dd> <dt>

*Guid* \[in\]
</dt> <dd>

Sets the GPT GUID of the disk. This parameter is only valid when the disk's **PartitionStyle** property is **GPT**. An error will be returned if the disk is any other partition style.

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

**The disk is offline.** (41003)
</dt> <dt>

**A parameter is not valid for this type of partition.** (41006)
</dt> <dt>

**Operation not supported on a critical disk.** (41009)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
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

[**MSFT\_Disk**](msft-disk.md)
</dt> </dl>

 

 





