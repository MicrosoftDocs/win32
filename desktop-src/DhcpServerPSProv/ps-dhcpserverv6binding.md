---
title: PS\_DhcpServerv6Binding class
description: Return all IPv6 Interface Bindings for a DHCP Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00a72f63-86b1-4bca-917b-3feb66813b8a
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6Binding class
- PS_DhcpServerv6Binding class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Binding
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv6Binding class

Return all IPv6 Interface Bindings for a DHCP Server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6Binding
{
};
```

## Members

The **PS\_DhcpServerv6Binding** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6Binding** class has these methods.



| Method                                    | Description                                                                                  |
|:------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6binding.md) | Returns the IPv6 interfaces to which a DHCP Server is bound.<br/>                      |
| [**Set**](set-ps-dhcpserverv6binding.md) | Binds or unbinds the DHCP server from the specified IPv6 interface on the system.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





