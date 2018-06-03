---
title: Get method of the PS\_DhcpServerv6ScopeStatistics class
description: Gets the statistics corresponding to the specified IPv6 prefix for a DHCP Server. Returns statistics for all IPv6 prefixes on the server if no prefix is specified.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 14da34b6-25eb-4562-8fd1-b80164104322
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6ScopeStatistics class
- PS_DhcpServerv6ScopeStatistics class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6ScopeStatistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv6ScopeStatistics class

Gets the statistics corresponding to the specified IPv6 prefix for a DHCP Server. Returns statistics for all IPv6 prefixes on the server if no prefix is specified.

## Syntax


```mof
uint32 Get(
  [in]  string                      Prefix[],
  [in]  string                      ComputerName,
  [out] DhcpServerv6ScopeStatistics cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

The IPv6 prefixes of the scopes for which the statistics are requested.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6ScopeStatistics**](dhcpserverv6scopestatistics.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv6ScopeStatistics**](ps-dhcpserverv6scopestatistics.md)
</dt> </dl>

 

 





