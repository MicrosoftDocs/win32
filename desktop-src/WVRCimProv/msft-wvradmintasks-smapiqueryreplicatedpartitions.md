---
title: SmapiQueryReplicatedPartitions method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd582f740-6a2c-448b-8671-ab233f51923a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SmapiQueryReplicatedPartitions method", "SmapiQueryReplicatedPartitions method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, SmapiQueryReplicatedPartitions method"]
---

# SmapiQueryReplicatedPartitions method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 SmapiQueryReplicatedPartitions(
  [in]  string ComputerName,
  [in]  string ReplicationGroupName,
  [out] string PartitionObjectIds[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*PartitionObjectIds* \[out\]
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

 

 





