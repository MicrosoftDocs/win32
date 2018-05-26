---
title: Set method of the PS\_BgpPeer class
description: Updates the configuration of the specified BGP peer.
audience: developer
ms.assetid: 46a5d9ff-e870-480e-ad04-0cde22e0175f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_BgpPeer class
- PS_BgpPeer class, Set method
topic_type:
- apiref
api_name:
- PS_BgpPeer.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_BgpPeer class

Updates the configuration of the specified BGP peer.

## Syntax


```mof
uint32 Set(
  [in]  string        Name,
  [in]  string        LocalIPAddress,
  [in]  string        PeerIPAddress,
  [in]  uint32        LocalASN,
  [in]  uint32        PeerASN,
  [in]  uint32        OperationMode,
  [in]  uint32        PeeringMode,
  [in]  uint16        HoldTimeSec,
  [in]  uint16        IdleHoldTimeSec,
  [in]  uint16        Weight,
  [in]  boolean       RouteReflectorClient,
  [in]  uint32        MaxAllowedPrefix,
  [in]  string        RoutingDomain,
  [in]  boolean       PassThru,
  [in]  boolean       Force,
  [in]  boolean       ClearPrefixLimit,
  [out] BgpPeerConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the peer to update.

</dd> <dt>

*LocalIPAddress* \[in\]
</dt> <dd>

The IP address of the local BGP router.

</dd> <dt>

*PeerIPAddress* \[in\]
</dt> <dd>

The IP address of the BGP router for the peer.

</dd> <dt>

*LocalASN* \[in\]
</dt> <dd>

The Autonomous System Number (ASN) of the local BGP router instance.

</dd> <dt>

*PeerASN* \[in\]
</dt> <dd>

The ASN of the BGP router instance for the peer.

</dd> <dt>

*OperationMode* \[in\]
</dt> <dd>

The mode of operation for the local BGP router. You must set this parameter to one of the following values.

<dt>

1
</dt> <dd>

Initiates and accepts peering requests.

</dd> <dt>

2
</dt> <dd>

Passively accepts peering requests.

</dd> </dl> </dd> <dt>

*PeeringMode* \[in\]
</dt> <dd>

An enumeration parameter that specifies the peering mode for the peer.

</dd> <dt>

*HoldTimeSec* \[in\]
</dt> <dd>

Configured value of the HoldTime in seconds after which the BGP Session expires if no BGP message is received.

</dd> <dt>

*IdleHoldTimeSec* \[in\]
</dt> <dd>

The duration, in seconds, before a BGP session expires due to inactivity.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

The administrative preference assigned to the routes of the peer.

</dd> <dt>

*RouteReflectorClient* \[in\]
</dt> <dd>

Whether the peer is a client peer or non-client peer.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*MaxAllowedPrefix* \[in\]
</dt> <dd>

The maximum number IP network prefixes that the local BGP router can learn from the peer.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the cmdlet returns an output object. **True** to return an output object; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to use a confirmation prompt to modify the configuration of the peer. **True** to use a confirmation prompt; otherwise **false**.

</dd> <dt>

*ClearPrefixLimit* \[in\]
</dt> <dd>

Indicates whether an unlimited number of network prefixes is to be learned from the peer. **True** to learn an unlimited number of network prefixes; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpPeerConfig**](bgppeerconfig.md) object that receives the additional BGP peer.

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

[**PS\_BgpPeer**](ps-bgppeer.md)
</dt> </dl>

 

 





