---
title: PS\_DhcpServer class
description: Dhcp Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 115f8ae1-3efe-4324-8454-546d2be66b14
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DhcpServer class
- PS_DhcpServer class, described
topic_type:
- apiref
api_name:
- PS_DhcpServer
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DhcpServer class

Dhcp Server

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class PS_DhcpServer
{
};
```

## Members

The **PS\_DhcpServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DhcpServer** class has these methods.



| Method                                   | Description                                                                      |
|:-----------------------------------------|:---------------------------------------------------------------------------------|
| [**Backup**](backup-ps-dhcpserver.md)   | Backs up the DHCP database of DHCP Server to the specified location<br/>   |
| [**Restore**](restore-ps-dhcpserver.md) | Restores the database of the DHCP Server from the specified location.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





