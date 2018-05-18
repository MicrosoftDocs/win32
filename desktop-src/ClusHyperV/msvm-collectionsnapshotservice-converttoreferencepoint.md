---
title: ConvertToReferencePoint method of the Msvm\_CollectionSnapshotService class
description: Converts a recovery snapshot of a virtual system collection to a reference point collection. After the conversion, the snapshot collection is deleted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cd34859b-afa4-422d-9227-1d10bb678df7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ConvertToReferencePoint method", "ConvertToReferencePoint method, Msvm_CollectionSnapshotService class", "Msvm_CollectionSnapshotService class, ConvertToReferencePoint method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionSnapshotService.ConvertToReferencePoint
api_location:
- VMMS.exe
api_type:
- COM
---

# ConvertToReferencePoint method of the Msvm\_CollectionSnapshotService class

Converts a recovery snapshot of a virtual system collection to a reference point collection. After the conversion, the snapshot collection is deleted.

## Syntax


```mof
uint32 ConvertToReferencePoint(
  [in]      Msvm_SnapshotCollection       REF AffectedSnapshotCollection,
  [in, out] Msvm_ReferencePointCollection REF ResultingReferencePointCollection,
  [out]     CIM_ConcreteJob               REF Job
);
```



## Parameters

<dl> <dt>

*AffectedSnapshotCollection* \[in\]
</dt> <dd>

A reference to the virtual system snapshot collection to convert.

</dd> <dt>

*ResultingReferencePointCollection* \[in, out\]
</dt> <dd>

A reference to the new virtual system reference point collection.

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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> </dl>

 

 





