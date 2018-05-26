---
title: GetByActiveUserActivity method of the PS\_RemoteAccessUserActivityLocal class
description: This cmdlet displays the following1. Remote user activity over an active connection2. Remote user activity based on accounting data.
audience: developer
ms.assetid: e9a1d167-6dd2-4a80-a759-25160bf7e377
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByActiveUserActivity method
- GetByActiveUserActivity method, PS_RemoteAccessUserActivityLocal class
- PS_RemoteAccessUserActivityLocal class, GetByActiveUserActivity method
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivityLocal.GetByActiveUserActivity
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByActiveUserActivity method of the PS\_RemoteAccessUserActivityLocal class

This cmdlet displays the following1. Remote user activity over an active connection2. Remote user activity based on accounting data.

## Syntax


```mof
uint32 GetByActiveUserActivity(
  [in]  string                        UserName,
  [in]  string                        HostIPAddress,
  [out] RemoteAccessUserActivityLocal cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

User name for which to get the User Activity

</dd> <dt>

*HostIPAddress* \[in\]
</dt> <dd>

Host IP Address for which to get the User Activity

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains an array of [**RemoteAccessUserActivityLocal**](ps-remoteaccessuseractivitylocal.md) that describe the User Activity objects for the specified user/host IP.

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

[**PS\_RemoteAccessUserActivityLocal**](ps-remoteaccessuseractivitylocal.md)
</dt> </dl>

 

 





