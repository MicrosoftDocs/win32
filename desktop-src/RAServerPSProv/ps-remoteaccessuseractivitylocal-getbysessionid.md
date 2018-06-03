---
title: GetBySessionId method of the PS\_RemoteAccessUserActivityLocal class
description: Retrieves the user activity for a particular session.
audience: developer
ms.assetid: affab9d9-98c6-4f93-a76c-4eaafda8f964
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetBySessionId method
- GetBySessionId method, PS_RemoteAccessUserActivityLocal class
- PS_RemoteAccessUserActivityLocal class, GetBySessionId method
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivityLocal.GetBySessionId
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetBySessionId method of the PS\_RemoteAccessUserActivityLocal class

Retrieves the user activity for a particular session.

## Syntax


```mof
uint32 GetBySessionId(
  [in]  uint64                        SessionId,
  [out] RemoteAccessUserActivityLocal cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*SessionId* \[in\]
</dt> <dd>

Identifier of the session for which to get the User Activity

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns an array of [**RemoteAccessUserActivityLocal**](ps-remoteaccessuseractivitylocal.md) objects that describe the User Activity objects for the specified session.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessUserActivityLocal**](ps-remoteaccessuseractivitylocal.md)
</dt> </dl>

 

 





