---
title: GetAccessControlEntries method of the MSFT\_FileShare class
description: Gets the access control entries for specified accounts.
ms.assetid: 252AD23C-4951-4C1D-A9FD-42E35A2ED81F
keywords:
- GetAccessControlEntries method Windows Storage Management API
- GetAccessControlEntries method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , GetAccessControlEntries method
topic_type:
- apiref
api_name:
- MSFT_FileShare.GetAccessControlEntries
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

# GetAccessControlEntries method of the MSFT\_FileShare class

Gets the access control entries for specified accounts.

## Syntax


```mof
UInt32 GetAccessControlEntries(
  [out] String AccessControlEntries[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccessControlEntries* \[out\]
</dt> <dd>

An array of strings containing embedded [**MSFT\_FileShareAccessControlEntry**](msft-fileshareaccesscontrolentry.md) objects specifying the access control entries for the share.

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

 

 





