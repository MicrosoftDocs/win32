---
title: VpnRoutingDomainDefaultConfig class
description: Represents the default routing domain IPsec configuration.
audience: developer
ms.assetid: '5c2dcfc9-ff84-42c6-a9ca-759bdcd9661b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnRoutingDomainDefaultConfig class", "VpnRoutingDomainDefaultConfig class, described"]
topic_type:
- apiref
api_name:
- VpnRoutingDomainDefaultConfig
- VpnRoutingDomainDefaultConfig.RoutingDomain
- VpnRoutingDomainDefaultConfig.RoutingDomainID
- VpnRoutingDomainDefaultConfig.RoutingDomainStatus
- VpnRoutingDomainDefaultConfig.VpnStatus
- VpnRoutingDomainDefaultConfig.VpnS2SStatus
- VpnRoutingDomainDefaultConfig.RoutingStatus
- VpnRoutingDomainDefaultConfig.EnableQoS
- VpnRoutingDomainDefaultConfig.TxBandwidthKbps
- VpnRoutingDomainDefaultConfig.RxBandwidthKbps
- VpnRoutingDomainDefaultConfig.IPAddressRange
- VpnRoutingDomainDefaultConfig.IPv6Prefix
- VpnRoutingDomainDefaultConfig.AvailabilityStatus
- VpnRoutingDomainDefaultConfig.InterimAccountingPeriodSec
- VpnRoutingDomainDefaultConfig.DnsIPAddress
- VpnRoutingDomainDefaultConfig.NetBiosIPAddress
- VpnRoutingDomainDefaultConfig.MaximumVpnConnections
- VpnRoutingDomainDefaultConfig.TenantName
- VpnRoutingDomainDefaultConfig.EncryptionType
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnRoutingDomainDefaultConfig class

Represents the default routing domain IPsec configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnRoutingDomainDefaultConfig : VpnRoutingDomainConfig
{
  string RoutingDomain;
  string RoutingDomainID;
  string RoutingDomainStatus;
  uint32 VpnStatus;
  uint32 VpnS2SStatus;
  uint32 RoutingStatus;
  uint32 EnableQoS;
  uint64 TxBandwidthKbps;
  uint64 RxBandwidthKbps;
  string IPAddressRange[];
  string IPv6Prefix;
  string AvailabilityStatus;
  uint32 InterimAccountingPeriodSec;
  string DnsIPAddress[];
  string NetBiosIPAddress[];
  uint32 MaximumVpnConnections;
  string TenantName[];
  string EncryptionType;
};
```

## Members

The **VpnRoutingDomainDefaultConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnRoutingDomainDefaultConfig** class has these properties.

<dl> <dt>

**AvailabilityStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The availability status of the routing domain

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

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

**EncryptionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Sets the type of encryption to use.

The possible values are.

<dt>

<span id="MaximumEncryption"></span><span id="maximumencryption"></span><span id="MAXIMUMENCRYPTION"></span>

**MaximumEncryption** ("MaximumEncryption")


</dt> <dd></dd> <dt>

<span id="OptionalEncryption"></span><span id="optionalencryption"></span><span id="OPTIONALENCRYPTION"></span>

**OptionalEncryption** ("OptionalEncryption")


</dt> <dd></dd> <dt>

<span id="RequireEncryption"></span><span id="requireencryption"></span><span id="REQUIREENCRYPTION"></span>

**RequireEncryption** ("RequireEncryption")


</dt> <dd></dd> <dt>

<span id="NoEncryption"></span><span id="noencryption"></span><span id="NOENCRYPTION"></span>

**NoEncryption** ("NoEncryption")


</dt> <dd></dd> </dl>

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

**NetBiosIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Network Basic Input/Output System (NetBIOS) Server IP addresses for VPN clients

This property is inherited from [**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md).

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
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md)
</dt> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





