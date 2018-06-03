---
title: RemoteAccessRoutingDomainConfiguration class
description: A Remote Access routing domain configuration.
audience: developer
ms.assetid: 5469f10c-34e1-43b6-924c-e399a523bef2
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessRoutingDomainConfiguration class
- RemoteAccessRoutingDomainConfiguration class, described
topic_type:
- apiref
api_name:
- RemoteAccessRoutingDomainConfiguration
- RemoteAccessRoutingDomainConfiguration.RoutingDomainConfig
- RemoteAccessRoutingDomainConfiguration.Ipv4TransportInfo
- RemoteAccessRoutingDomainConfiguration.Ipv6TransportInfo
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessRoutingDomainConfiguration class

A Remote Access routing domain configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessRoutingDomainConfiguration
{
  object RoutingDomainConfig;
  uint8  Ipv4TransportInfo[];
  uint8  Ipv6TransportInfo[];
};
```

## Members

The **RemoteAccessRoutingDomainConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessRoutingDomainConfiguration** class has these properties.

<dl> <dt>

**Ipv4TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4 transport information of the routing domain

</dd> <dt>

**Ipv6TransportInfo**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 transport information of the routing domain

</dd> <dt>

**RoutingDomainConfig**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

The configuration of the routing domain as an embedded object

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

 

 





