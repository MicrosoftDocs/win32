---
title: PS\_DhcpServerv6Class class
description: Dhcp Server v6Class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5264202c-0be7-40c9-bf53-d6066b7e38ad
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6Class class
- PS_DhcpServerv6Class class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Class
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv6Class class

Dhcp Server v6Class

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6Class
{
};
```

## Members

The **PS\_DhcpServerv6Class** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6Class** class has these methods.



| Method                                        | Description                                                                            |
|:----------------------------------------------|:---------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv6class.md)       | Adds an IPv6 vendor or user class to the DHCP Server.<br/>                       |
| [**Get**](get-ps-dhcpserverv6class.md)       | Gets the IPv6 vendor or user class from the DHCP Server<br/>                     |
| [**Remove**](remove-ps-dhcpserverv6class.md) | Deletes an IPv6 vendor class or user class from a DHCP Server<br/>               |
| [**Set**](set-ps-dhcpserverv6class.md)       | Modifies the properties of an IPv6 vendor or user class on the DHCP Server.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





