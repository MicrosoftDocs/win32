---
title: PS\_DhcpServerDatabase class
description: Dhcp Server Database Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bf26e7e5-dfd5-471a-ac9e-4b9e15bf4ffe
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerDatabase class
- PS_DhcpServerDatabase class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerDatabase
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerDatabase class

Dhcp Server Database Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerDatabase
{
};
```

## Members

The **PS\_DhcpServerDatabase** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerDatabase** class has these methods.



| Method                                   | Description                                                                                 |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverdatabase.md) | Gets the configuration parameters related to the database of the DHCP server.<br/>    |
| [**Set**](set-ps-dhcpserverdatabase.md) | Modifies one or more configuration parameters of the database of the DHCP server<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





