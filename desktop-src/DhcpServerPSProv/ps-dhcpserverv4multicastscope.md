---
title: PS\_DhcpServerv4MulticastScope class
description: PS\_DhcpServerv4MulticastScope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 334679e6-1e9e-4997-b7b8-a0fb306cde21
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4MulticastScope class
- PS_DhcpServerv4MulticastScope class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastScope
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4MulticastScope class

PS\_DhcpServerv4MulticastScope

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4MulticastScope
{
};
```

## Members

The **PS\_DhcpServerv4MulticastScope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4MulticastScope** class has these methods.



| Method                                                 | Description                                                                                                                                                                                  |
|:-------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4multicastscope.md)       | Adds a Multicast Scope on the DHCP Server.<br/>                                                                                                                                        |
| [**Get**](get-ps-dhcpserverv4multicastscope.md)       | Returns one or more multicast scope objects corresponding to the specified scope names. If Name is not specified, the cmdlet gets all multicast scopes present on the DHCP server<br/> |
| [**Remove**](remove-ps-dhcpserverv4multicastscope.md) | Remove the specified multicast scope(s) from the DHCP Server.<br/>                                                                                                                     |
| [**Set**](set-ps-dhcpserverv4multicastscope.md)       | Modifies the specified properties of a Multicast Scope on the DHCP Server.<br/>                                                                                                        |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





