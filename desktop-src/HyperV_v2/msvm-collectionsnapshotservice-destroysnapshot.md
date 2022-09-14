---
description: Destroys an existing snapshot of virtual system collection. This method may as a side effect destroy other snapshots that are dependent on the affected snapshot.
ms.assetid: 79a529d5-35bb-4e63-a1b7-8943de9580e8
title: DestroySnapshot method of the Msvm_CollectionSnapshotService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionSnapshotService.DestroySnapshot
api_type: 
- COM
api_location: 
- vmms.exe
---

# DestroySnapshot method of the Msvm\_CollectionSnapshotService class

Destroys an existing snapshot of virtual system collection. This method may as a side effect destroy other snapshots that are dependent on the affected snapshot.

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

Reference to a [**CIM\_Collection**](cim-collection.md) that describes the affected virtual system snapshot collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](cim-concretejob.md) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

On success, returns either 0 (Complete) or 4096 (Job Started); otherwise, returns an error.

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

**DMTF Reserved** (..)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097..32767)
</dt> <dt>

**Vendor Specific** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 




