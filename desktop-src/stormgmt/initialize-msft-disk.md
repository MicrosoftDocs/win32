---
title: Initialize method of the MSFT\_Disk class
description: Initializes a RAW disk with a particular partition style.
ms.assetid: '70782a94-406f-4c28-9562-8df554b65463'
keywords: ["Initialize method Windows Storage Management API", "Initialize method Windows Storage Management API , MSFT_Disk class", "MSFT_Disk class Windows Storage Management API , Initialize method"]
topic_type:
- apiref
api_name:
- MSFT_Disk.Initialize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Initialize method of the MSFT\_Disk class

Initializes a RAW disk with a particular partition style.

## Syntax


```mof
UInt32 Initialize(
  [in]  UInt16 PartitionStyle,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*PartitionStyle* \[in\]
</dt> <dd>

The desired partition style for the disk. The default value for this parameter is **GPT**.

<dl> <dt>

<span id="MBR"></span><span id="mbr"></span>**MBR** (1)
</dt> <dt>

<span id="GPT_"></span><span id="gpt_"></span>**GPT** (2 )
</dt> </dl> </dd> <dt>

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

**The disk has already been initialized.** (41001)
</dt> <dt>

**The specified partition type is not valid.** (41010)
</dt> <dt>

**The disk is not large enough to support a GPT partition style.** (41014)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
</dt> </dl>

## Remarks

If no partition style is specified, GPT will be selected by default. If the disk is already initialized, this method will fail with a well-defined error code.

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

 

 





