---
title: WvrRemoveReplicaById method of the MSFT\_WvrAdminTasks class
description: Removes a volume from an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bebc73c1-f4f6-4018-81b8-d17f8915774a
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrRemoveReplicaById method
- WvrRemoveReplicaById method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrRemoveReplicaById method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WvrRemoveReplicaById method of the MSFT\_WvrAdminTasks class

Removes a volume from an existing replication group.

## Syntax


```mof
uint32 WvrRemoveReplicaById(
  [in] string  ReplicationGroupName,
  [in] string  ReplicaSetId[],
  [in] boolean IsPrimary
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*ReplicaSetId* \[in\]
</dt> <dd>

The replica set IDs to remove.

</dd> <dt>

*IsPrimary* \[in\]
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

 

 





