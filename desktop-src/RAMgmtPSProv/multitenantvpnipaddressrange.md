---
title: MultiTenantVpnIPAddressRange class
description: Represents an IP address range in a routing domain on a multi-tenant VPN.
audience: developer
ms.assetid: '5a8b74a8-e18f-4d08-aa81-86099cf0c1d8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MultiTenantVpnIPAddressRange class", "MultiTenantVpnIPAddressRange class, described"]
topic_type:
- apiref
api_name:
- MultiTenantVpnIPAddressRange
- MultiTenantVpnIPAddressRange.StartIPAddress
- MultiTenantVpnIPAddressRange.EndIPAddress
- MultiTenantVpnIPAddressRange.RoutingDomain
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# MultiTenantVpnIPAddressRange class

Represents an IP address range in a routing domain on a multi-tenant VPN

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class MultiTenantVpnIPAddressRange : VpnIPAddressRange
{
  string StartIPAddress;
  string EndIPAddress;
  string RoutingDomain;
};
```

## Members

The **MultiTenantVpnIPAddressRange** class has these types of members:

-   [Properties](#properties)

### Properties

The **MultiTenantVpnIPAddressRange** class has these properties.

<dl> <dt>

**EndIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

End IP address of the Range

This property is inherited from [**VpnIPAddressRange**](vpnipaddressrange.md).

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The friendly name of the routing domain

</dd> <dt>

**StartIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Start IP address of the Range

This property is inherited from [**VpnIPAddressRange**](vpnipaddressrange.md).

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

[**VpnIPAddressRange**](vpnipaddressrange.md)
</dt> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





