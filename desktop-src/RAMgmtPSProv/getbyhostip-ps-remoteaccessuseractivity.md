---
title: GetByHostIP method of the PS\_RemoteAccessUserActivity class
description: This cmdlet displays the following1. Resources accessed over the active DA and VPN connections2. Resources accessed over historical DA and VPN connections.
audience: developer
ms.assetid: 80711289-4b13-4acd-b2c1-e3de92650c08
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByHostIP method
- GetByHostIP method, PS_RemoteAccessUserActivity class
- PS_RemoteAccessUserActivity class, GetByHostIP method
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivity.GetByHostIP
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByHostIP method of the PS\_RemoteAccessUserActivity class

This cmdlet displays the following1. Resources accessed over the active DA and VPN connections2. Resources accessed over historical DA and VPN connections

## Syntax


```mof
uint32 GetByHostIP(
  [in]  string                   HostIPAddress,
  [in]  string                   ComputerName,
  [in]  datetime                 EndDateTime,
  [in]  datetime                 StartDateTime,
  [out] RemoteAccessUserActivity cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*HostIPAddress* \[in\]
</dt> <dd>

Tunnel IP address of the connection. This can be IPv4 or IPv6 address

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

 

 





