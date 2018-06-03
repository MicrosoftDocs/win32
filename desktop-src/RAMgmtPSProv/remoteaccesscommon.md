---
title: RemoteAccessCommon class
description: Describes the Remote Access common configuration.
audience: developer
ms.assetid: 0751d0c3-073f-407e-85eb-85a12c52eba9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessCommon class
- RemoteAccessCommon class, described
topic_type:
- apiref
api_name:
- RemoteAccessCommon
- RemoteAccessCommon.InternetInterface
- RemoteAccessCommon.InternalInterface
- RemoteAccessCommon.SslCertificate
- RemoteAccessCommon.DAStatus
- RemoteAccessCommon.VpnStatus
- RemoteAccessCommon.VpnS2SStatus
- RemoteAccessCommon.LoadBalancing
- RemoteAccessCommon.SstpProxyStatus
- RemoteAccessCommon.RoutingStatus
- RemoteAccessCommon.UseHttp
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessCommon class

Describes the Remote Access common configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessCommon : RemoteAccessCore
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
};
```

## Members

The **RemoteAccessCommon** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessCommon** class has these properties.

<dl> <dt>

**DAStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether direct access is installed

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

The possible values are.

<dt>




</dt> <dd></dd> <dt>




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

</dd> <dt>

**VpnS2SStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether S2S VPN is installed

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



## See also

<dl> <dt>

[**RemoteAccessCore**](remoteaccesscore.md)
</dt> <dt>

[RAMgmtPSProvider Provider](remote-access-management.md)
</dt> </dl>

 

 





