---
title: Add method of the PS\_BgpPeer class
description: Adds a BGP peer to a BGP router.
audience: developer
ms.assetid: 2acd3cba-7a37-45e4-b5cd-6d40bd861af6
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_BgpPeer class
- PS_BgpPeer class, Add method
topic_type:
- apiref
api_name:
- PS_BgpPeer.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_BgpPeer class

Adds a BGP peer to a BGP router.

## Syntax


```mof
uint32 Add(
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
  [in]  boolean       PassThru,
  [in]  string        RoutingDomain,
  [out] BgpPeerConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the peer to add.

</dd> <dt>

*LocalIPAddress* \[in\]
</dt> <dd>

The IP address of the local BGP router.

</dd> <dt>

*PeerIPAddress* \[in\]
</dt> <dd>

The IP address of the BGP router for the new peer.

</dd> <dt>

*LocalASN* \[in\]
</dt> <dd>

The Autonomous System Number (ASN) of the local BGP router instance.

</dd> <dt>

*PeerASN* \[in\]
</dt> <dd>

The ASN of the BGP Router instance for the new peer.

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

An enumeration parameter that specifies the peering mode for the new peer.

</dd> <dt>

*HoldTimeSec* \[in\]
</dt> <dd>

The duration, in seconds, before a BGP session expires after a BGP message is received.

</dd> <dt>

*IdleHoldTimeSec* \[in\]
</dt> <dd>

The duration, in seconds, before a BGP session expires due to inactivity.

**Windows Server 2012:** This parameter is not supported before Windows Server 2012 R2.

</dd> <dt>

*Weight* \[in\]
</dt> <dd>

The administrative preference assigned to the routes of the new peer.

</dd> <dt>

*RouteReflectorClient* \[in\]
</dt> <dd>

Whether the peer is a client peer or non-client peer.

**Windows Server 2012 R2:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*MaxAllowedPrefix* \[in\]
</dt> <dd>

The maximum number IP network prefixes that the local BGP router can learn from the new peer.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the cmdlet returns an output object. **True** to return an output object; otherwise **false**.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

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

 

 





