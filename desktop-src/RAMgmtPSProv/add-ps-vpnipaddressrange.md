---
title: Add method of the PS\_VpnIPAddressRange class
description: This cmdlet adds a new IPv4 address range from which IPv4 addresses can be assigned to VPN clients.
audience: developer
ms.assetid: 4a6f4363-4b62-454b-90a2-c461ed3621fb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_VpnIPAddressRange class
- PS_VpnIPAddressRange class, Add method
topic_type:
- apiref
api_name:
- PS_VpnIPAddressRange.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_VpnIPAddressRange class

This cmdlet adds a new IPv4 address range from which IPv4 addresses can be assigned to VPN clients

## Syntax


```mof
uint32 Add(
  [in]  string            IPAddressRange[],
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  string            RoutingDomain,
  [out] VpnIPAddressRange cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddressRange* \[in\]
</dt> <dd>

Indicates the IP address range that has to be added to the pool. Consists of a start IP and an end IP. The range shouldn't overlap with an already existing range

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the VPN server machine specific tasks should be executed. If ComputerName is specified then the IPv4 address range is added on that VPN server

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the IP address range object that was added. By default this cmdlet does not generate any output

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The name of the routing domain of the IP address range.

**Windows Server 2012:** This parameter was changed from *RoutingDomainName* in Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The start and end IP address of the new range address range.

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

 

 





