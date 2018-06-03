---
title: SmapiQueryPartnerPartitions method of the MSFT\_WvrAdminTasks class
description: Retrieves the partner partition information for this replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2545ba3-1a71-45d2-9d43-3112d4538ebc
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SmapiQueryPartnerPartitions method
- SmapiQueryPartnerPartitions method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SmapiQueryPartnerPartitions method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SmapiQueryPartnerPartitions method of the MSFT\_WvrAdminTasks class

Retrieves the partner partition information for this replication group.

## Syntax


```mof
uint32 SmapiQueryPartnerPartitions(
  [in]  string   ReplicationGroupName,
  [in]  string   PartitionId,
  [out] string   PartnerComputerName,
  [out] string   PartnerPartitionObjectId,
  [out] uint16   PartnerPercentSynced,
  [out] datetime PartnerLastSyncTime,
  [out] uint32   PartnerReplicationStatus
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*PartitionId* \[in\]
</dt> <dd>

The partition ID.

</dd> <dt>

*PartnerComputerName* \[out\]
</dt> <dd>

the partner computer name.

</dd> <dt>

*PartnerPartitionObjectId* \[out\]
</dt> <dd>

The partner partition object ID.

</dd> <dt>

*PartnerPercentSynced* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*PartnerLastSyncTime* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*PartnerReplicationStatus* \[out\]
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

 

 





