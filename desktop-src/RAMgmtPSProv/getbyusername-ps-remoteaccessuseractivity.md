---
title: GetByUserName method of the PS\_RemoteAccessUserActivity class
description: This cmdlet displays the following1. Resources accessed over the active DA and VPN connections2. Resources accessed over historical DA and VPN connections.
audience: developer
ms.assetid: 843abcef-cb23-447d-9efd-8d415a0c1156
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByUserName method
- GetByUserName method, PS_RemoteAccessUserActivity class
- PS_RemoteAccessUserActivity class, GetByUserName method
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivity.GetByUserName
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetByUserName method of the PS\_RemoteAccessUserActivity class

This cmdlet displays the following1. Resources accessed over the active DA and VPN connections2. Resources accessed over historical DA and VPN connections

## Syntax


```mof
uint32 GetByUserName(
  [in]  string                   UserName,
  [in]  string                   ComputerName,
  [in]  datetime                 EndDateTime,
  [in]  datetime                 StartDateTime,
  [out] RemoteAccessUserActivity cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

Specifies the user whose activity needs to be retrieved. The name is provided in DOMAIN\\USERNAME format

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*EndDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which the user activity needs to be retrieved and indicates the end date. It is specified in the format MM/DD/YYYY Hour:Min:Sec \[AM/PM\].

</dd> <dt>

*StartDateTime* \[in\]
</dt> <dd>

This parameter is used to specify the time duration for which the user activity needs to be retrieved and indicates the start date. It is specified in the format MM/DD/YYYY Hour:Min:Sec \[AM/PM\].

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**RemoteAccessUserActivity**](remoteaccessuseractivity.md) object.

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

 

 





