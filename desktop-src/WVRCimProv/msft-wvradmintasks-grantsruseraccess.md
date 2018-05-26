---
title: GrantSrUserAccess method of the MSFT\_WvrAdminTasks class
description: Grants the user all capabilities required to manage Storage Replica on a given computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43e0f5ee-236f-481d-9aca-003bb40f4e38
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GrantSrUserAccess method
- GrantSrUserAccess method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, GrantSrUserAccess method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GrantSrUserAccess method of the MSFT\_WvrAdminTasks class

Grants the user all capabilities required to manage Storage Replica on a given computer.

## Syntax


```mof
uint32 GrantSrUserAccess(
  [in] string  ComputerName,
  [in] string  UserName,
  [in] boolean IgnoreErrors
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the computer to grant access on.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

The name of the user to grant access to.

</dd> <dt>

*IgnoreErrors* \[in\]
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

 

 





