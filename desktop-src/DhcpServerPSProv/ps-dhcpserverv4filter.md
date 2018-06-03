---
title: PS\_DhcpServerv4Filter class
description: DhcpServer v4Filter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a51348ba-7698-4ba1-a44a-cc40464e535e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Filter class
- PS_DhcpServerv4Filter class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Filter
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4Filter class

DhcpServer v4Filter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Filter
{
};
```

## Members

The **PS\_DhcpServerv4Filter** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Filter** class has these methods.



| Method                                         | Description                                                                                                     |
|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4filter.md)       | Adds a MAC address filter to the DHCP server<br/>                                                         |
| [**Get**](get-ps-dhcpserverv4filter.md)       | Gets the list of all MAC addresses from the allow or deny list on the DHCP Server.<br/>                   |
| [**Remove**](remove-ps-dhcpserverv4filter.md) | Deletes the specified MAC address or MAC address pattern from allow list or deny list of the Server.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





