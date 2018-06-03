---
title: UnblockAccess method of the MSFT\_SmbShare class
description: Updates a share's security descriptor to unblock accounts from accessing a share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fe704154-169b-47bb-a1e8-b3c59a2656c0
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- UnblockAccess method SMB
- UnblockAccess method SMB , MSFT_SmbShare class
- MSFT_SmbShare class SMB , UnblockAccess method
topic_type:
- apiref
api_name:
- MSFT_SmbShare.UnblockAccess
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UnblockAccess method of the MSFT\_SmbShare class

Updates a share's security descriptor to unblock accounts from accessing a share.

## Syntax


```mof
uint32 UnblockAccess(
  [in]  string                          AccountName[],
  [out] MSFT_SmbShareAccessControlEntry Output[]
);
```



## Parameters

<dl> <dt>

*AccountName* \[in\]
</dt> <dd>

The array of names of accounts whose access is being unblocked.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

An array of instances of the [**MSFT\_SmbShareAccessControlEntry**](msft-smbshareaccesscontrolentry.md) class that represent the updated access control entries for the share.

</dd> </dl>

## Remarks

To unblock access, all existing access-denied access control entries (ACE) for the specified accounts are removed.

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

 

 





