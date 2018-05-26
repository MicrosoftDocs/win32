---
title: Remove method of the PS\_VpnIPAddressRange class
description: This cmdlet removes an existing IPv4 address range from the pool for IP address assignment.
audience: developer
ms.assetid: 50dd0191-56ed-4d89-b6d3-e17cf934c7c4
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnIPAddressRange class
- PS_VpnIPAddressRange class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnIPAddressRange.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_VpnIPAddressRange class

This cmdlet removes an existing IPv4 address range from the pool for IP address assignment

## Syntax


```mof
uint32 Remove(
  [in]  string            IPAddress,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  boolean           Force,
  [in]  string            RoutingDomain,
  [out] VpnIPAddressRange cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

Indicates the Start IP address of the range that has to be deleted

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the VPN server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object, viz. the IPv4 address range that was deleted. By default this cmdlet does not generate any output

</dd> <dt>

*Force* \[in\]
</dt> <dd>

The cmdlet ensures that there is at least one address range always present by disallowing deletion of the last address range. This poses a problem where there is only one range to start with and a user needs to replace that range with a new one. The Force parameter is used to override the normal behavior and allow deletion of the last address range so that a new range can be added later.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The name of the routing domain of the IP address range.

**Windows Server 2012:** This parameter was changed from *RoutingDomainName* in Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Start and end IP address of the range that was deleted

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnIPAddressRange**](ps-vpnipaddressrange.md)
</dt> </dl>

 

 





