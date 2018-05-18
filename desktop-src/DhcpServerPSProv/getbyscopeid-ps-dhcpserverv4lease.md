---
title: GetByScopeId method of the PS\_DhcpServerv4Lease class
description: Gets one or more lease records from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5a552f05-68f7-4434-974f-81466364bd6f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByScopeId method", "GetByScopeId method, PS_DhcpServerv4Lease class", "PS_DhcpServerv4Lease class, GetByScopeId method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease.GetByScopeId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByScopeId method of the PS\_DhcpServerv4Lease class

Gets one or more lease records from the DHCP server.

## Syntax


```mof
uint32 GetByScopeId(
  [in]  string            ComputerName,
  [in]  string            ScopeId,
  [in]  boolean           AllLeases,
  [out] DhcpServerv4Lease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Scope identifier (in IPv4 address format) from which the IPv4 address leases are to be retrieved

</dd> <dt>

*AllLeases* \[in\]
</dt> <dd>

If specified, all the IP address leases regardless of address state are returned. If not specified, only active leases are returned

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

 

 





