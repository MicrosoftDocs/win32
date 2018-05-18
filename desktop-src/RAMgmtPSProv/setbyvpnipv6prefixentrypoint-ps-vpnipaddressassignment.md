---
title: SetByVpnIPv6PrefixEntrypoint method of the PS\_VpnIPAddressAssignment class
description: This cmdlet does the following1. Configure the IPv4 address assignment method2. Configure the IPv6 prefix for IPv6 address assignment.
audience: developer
ms.assetid: '0e8f6881-44ce-462f-887e-8560d98843ee'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByVpnIPv6PrefixEntrypoint method", "SetByVpnIPv6PrefixEntrypoint method, PS_VpnIPAddressAssignment class", "PS_VpnIPAddressAssignment class, SetByVpnIPv6PrefixEntrypoint method"]
topic_type:
- apiref
api_name:
- PS_VpnIPAddressAssignment.SetByVpnIPv6PrefixEntrypoint
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# SetByVpnIPv6PrefixEntrypoint method of the PS\_VpnIPAddressAssignment class

This cmdlet does the following1. Configure the IPv4 address assignment method2. Configure the IPv6 prefix for IPv6 address assignment

## Syntax


```mof
uint32 SetByVpnIPv6PrefixEntrypoint(
  [in]  string                 ComputerName,
  [in]  string                 IPv6Prefix,
  [in]  boolean                PassThru,
  [in]  string                 EntrypointName,
  [out] VpnIPAddressAssignment cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the VPN server machine specific tasks should be executed

</dd> <dt>

*IPv6Prefix* \[in\]
</dt> <dd>

Specifies the IPv6 prefix used for IPv6 address assignment

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the VPN IP address assignment policy object. By default this cmdlet does not generate any output

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multisite deployment for which the IPv6 prefix needs to be configured. Entrypoint is not applicable to the IPv4 address assignment properties as these properties are always configured at the individual server level and not site level

If an entrypoint is not specified in a multisite deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter

If both entrypoint and ComputerName are specified and the ComputerName does not belong to the site represented by the entrypoint then the entrypoint takes precedence and the authentication type is configured for it

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Type of IPv4 assignment (DHCP, StaticPool) 2. List of IPv4 address ranges (if static pool was set)

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnIPAddressAssignment**](ps-vpnipaddressassignment.md)
</dt> </dl>

 

 





