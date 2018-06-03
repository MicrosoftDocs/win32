---
title: PS\_DhcpServerv4Reservation class
description: Retrieves, updates, or removes an IPv4 reservation for a DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de83b411-85c0-4bb4-afc9-241141b72135
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Reservation class
- PS_DhcpServerv4Reservation class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Reservation
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4Reservation class

Retrieves, updates, or removes an IPv4 reservation for a DHCP server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Reservation
{
};
```

## Members

The **PS\_DhcpServerv4Reservation** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Reservation** class has these methods.



| Method                                                                    | Description                                                                                                                                                                                         |
|:--------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4reservation.md)                             | Reserves the specified IPv4 address in the scope for a client.<br/>                                                                                                                           |
| [**GetByClientId**](getbyclientid-ps-dhcpserverv4reservation.md)         | Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.<br/> |
| [**GetByIPAddress**](getbyipaddress-ps-dhcpserverv4reservation.md)       | Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.<br/> |
| [**GetByScopeId**](getbyscopeid-ps-dhcpserverv4reservation.md)           | Gets the IPv4 reservation(s) for the specified IP addresses or client identifiers. If only a scope identifier is specified, all IPv4 reservations from the specified scope are returned.<br/> |
| [**RemoveByClientId**](removebyclientid-ps-dhcpserverv4reservation.md)   | Deletes the IPv4 Reservation from the specified scope<br/>                                                                                                                                    |
| [**RemoveByIPAddress**](removebyipaddress-ps-dhcpserverv4reservation.md) | Deletes the IPv4 Reservation from the specified scope<br/>                                                                                                                                    |
| [**RemoveByScopeId**](removebyscopeid-ps-dhcpserverv4reservation.md)     | Deletes the IPv4 Reservation from the specified scope<br/>                                                                                                                                    |
| [**Set**](set-ps-dhcpserverv4reservation.md)                             | Modifies/sets the properties of an IPv4 reservation<br/>                                                                                                                                      |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





