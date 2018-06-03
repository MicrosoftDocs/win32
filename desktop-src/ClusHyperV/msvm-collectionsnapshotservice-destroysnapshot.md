---
title: DestroySnapshot method of the Msvm\_CollectionSnapshotService class
description: Deletes a snapshot of a virtual system collection. When this method completes, the dependent snapshots are also deleted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d87ec863-be24-4210-9bd2-3c8dc4e5bc9d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DestroySnapshot method
- DestroySnapshot method, Msvm_CollectionSnapshotService class
- Msvm_CollectionSnapshotService class, DestroySnapshot method
topic_type:
- apiref
api_name:
- Msvm_CollectionSnapshotService.DestroySnapshot
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DestroySnapshot method of the Msvm\_CollectionSnapshotService class

Deletes a snapshot of a virtual system collection. When this method completes, the dependent snapshots are also deleted.

## Syntax


```mof
uint32 DestroySnapshot(
  [in]  CIM_Collection  REF AffectedSnapshotCollection,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSnapshotCollection* \[in\]
</dt> <dd>

Reference to the affected virtual system snapshot collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional job to use for this operation if it is performed asynchronously.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Invalid Type** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 





