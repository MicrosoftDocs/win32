---
title: RevokeAccess method of the MSFT\_SMFileShare class
description: Revokes access to the file share for the specified users.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1a67ab1f-fcec-4c53-81a5-7f84b187a23e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RevokeAccess method
- RevokeAccess method, MSFT_SMFileShare class
- MSFT_SMFileShare class, RevokeAccess method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RevokeAccess method of the MSFT\_SMFileShare class

Revokes access to the file share for the specified users.

## Syntax


```mof
UInt32 RevokeAccess(
  [in]            string                AccountNames[],
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccountNames* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMFileShare**](msft-smfileshare.md)
</dt> </dl>

 

 





