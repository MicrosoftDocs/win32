---
title: PS\_DhcpServerv4MulticastExclusionRange class
description: PS\_DhcpServerv4MulticastExclusionRange class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd0f3d2a-b375-4502-b885-70116a24bb40
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4MulticastExclusionRange class
- PS_DhcpServerv4MulticastExclusionRange class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastExclusionRange
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4MulticastExclusionRange class

PS\_DhcpServerv4MulticastExclusionRange class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4MulticastExclusionRange
{
};
```

## Members

The **PS\_DhcpServerv4MulticastExclusionRange** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4MulticastExclusionRange** class has these methods.



| Method                                                          | Description                                                                         |
|:----------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4multicastexclusionrange.md)       | Sets the range of addresses to exclude from a multicast scope<br/>            |
| [**Get**](get-ps-dhcpserverv4multicastexclusionrange.md)       | Returns the Exclusion range for the specified multicast scopes<br/>           |
| [**Remove**](remove-ps-dhcpserverv4multicastexclusionrange.md) | Removes a range of addresses previously excluded from a multicast scope.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





