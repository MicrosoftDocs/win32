---
title: PS\_DhcpServerv6OptionValue class
description: PS\_DhcpServerv6OptionValue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8c48da41-fa5e-4dea-8113-f429ee9c1b93
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6OptionValue class
- PS_DhcpServerv6OptionValue class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionValue
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv6OptionValue class

PS\_DhcpServerv6OptionValue

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6OptionValue
{
};
```

## Members

The **PS\_DhcpServerv6OptionValue** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6OptionValue** class has these methods.



| Method                                                                      | Description                                                                                                                                                                          |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6optionvalue.md)                               | Returns the IPv6 option values for one or more IPv6 options either for a specific Reserved IP, scope or server level.<br/>                                                     |
| [**Remove**](remove-ps-dhcpserverv6optionvalue.md)                         | Deletes one or more DHCPv6 option values set at the reservation level, scope level or server level, either for the standard IPv6 options or for a specified vendor class.<br/> |
| [**SetByCommonOptions**](setbycommonoptions-ps-dhcpserverv6optionvalue.md) | Sets an IPv6 option value at the Server, Scope or Reservation Level. Any previously set option value(s) for the specified option id are discarded.<br/>                        |
| [**SetByOptionId**](setbyoptionid-ps-dhcpserverv6optionvalue.md)           | Sets an IPv6 option value at the Server, Scope or Reservation Level. Any previously set option value(s) for the specified option id are discarded.<br/>                        |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





