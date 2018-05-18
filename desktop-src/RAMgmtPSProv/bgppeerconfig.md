---
title: BgpPeerConfig class
description: Retrieves information about a peer configuration of a Border Gateway Protocol (BGP) router.
audience: developer
ms.assetid: 'f4f0c9bc-7bb9-43d4-b7ed-51fbd5f589ef'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["BgpPeerConfig class", "BgpPeerConfig class, described"]
topic_type:
- apiref
api_name:
- BgpPeerConfig
- BgpPeerConfig.RoutingDomain
- BgpPeerConfig.PeerName
- BgpPeerConfig.LocalIPAddress
- BgpPeerConfig.PeerIPAddress
- BgpPeerConfig.LocalASN
- BgpPeerConfig.PeerASN
- BgpPeerConfig.OperationMode
- BgpPeerConfig.PeeringMode
- BgpPeerConfig.HoldTimeSec
- BgpPeerConfig.IdleHoldTimeSec
- BgpPeerConfig.Weight
- BgpPeerConfig.ConnectivityStatus
- BgpPeerConfig.IngressPolicyList
- BgpPeerConfig.EgressPolicyList
- BgpPeerConfig.MaxAllowedPrefix
- BgpPeerConfig.RouteReflectorClient
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# BgpPeerConfig class

Retrieves information about a peer configuration of a Border Gateway Protocol (BGP) router.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpPeerConfig
{
  string  RoutingDomain;
  string  PeerName;
  string  LocalIPAddress;
  string  PeerIPAddress;
  uint32  LocalASN;
  uint32  PeerASN;
  uint32  OperationMode;
  uint32  PeeringMode;
  uint16  HoldTimeSec;
  uint16  IdleHoldTimeSec;
  uint16  Weight;
  uint32  ConnectivityStatus;
  string  IngressPolicyList[];
  string  EgressPolicyList[];
  uint32  MaxAllowedPrefix;
  boolean RouteReflectorClient;
};
```

## Members

The **BgpPeerConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpPeerConfig** class has these properties.

<dl> <dt>

**ConnectivityStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the peer connection.

</dd> <dt>

**EgressPolicyList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of policy IDs that are applied to outgoing BGP route advertisements

</dd> <dt>

**HoldTimeSec**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When a BGP Session expires due to a lack of response from the peer, in seconds.

</dd> <dt>

**IdleHoldTimeSec**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When a BGP Session expires due to a lack of activity, in seconds.

</dd> <dt>

**IngressPolicyList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The list of policy IDs that are applied to incoming BGP route advertisements.

</dd> <dt>

**LocalASN**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local Autonomous System Number (ASN) of the BGP router instance that connects with the peer.

</dd> <dt>

**LocalIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local IP address of the BGP router.

</dd> <dt>

**MaxAllowedPrefix**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of IPv4 / IPv6 network prefixes that a neighbor is allowed to learn.

</dd> <dt>

**OperationMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The mode of operation of the BGP router.

</dd> <dt>

**PeerASN**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ASN of the peer BGP router.

</dd> <dt>

**PeeringMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether manual peering mode is enabled for the peer.

</dd> <dt>

**PeerIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the peer BGP router.

</dd> <dt>

**PeerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined alphanumeric ID for the peer.

</dd> <dt>

**RouteReflectorClient**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether peer is a client peer or non-client peer.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined alphanumeric ID of the BGP routing domain.

> [!Note]  
> This property is only used with multi-tenant deployments.

 

</dd> <dt>

**Weight**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The administrative preferences that are assigned to peer routes.

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

 

 





