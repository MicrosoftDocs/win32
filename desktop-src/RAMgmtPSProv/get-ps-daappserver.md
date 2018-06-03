---
title: Get method of the PS\_DAAppServer class
description: This cmdlet displays the list of application server security groups that are part of the DA deployment and the properties of the connections made to them.
audience: developer
ms.assetid: 9e67b010-be50-441e-bbef-70acc31e509f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DAAppServer class
- PS_DAAppServer class, Get method
topic_type:
- apiref
api_name:
- PS_DAAppServer.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DAAppServer class

This cmdlet displays the list of application server security groups that are part of the DA deployment and the properties of the connections made to them. This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.

## Syntax


```mof
uint32 Get(
  [in]  string      ComputerName,
  [out] DAAppServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The following will be displayed 1. The list of application server security groups: Each security group is specified in DOMAIN\\SG\_NAME format 2. List of application server GPOs in DOMAIN\\GPO\_NAME format 2. Property of the connection to an application server - If there are no application servers configured then the default value is NoE2EAuth (No end-to-end authentication required) 3. Status of IPsec traffic protection (enabled or disabled) - If there are no application servers configured then the default value is Disable

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

[**PS\_DAAppServer**](ps-daappserver.md)
</dt> </dl>

 

 





