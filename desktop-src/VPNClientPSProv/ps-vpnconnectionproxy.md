---
title: PS\_VpnConnectionProxy class
description: The PS\_VpnConnectionProxy class provides a method to modify the proxy configuration of a VPN profile.
audience: developer
ms.assetid: '1AC26802-FD61-4C7E-80B9-B65CAF7FA8C6'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnConnectionProxy class", "PS_VpnConnectionProxy class, described"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionProxy
- PS_VpnConnectionProxy.AutoDetect
- PS_VpnConnectionProxy.AutoConfigurationScript
- PS_VpnConnectionProxy.ProxyServer
- PS_VpnConnectionProxy.BypassProxyForLocal
- PS_VpnConnectionProxy.ExceptionPrefix
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnConnectionProxy class

The **PS\_VpnConnectionProxy** class provides a method to modify the proxy configuration of a VPN profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionProxy
{
  boolean AutoDetect;
  string  AutoConfigurationScript;
  string  ProxyServer;
  boolean BypassProxyForLocal;
  string  ExceptionPrefix[];
};
```

## Members

The **PS\_VpnConnectionProxy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **PS\_VpnConnectionProxy** class has these methods.



| Method                                   | Description                                               |
|:-----------------------------------------|:----------------------------------------------------------|
| [**Set**](set-ps-vpnconnectionproxy.md) | Configures the web proxy for a VPN connection.<br/> |



 

### Properties

The **PS\_VpnConnectionProxy** class has these properties.

<dl> <dt>

**AutoConfigurationScript**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The web proxy auto detection (WPAD) script for automatic web proxy configuration.

</dd> <dt>

**AutoDetect**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

**true** to automatically detect proxy settings; otherwise, **false**.

</dd> <dt>

**BypassProxyForLocal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to bypass the web proxy for local (intranet) addresses; otherwise, **false**.

</dd> <dt>

**ExceptionPrefix**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The prefixes of the addresses for which no web proxy should be used.

</dd> <dt>

**ProxyServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The web proxy server address and port number pair, separated by a colon.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





