---
title: PS\_DhcpServerv6OptionDefinition class
description: PS\_DhcpServerv6OptionDefinition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7f094e1e-b4fc-4177-b88c-2bf68cf307e1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6OptionDefinition class
- PS_DhcpServerv6OptionDefinition class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6OptionDefinition
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv6OptionDefinition class

PS\_DhcpServerv6OptionDefinition

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6OptionDefinition
{
};
```

## Members

The **PS\_DhcpServerv6OptionDefinition** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6OptionDefinition** class has these methods.



| Method                                                   | Description                                                                                                                                                              |
|:---------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv6optiondefinition.md)       | Adds a DHCPv6 option definition to a DHCP Server running on local or remote computer.<br/>                                                                         |
| [**Get**](get-ps-dhcpserverv6optiondefinition.md)       | Get the option definition for the option identified by the option id. If no option id is specified, all option definitions will be returned.<br/>                  |
| [**Remove**](remove-ps-dhcpserverv6optiondefinition.md) | Deletes one or more IPv4 option definitions from the Server. If VendorClass is specified, only option definitions for the specified vendor class are deleted.<br/> |
| [**Set**](set-ps-dhcpserverv6optiondefinition.md)       | Modifies the properties of an existing DHCPv6 option definition.<br/>                                                                                              |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





