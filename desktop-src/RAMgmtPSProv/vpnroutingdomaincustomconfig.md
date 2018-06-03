---
title: VpnRoutingDomainCustomConfig class
description: Represents a custom Internet Protocol Security (IPsec) configuration for a routing domain.
audience: developer
ms.assetid: 11e5b6d6-9162-4e16-9dbe-21673e35e874
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnRoutingDomainCustomConfig class
- VpnRoutingDomainCustomConfig class, described
topic_type:
- apiref
api_name:
- VpnRoutingDomainCustomConfig
- VpnRoutingDomainCustomConfig.RoutingDomain
- VpnRoutingDomainCustomConfig.RoutingDomainID
- VpnRoutingDomainCustomConfig.RoutingDomainStatus
- VpnRoutingDomainCustomConfig.VpnStatus
- VpnRoutingDomainCustomConfig.VpnS2SStatus
- VpnRoutingDomainCustomConfig.RoutingStatus
- VpnRoutingDomainCustomConfig.EnableQoS
- VpnRoutingDomainCustomConfig.TxBandwidthKbps
- VpnRoutingDomainCustomConfig.RxBandwidthKbps
- VpnRoutingDomainCustomConfig.IPAddressRange
- VpnRoutingDomainCustomConfig.IPv6Prefix
- VpnRoutingDomainCustomConfig.AvailabilityStatus
- VpnRoutingDomainCustomConfig.InterimAccountingPeriodSec
- VpnRoutingDomainCustomConfig.DnsIPAddress
- VpnRoutingDomainCustomConfig.NetBiosIPAddress
- VpnRoutingDomainCustomConfig.MaximumVpnConnections
- VpnRoutingDomainCustomConfig.TenantName
- VpnRoutingDomainCustomConfig.CustomPolicy
- VpnRoutingDomainCustomConfig.EncryptionMethod
- VpnRoutingDomainCustomConfig.IntegrityCheckMethod
- VpnRoutingDomainCustomConfig.CipherTransformConstant
- VpnRoutingDomainCustomConfig.PfsGroup
- VpnRoutingDomainCustomConfig.AuthenticationTransformConstant
- VpnRoutingDomainCustomConfig.DHGroup
- VpnRoutingDomainCustomConfig.IdleDisconnectSec
- VpnRoutingDomainCustomConfig.SaLifeTimeSec
- VpnRoutingDomainCustomConfig.SaRenegotiationDataSizeKB
- VpnRoutingDomainCustomConfig.MMSaLifeTimeSec
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VpnRoutingDomainCustomConfig class

Represents a custom Internet Protocol Security (IPsec) configuration for a routing domain

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnRoutingDomainCustomConfig : VpnRoutingDomainConfig
{
  string  RoutingDomain;
  string  RoutingDomainID;
  string  RoutingDomainStatus;
  uint32  VpnStatus;
  uint32  VpnS2SStatus;
  uint32  RoutingStatus;
  uint32  EnableQoS;
  uint64  TxBandwidthKbps;
  uint64  RxBandwidthKbps;
  string  IPAddressRange[];
  string  IPv6Prefix;
  string  AvailabilityStatus;
  uint32  InterimAccountingPeriodSec;
  string  DnsIPAddress[];
  string  NetBiosIPAddress[];
  uint32  MaximumVpnConnections;
  string  TenantName[];
  boolean CustomPolicy;
  uint32  EncryptionMethod;
  uint32  IntegrityCheckMethod;
  uint32  CipherTransformConstant;
  uint32  PfsGroup;
  uint32  AuthenticationTransformConstant;
  uint32  DHGroup;
  uint32  IdleDisconnectSec;
  uint32  SaLifeTimeSec;
  uint32  SaRenegotiationDataSizeKB;
  uint32  MMSaLifeTimeSec;
};
```

## Members

The **VpnRoutingDomainCustomConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnRoutingDomainCustomConfig** class has these properties.

<dl> <dt>

**AuthenticationTransformConstant**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authentication transform of the IPsec policy

</dd> <dt>

**AvailabilityStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The availability status of the routing domain

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**CipherTransformConstant**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The cipher algorithm of the IPsec policy

</dd> <dt>

**CustomPolicy**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The custom Internet Key Exchange (IKE) policy

</dd> <dt>

**DHGroup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Diffie-Hellman (DH) group of the IPsec policy

</dd> <dt>

**DnsIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS server IP addresses for VPN clients

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**EnableQoS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether QoS is enabled for VPN

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The encryption method of the IKE policy

</dd> <dt>

**IdleDisconnectSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time after which an idle connection is terminated, in seconds

</dd> <dt>

**IntegrityCheckMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The integrity method of the IPsec policy

</dd> <dt>

**InterimAccountingPeriodSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The interval in which to log interim accounting, in seconds

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**IPAddressRange**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of the start and end IP addresses for the IP address range of the routing domain

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**IPv6Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 prefix for address assignment

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**MaximumVpnConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of VPN connections allowed in the VPN routing domain

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**MMSaLifeTimeSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of main mode security association (SA) after which the MM SA is no longer valid, in seconds

**Windows Server 2012 R2:** This property is not available before Windows Server 2016.

</dd> <dt>

**NetBiosIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Network Basic Input/Output System (NetBIOS) Server IP addresses for VPN clients

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**PfsGroup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The perfect forward secrecy (PFS) group

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly Name of the routing domain

This property is inherited from [**RoutingDomainConfiguration**](routingdomainconfiguration.md).

</dd> <dt>

**RoutingDomainID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the routing domain

This property is inherited from [**RoutingDomainConfiguration**](routingdomainconfiguration.md).

</dd> <dt>

**RoutingDomainStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the routing domain

This property is inherited from [**RoutingDomainConfiguration**](routingdomainconfiguration.md).

</dd> <dt>

**RoutingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The routing status for the routing domain

This property is inherited from [**RoutingDomainConfiguration**](routingdomainconfiguration.md).

</dd> <dt>

**RxBandwidthKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The incoming bandwidth limit for VPN, in kbps.

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**SaLifeTimeSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The lifetime of a security association (SA) after which the SA becomes invalid, in seconds

</dd> <dt>

**SaRenegotiationDataSizeKB**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The transfer limit for an SA after which the SA will be renegotiated, in kilobytes

</dd> <dt>

**TenantName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the tenant for the VPN routing domain

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**TxBandwidthKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The outgoing bandwidth limit for VPN, in kbps.

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

</dd> <dt>

**VpnS2SStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The site-to-site (S2S) status for the routing domain

This property is inherited from [**RoutingDomainConfiguration**](routingdomainconfiguration.md).

</dd> <dt>

**VpnStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The VPN status for the routing domain

This property is inherited from [**RoutingDomainConfiguration**](routingdomainconfiguration.md).

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

[**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md)
</dt> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





