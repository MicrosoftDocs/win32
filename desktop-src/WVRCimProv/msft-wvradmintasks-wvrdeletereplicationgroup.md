---
title: WvrDeleteReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Deletes a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 16e4ba77-ce70-4f21-b599-f6159646642c
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrDeleteReplicationGroup method
- WvrDeleteReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrDeleteReplicationGroup method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrDeleteReplicationGroup method of the MSFT\_WvrAdminTasks class

Deletes a replication group.

## Syntax


```mof
uint32 WvrDeleteReplicationGroup(
  [in] string  ReplicationGroupName,
  [in] boolean FullCleanup
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*FullCleanup* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





