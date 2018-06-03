---
title: Uninstall method of the PS\_RemoteAccess class
description: This cmdlet uninstalls DirectAccess and VPN service (both remote access VPN and site-to-site VPN).
audience: developer
ms.assetid: 64baa78a-7bdd-4a2d-851f-2ddd88e59c31
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Uninstall method
- Uninstall method, PS_RemoteAccess class
- PS_RemoteAccess class, Uninstall method
topic_type:
- apiref
api_name:
- PS_RemoteAccess.Uninstall
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Uninstall method of the PS\_RemoteAccess class

This cmdlet uninstalls DirectAccess and VPN service (both remote access VPN and site-to-site VPN).

## Syntax


```mof
uint32 Uninstall(
  [in] string  VpnType,
  [in] string  EntrypointName,
  [in] string  ComputerName,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*VpnType* \[in\]
</dt> <dd>

The type of VPN to uninstall. You can set this value to Vpn or VpnS2S.

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment where VPN needs to be uninstalled. It is not applicable to DA. If entrypoint is not specified then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and VPN is uninstalled at the site indicated by it. Note that in a multi-site deployment case VPN can only be uninstalled one site at a time.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The IP address or hostname of the machine on which the remote access server machine specific tasks should be executed.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes 1. Uninstall of Remote Access after which users will not be able to connect remotely to corpnet. 2. If NLS is on DA server then uninstallation will lead to decommissioning of the NLS URL and clients that have not received updated policies will always be detected to be outside corpnet and will not be able to access corp resources when inside corpnet.

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

 

 





