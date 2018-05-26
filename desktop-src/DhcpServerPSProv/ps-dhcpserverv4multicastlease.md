---
title: PS\_DhcpServerv4MulticastLease class
description: PS\_DhcpServerv4MulticastLease class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0609bd48-e3c0-4b34-a652-d8a632ddbff8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerv4MulticastLease class
- PS_DhcpServerv4MulticastLease class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerv4MulticastLease
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServerv4MulticastLease class

PS\_DhcpServerv4MulticastLease class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerv4MulticastLease
{
};
```

## Members

The **PS\_DhcpServerv4MulticastLease** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerv4MulticastLease** class has these methods.



| Method                                                 | Description                                                                                                                    |
|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverv4multicastlease.md)       | Gets multicast leases corresponding to the specified scope name<br/>                                                     |
| [**Remove**](remove-ps-dhcpserverv4multicastlease.md) | Deletes one or more multicast scope leases corresponding to the specified multicast scope or specified IP addresses<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





