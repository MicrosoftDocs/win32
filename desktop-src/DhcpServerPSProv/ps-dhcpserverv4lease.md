---
title: PS\_DhcpServerv4Lease class
description: DhcpServer v4Lease.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7f1d7482-cbb4-4a9e-b73e-39cab88153b6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv4Lease class", "PS_DhcpServerv4Lease class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv4Lease class

DhcpServer v4Lease.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Lease
{
};
```

## Members

The **PS\_DhcpServerv4Lease** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Lease** class has these methods.



| Method                                                              | Description                                                                     |
|:--------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4lease.md)                             | Adds a new IPv4 address lease in the DHCP server<br/>                     |
| [**GetByBadLeases**](getbybadleases-ps-dhcpserverv4lease.md)       | Gets one or more lease records from the DHCP server<br/>                  |
| [**GetByClientId**](getbyclientid-ps-dhcpserverv4lease.md)         | Gets one or more lease records from the DHCP server<br/>                  |
| [**GetByIPAddress**](getbyipaddress-ps-dhcpserverv4lease.md)       | Gets one or more lease records from the DHCP server<br/>                  |
| [**GetByScopeId**](getbyscopeid-ps-dhcpserverv4lease.md)           | Gets one or more lease records from the DHCP server<br/>                  |
| [**RemoveByBadLeases**](removebybadleases-ps-dhcpserverv4lease.md) | Deletes the specified IPv4 address lease record from the DHCP server<br/> |
| [**RemoveByClientId**](removebyclientid-ps-dhcpserverv4lease.md)   | Deletes the specified IPv4 address lease record from the DHCP server<br/> |
| [**RemoveByIPAddress**](removebyipaddress-ps-dhcpserverv4lease.md) | Deletes the specified IPv4 address lease record from the DHCP server<br/> |
| [**RemoveByScopeId**](removebyscopeid-ps-dhcpserverv4lease.md)     | Deletes the specified IPv4 address lease record from the DHCP server<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





