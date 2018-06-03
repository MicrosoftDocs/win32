---
title: PS\_DhcpServerv4Class class
description: DhcpServerv4 user or vendor Class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 276a7206-7c4a-4986-a9f9-3159b3e5373f
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Class class
- PS_DhcpServerv4Class class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Class
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4Class class

DhcpServerv4 user or vendor Class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Class
{
};
```

## Members

The **PS\_DhcpServerv4Class** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Class** class has these methods.



| Method                                        | Description                                                                                          |
|:----------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4class.md)       | Adds an IPv4 vendor or user class to the DHCP Server<br/>                                      |
| [**Get**](get-ps-dhcpserverv4class.md)       | Retrieves an IPv4 vendor or user class from the DHCP Server.<br/>                              |
| [**Remove**](remove-ps-dhcpserverv4class.md) | Deletes an IPv4 vendor class or user class from a DHCP Server.<br/>                            |
| [**Set**](set-ps-dhcpserverv4class.md)       | Modifies an IPv4 vendor class or user class on the DHCP Server with specified parameters.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





