---
title: RevokeAccess method of the MSFT\_SmbShare class
description: Updates a share's security descriptor to revoke permission to access a share from a set of accounts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '76a4fa1d-cfe7-4f88-aabe-49240e66c41f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'server-message-block-(smb)'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RevokeAccess method SMB", "RevokeAccess method SMB , MSFT_SmbShare class", "MSFT_SmbShare class SMB , RevokeAccess method"]
topic_type:
- apiref
api_name:
- MSFT_SmbShare.RevokeAccess
api_location:
- SmbWmiV2.dll
api_type:
- COM
---

# RevokeAccess method of the MSFT\_SmbShare class

Updates a share's security descriptor to revoke permission to access a share from a set of accounts.

## Syntax


```mof
uint32 RevokeAccess(
  [in]  string                          AccountName[],
  [out] MSFT_SmbShareAccessControlEntry Output[]
);
```



## Parameters

<dl> <dt>

*AccountName* \[in\]
</dt> <dd>

An array of strings containing the names of accounts whose access permissions will be revoked.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

An array of instances of the [**MSFT\_SmbShareAccessControlEntry**](msft-smbshareaccesscontrolentry.md) class that represent the updated access control entries for the share.

</dd> </dl>

## Remarks

To revoke access, all existing access-allowed access control entries (ACE) for the specified accounts are removed.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbShare**](msft-smbshare.md)
</dt> </dl>

 

 





