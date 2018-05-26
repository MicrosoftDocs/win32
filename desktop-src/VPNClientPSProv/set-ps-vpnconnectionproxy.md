---
title: Set method of the PS\_VpnConnectionProxy class
description: Configures the web proxy for a VPN connection.
audience: developer
ms.assetid: A7F386CC-0E72-4EF6-9EBF-58777A43F2A2
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_VpnConnectionProxy class
- PS_VpnConnectionProxy class, Set method
topic_type:
- apiref
api_name:
- PS_VpnConnectionProxy.Set
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_VpnConnectionProxy class

Configures the web proxy for a VPN connection.

## Syntax


```mof
uint32 Set(
  [in]  boolean            AutoDetect,
  [in]  string             AutoConfigurationScript,
  [in]  string             ProxyServer,
  [in]  boolean            BypassProxyForLocal,
  [in]  string             ExceptionPrefix[],
  [in]  string             ConnectionName,
  [in]  boolean            PassThru,
  [out] VpnConnectionProxy cmdletOutput
);
```



## Parameters

<dl> <dt>

*AutoDetect* \[in\]
</dt> <dd>

**true** to automatically detect proxy settings; otherwise, **false**.

</dd> <dt>

*AutoConfigurationScript* \[in\]
</dt> <dd>

The web proxy auto detection (WPAD) script for automatic web proxy configuration.

</dd> <dt>

*ProxyServer* \[in\]
</dt> <dd>

The web proxy server address and port number pair, separated by a colon.

</dd> <dt>

*BypassProxyForLocal* \[in\]
</dt> <dd>

**true** to bypass the web proxy for local (intranet) addresses; otherwise, **false**.

</dd> <dt>

*ExceptionPrefix* \[in\]
</dt> <dd>

The prefixes of the addresses for which no web proxy should be used.

</dd> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionProxy**](vpnconnectionproxy.md) object that contains the proxy configuration for the VPN connection; otherwise, **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionProxy**](vpnconnectionproxy.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnectionProxy**](ps-vpnconnectionproxy.md)
</dt> </dl>

 

 





