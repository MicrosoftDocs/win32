---
title: RevokeSrUserAccess method of the MSFT\_WvrAdminTasks class
description: Revokes capabilities required for the user to manage Storage Replica on a given computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb66041a-9330-4662-a145-9e9ec025eefe
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RevokeSrUserAccess method
- RevokeSrUserAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, RevokeSrUserAccess method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.RevokeSrUserAccess
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RevokeSrUserAccess method of the MSFT\_WvrAdminTasks class

Revokes capabilities required for the user to manage Storage Replica on a given computer.

## Syntax


```mof
uint32 RevokeSrUserAccess(
  [in] string  ComputerName,
  [in] string  UserName,
  [in] boolean RemoveFromRemoteManagementUsersGroup
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the computer.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The name of the user to revoke access.

</dd> <dt>

*RemoveFromRemoteManagementUsersGroup* \[in\]
</dt> <dd>

**true** to remove the user from the group; otherwise, **false**.

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

 

 





