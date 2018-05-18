---
title: BgpRouteInfo class
description: Retrieves the configuration of a Border Gateway Protocol (BGP) route.
audience: developer
ms.assetid: '8c065e49-eb6f-4a19-a697-a12d19edebb7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["BgpRouteInfo class", "BgpRouteInfo class, described"]
topic_type:
- apiref
api_name:
- BgpRouteInfo
- BgpRouteInfo.RoutingDomain
- BgpRouteInfo.Network
- BgpRouteInfo.NextHop
- BgpRouteInfo.Origin
- BgpRouteInfo.ASPath
- BgpRouteInfo.LocalPref
- BgpRouteInfo.Community
- BgpRouteInfo.MED
- BgpRouteInfo.LearnedFromPeer
- BgpRouteInfo.State
- BgpRouteInfo.ClusterList
- BgpRouteInfo.OriginatorId
- BgpRouteInfo.Aggregator
- BgpRouteInfo.Aggregate
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# BgpRouteInfo class

Retrieves the configuration of a Border Gateway Protocol (BGP) route.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpRouteInfo
{
  string        RoutingDomain;
  string        Network;
  string        NextHop;
  string        Origin;
  ASPathSegment ASPath[];
  uint32        LocalPref;
  string        Community[];
  uint32        MED;
  string        LearnedFromPeer;
  uint32        State[];
  uint32        ClusterList[];
  string        OriginatorId;
  string        Aggregator;
  boolean       Aggregate;
};
```

## Members

The **BgpRouteInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpRouteInfo** class has these properties.

<dl> <dt>

**Aggregate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the route is an aggregate route.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**Aggregator**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains the 2 byte ASN\|IpAddress of the aggregating node in case the route is an aggregated route

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**ASPath**
</dt> <dd> <dl> <dt>

Data type: **ASPathSegment** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**ASPathSegment**](aspathsegment.md)")
</dt> </dl>

An array of the Autonomous System Numbers (ASN) of the autonomous system (AS) path of the BGP route.

</dd> <dt>

**ClusterList**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Cluster Ids that make up the cluster list of the route.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**Community**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The community attribute values associated with the prefix of the BGP route.

</dd> <dt>

**LearnedFromPeer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The PeerID that indicates the origin of the of the prefix of the BGP route.

</dd> <dt>

**LocalPref**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local preference value of the BGP route.

</dd> <dt>

**MED**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The multi-exit discriminator (MED) of the BGP route.

</dd> <dt>

**Network**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of the IPv4 or IPv6 network address from the BGP router's Local Routing Information Base (Local-RIB), and the network mask for the Classless Inter-Domain Routing (CIDR) network address.

</dd> <dt>

**NextHop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the next hop on the destination network

</dd> <dt>

**Origin**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path origin type of the destination network.

The possible values are.

<dt>

<span id="IGP"></span><span id="igp"></span>

**IGP** ("IGP")


</dt> <dd></dd> <dt>

<span id="EGP"></span><span id="egp"></span>

**EGP** ("EGP")


</dt> <dd></dd> <dt>

<span id="INCOMPLETE"></span><span id="incomplete"></span>

**INCOMPLETE** ("INCOMPLETE")


</dt> <dd></dd> </dl>

</dd> <dt>

**OriginatorId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The BGP identifier of the originator of the route in the local autonomous system (AS).

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined alphanumeric ID of the network's routing domain.

> [!Note]  
> This property is only used with multi-tenant deployments.

 

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A flag that indicates the state of route.

Examples: BestPath or Suppressed

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





