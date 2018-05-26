---
title: WvrGetOrphanedPartitionDbRecords method of the MSFT\_WvrAdminTasks class
description: Retrieves a list of orphaned Storage Replica metadata from the Storage Replica partition database for a replication group. If no ReplicationGroupName is specified the operation will be performed at a machine level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0ed0f322-c4bd-4bc9-8358-67eb3dc2630a
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrGetOrphanedPartitionDbRecords method
- WvrGetOrphanedPartitionDbRecords method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrGetOrphanedPartitionDbRecords method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrGetOrphanedPartitionDbRecords method of the MSFT\_WvrAdminTasks class

Retrieves a list of orphaned Storage Replica metadata from the Storage Replica partition database for a replication group. If no *ReplicationGroupName* is specified the operation will be performed at a machine level.

## Syntax


```mof
uint32 WvrGetOrphanedPartitionDbRecords(
  [in]  string                    ReplicationGroupName,
  [out] MSFT_WvrPartitionDbRecord OrphanedDbRecords[]
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*OrphanedDbRecords* \[out\]
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

 

 





