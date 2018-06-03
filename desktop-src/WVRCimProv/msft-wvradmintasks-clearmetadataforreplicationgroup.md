---
title: ClearMetadataForReplicationGroup method of the MSFT\_WvrAdminTasks class
description: Removes orphaned Storage Replica metadata from the partition, and system volume information folder for a replication group. This operation may result in the restart of the specified computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 833b09d5-e76b-4124-8e53-30bb6e2d12c9
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ClearMetadataForReplicationGroup method
- ClearMetadataForReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, ClearMetadataForReplicationGroup method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClearMetadataForReplicationGroup method of the MSFT\_WvrAdminTasks class

Removes orphaned Storage Replica metadata from the partition, and system volume information folder for a replication group. This operation may result in the restart of the specified computer.

## Syntax


```mof
uint32 ClearMetadataForReplicationGroup(
  [in] string  ComputerName,
  [in] string  Name,
  [in] boolean Logs,
  [in] boolean Partition,
  [in] boolean NoRestart
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Name* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Logs* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Partition* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*NoRestart* \[in\]
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

 

 





