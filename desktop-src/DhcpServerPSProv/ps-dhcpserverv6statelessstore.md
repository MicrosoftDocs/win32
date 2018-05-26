---
title: PS\_DhcpServerv6StatelessStore class
description: Dhcp Server v6StatelessStore.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 408c6e97-79c4-4ba9-af2f-5d860f209cfd
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6StatelessStore class
- PS_DhcpServerv6StatelessStore class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6StatelessStore
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv6StatelessStore class

Dhcp Server v6StatelessStore.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6StatelessStore
{
};
```

## Members

The **PS\_DhcpServerv6StatelessStore** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6StatelessStore** class has these methods.



| Method                                           | Description                                                                              |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv6statelessstore.md) | Returns the properties of IPv6 stateless store for the specified IPv6 subnet.<br/> |
| [**Set**](set-ps-dhcpserverv6statelessstore.md) | Sets the properties of IPv6 stateless store for the specified IPv6 prefix.<br/>    |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





