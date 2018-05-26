---
title: Get method of the PS\_RemoteAccess class
description: This cmdlet displays the configuration of DirectAccess and VPN.
audience: developer
ms.assetid: 65c3fc93-1a39-418b-adbf-9232f56a51cb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccess class
- PS_RemoteAccess class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccess.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_RemoteAccess class

This cmdlet displays the configuration of DirectAccess and VPN.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [in]  string             EntrypointName,
  [out] RemoteAccessCommon cmdletOutput
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

Entrypoint refers to the identity of a site in a multi-site deployment to which down-level clients are added, i.e., these clients can only connect to the specified site. If entrypoint parameter is not specified then the site to which the computer on which the cmdlet is executed belongs is used (user may or may not be specifying a ComputerName)

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Object consists of the following. 1. Status of DirectAccess - installed or uninstalled. 2. Deployment mode for DirectAccess - Remote Access and management of remote clients OR Management of remote clients. 3. DirectAccess configuration. 4. Status of VPN - installed or uninstalled. 5. VPN configuration. 6. Configuration common to DirectAccess and VPN. Note that if either VPN or DA is not installed its configuration is not displayed. The DirectAccess configuration will be a collation of the output of all other DirectAccess configuration cmdlets. The VPN configuration contains the following. 1. Address Assignment type - DHCP or StaticPool. 2. Static Pool - all the configured IP address ranges, if static pool address assignment is configured 3. Authentication type - Windows, LocalNPS or ExternalRADIUS 4. External RADIUS servers - IPv4/IPv6 address or hostname of the RADIUS servers used for authentication, if external RADIUS authentication is configured. The common configuration contains the following 1. Internet Interface - name of the Internet facing interface 2. Internal Interface - name of the intranet facing interface, this will not be displayed in case of single NIC config 3. ConnectTo address 4. SSL certificate

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

[**PS\_RemoteAccess**](ps-remoteaccess.md)
</dt> </dl>

 

 





