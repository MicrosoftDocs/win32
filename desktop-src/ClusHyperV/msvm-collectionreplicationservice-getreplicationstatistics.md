---
title: GetReplicationStatistics method of the Msvm\_CollectionReplicationService class
description: Retrieves replication statistics associated with virtual system collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6e48e956-405e-4487-b200-880756def146
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetReplicationStatistics method
- GetReplicationStatistics method, Msvm_CollectionReplicationService class
- Msvm_CollectionReplicationService class, GetReplicationStatistics method
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.GetReplicationStatistics
api_location:
- clushyperv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetReplicationStatistics method of the Msvm\_CollectionReplicationService class

Retrieves replication statistics associated with virtual system collection.

## Syntax


```mof
uint32 GetReplicationStatistics(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [out] string                   ReplicationStatistics,
  [out] string                   ReplicationHealthIssues[1],
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the Hyper-V replica enabled [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) for which replication statistics need to be retrieved.

</dd> <dt>

*ReplicationStatistics* \[out\]
</dt> <dd>

If successful, this object contains the replication statistics for the requested virtual system collection. This is an embedded instance of [**Msvm\_CollectionReplicationStatistics**](msvm-collectionreplicationstatistics.md).

</dd> <dt>

*ReplicationHealthIssues* \[out\]
</dt> <dd>

If successful, this object contains the array of Group-level and VM-level error description strings that indicate reasons for the current replication health period being in warning, or in error for the requested virtual machine collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A [**CIM\_ConcreteJob**](cim-concretejob.md) reference to the job (can be null if the task is completed).

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Clushyperv.dll</dt> </dl>              |



## See also

<dl> <dt>

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> </dl>

 

 





