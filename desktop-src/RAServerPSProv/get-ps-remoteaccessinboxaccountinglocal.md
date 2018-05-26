---
title: Get method of the PS\_RemoteAccessInboxAccountingLocal class
description: Get the status for Inbox accounting.
audience: developer
ms.assetid: f347c78b-690f-48e3-8857-3b6f65e25548
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccessInboxAccountingLocal class
- PS_RemoteAccessInboxAccountingLocal class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccessInboxAccountingLocal.Get
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_RemoteAccessInboxAccountingLocal class

Get the status for Inbox accounting.

## Syntax


```mof
uint32 Get(
  [out] RemoteAccessInboxAccountingLocal cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns a [**RemoteAccessInboxAccountingLocal**](ps-remoteaccessinboxaccountinglocal.md) containing the entire Inbox Accounting Configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessInboxAccountingLocal**](ps-remoteaccessinboxaccountinglocal.md)
</dt> </dl>

 

 





