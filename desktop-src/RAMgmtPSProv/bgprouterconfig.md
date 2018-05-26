---
title: BgpRouterConfig class
description: Retrieves the routing domain configuration of a Border Gateway Protocol (BGP) router.
audience: developer
ms.assetid: 2bc56cd9-96b1-42a1-8a3d-c3c756f1b9e2
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BgpRouterConfig class
- BgpRouterConfig class, described
topic_type:
- apiref
api_name:
- BgpRouterConfig
- BgpRouterConfig.RoutingDomain
- BgpRouterConfig.BgpIdentifier
- BgpRouterConfig.LocalASN
- BgpRouterConfig.IPv6Routing
- BgpRouterConfig.LocalIPv6Address
- BgpRouterConfig.CompareMEDAcrossASN
- BgpRouterConfig.DefaultGatewayRouting
- BgpRouterConfig.PeerName
- BgpRouterConfig.PolicyName
- BgpRouterConfig.TransitRouting
- BgpRouterConfig.RouteReflector
- BgpRouterConfig.ClusterId
- BgpRouterConfig.ClientToClientReflection
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BgpRouterConfig class

Retrieves the routing domain configuration of a Border Gateway Protocol (BGP) router.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpRouterConfig
{
  string  RoutingDomain;
  string  BgpIdentifier;
  uint32  LocalASN;
  uint32  IPv6Routing;
  string  LocalIPv6Address;
  boolean CompareMEDAcrossASN;
  boolean DefaultGatewayRouting;
  string  PeerName[];
  string  PolicyName[];
  uint32  TransitRouting;
  uint32  RouteReflector;
  uint32  ClusterId;
  uint32  ClientToClientReflection;
};
```

## Members

The **BgpRouterConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpRouterConfig** class has these properties.

<dl> <dt>

**BgpIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The 4 byte local ID of the BGP router.

</dd> <dt>

**ClientToClientReflection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether client to client reflection is enabled.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ClusterId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cluster id of the route reflector.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**CompareMEDAcrossASN**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the BGP router compares multi-exit discriminator (MED) values across different autonomous systems.

</dd> <dt>

**DefaultGatewayRouting**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether unresolved routes are routed to the default internet gateway.

</dd> <dt>

**IPv6Routing**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPv6 capability announcement state of BGP router.

</dd> <dt>

**LocalASN**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local Autonomous System Number (ASN) of the BGP router.

</dd> <dt>

**LocalIPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local peering IPv6 address of the BGP router.

</dd> <dt>

**PeerName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of peer names that are configured for this tenant.

</dd> <dt>

**PolicyName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of policy names that are configured for this tenant.

</dd> <dt>

**RouteReflector**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the Bgp router will act as a route reflector.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user defined alphanumeric ID of the routing domain.

> [!Note]  
> This property is only used with multi-tenant deployments.

 

</dd> <dt>

**TransitRouting**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether transit routing is enabled.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

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

 

 





