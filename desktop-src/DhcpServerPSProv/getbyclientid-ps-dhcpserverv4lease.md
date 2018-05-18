---
title: GetByClientId method of the PS\_DhcpServerv4Lease class
description: Gets one or more lease records from the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6c88d7b8-aae3-4ef1-a333-0a60f2ba8ed8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByClientId method", "GetByClientId method, PS_DhcpServerv4Lease class", "PS_DhcpServerv4Lease class, GetByClientId method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease.GetByClientId
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# GetByClientId method of the PS\_DhcpServerv4Lease class

Gets one or more lease records from the DHCP server.

## Syntax


```mof
uint32 GetByClientId(
  [in]  string            ComputerName,
  [in]  string            ClientId[],
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

*ClientId* \[in\]
</dt> <dd>

Client identifier for which the IP address lease record is to be retrieved.

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

 

 





