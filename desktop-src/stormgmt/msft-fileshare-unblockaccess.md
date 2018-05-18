---
title: UnblockAccess method of the MSFT\_FileShare class
description: Removes specified users from the denied access list for the file share.
ms.assetid: 'DA0B78BE-571F-4B5E-9120-7321FE2BB977'
keywords: ["UnblockAccess method Windows Storage Management API", "UnblockAccess method Windows Storage Management API , MSFT_FileShare class", "MSFT_FileShare class Windows Storage Management API , UnblockAccess method"]
topic_type:
- apiref
api_name:
- MSFT_FileShare.UnblockAccess
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# UnblockAccess method of the MSFT\_FileShare class

Removes specified users from the denied access list for the file share.

## Syntax


```mof
UInt32 UnblockAccess(
  [in]  String AccountNames[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccountNames* \[in\]
</dt> <dd>

User accounts to remove from the deny access list for the file share.

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

**Cache out of date** (40003)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileShare**](msft-fileshare.md)
</dt> </dl>

 

 





