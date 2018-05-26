---
title: SetByVpnIPAddressAssignment method of the PS\_VpnIPAddressAssignment class
description: This cmdlet does the following1. Configure the IPv4 address assignment method2. Configure the IPv6 prefix for IPv6 address assignment.
audience: developer
ms.assetid: a980a73d-1969-4039-bfe5-0561f48ae2bc
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByVpnIPAddressAssignment method
- SetByVpnIPAddressAssignment method, PS_VpnIPAddressAssignment class
- PS_VpnIPAddressAssignment class, SetByVpnIPAddressAssignment method
topic_type:
- apiref
api_name:
- PS_VpnIPAddressAssignment.SetByVpnIPAddressAssignment
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByVpnIPAddressAssignment method of the PS\_VpnIPAddressAssignment class

This cmdlet does the following1. Configure the IPv4 address assignment method2. Configure the IPv6 prefix for IPv6 address assignment

## Syntax


```mof
uint32 SetByVpnIPAddressAssignment(
  [in]  boolean                PassThru,
  [in]  string                 IPAddressRange[],
  [in]  string                 ComputerName,
  [in]  string                 IPAssignmentMethod,
  [in]  string                 IPv6Prefix,
  [out] VpnIPAddressAssignment cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the VPN IP address assignment policy object. By default this cmdlet does not generate any output

</dd> <dt>

*IPAddressRange* \[in\]
</dt> <dd>

Indicates the IP address range from which IP addresses are allocated to VPN clients. Consists of a start IP and an end IP. This parameter can be configured only if the IPAssignmentMethod parameter is specified to be StaticPool. If there are no pre-existing IPv4 address pools (see cmdlet description for more details) then it is mandatory to specify an address range

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the VPN server machine specific tasks should be executed

</dd> <dt>

*IPAssignmentMethod* \[in\]
</dt> <dd>

Indicates the mechanism for IPv4 address assignment. Can take one of the following values: 1. Dhcp 2. StaticPool When load balancing is active the IPv4 address assignment method cannot be configured to DHCP. Only static pool is supported

<dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** ("Dhcp")


</dt> <dd></dd> <dt>

<span id="StaticPool"></span><span id="staticpool"></span><span id="STATICPOOL"></span>

**StaticPool** ("StaticPool")


</dt> <dd></dd> </dl> </dd> <dt>

*IPv6Prefix* \[in\]
</dt> <dd>

Specifies the IPv6 prefix used for IPv6 address assignment

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Type of IPv4 assignment (DHCP, StaticPool). 2. List of IPv4 address ranges (if static pool was set)

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

[**PS\_VpnIPAddressAssignment**](ps-vpnipaddressassignment.md)
</dt> </dl>

 

 





