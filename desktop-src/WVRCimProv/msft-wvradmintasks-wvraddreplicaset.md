---
title: WvrAddReplicaSet method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 11495cb6-6d7a-4377-ac16-9fd8c360551c
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrAddReplicaSet method
- WvrAddReplicaSet method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrAddReplicaSet method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.WvrAddReplicaSet
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrAddReplicaSet method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 WvrAddReplicaSet(
  [in] string SourceReplicationGroupName,
  [in] string SourcePartitionId,
  [in] string TargetComputerName,
  [in] string TargetReplicationGroupName,
  [in] string TargetPartitionId
);
```



## Parameters

<dl> <dt>

*SourceReplicationGroupName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*SourcePartitionId* \[in\]
</dt> <dd>

Identifies the source partition.

</dd> <dt>

*TargetComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the target computer.

</dd> <dt>

*TargetReplicationGroupName* \[in\]
</dt> <dd>

The name of the target replication group.

</dd> <dt>

*TargetPartitionId* \[in\]
</dt> <dd>

Identifies the target partition.

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

 

 





