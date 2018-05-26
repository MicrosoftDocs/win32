---
title: GetByAccountingUserActivity method of the PS\_RemoteAccessUserActivityLocal class
description: This cmdlet displays the following1. Remote user activity over an active connection2. Remote user activity based on accounting data.
audience: developer
ms.assetid: 5b7a94f3-21df-4df1-b794-902a885bc015
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByAccountingUserActivity method
- GetByAccountingUserActivity method, PS_RemoteAccessUserActivityLocal class
- PS_RemoteAccessUserActivityLocal class, GetByAccountingUserActivity method
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivityLocal.GetByAccountingUserActivity
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByAccountingUserActivity method of the PS\_RemoteAccessUserActivityLocal class

This cmdlet displays the following1. Remote user activity over an active connection2. Remote user activity based on accounting data.

## Syntax


```mof
uint32 GetByAccountingUserActivity(
  [in]  datetime                      StartDateTime,
  [in]  datetime                      EndDateTime,
  [in]  string                        HostIPAddress,
  [in]  string                        UserName,
  [out] RemoteAccessUserActivityLocal cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*StartDateTime* \[in\]
</dt> <dd>

Start date from when to get the User Activity from Accounting data.

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

End date till when to get the User Activity from Accounting data.

</dd> <dt>

*HostIPAddress* \[in\]
</dt> <dd>

Host IP Address for which to get the User Activity.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

User name for which to get the User Activity.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of [**RemoteAccessUserActivityLocal**](ps-remoteaccessuseractivitylocal.md) containing the User Activity objects for the specified user/host IP.

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

 

 





