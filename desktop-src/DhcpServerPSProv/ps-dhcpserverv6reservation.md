---
title: PS\_DhcpServerv6Reservation class
description: PS\_DhcpServerv6Reservation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cae3ee54-3a0d-4e4d-8812-e74d8bd3b7da
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6Reservation class
- PS_DhcpServerv6Reservation class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Reservation
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv6Reservation class

PS\_DhcpServerv6Reservation

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6Reservation
{
};
```

## Members

The **PS\_DhcpServerv6Reservation** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6Reservation** class has these methods.



| Method                                                                    | Description                                                           |
|:--------------------------------------------------------------------------|:----------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv6reservation.md)                             | Add an IPv6 Reservation to an IPv6 Prefix/Scope.<br/>           |
| [**GetByIPAddress**](getbyipaddress-ps-dhcpserverv6reservation.md)       | Returns the reserved IPv6 addresses on the server.<br/>         |
| [**GetByPrefix**](getbyprefix-ps-dhcpserverv6reservation.md)             | Returns the reserved IPv6 addresses on the server.<br/>         |
| [**RemoveByIPAddress**](removebyipaddress-ps-dhcpserverv6reservation.md) | Deletes the IPv6 reservation(s) from the specified scope.<br/>  |
| [**RemoveByPrefix**](removebyprefix-ps-dhcpserverv6reservation.md)       | Deletes the IPv6 reservation(s) from the specified scope.<br/>  |
| [**Set**](set-ps-dhcpserverv6reservation.md)                             | Modifies the properties of the specified IPv6 Reservation.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





