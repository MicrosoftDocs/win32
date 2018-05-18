---
title: WvrAddReplicaById method of the MSFT\_WvrAdminTasks class
description: Adds a volume to an existing replication group and assigns a replica set ID to the volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6efc20b8-0fca-40d0-a9ad-d004b681e90b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["WvrAddReplicaById method", "WvrAddReplicaById method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, WvrAddReplicaById method"]
---

# WvrAddReplicaById method of the MSFT\_WvrAdminTasks class

Adds a volume to an existing replication group and assigns a replica set ID to the volume.

## Syntax


```mof
uint32 WvrAddReplicaById(
  [in] string  ReplicationGroupName,
  [in] string  VolumeName[],
  [in] string  ReplicaSetId[],
  [in] boolean IsPrimary,
  [in] boolean Seeded
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

The name of the volumes to add.

</dd> <dt>

*ReplicaSetId* \[in\]
</dt> <dd>

The replica set IDs to associate with the new volumes.

</dd> <dt>

*IsPrimary* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Seeded* \[in\]
</dt> <dd>

TBD

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

 

 





