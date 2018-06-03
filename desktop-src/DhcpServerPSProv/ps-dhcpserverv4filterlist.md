---
title: PS\_DhcpServerv4FilterList class
description: DhcpServer v4FilterList.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e67837fa-4fd6-44e2-ba1c-8ee45d63ec9c
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4FilterList class
- PS_DhcpServerv4FilterList class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4FilterList
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4FilterList class

DhcpServer v4FilterList.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4FilterList
{
};
```

## Members

The **PS\_DhcpServerv4FilterList** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4FilterList** class has these methods.



| Method                                       | Description                                                                                              |
|:---------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv4filterlist.md) | Gets the status (enabled/disabled) of the allow and deny filter lists set on the DHCP Server.<br/> |
| [**Set**](set-ps-dhcpserverv4filterlist.md) | Enables or disables the allow and/or deny MAC address filter lists on the DHCP Server.<br/>        |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





