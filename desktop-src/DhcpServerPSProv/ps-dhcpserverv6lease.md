---
title: PS\_DhcpServerv6Lease class
description: DhcpServer v6Lease.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ca6f186c-73ad-4c5c-bf5f-c83a3803f63e
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6Lease class
- PS_DhcpServerv6Lease class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6Lease
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv6Lease class

DhcpServer v6Lease

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6Lease
{
};
```

## Members

The **PS\_DhcpServerv6Lease** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6Lease** class has these methods.



| Method                                                              | Description                                                          |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv6lease.md)                             | Adds a new IPv6 address lease to the DHCP server.<br/>         |
| [**GetByIPAddress**](getbyipaddress-ps-dhcpserverv6lease.md)       | Gets one or more IPv6 lease records from the DHCP server.<br/> |
| [**GetByPrefix**](getbyprefix-ps-dhcpserverv6lease.md)             | Gets one or more IPv6 lease records from the DHCP server.<br/> |
| [**RemoveByIPAddress**](removebyipaddress-ps-dhcpserverv6lease.md) | Deletes one or more IPv6 lease records from the server.<br/>   |
| [**RemoveByPrefix**](removebyprefix-ps-dhcpserverv6lease.md)       | Deletes one or more IPv6 lease records from the server.<br/>   |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





