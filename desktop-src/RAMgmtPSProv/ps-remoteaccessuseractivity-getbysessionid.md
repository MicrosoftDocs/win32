---
title: GetBySessionId method of the PS\_RemoteAccessUserActivity class
description: This cmdlet displays the following.
audience: developer
ms.assetid: eece8005-13fe-4935-aed1-c12a79f29ecb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetBySessionId method
- GetBySessionId method, PS_RemoteAccessUserActivity class
- PS_RemoteAccessUserActivity class, GetBySessionId method
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivity.GetBySessionId
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetBySessionId method of the PS\_RemoteAccessUserActivity class

This cmdlet displays the following

1. Resources accessed over the active DA and VPN connections

2. Resources accessed over historical DA and VPN connections

## Syntax


```mof
uint32 GetBySessionId(
  [in]  string                   ComputerName,
  [in]  uint64                   SessionId,
  [out] RemoteAccessUserActivity cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the computer on which the Remote Access server computer specific tasks should be executed

</dd> <dt>

*SessionId* \[in\]
</dt> <dd>

An identifier for the Session, for which the User Activity data is to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

In both real-time and accounting cases the object consists of the following properties. A separate instance of the object is outputted for every corporate network resource that is accessed over the connection

1. IP address of the server in corporate network

2. Identity of the protocol using which the server is being accessed

3. Port no. using which the server is being accessed

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessUserActivity**](ps-remoteaccessuseractivity.md)
</dt> </dl>

 

 





