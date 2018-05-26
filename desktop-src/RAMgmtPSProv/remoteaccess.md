---
title: RemoteAccess class
description: Remote Access Configuration.
audience: developer
ms.assetid: 65c3fc93-1a39-418b-adbf-9232f56a51cb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccess class
- RemoteAccess class, described
topic_type:
- apiref
api_name:
- RemoteAccess
- RemoteAccess.InternetInterface
- RemoteAccess.InternalInterface
- RemoteAccess.SslCertificate
- RemoteAccess.DAStatus
- RemoteAccess.VpnStatus
- RemoteAccess.VpnS2SStatus
- RemoteAccess.LoadBalancing
- RemoteAccess.SstpProxyStatus
- RemoteAccess.RoutingStatus
- RemoteAccess.UseHttp
- RemoteAccess.DAConfiguration
- RemoteAccess.VpnConfiguration
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoteAccess class

Remote Access Configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccess : RemoteAccessCommon
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
  DirectAccessConfiguration          DAConfiguration;
  VirtualPrivateNetworkConfiguration VpnConfiguration;
};
```

## Members

The **RemoteAccess** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccess** class has these properties.

<dl> <dt>

**DAConfiguration**
</dt> <dd> <dl> <dt>

Data type: **DirectAccessConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DirectAccessConfiguration**](directaccessconfiguration.md)")
</dt> </dl>

[**DirectAccessConfiguration**](directaccessconfiguration.md) embedded instance

</dd> <dt>

**DAStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether direct access is installed

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

Intranet facing interface

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**InternetInterface**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Internet facing interface

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**LoadBalancing**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether load balancing is enabled

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

Whether routing is installed

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**SslCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of IP-HTTPS/SSL certificates

This property is inherited from [**RemoteAccessCore**](remoteaccesscore.md).

</dd> <dt>

**SstpProxyStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether an SSTP Proxy is installed

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**UseHttp**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to use HTTP; otherwise, **false**

This property is inherited from [**RemoteAccessCommon**](remoteaccesscommon.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

**VpnConfiguration**
</dt> <dd> <dl> <dt>

Data type: **VirtualPrivateNetworkConfiguration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VirtualPrivateNetworkConfiguration**](virtualprivatenetworkconfiguration.md)")
</dt> </dl>

[**VirtualPrivateNetworkConfiguration**](virtualprivatenetworkconfiguration.md) embedded instance

</dd> <dt>

**VpnS2SStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether S2S VPN is installed

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

Whether VPN is installed

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



 

 





