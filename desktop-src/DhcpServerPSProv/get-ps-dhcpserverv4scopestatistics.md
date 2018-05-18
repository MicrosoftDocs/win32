---
title: Get method of the PS\_DhcpServerv4ScopeStatistics class
description: Returns scope statistics corresponding to the IPv4 scopes on the Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '16ef6135-ccac-4472-8a8b-1cbeef3b2d5b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DhcpServerv4ScopeStatistics class", "PS_DhcpServerv4ScopeStatistics class, Get method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4ScopeStatistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Get method of the PS\_DhcpServerv4ScopeStatistics class

Returns scope statistics corresponding to the IPv4 scopes on the Server.

## Syntax


```mof
uint32 Get(
  [in]  string                      ScopeId[],
  [in]  string                      ComputerName,
  [in]  boolean                     Failover,
  [out] DhcpServerv4ScopeStatistics cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ScopeId* \[in\]
</dt> <dd>

The scope identifiers (in IPv4 address format) whose statistics are to be returned

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Failover* \[in\]
</dt> <dd>

If specified, the failover related scope statistics will be returned as part of the scope statistics if the scope is configured for failover

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4ScopeStatistics**](dhcpserverv4scopestatistics.md) class.

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

[**PS\_DhcpServerv4ScopeStatistics**](ps-dhcpserverv4scopestatistics.md)
</dt> </dl>

 

 





