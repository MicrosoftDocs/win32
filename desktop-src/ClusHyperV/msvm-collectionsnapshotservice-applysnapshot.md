---
title: ApplySnapshot method of the Msvm\_CollectionSnapshotService class
description: Applies a snapshot collection to the collection of virtual computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e9186210-9c2d-4cad-936f-85044dd0dd41'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ApplySnapshot method", "ApplySnapshot method, Msvm_CollectionSnapshotService class", "Msvm_CollectionSnapshotService class, ApplySnapshot method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionSnapshotService.ApplySnapshot
api_location:
- VMMS.exe
api_type:
- COM
---

# ApplySnapshot method of the Msvm\_CollectionSnapshotService class

Applies a snapshot collection to the collection of virtual computer system.

## Syntax


```mof
uint32 ApplySnapshot(
  [in]  CIM_Collection  REF SnapshotCollection,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SnapshotCollection* \[in\]
</dt> <dd>

A reference to a [**CIM\_Collection**](cim-collection.md) that represents the snapshot collection to be applied.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](cim-concretejob.md) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
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

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 





