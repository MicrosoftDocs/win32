---
title: DeactivateReplicaSet method of the MSFT\_WvrAdminTasks class
description: Removes a partition from replication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '234d9bd5-ad06-4620-8819-932bf3f8a2c3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DeactivateReplicaSet method", "DeactivateReplicaSet method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, DeactivateReplicaSet method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.DeactivateReplicaSet
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# DeactivateReplicaSet method of the MSFT\_WvrAdminTasks class

Removes a partition from replication.

## Syntax


```mof
uint32 DeactivateReplicaSet(
  [in] string ReplicationGroupName,
  [in] string ReplicaSetId[]
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group to modify.

</dd> <dt>

*ReplicaSetId* \[in\]
</dt> <dd>

The IDs of the replicas to remove from the group.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





