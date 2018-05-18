---
title: VpnRoutingDomainConfig class
description: Represents a site-to-site (S2S) VPN routing domain configuration.
audience: developer
ms.assetid: '0d4aa919-6d2c-4eb6-b123-c0785f631467'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnRoutingDomainConfig class", "VpnRoutingDomainConfig class, described"]
topic_type:
- apiref
api_name:
- VpnRoutingDomainConfig
- VpnRoutingDomainConfig.RoutingDomain
- VpnRoutingDomainConfig.RoutingDomainID
- VpnRoutingDomainConfig.RoutingDomainStatus
- VpnRoutingDomainConfig.VpnStatus
- VpnRoutingDomainConfig.VpnS2SStatus
- VpnRoutingDomainConfig.RoutingStatus
- VpnRoutingDomainConfig.EnableQoS
- VpnRoutingDomainConfig.TxBandwidthKbps
- VpnRoutingDomainConfig.RxBandwidthKbps
- VpnRoutingDomainConfig.IPAddressRange
- VpnRoutingDomainConfig.IPv6Prefix
- VpnRoutingDomainConfig.AvailabilityStatus
- VpnRoutingDomainConfig.InterimAccountingPeriodSec
- VpnRoutingDomainConfig.DnsIPAddress
- VpnRoutingDomainConfig.NetBiosIPAddress
- VpnRoutingDomainConfig.MaximumVpnConnections
- VpnRoutingDomainConfig.TenantName
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnRoutingDomainConfig class

Represents a site-to-site (S2S) VPN routing domain configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnRoutingDomainConfig : RoutingDomainConfiguration
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
};
```

## Members

The **VpnRoutingDomainConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnRoutingDomainConfig** class has these properties.

<dl> <dt>

**AvailabilityStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The availability status of the routing domain

</dd> <dt>

**DnsIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS server IP addresses for VPN clients

</dd> <dt>

**EnableQoS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether QoS is enabled for VPN

</dd> <dt>

**InterimAccountingPeriodSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The interval in which to log interim accounting, in seconds

</dd> <dt>

**IPAddressRange**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of the start and end IP addresses for the IP address range of the routing domain

</dd> <dt>

**IPv6Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 prefix for address assignment

</dd> <dt>

**MaximumVpnConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of VPN connections allowed in the VPN routing domain

</dd> <dt>

**NetBiosIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Network Basic Input/Output System (NetBIOS) Server IP addresses for VPN clients

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

</dd> <dt>

**TenantName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the tenant for the VPN routing domain

</dd> <dt>

**TxBandwidthKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The outgoing bandwidth limit for VPN, in kbps.

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

[**RoutingDomainConfiguration**](routingdomainconfiguration.md)
</dt> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





