---
title: PS\_DhcpServerAuditLog class
description: Dhcp Server Log Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7cdb3b9c-fd15-44af-b1e4-8d76eb15d8bb
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServerAuditLog class
- PS_DhcpServerAuditLog class, described
topic_type:
- apiref
api_name:
- PS_DhcpServerAuditLog
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DhcpServerAuditLog class

Dhcp Server Log Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServerAuditLog
{
};
```

## Members

The **PS\_DhcpServerAuditLog** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServerAuditLog** class has these methods.



| Method                                   | Description                                                                                             |
|:-----------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dhcpserverauditlog.md) | Gets the configuration parameters related to the audit log of the DHCP server.<br/>               |
| [**Set**](set-ps-dhcpserverauditlog.md) | Sets DHCP server audit log configuration on the server - including enabling or disabling it.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





