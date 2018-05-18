---
title: GetByPrefix method of the PS\_DhcpServerv6Lease class
description: Gets one or more IPv6 lease records from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a90fbf77-a992-4059-9cdd-f7b729167641'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByPrefix method", "GetByPrefix method, PS_DhcpServerv6Lease class", "PS_DhcpServerv6Lease class, GetByPrefix method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Lease.GetByPrefix
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByPrefix method of the PS\_DhcpServerv6Lease class

Gets one or more IPv6 lease records from the DHCP server.

## Syntax


```mof
uint32 GetByPrefix(
  [in]  string            ComputerName,
  [in]  string            Prefix,
  [out] DhcpServerv6Lease cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

Subnet prefix of the scope from which the lease records are to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Lease**](dhcpserverv6lease.md) class.

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

[**PS\_DhcpServerv6Lease**](ps-dhcpserverv6lease.md)
</dt> </dl>

 

 





