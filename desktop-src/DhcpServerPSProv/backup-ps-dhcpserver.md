---
title: Backup method of the PS\_DhcpServer class
description: Backs up the DHCP database of DHCP Server to the specified location.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 564923d5-b13a-4e30-b030-fe6d9660efa1
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Backup method
- Backup method, PS_DhcpServer class
- PS_DhcpServer class, Backup method
topic_type:
- apiref
api_name:
- PS_DhcpServer.Backup
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Backup method of the PS\_DhcpServer class

Backs up the DHCP database of DHCP Server to the specified location.

## Syntax


```mof
uint32 Backup(
  [in] string ComputerName,
  [in] string Path
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

The path to the directory where the backed up database will be stored.

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

 

 





