---
title: GrantAccess method of the MSFT\_SMFileShare class
description: Grants the specified users access to the file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 30ed5239-797e-4631-9b34-fb1746f29159
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GrantAccess method
- GrantAccess method, MSFT_SMFileShare class
- MSFT_SMFileShare class, GrantAccess method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GrantAccess method of the MSFT\_SMFileShare class

Grants the specified users access to the file share.

## Syntax


```mof
UInt32 GrantAccess(
  [in]            string                AccountNames[],
  [in]            uint32                AccessRight,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*AccountNames* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AccessRight* \[in\]
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

 

 





