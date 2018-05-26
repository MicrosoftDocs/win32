---
title: PS\_DhcpServerv4PolicyIPRange class
description: Dhcp Server v4Policy IPRange.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 091e9821-49de-48e3-8009-deb56bd7357d
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4PolicyIPRange class
- PS_DhcpServerv4PolicyIPRange class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4PolicyIPRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4PolicyIPRange class

Dhcp Server v4Policy IPRange.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4PolicyIPRange
{
};
```

## Members

The **PS\_DhcpServerv4PolicyIPRange** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4PolicyIPRange** class has these methods.



| Method                                                | Description                                                                |
|:------------------------------------------------------|:---------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4policyiprange.md)       | Adds an IP range to an existing policy at the scope level.<br/>      |
| [**Get**](get-ps-dhcpserverv4policyiprange.md)       | Gets an IP range(s) from a policy in the specified scope.<br/>       |
| [**Remove**](remove-ps-dhcpserverv4policyiprange.md) | Deletes an IP range from an existing policy at the scope level.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





