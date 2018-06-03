---
title: ActivateReplicaSet method of the MSFT\_WvrAdminTasks class
description: Assigns replica set IDs and partitions to replication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0c437347-5846-4f97-a6ea-3ce46a3569fa
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ActivateReplicaSet method
- ActivateReplicaSet method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, ActivateReplicaSet method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.ActivateReplicaSet
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ActivateReplicaSet method of the MSFT\_WvrAdminTasks class

Assigns replica set IDs and partitions to replication.

## Syntax


```mof
uint32 ActivateReplicaSet(
  [in] string ReplicationGroupName,
  [in] string ReplicaSetId[]
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

Identifies the replication group to modify.

</dd> <dt>

*ReplicaSetId* \[in\]
</dt> <dd>

The IDs of the set of replicas to add to the replication group.

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

 

 





