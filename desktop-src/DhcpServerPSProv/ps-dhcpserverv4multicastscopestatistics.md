---
title: PS\_DhcpServerv4MulticastScopeStatistics class
description: PS\_DhcpServerv4MulticastScopeStatistics class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3009b6d0-107b-4d6e-8ea3-fc73aa0410c6
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4MulticastScopeStatistics class
- PS_DhcpServerv4MulticastScopeStatistics class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScopeStatistics
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4MulticastScopeStatistics class

PS\_DhcpServerv4MulticastScopeStatistics class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4MulticastScopeStatistics
{
};
```

## Members

The **PS\_DhcpServerv4MulticastScopeStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4MulticastScopeStatistics** class has these methods.



| Method                                                     | Description                                                                                                                                                            |
|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv4multicastscopestatistics.md) | Returns multicast scope statistics corresponding to specified multicast scope name(s). Returns statistics for all multicast scopes if no name is specified.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





