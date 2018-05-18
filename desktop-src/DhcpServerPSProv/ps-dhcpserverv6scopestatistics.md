---
title: PS\_DhcpServerv6ScopeStatistics class
description: Returns IPv6 Prefix statistics corresponding to the IPv6 Prefix specified for a DHCP Server. Returns statistics for all IPv6 Prefixes if no Prefix is specified.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4af7cb56-5c7c-4d36-8b50-a683cf8ee858'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv6ScopeStatistics class", "PS_DhcpServerv6ScopeStatistics class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6ScopeStatistics
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv6ScopeStatistics class

Returns IPv6 Prefix statistics corresponding to the IPv6 Prefix specified for a DHCP Server. Returns statistics for all IPv6 Prefixes if no Prefix is specified.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6ScopeStatistics
{
};
```

## Members

The **PS\_DhcpServerv6ScopeStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6ScopeStatistics** class has these methods.



| Method                                            | Description                                                                                                                                                                    |
|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6scopestatistics.md) | Gets the statistics corresponding to the specified IPv6 prefix for a DHCP Server. Returns statistics for all IPv6 prefixes on the server if no prefix is specified.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





