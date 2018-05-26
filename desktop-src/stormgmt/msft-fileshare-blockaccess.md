---
title: BlockAccess method of the MSFT\_FileShare class
description: Denies specified users access to the file share.
ms.assetid: FA3B0467-BE7E-4847-8AA3-BF73E622E83F
keywords:
- BlockAccess method Windows Storage Management API
- BlockAccess method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , BlockAccess method
topic_type:
- apiref
api_name:
- MSFT_FileShare.BlockAccess
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

# BlockAccess method of the MSFT\_FileShare class

Denies specified users access to the file share.

## Syntax


```mof
UInt32 BlockAccess(
  [in]  String AccountNames[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccountNames* \[in\]
</dt> <dd>

User accounts to be denied access to the file share.

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileShare**](msft-fileshare.md)
</dt> </dl>

 

 





