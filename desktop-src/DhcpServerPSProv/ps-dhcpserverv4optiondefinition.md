---
title: PS\_DhcpServerv4OptionDefinition class
description: PS\_DhcpServerv4OptionDefinition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3b72f6db-7a67-41cd-ae15-4aab24fd9257
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4OptionDefinition class
- PS_DhcpServerv4OptionDefinition class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4OptionDefinition
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4OptionDefinition class

PS\_DhcpServerv4OptionDefinition

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4OptionDefinition
{
};
```

## Members

The **PS\_DhcpServerv4OptionDefinition** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4OptionDefinition** class has these methods.



| Method                                                   | Description                                                               |
|:---------------------------------------------------------|:--------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4optiondefinition.md)       | Adds a new DHCPv4 option definition on the server.<br/>             |
| [**Get**](get-ps-dhcpserverv4optiondefinition.md)       | Gets the DHCPv4 option definition for the specified option ids<br/> |
| [**Remove**](remove-ps-dhcpserverv4optiondefinition.md) | Delete one or more IPv4 option definitions from a DHCP Server.<br/> |
| [**Set**](set-ps-dhcpserverv4optiondefinition.md)       | Modifies the properties of an existing IPv4 Option definition<br/>  |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





