---
title: PS\_DhcpServerv6ExclusionRange class
description: PS\_DhcpServerv6ExclusionRange.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 883a7e43-caee-405b-a5a3-b3833fe0e10d
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv6ExclusionRange class
- PS_DhcpServerv6ExclusionRange class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv6ExclusionRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv6ExclusionRange class

PS\_DhcpServerv6ExclusionRange

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv6ExclusionRange
{
};
```

## Members

The **PS\_DhcpServerv6ExclusionRange** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv6ExclusionRange** class has these methods.



| Method                                                 | Description                                                                                                                                        |
|:-------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv6exclusionrange.md)       | Sets the range of IPv6 addresses to exclude from an IPv6 scope. IP addresses from this range will not be leased out by the DHCP server.<br/> |
| [**Get**](get-ps-dhcpserverv6exclusionrange.md)       | Returns the IPv6 address ranges excluded from the specified IPv6 subnet prefix.<br/>                                                         |
| [**Remove**](remove-ps-dhcpserverv6exclusionrange.md) | Deletes a range of IP addresses previously excluded from an IPv4 Scope.<br/>                                                                 |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





