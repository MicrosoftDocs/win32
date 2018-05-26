---
title: ReverseReplicationRelationship method of the Msvm\_CollectionReplicationService class
description: Reverses replication for the recovery collection using the collection replication setting specified. This API requires the collection that is a recovery collection in failover committed state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cf659289-0973-4e6c-8d3f-b310b3eef827
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ReverseReplicationRelationship method
- ReverseReplicationRelationship method, Msvm_CollectionReplicationService class
- Msvm_CollectionReplicationService class, ReverseReplicationRelationship method
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.ReverseReplicationRelationship
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ReverseReplicationRelationship method of the Msvm\_CollectionReplicationService class

Reverses replication for the recovery collection using the collection replication setting specified. This API requires the collection that is a recovery collection in failover committed state.

## Syntax


```mof
uint32 ReverseReplicationRelationship(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  string                   CollectionReplicationSettingData,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) instance for which the replication should be reversed.

</dd> <dt>

*CollectionReplicationSettingData* \[in\]
</dt> <dd>

A [**CollectionReplicationSettingData**](msvm-collectionreplicationsettingdata.md) containing the setting data for replication.

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
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> </dl>

 

 





