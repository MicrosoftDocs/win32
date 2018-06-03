---
title: WvrClearOrphanedLogs method of the MSFT\_WvrAdminTasks class
description: Removes orphaned Storage Replica metadata from the Storage Replica log container for a replication group. If no ReplicationGroupName is specified the operation will be performed at a machine level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4da7b1e4-90dc-4663-8c88-51119171e154
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrClearOrphanedLogs method
- WvrClearOrphanedLogs method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrClearOrphanedLogs method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrClearOrphanedLogs method of the MSFT\_WvrAdminTasks class

Removes orphaned Storage Replica metadata from the Storage Replica log container for a replication group. If no *ReplicationGroupName* is specified the operation will be performed at a machine level.

## Syntax


```mof
uint32 WvrClearOrphanedLogs(
  [in] string ReplicationGroupName
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
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

 

 





