---
title: PS\_DhcpServerv6StatelessStatistics class
description: Dhcp Server v6StatelessStatistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ea0607f4-9c83-4b7a-8967-8ab538c57700
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6StatelessStatistics class
- PS_DhcpServerv6StatelessStatistics class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6StatelessStatistics
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv6StatelessStatistics class

Dhcp Server v6StatelessStatistics

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6StatelessStatistics
{
};
```

## Members

The **PS\_DhcpServerv6StatelessStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6StatelessStatistics** class has these methods.



| Method                                                | Description                                                                                                                               |
|:------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6statelessstatistics.md) | Returns a list of IPv6 subnet prefixes which have stateless clients and the number of addresses in use in each of the subnets.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





