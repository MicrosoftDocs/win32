---
title: CheckServerPreRequisites method of the PS\_RemoteAccessLocal class
description: This method checks all the pre-requisites on the DA server itself.
audience: developer
ms.assetid: 34f1a3ae-9519-41db-b898-149a4813ff43
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CheckServerPreRequisites method
- CheckServerPreRequisites method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, CheckServerPreRequisites method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.CheckServerPreRequisites
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CheckServerPreRequisites method of the PS\_RemoteAccessLocal class

This method checks all the pre-requisites on the DA server itself.

## Syntax


```mof
uint32 CheckServerPreRequisites(
  [out] uint8 Status[]
);
```



## Parameters

<dl> <dt>

*Status* \[out\]
</dt> <dd>

Status codes for the server side checks.

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

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





