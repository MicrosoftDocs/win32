---
title: Get method of the PS\_DAClient class
description: This cmdlet displays the list of client security groups that are part of the DA deployment and the client properties.
audience: developer
ms.assetid: 0ac855e9-e714-4501-87e5-9da3736c7e50
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DAClient class
- PS_DAClient class, Get method
topic_type:
- apiref
api_name:
- PS_DAClient.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DAClient class

This cmdlet displays the list of client security groups that are part of the DA deployment and the client properties.

## Syntax


```mof
uint32 Get(
  [in]  string   ComputerName,
  [in]  string   EntrypointName,
  [out] DAClient cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment. When specified only those downlevel SGs and GPOs that belong to the specified site (i.e., these clients connect only to this site) are displayed. However, all W8 SGs and GPOs are displayed as they are independent of site. If there is a multi-site deployment then downlevel client SG and GPO information is always retrieved only for a specific site. If the entrypoint is not specified then the site to which the computer on which the cmdlet is executed belongs is used (user may or may not be specifying a ComputerName). It is not possible to retrieve all the downlevel SGs and GPOs across all sites. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the authentication type is configured for it. If there is no multi-site deployment but user specifies the entrypoint param then the cmdlet returns an error message

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of client security groups in the DA deployment (each name is specified in DOMAIN\\SG\_NAME format). 2. List of client GPOs. 3. Status of force tunneling. 4. NRPT object corresponding to force tunneling. 5. Status of policy to deploy DA only on laptops and notebooks and not on all computers in the domain. 6. Status of whether appropriate policies should be deployed on downlevel clients (W7) clients such that they too can connect to the W8 DA Server

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

[**PS\_DAClient**](ps-daclient.md)
</dt> </dl>

 

 





