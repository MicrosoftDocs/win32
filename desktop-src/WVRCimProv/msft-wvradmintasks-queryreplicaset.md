---
title: QueryReplicaSet method of the MSFT\_WvrAdminTasks class
description: Returns replica set information for a given replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93f1d0ba-393a-4363-a0f4-ca9353dff189
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- QueryReplicaSet method
- QueryReplicaSet method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, QueryReplicaSet method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# QueryReplicaSet method of the MSFT\_WvrAdminTasks class

Returns replica set information for a given replication group.

## Syntax


```mof
uint32 QueryReplicaSet(
  [in]  string ReplicationGroupName,
  [in]  string VolumeName,
  [out] string PartitionId,
  [out] string ReplicaSetId
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*VolumeName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PartitionId* \[out\]
</dt> <dd>

Identifies the partition containing the replica set.

</dd> <dt>

*ReplicaSetId* \[out\]
</dt> <dd>

Identifies the replica set.

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

 

 





