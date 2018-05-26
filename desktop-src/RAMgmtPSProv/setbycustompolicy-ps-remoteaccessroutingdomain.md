---
title: SetByCustomPolicy method of the PS\_RemoteAccessRoutingDomain class
description: Updates site-to-site (S2S) VPN settings for a custom routing domain configuration.
audience: developer
ms.assetid: 737d5cdb-a9ea-4697-9428-2523b23b9282
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByCustomPolicy method
- SetByCustomPolicy method, PS_RemoteAccessRoutingDomain class
- PS_RemoteAccessRoutingDomain class, SetByCustomPolicy method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRoutingDomain.SetByCustomPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByCustomPolicy method of the PS\_RemoteAccessRoutingDomain class

Updates site-to-site (S2S) VPN settings for a custom routing domain configuration.

## Syntax


```mof
uint32 SetByCustomPolicy(
  [in]  string                 Name,
  [in]  uint32                 IdleDisconnectSec,
  [in]  uint32                 InterimAccountingPeriodSec,
  [in]  string                 IPAddressRange[],
  [in]  string                 IPv6Prefix,
  [in]  uint32                 SaLifeTimeSec,
  [in]  uint32                 MMSaLifeTimeSec,
  [in]  string                 NetBiosIPAddress[],
  [in]  uint32                 MaximumVpnConnections,
  [in]  string                 TenantName[],
  [in]  boolean                PassThru,
  [in]  boolean                Force,
  [in]  uint32                 EnableQoS,
  [in]  uint64                 TxBandwidthKbps,
  [in]  uint64                 RxBandwidthKbps,
  [in]  string                 DnsIPAddress[],
  [in]  boolean                CustomPolicy,
  [in]  uint32                 AuthenticationTransformConstant,
  [in]  uint32                 CipherTransformConstant,
  [in]  uint32                 EncryptionMethod,
  [in]  uint32                 IntegrityCheckMethod,
  [in]  uint32                 PfsGroup,
  [in]  uint32                 SaRenegotiationDataSizeKB,
  [in]  uint32                 DHGroup,
  [out] VpnRoutingDomainConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the routing domain.

</dd> <dt>

*IdleDisconnectSec* \[in\]
</dt> <dd>

The time, in seconds, after which an idle connection is terminated.

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

*SaLifeTimeSec* \[in\]
</dt> <dd>

Lifetime of a security association (SA) in seconds, after which the SA is no longer valid .

</dd> <dt>

*MMSaLifeTimeSec* \[in\]
</dt> <dd>

Lifetime of main mode security association (SA) in seconds, after which the MM SA is no longer valid.

**Windows Server 2012 R2:** This property is not supported before Windows Server 2016.

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

*CustomPolicy* \[in\]
</dt> <dd>

Indicates whether to use a custom Internet Key Exchange (IKE) Internet Protocol Security (IPsec) policy. **True** to use a custom IKE policy; otherwise **false**.

</dd> <dt>

*AuthenticationTransformConstant* \[in\]
</dt> <dd>

The authentication transform value for the IPsec policy.

</dd> <dt>

*CipherTransformConstant* \[in\]
</dt> <dd>

The cipher transform value for the IPsec policy.

</dd> <dt>

*EncryptionMethod* \[in\]
</dt> <dd>

The encryption method for the IKE policy.

</dd> <dt>

*IntegrityCheckMethod* \[in\]
</dt> <dd>

The integrity method for the IPsec policy.

</dd> <dt>

*PfsGroup* \[in\]
</dt> <dd>

The perfect forward secrecy (PFS) Group for the IPsec policy.

</dd> <dt>

*SaRenegotiationDataSizeKB* \[in\]
</dt> <dd>

The amount of data, in kilobytes, to transfer using an SA before the SA is renegotiated.

</dd> <dt>

*DHGroup* \[in\]
</dt> <dd>

The Diffie-Hellman (DH) Group for the IPsec policy.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md) object that receives the VPN settings.

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

[**PS\_RemoteAccessRoutingDomain**](ps-remoteaccessroutingdomain.md)
</dt> </dl>

 

 





