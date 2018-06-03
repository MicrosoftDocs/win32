---
title: GrantAccess method of the MSFT\_FileShare class
description: Grants to the specified user accounts the specified access to the file share.
ms.assetid: 9303326E-062D-452A-9E3C-AD9F394A49D4
keywords:
- GrantAccess method Windows Storage Management API
- GrantAccess method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , GrantAccess method
topic_type:
- apiref
api_name:
- MSFT_FileShare.GrantAccess
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

# GrantAccess method of the MSFT\_FileShare class

Grants to the specified user accounts the specified access to the file share.

## Syntax


```mof
UInt32 GrantAccess(
  [in]  String AccountNames[],
  [in]  UInt32 AccessRight,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccountNames* \[in\]
</dt> <dd>

User accounts to be granted access to the file share.

</dd> <dt>

*AccessRight* \[in\]
</dt> <dd>

Access to be granted to the specified user accounts.

<dl> <dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>**Full** (0)
</dt> <dt>

<span id="Change"></span><span id="change"></span><span id="CHANGE"></span>**Change** (1)
</dt> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>**Read** (2)
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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**The operation is not supported while the cluster is being upgraded.** (40009)
</dt> <dt>

**At least one account name needs to be specified.** (58003)
</dt> <dt>

**You must specify an access right.** (58004)
</dt> <dt>

**The specified user account could not be found.** (58005)
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

 

 





