---
title: ResetReplicationStatistics method of the Msvm\_CollectionReplicationService class
description: Resets replication statistics associated with virtual system collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0bd34888-d5d6-44b1-bc39-9a8dd8fa0bc7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ResetReplicationStatistics method
- ResetReplicationStatistics method, Msvm_CollectionReplicationService class
- Msvm_CollectionReplicationService class, ResetReplicationStatistics method
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.ResetReplicationStatistics
api_location:
- clushyperv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResetReplicationStatistics method of the Msvm\_CollectionReplicationService class

Resets replication statistics associated with virtual system collection.

## Syntax


```mof
uint32 ResetReplicationStatistics(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the Hyper-V replica enabled [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md).

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

 

 





