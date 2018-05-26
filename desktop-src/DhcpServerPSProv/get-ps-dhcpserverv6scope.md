---
title: Get method of the PS\_DhcpServerv6Scope class
description: Get the scope information for the specified IPv6 prefixes on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 436eeccf-52f5-4aca-8bbe-7c4286bb7bab
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DhcpServerv6Scope class
- PS_DhcpServerv6Scope class, Get method
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Scope.Get
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DhcpServerv6Scope class

Get the scope information for the specified IPv6 prefixes on the server

## Syntax


```mof
uint32 Get(
  [in]  string            ComputerName,
  [in]  string            Prefix[],
  [out] DhcpServerv6Scope cmdletOutput[]
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

The IPv6 prefixes for which the scope information is being requested.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv6Scope**](dhcpserverv6scope.md) class.

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

[**PS\_DhcpServerv6Scope**](ps-dhcpserverv6scope.md)
</dt> </dl>

 

 





