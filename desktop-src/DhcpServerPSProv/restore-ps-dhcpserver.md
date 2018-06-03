---
title: Restore method of the PS\_DhcpServer class
description: Restores the database of the DHCP Server from the specified location.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 725dea28-a7ae-471c-a10f-0901e7ce8ff8
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Restore method
- Restore method, PS_DhcpServer class
- PS_DhcpServer class, Restore method
topic_type:
- apiref
api_name:
- PS_DhcpServer.Restore
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Restore method of the PS\_DhcpServer class

Restores the database of the DHCP Server from the specified location.

## Syntax


```mof
uint32 Restore(
  [in] string  ComputerName,
  [in] string  Path,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Path to the location where the backup database is stored.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, user confirmation will not be sought.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServer**](ps-dhcpserver.md)
</dt> </dl>

 

 





