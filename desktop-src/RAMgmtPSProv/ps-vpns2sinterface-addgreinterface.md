---
title: AddGREInterface method of the PS\_VpnS2SInterface class
description: Creates an S2S interface.
audience: developer
ms.assetid: 597727AF-A40A-4D1F-95DF-71D9E09E0534
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddGREInterface method
- AddGREInterface method, PS_VpnS2SInterface interface
- PS_VpnS2SInterface interface, AddGREInterface method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddGREInterface method of the PS\_VpnS2SInterface class

Creates an S2S interface.

## Syntax


```mof
static uint32 AddGREInterface(
  [in]  string          Name,
  [in]  uint32          GreKey,
  [in]  string          Destination[],
  [in]  boolean         AdminStatus,
  [in]  uint32          EnableQoS,
  [in]  uint64          TxBandwidthKbps,
  [in]  uint64          RxBandwidthKbps,
  [in]  string          IPv4Subnet[],
  [in]  string          IPv6Subnet[],
  [in]  boolean         PassThru,
  [in]  string          RoutingDomain,
  [in]  boolean         InternalIPv4,
  [in]  boolean         InternalIPv6,
  [in]  string          IPv4Address,
  [in]  string          IPv6Address,
  [in]  string          SourceIpAddress,
  [in]  boolean         GreTunnel,
  [out] VpnS2SInterface cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the connection.

</dd> <dt>

*GreKey* \[in\]
</dt> <dd>

The GRE key for this interface.

</dd> <dt>

*Destination* \[in\]
</dt> <dd>

The destination end-point of the S2S connection.

</dd> <dt>

*AdminStatus* \[in\]
</dt> <dd>

The admin status of the cmdlet.

</dd> <dt>

*EnableQoS* \[in\]
</dt> <dd>

Whether QoS is enabled on the interface.

</dd> <dt>

*TxBandwidthKbps* \[in\]
</dt> <dd>

The transmit bandwidth limit for the interface, in kbps.

</dd> <dt>

*RxBandwidthKbps* \[in\]
</dt> <dd>

The receive bandwidth limit for the interface, in kbps.

</dd> <dt>

*IPv4Subnet* \[in\]
</dt> <dd>

The IPv4 subnet that is routed on this connection.

</dd> <dt>

*IPv6Subnet* \[in\]
</dt> <dd>

The IPv6 subnet that is routed on this connection.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Set **True** to return the object or objects on which the operation is done.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The routing domain name to which the interface is added.

</dd> <dt>

*InternalIPv4* \[in\]
</dt> <dd>

Specifies Negotiation of IPv4 Address.

</dd> <dt>

*InternalIPv6* \[in\]
</dt> <dd>

Specifies Negotiation of IPv6 Address.

</dd> <dt>

*IPv4Address* \[in\]
</dt> <dd>

The IPv4 address for this interface.

</dd> <dt>

*IPv6Address* \[in\]
</dt> <dd>

The IPv6 address for this interface.

</dd> <dt>

*SourceIpAddress* \[in\]
</dt> <dd>

The IP address of the interface.

</dd> <dt>

*GreTunnel* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterface**](ps-vpns2sinterface.md)
</dt> </dl>

 

 





