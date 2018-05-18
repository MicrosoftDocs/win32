---
title: PS\_DhcpServerv6FreeIPAddress class
description: Dhcp Server v6FreeIPAddress.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '139def69-f860-4365-a651-aa5f704802e8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv6FreeIPAddress class", "PS_DhcpServerv6FreeIPAddress class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv6FreeIPAddress
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv6FreeIPAddress class

Dhcp Server v6FreeIPAddress

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6FreeIPAddress
{
};
```

## Members

The **PS\_DhcpServerv6FreeIPAddress** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6FreeIPAddress** class has these methods.



| Method                                          | Description                                                           |
|:------------------------------------------------|:----------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6freeipaddress.md) | Get free/unassigned IPAddress(es) from the specified scope<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





