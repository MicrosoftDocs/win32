---
title: PrepareForReverseReplication method of the Msvm\_CollectionReplicationService class
description: Prepares the collection for reverse replication from a failed-over recovery collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'be1e3946-95b2-4f9f-8f47-93508723740d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PrepareForReverseReplication method", "PrepareForReverseReplication method, Msvm_CollectionReplicationService class", "Msvm_CollectionReplicationService class, PrepareForReverseReplication method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.PrepareForReverseReplication
api_location:
- VMMS.exe
api_type:
- COM
---

# PrepareForReverseReplication method of the Msvm\_CollectionReplicationService class

Prepares the collection for reverse replication from a failed-over recovery collection.

## Syntax


```mof
uint32 PrepareForReverseReplication(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) instance which needs to be prepared for reverse replication.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job (can be null if the task is completed).

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> </dl>

 

 





