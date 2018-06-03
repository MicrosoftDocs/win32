---
title: VpnMultiTenancy class
description: Represents a site-to-site (S2S) VPN multi-tenant configuration.
audience: developer
ms.assetid: ff0632ae-1a82-4f0e-af7c-b64ba76d8946
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnMultiTenancy class
- VpnMultiTenancy class, described
topic_type:
- apiref
api_name:
- VpnMultiTenancy
- VpnMultiTenancy.InternetInterface
- VpnMultiTenancy.InternalInterface
- VpnMultiTenancy.SslCertificate
- VpnMultiTenancy.DAStatus
- VpnMultiTenancy.VpnStatus
- VpnMultiTenancy.VpnS2SStatus
- VpnMultiTenancy.LoadBalancing
- VpnMultiTenancy.SstpProxyStatus
- VpnMultiTenancy.RoutingStatus
- VpnMultiTenancy.UseHttp
- VpnMultiTenancy.VpnMultiTenancyStatus
- VpnMultiTenancy.CapacityKbps
- VpnMultiTenancy.AuthenticationPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VpnMultiTenancy class

Represents a site-to-site (S2S) VPN multi-tenant configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnMultiTenancy : RemoteAccessCommon
{
  string  InternetInterface;
  string  InternalInterface;
  uint8   SslCertificate[];
  string  DAStatus;
  string  VpnStatus;
  string  VpnS2SStatus;
  string  LoadBalancing;
  string  SstpProxyStatus;
  string  RoutingStatus;
  boolean UseHttp;
  string  VpnMultiTenancyStatus;
  uint64  CapacityKbps;
  VpnAuth AuthenticationPolicy;
};
```

## Members

The **VpnMultiTenancy** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnMultiTenancy** class has these properties.

<dl> <dt>

**AuthenticationPolicy**
</dt> <dd> <dl> <dt>

Data type: **VpnAuth**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnAuth**](vpnauth.md)")
</dt> </dl>

A [**VpnAuth**](vpnauth.md) embedded instance

</dd> <dt>

**CapacityKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bandwidth capacity of the routing domain, in kbps.

</dd> <dt>

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

**VpnMultiTenancyStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether multi-tenant VPN services are installed

The possible values are.

<dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** ("Installed")


</dt> <dd></dd> <dt>

<span id="Uninstalled"></span><span id="uninstalled"></span><span id="UNINSTALLED"></span>

**Uninstalled** ("Uninstalled")


</dt> <dd></dd> </dl>

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**RemoteAccessCommon**](remoteaccesscommon.md)
</dt> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





