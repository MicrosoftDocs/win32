---
title: SetByEncryptionType method of the PS\_RemoteAccessRoutingDomain class
description: Updates the site-to-site (S2S) VPN settings for the specified encryption type.
audience: developer
ms.assetid: '03e44d61-9626-48be-ba8b-f89ec1655470'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByEncryptionType method", "SetByEncryptionType method, PS_RemoteAccessRoutingDomain class", "PS_RemoteAccessRoutingDomain class, SetByEncryptionType method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessRoutingDomain.SetByEncryptionType
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# SetByEncryptionType method of the PS\_RemoteAccessRoutingDomain class

Updates the site-to-site (S2S) VPN settings for the specified encryption type.

## Syntax


```mof
uint32 SetByEncryptionType(
  [in]  string                 Name,
  [in]  uint32                 InterimAccountingPeriodSec,
  [in]  string                 IPAddressRange[],
  [in]  string                 IPv6Prefix,
  [in]  string                 NetBiosIPAddress[],
  [in]  uint32                 MaximumVpnConnections,
  [in]  string                 TenantName[],
  [in]  boolean                PassThru,
  [in]  boolean                Force,
  [in]  uint32                 EnableQoS,
  [in]  uint64                 TxBandwidthKbps,
  [in]  uint64                 RxBandwidthKbps,
  [in]  string                 DnsIPAddress[],
  [in]  string                 EncryptionType,
  [out] VpnRoutingDomainConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the routing domain.

</dd> <dt>

*InterimAccountingPeriodSec* \[in\]
</dt> <dd>

The interval, in seconds, at which to log interim accounting.

</dd> <dt>

*IPAddressRange* \[in\]
</dt> <dd>

An array that contains the start and end IP addresses that specify the range of IP addresses to allocate to VPN clients.

</dd> <dt>

*IPv6Prefix* \[in\]
</dt> <dd>

The IPv6 prefix to assign to VPN clients. If this parameter is set to Null, it will disable IPv6 VPN connections to the tenant.

</dd> <dt>

*NetBiosIPAddress* \[in\]
</dt> <dd>

An array that contains the Network Basic Input/Output System (NetBIOS) server IP addresses for VPN clients.

</dd> <dt>

*MaximumVpnConnections* \[in\]
</dt> <dd>

The maximum number of VPN connections for the routing domain.

</dd> <dt>

*TenantName* \[in\]
</dt> <dd>

An array that contains the tenant names that host the routing domain.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns and object.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether this method uses the default confirmation prompt before performing the operation. **True** to use the default confirmation prompt, otherwise **false**. The default value for this parameter is **True**.

</dd> <dt>

*EnableQoS* \[in\]
</dt> <dd>

Indicates whether QoS is enabled on the network interface. 0 to enable QoS; otherwise 1.

</dd> <dt>

*TxBandwidthKbps* \[in\]
</dt> <dd>

The bandwidth limit for outgoing traffic from the VPN interface, in kbps.

</dd> <dt>

*RxBandwidthKbps* \[in\]
</dt> <dd>

The bandwidth limit for incoming traffic to the VPN interface, in kbps.

</dd> <dt>

*DnsIPAddress* \[in\]
</dt> <dd>

An array that contains the IP addresses of the Domain Name System (DNS) servers.

</dd> <dt>

*EncryptionType* \[in\]
</dt> <dd>

The encryption type for the VPN settings.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md) object that receives the VPN settings.

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

[**PS\_RemoteAccessRoutingDomain**](ps-remoteaccessroutingdomain.md)
</dt> </dl>

 

 





