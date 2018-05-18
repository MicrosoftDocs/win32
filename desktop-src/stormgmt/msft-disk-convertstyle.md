---
title: ConvertStyle method of the MSFT\_Disk class
description: Converts the partition style of an already initialized disk.
ms.assetid: '38C1C3A0-DAB0-490F-A308-D0966364B728'
keywords: ["ConvertStyle method Windows Storage Management API", "ConvertStyle method Windows Storage Management API , MSFT_Disk class", "MSFT_Disk class Windows Storage Management API , ConvertStyle method"]
topic_type:
- apiref
api_name:
- MSFT_Disk.ConvertStyle
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# ConvertStyle method of the MSFT\_Disk class

Converts the partition style of an already initialized disk.

## Syntax


```mof
UInt32 ConvertStyle(
  [in]  UInt16 PartitionStyle,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*PartitionStyle* \[in\]
</dt> <dd>

The new partition style for the disk. This parameter is required.

<dl> <dt>

<span id="MBR"></span><span id="mbr"></span>**MBR** (1)
</dt> <dt>

<span id="GPT"></span><span id="gpt"></span>**GPT** (2)
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

**The disk has not been initialized.** (41000)
</dt> <dt>

**The disk is read only.** (41002)
</dt> <dt>

**The disk is offline.** (41003)
</dt> <dt>

**Operation not supported on a critical disk.** (41009)
</dt> <dt>

**Cannot convert the style of a disk with data or other known partitions on it.** (41013)
</dt> <dt>

**The disk is not large enough to support a GPT partition style.** (41014)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be removed from the cluster to perform this operation.** (41019)
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

 

 





