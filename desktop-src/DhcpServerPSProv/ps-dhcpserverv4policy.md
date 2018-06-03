---
title: PS\_DhcpServerv4Policy class
description: Dhcp Server v4Policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 353b429f-008e-421f-9a25-40d6abcf4815
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4Policy class
- PS_DhcpServerv4Policy class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Policy
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerv4Policy class

Dhcp Server v4Policy

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4Policy
{
};
```

## Members

The **PS\_DhcpServerv4Policy** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4Policy** class has these methods.



| Method                                         | Description                                                                                                      |
|:-----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverv4policy.md)       | Adds a new policy either at the Server level or at the Scope level.<br/>                                   |
| [**Get**](get-ps-dhcpserverv4policy.md)       | Gets one or more policies at the server level or the scope level.<br/>                                     |
| [**Remove**](remove-ps-dhcpserverv4policy.md) | Deletes the specified IPv4 policy(ies) either at the server level or the specified scope level.<br/>       |
| [**Set**](set-ps-dhcpserverv4policy.md)       | Sets the properties of an existing policy either at the server level or at the specified scope level.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





