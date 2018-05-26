---
title: GrantAccess method of the MSFT\_SmbShare class
description: Updates a shares security descriptor to grant accounts permission to access a share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: db2fad8d-badb-408c-837a-ce4fccf05066
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GrantAccess method SMB
- GrantAccess method SMB , MSFT_SmbShare class
- MSFT_SmbShare class SMB , GrantAccess method
topic_type:
- apiref
api_name:
- MSFT_SmbShare.GrantAccess
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GrantAccess method of the MSFT\_SmbShare class

Updates a share's security descriptor to grant accounts permission to access a share.

## Syntax


```mof
uint32 GrantAccess(
  [in]  string                          AccountName[],
  [in]  uint32                          AccessRight,
  [out] MSFT_SmbShareAccessControlEntry Output[]
);
```



## Parameters

<dl> <dt>

*AccountName* \[in\]
</dt> <dd>

An array of strings containing the account names to which access will be granted.

</dd> <dt>

*AccessRight* \[in\]
</dt> <dd>

The access rights to be granted.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

An array of instances of the [**MSFT\_SmbShareAccessControlEntry**](msft-smbshareaccesscontrolentry.md) class that represent the updated access control entries for the share.

</dd> </dl>

## Remarks

To grant access, all existing allow ACEs for the specified accounts are removed and replaced with ACEs that grant the specified access rights.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbShare**](msft-smbshare.md)
</dt> </dl>

 

 





