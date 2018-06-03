---
title: PS\_DhcpServerInDC class
description: DhcpServerInDC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 69c654eb-e5e4-404c-8edc-6b78fe9621e1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerInDC class
- PS_DhcpServerInDC class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerInDC
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerInDC class

DhcpServerInDC.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerInDC
{
};
```

## Members

The **PS\_DhcpServerInDC** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerInDC** class has these methods.



| Method                                     | Description                                                                                                                                                                                                       |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dhcpserverindc.md)       | Adds the server to the list of authorized DHCP servers in AD. A DHCP server running on a domain joined computer needs to be authorized in AD so that it can start leasing IP addresses on the network.<br/> |
| [**Get**](get-ps-dhcpserverindc.md)       | Retrieve the list of authorized DHCP servers from AD<br/>                                                                                                                                                   |
| [**Remove**](remove-ps-dhcpserverindc.md) | Deletes the specified DHCP server from the list of authorized servers in AD.<br/>                                                                                                                           |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





