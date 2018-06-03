---
title: SetVpnPorts method of the PS\_RemoteAccessLocal class
description: This method sets the ports required by VPN to the default values based on the whether Vpn and/or site-to-site Vpn are enabled.
audience: developer
ms.assetid: 6cd2a050-e752-49cd-a1f7-52f9638e3216
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetVpnPorts method
- SetVpnPorts method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, SetVpnPorts method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.SetVpnPorts
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetVpnPorts method of the PS\_RemoteAccessLocal class

This method sets the ports required by VPN to the default values based on the whether Vpn and/or site-to-site Vpn are enabled.

## Syntax


```mof
uint32 SetVpnPorts(
  [in] boolean IsVpnEnabled,
  [in] boolean IsS2SVpnEnabled
);
```



## Parameters

<dl> <dt>

*IsVpnEnabled* \[in\]
</dt> <dd>

Parameter indicating whether Vpn is enabled

</dd> <dt>

*IsS2SVpnEnabled* \[in\]
</dt> <dd>

Parameter indicating whether Site to Site Vpn is enabled

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

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





