---
title: WvrRevokeUserAccess method of the MSFT\_WvrAdminTasks class
description: Performs a CIM call to revoke the user permissions to manage Storage Replica.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23e8416f-9c94-44d2-b164-436ab031fc15
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrRevokeUserAccess method
- WvrRevokeUserAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrRevokeUserAccess method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrRevokeUserAccess method of the MSFT\_WvrAdminTasks class

Performs a CIM call to revoke the user permissions to manage Storage Replica.

## Syntax


```mof
uint32 WvrRevokeUserAccess(
  [in] string  UserName,
  [in] boolean RemoveFromRemoteManagementUsersGroup
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The name of the user to revoke permissions from.

</dd> <dt>

*RemoveFromRemoteManagementUsersGroup* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





