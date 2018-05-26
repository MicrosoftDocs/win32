---
title: PS\_DhcpServerv4OptionValue class
description: PS\_DhcpServerv4OptionValue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 58eab1ad-626d-4dde-92ed-8751fa8a906b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4OptionValue class
- PS_DhcpServerv4OptionValue class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionValue
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4OptionValue class

PS\_DhcpServerv4OptionValue

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4OptionValue
{
};
```

## Members

The **PS\_DhcpServerv4OptionValue** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4OptionValue** class has these methods.



| Method                                                                      | Description                                                                                                                                                                    |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv4optionvalue.md)                               | Returns the IPv4 option Values for one or more IPv4 options at the server, scope or reservation level.<br/>                                                              |
| [**Remove**](remove-ps-dhcpserverv4optionvalue.md)                         | Deletes one more more IPv4 option values at the server, scope or reservation level, either for the standard IPv4 options or for the specified vendor or user Class.<br/> |
| [**SetByCommonOptions**](setbycommonoptions-ps-dhcpserverv4optionvalue.md) | Sets an IPv4 Option Value at the Server, Scope or Reservation level. Any previously set option value(s) for the specified option id are discarded.<br/>                  |
| [**SetByOptionId**](setbyoptionid-ps-dhcpserverv4optionvalue.md)           | Sets an IPv4 Option Value at the Server, Scope or Reservation level. Any previously set option value(s) for the specified option id are discarded.<br/>                  |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





