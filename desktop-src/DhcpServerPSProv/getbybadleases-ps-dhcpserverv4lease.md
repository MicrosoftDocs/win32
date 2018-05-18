---
title: GetByBadLeases method of the PS\_DhcpServerv4Lease class
description: Gets one or more lease records from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8a649301-887d-402f-9d56-d69d920c569e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByBadLeases method", "GetByBadLeases method, PS_DhcpServerv4Lease class", "PS_DhcpServerv4Lease class, GetByBadLeases method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease.GetByBadLeases
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByBadLeases method of the PS\_DhcpServerv4Lease class

Gets one or more lease records from the DHCP server.

## Syntax


```mof
uint32 GetByBadLeases(
  [in]  string            ComputerName,
  [in]  boolean           BadLeases,
  [in]  string            ScopeId,
  [out] DhcpServerv4Lease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*BadLeases* \[in\]
</dt> <dd>

If specified, only bad leases are returned. If an IP address lease is declined by the client because of a conflict, the lease record is marked as bad (declined) by the DHCP server. An IP address lease in this state is not offered to any client until expiry of a timer (10 minutes).

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the IPv4 address leases are to be retrieved

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Lease**](dhcpserverv4lease.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Lease**](ps-dhcpserverv4lease.md)
</dt> </dl>

 

 





