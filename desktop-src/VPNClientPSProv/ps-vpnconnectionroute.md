---
title: PS\_VpnConnectionRoute class
description: The PS\_VpnConnectionRoute class provides methods to add or remove routes to be plumbed for a VPN profile.
audience: developer
ms.assetid: 'B2A6EDD1-49D3-4E8D-81CF-55902E8EE3B4'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnConnectionRoute class", "PS_VpnConnectionRoute class, described"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionRoute
- PS_VpnConnectionRoute.DestinationPrefix
- PS_VpnConnectionRoute.RouteMetric
- PS_VpnConnectionRoute.AddressFamily
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnConnectionRoute class

The **PS\_VpnConnectionRoute** class provides methods to add or remove routes to be plumbed for a VPN profile.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_VpnConnectionRoute
{
  string DestinationPrefix;
  uint32 RouteMetric;
  uint16 AddressFamily;
};
```

## Members

The **PS\_VpnConnectionRoute** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **PS\_VpnConnectionRoute** class has these methods.



| Method                                         | Description                                                                 |
|:-----------------------------------------------|:----------------------------------------------------------------------------|
| [**Add**](add-ps-vpnconnectionroute.md)       | Adds a route to be plumbed for a VPN profile.<br/>                    |
| [**Remove**](remove-ps-vpnconnectionroute.md) | Removes a route from the routes to be plumbed for a VPN profile.<br/> |



 

### Properties

The **PS\_VpnConnectionRoute** class has these properties.

<dl> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the address family for this route is IPv4 or IPv6.

<dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (2)


</dt> <dd>

The address family is IPv4.

</dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (23)


</dt> <dd>

The address family is IPv6.

</dd> </dl>

</dd> <dt>

**DestinationPrefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Destination prefix of the route to be added.

</dd> <dt>

**RouteMetric**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Metric of the route being added.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



 

 





