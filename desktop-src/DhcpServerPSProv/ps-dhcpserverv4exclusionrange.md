---
title: PS\_DhcpServerv4ExclusionRange class
description: PS\_DhcpServerv4ExclusionRange.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'aee3f888-a7ea-4313-a4b4-0133110b9615'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DhcpServerv4ExclusionRange class", "PS_DhcpServerv4ExclusionRange class, described"]
topic_type:
- apiref
api_name:
- PS_DhcpServerv4ExclusionRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# PS\_DhcpServerv4ExclusionRange class

PS\_DhcpServerv4ExclusionRange.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4ExclusionRange
{
};
```

## Members

The **PS\_DhcpServerv4ExclusionRange** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4ExclusionRange** class has these methods.



| Method                                                 | Description                                                                                                                                                                  |
|:-------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4exclusionrange.md)       | Adds a range of excluded IP addresses for an IPv4 scope.<br/>                                                                                                          |
| [**Get**](get-ps-dhcpserverv4exclusionrange.md)       | Returns the IPv4 address ranges excluded from the specified scope IDs. If scope id is not specified, all IPv4 address ranges excluded on the server are returned.<br/> |
| [**Remove**](remove-ps-dhcpserverv4exclusionrange.md) | Deletes a range of IPv4 addresses previously excluded from an IPv4 Scope.<br/>                                                                                         |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





