---
title: PS\_DhcpServerv4Scope class
description: PS\_DhcpServerv4Scope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dd50faae-4143-4971-bb34-543a29235bcf
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Scope class
- PS_DhcpServerv4Scope class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Scope
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4Scope class

PS\_DhcpServerv4Scope

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Scope
{
};
```

## Members

The **PS\_DhcpServerv4Scope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Scope** class has these methods.



| Method                                                              | Description                                                                                                                                                 |
|:--------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4scope.md)                             | Adds an IPv4 scope on the server<br/>                                                                                                                 |
| [**Get**](get-ps-dhcpserverv4scope.md)                             | Returns the IPv4 scope configuration of the specified scopes. If scope id is not specified all the scopes configured on the server are returned.<br/> |
| [**Remove**](remove-ps-dhcpserverv4scope.md)                       | Deletes the specified IPv4 scopes from the Server<br/>                                                                                                |
| [**SetByWithoutRange**](setbywithoutrange-ps-dhcpserverv4scope.md) | Sets the properties of an existing IPv4 Scope on the server<br/>                                                                                      |
| [**SetByWithRange**](setbywithrange-ps-dhcpserverv4scope.md)       | Sets the properties of an existing IPv4 Scope on the server<br/>                                                                                      |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





