---
title: PS\_DhcpServerv4ScopeStatistics class
description: Returns IPv4 Scope statistics corresponding to the IPv4 Scope IDs specified for a DHCP Server. Returns statistics for all IPv4 Scopes if no Scope ID is specified.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cb863d20-f25e-44c6-b6d1-974bd5cf6192'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv4ScopeStatistics class", "PS_DhcpServerv4ScopeStatistics class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4ScopeStatistics
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv4ScopeStatistics class

Returns IPv4 Scope statistics corresponding to the IPv4 Scope IDs specified for a DHCP Server. Returns statistics for all IPv4 Scopes if no Scope ID is specified.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4ScopeStatistics
{
};
```

## Members

The **PS\_DhcpServerv4ScopeStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4ScopeStatistics** class has these methods.



| Method                                            | Description                                                                         |
|:--------------------------------------------------|:------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv4scopestatistics.md) | Returns scope statistics corresponding to the IPv4 scopes on the Server.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





