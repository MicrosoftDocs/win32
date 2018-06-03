---
title: PS\_DhcpServerv4Superscope class
description: DhcpServerv4Superscope.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9ef40fa5-b149-413f-a7fe-672c69862ad3
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Superscope class
- PS_DhcpServerv4Superscope class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Superscope
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4Superscope class

DhcpServerv4Superscope

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Superscope
{
};
```

## Members

The **PS\_DhcpServerv4Superscope** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Superscope** class has these methods.



| Method                                             | Description                                                                                                                                                    |
|:---------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4superscope.md)       | Adds the specified scopes to a superscope<br/>                                                                                                           |
| [**Get**](get-ps-dhcpserverv4superscope.md)       | Returns configuration of specified superscope<br/>                                                                                                       |
| [**Remove**](remove-ps-dhcpserverv4superscope.md) | Removes the specified scope(s) from a superscope. Superscope is deleted if there are no scopes left in the superscope.<br/>                              |
| [**Rename**](ps-dhcpserverv4superscope-rename.md) | Renames the superscope with the specified name.<br/> **Windows Server 2012:** This method is supported beginning with Windows Server 2012 R2.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





