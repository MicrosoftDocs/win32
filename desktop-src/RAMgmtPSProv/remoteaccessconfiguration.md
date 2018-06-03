---
title: RemoteAccessConfiguration class
description: Manages a Remote Access configuration.
audience: developer
ms.assetid: 4bca8d34-12af-4f7c-8888-b0466a745704
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessConfiguration class
- RemoteAccessConfiguration class, described
topic_type:
- apiref
api_name:
- RemoteAccessConfiguration
- RemoteAccessConfiguration.Version
- RemoteAccessConfiguration.RemoteAccessCapacityKbps
- RemoteAccessConfiguration.RoutingDomainConfig
- RemoteAccessConfiguration.S2SInterfaceConfiguration
- RemoteAccessConfiguration.VSIDs
- RemoteAccessConfiguration.GlobalIpv4TransportInfo
- RemoteAccessConfiguration.GlobalIpv6TransportInfo
- RemoteAccessConfiguration.ServerAuthConfig
- RemoteAccessConfiguration.ServerIpSecConfiguration
- RemoteAccessConfiguration.RadiusServerConfigs
- RemoteAccessConfiguration.RadiusAccountingStatus
- RemoteAccessConfiguration.VPNAuthType
- RemoteAccessConfiguration.BGPPeerConfig
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessConfiguration class

Manages a Remote Access configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessConfiguration
{
  uint32                                 Version;
  uint64                                 RemoteAccessCapacityKbps;
  RemoteAccessRoutingDomainConfiguration RoutingDomainConfig[];
  RemoteAccessS2SConfiguration           S2SInterfaceConfiguration[];
  VSIDConfiguration                      VSIDs[];
  uint8                                  GlobalIpv4TransportInfo[];
  uint8                                  GlobalIpv6TransportInfo[];
  RemoteAccessServerAuthConfiguration    ServerAuthConfig;
  object                                 ServerIpSecConfiguration;
  RemoteAccessRadiusConfig               RadiusServerConfigs[];
  string                                 RadiusAccountingStatus;
  string                                 VPNAuthType;
  RemoteAccessBgpPeerConfig              BGPPeerConfig[];
};
```

## Members

The **RemoteAccessConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessConfiguration** class has these properties.

<dl> <dt>

**BGPPeerConfig**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessBgpPeerConfig** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessBgpPeerConfig**](remoteaccessbgppeerconfig.md)")
</dt> </dl>

A [**RemoteAccessBgpPeerConfig**](remoteaccessbgppeerconfig.md) embedded instance

</dd> <dt>

**GlobalIpv4TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The global IPv4 transport information

</dd> <dt>

**GlobalIpv6TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The global IPv6 transport information

</dd> <dt>

**RadiusAccountingStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The status of the RADIUS accounting configuration.

</dd> <dt>

**RadiusServerConfigs**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessRadiusConfig** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessRadiusConfig**](remoteaccessradiusconfig.md)")
</dt> </dl>

The Remote Authentication Dial In User Service (RADIUS) server configuration as a [**RemoteAccessRadiusConfig**](remoteaccessradiusconfig.md) embedded instance

</dd> <dt>

**RemoteAccessCapacityKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bandwidth limit for remote access clients, in kbps.

</dd> <dt>

**RoutingDomainConfig**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessRoutingDomainConfiguration** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessRoutingDomainConfiguration**](remoteaccessroutingdomainconfiguration.md)")
</dt> </dl>

A [**RemoteAccessRoutingDomainConfiguration**](remoteaccessroutingdomainconfiguration.md) embedded instance

</dd> <dt>

**S2SInterfaceConfiguration**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessS2SConfiguration** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessS2SConfiguration**](remoteaccesss2sconfiguration.md)")
</dt> </dl>

A [**RemoteAccessS2SConfiguration**](remoteaccesss2sconfiguration.md) embedded instance

</dd> <dt>

**ServerAuthConfig**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessServerAuthConfiguration**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessServerAuthConfiguration**](remoteaccessserverauthconfiguration.md)")
</dt> </dl>

A [**RemoteAccessServerAuthConfiguration**](remoteaccessserverauthconfiguration.md) embedded instance

</dd> <dt>

**ServerIpSecConfiguration**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

The server IPsec configuration as an embedded object

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Remote Access configuration

</dd> <dt>

**VPNAuthType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authentication type for VPNs

</dd> <dt>

**VSIDs**
</dt> <dd> <dl> <dt>

Data type: **VSIDConfiguration** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VSIDConfiguration**](vsidconfiguration.md)")
</dt> </dl>

The Virtual Subnet ID (VSID) configuration as a [**VSIDConfiguration**](vsidconfiguration.md) embedded instance

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

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





