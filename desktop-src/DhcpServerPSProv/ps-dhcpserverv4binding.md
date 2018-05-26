---
title: PS\_DhcpServerv4Binding class
description: Return all IPv4 Interface Bindings for a DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6e7e4ab1-a4b6-4cdf-9354-a55acbc738f1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Binding class
- PS_DhcpServerv4Binding class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Binding
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4Binding class

Return all IPv4 Interface Bindings for a DHCP Server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Binding
{
};
```

## Members

The **PS\_DhcpServerv4Binding** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Binding** class has these methods.



| Method                                    | Description                                                                                  |
|:------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv4binding.md) | Gets all IPv4 interfaces in the system to which the DHCP Server is bound to.<br/>      |
| [**Set**](set-ps-dhcpserverv4binding.md) | Binds or unbinds the DHCP server from the specified IPv4 interface on the system.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





