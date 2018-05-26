---
title: RemoteAccessVpn class
description: Remote Access VPN configuration consisting of the Remote Access common configuration.
audience: developer
ms.assetid: 2cb3a969-652d-436d-83d7-9fe1787d4232
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessVpn class
- RemoteAccessVpn class, described
topic_type:
- apiref
api_name:
- RemoteAccessVpn
- RemoteAccessVpn.InternetInterface
- RemoteAccessVpn.InternalInterface
- RemoteAccessVpn.SslCertificate
- RemoteAccessVpn.DAStatus
- RemoteAccessVpn.VpnStatus
- RemoteAccessVpn.VpnS2SStatus
- RemoteAccessVpn.LoadBalancing
- RemoteAccessVpn.SstpProxyStatus
- RemoteAccessVpn.RoutingStatus
- RemoteAccessVpn.UseHttp
- RemoteAccessVpn.VpnConfiguration
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccessVpn class

Remote Access VPN configuration consisting of the Remote Access common configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessVpn : RemoteAccessCommon
{
  string                             InternetInterface;
  string                             InternalInterface;
  uint8                              SslCertificate[];
  string                             DAStatus;
  string                             VpnStatus;
  string                             VpnS2SStatus;
  string                             LoadBalancing;
  string                             SstpProxyStatus;
  string                             RoutingStatus;
  boolean                            UseHttp;
  VirtualPrivateNetworkConfiguration VpnConfiguration;
};
```

## Members

The **RemoteAccessVpn** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessVpn** class has these properties.

<dl> <dt>

**DAStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether direct access is installed.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

</dd> <dt>

**InternalInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Intranet facing interface.

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**InternetInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Internet facing interface.

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**LoadBalancing**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether load balancing is enabled.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

The possible values are.

<dt>



 ("Installed")


</dt> <dd></dd> <dt>



 ("Uninstalled")


</dt> <dd></dd> <dt>

<span id="NotConfigured"></span><span id="notconfigured"></span><span id="NOTCONFIGURED"></span>

**NotConfigured** ("NotConfigured")


</dt> <dd></dd> <dt>

<span id="Configured"></span><span id="configured"></span><span id="CONFIGURED"></span>

**Configured** ("Configured")


</dt> <dd></dd> </dl>

</dd> <dt>

**RoutingStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether routing is installed.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

</dd> <dt>

**SslCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of IP-HTTPS/SSL certificates.

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**SstpProxyStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether an SSTP Proxy is installed.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

</dd> <dt>

**UseHttp**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to use HTTP; otherwise, **false**

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

</dd> <dt>

**VpnConfiguration**
</dt> <dd> <dl> <dt>

Data type: **VirtualPrivateNetworkConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VirtualPrivateNetworkConfiguration**](virtualprivatenetworkconfiguration.md)")
</dt> </dl>

A [**VirtualPrivateNetworkConfiguration**](virtualprivatenetworkconfiguration.md) embedded instance

</dd> <dt>

**VpnS2SStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether S2S VPN is installed.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

</dd> <dt>

**VpnStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether VPN is installed.

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





