---
title: WvrInitializeReplicationGroup method of the MSFT\_WvrAdminTasks class
description: This routine initializes a newly provisioned replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e547fc7d-5e0a-43b0-adc9-e4fd0a366de0
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WvrInitializeReplicationGroup method
- WvrInitializeReplicationGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, WvrInitializeReplicationGroup method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WvrInitializeReplicationGroup method of the MSFT\_WvrAdminTasks class

This routine initializes a newly provisioned replication group.

## Syntax


```mof
uint32 WvrInitializeReplicationGroup(
  [in] string ReplicationGroupName,
  [in] string ReplicaSetIds[],
  [in] uint32 ReplicationRole,
  [in] string PartnerReplicationGroupName,
  [in] string PartnerReplicationGroupEndpoint,
  [in] string partnerReplicationGroupId,
  [in] string PartnershipId
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ReplicaSetIds* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ReplicationRole* \[in\]
</dt> <dd>

n/a

<dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>

**Source** (1)


</dt> <dd></dd> <dt>

<span id="Destination"></span><span id="destination"></span><span id="DESTINATION"></span>

**Destination** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*PartnerReplicationGroupName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PartnerReplicationGroupEndpoint* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*partnerReplicationGroupId* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PartnershipId* \[in\]
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

 

 





