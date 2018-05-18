---
title: Refresh method of the MSFT\_Disk class
description: Refreshes the cached disk layout information.
ms.assetid: '4BFE5289-DA95-4ED7-993E-496E97D9695A'
keywords: ["Refresh method Windows Storage Management API", "Refresh method Windows Storage Management API , MSFT_Disk class", "MSFT_Disk class Windows Storage Management API , Refresh method"]
topic_type:
- apiref
api_name:
- MSFT_Disk.Refresh
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# Refresh method of the MSFT\_Disk class

Refreshes the cached disk layout information.

## Syntax


```mof
UInt32 Refresh(
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

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
</dt> </dl>

## Remarks

This method is useful when the backing disk has changed size (if the backing data store is a VHD or a virtual disk).

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

 

 





