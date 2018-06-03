---
title: Get method of the PS\_DhcpServerv6StatelessStatistics class
description: Returns a list of IPv6 subnet prefixes which have stateless clients and the number of addresses in use in each of the subnets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f78ff2eb-3e2e-4a83-b4af-7f76b9800342
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6StatelessStatistics class
- PS_DhcpServerv6StatelessStatistics class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6StatelessStatistics.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DhcpServerv6StatelessStatistics class

Returns a list of IPv6 subnet prefixes which have stateless clients and the number of addresses in use in each of the subnets.

## Syntax


```mof
uint32 Get(
  [in]  string                          ComputerName,
  [out] DhcpServerv6StatelessStatistics cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6StatelessStatistics**](dhcpserverv6statelessstatistics.md) class.

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

[**PS\_DhcpServerv6StatelessStatistics**](ps-dhcpserverv6statelessstatistics.md)
</dt> </dl>

 

 





