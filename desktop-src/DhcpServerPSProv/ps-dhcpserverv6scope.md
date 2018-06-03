---
title: PS\_DhcpServerv6Scope class
description: Add a scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28421666-a1c2-424c-9a02-a39ab9611565
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6Scope class
- PS_DhcpServerv6Scope class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Scope
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv6Scope class

add a scope

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6Scope
{
};
```

## Members

The **PS\_DhcpServerv6Scope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6Scope** class has these methods.



| Method                                        | Description                                                                                     |
|:----------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv6scope.md)       | Adds an IPv6 scope to the DHCP server with the specified parameters.<br/>                 |
| [**Get**](get-ps-dhcpserverv6scope.md)       | Get the scope information for the specified IPv6 prefixes on the server<br/>              |
| [**Remove**](remove-ps-dhcpserverv6scope.md) | Deletes the IPv6 Scopes from the DHCP Server corresponding to the specified prefixes<br/> |
| [**Set**](set-ps-dhcpserverv6scope.md)       | Modifies the properties of a IPv6 scope on the server<br/>                                |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





