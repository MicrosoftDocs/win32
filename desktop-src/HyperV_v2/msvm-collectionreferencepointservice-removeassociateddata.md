---
description: RemoveAssociatedData method of the Msvm_CollectionReferencePointService class - Removes the data log associated with the reference point.
ms.assetid: 42242b76-9123-41a7-b8b1-82d2e827ea53
title: RemoveAssociatedData method of the Msvm_CollectionReferencePointService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionReferencePointService.RemoveAssociatedData
api_type: 
- COM
api_location: 
- vmms.exe
---

# RemoveAssociatedData method of the Msvm\_CollectionReferencePointService class

Removes the data log associated with the reference point.

## Syntax


```mof
uint32 RemoveAssociatedData(
  [in]  CIM_Collection  REF AffectedReferencePointCollection,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*AffectedReferencePointCollection* \[in\]
</dt> <dd>

Reference to the affected virtual system reference point collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is long running, then optionally a job may be returned.

</dd> </dl>

## Return value

If successful, returns either 0 (no error), or 4096 (job started); otherwise, return an error.

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

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> </dl>

 

 




