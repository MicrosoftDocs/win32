---
title: RemoveAssociatedData method of the Msvm\_CollectionReferencePointService class
description: Removes the data log associated with a reference point.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0bb11ce5-0293-45dc-85a3-18cd2e9dba1f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveAssociatedData method", "RemoveAssociatedData method, Msvm_CollectionReferencePointService class", "Msvm_CollectionReferencePointService class, RemoveAssociatedData method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionReferencePointService.RemoveAssociatedData
api_location:
- VMMS.exe
api_type:
- COM
---

# RemoveAssociatedData method of the Msvm\_CollectionReferencePointService class

Removes the data log associated with a reference point.

## Syntax


```mof
uint32 RemoveAssociatedData(
  [in]  CIM_Collection  REF AffectedReferencePointCollection,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*AffectedReferencePointCollection* \[in\]
</dt> <dd>

A reference to the affected reference point collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to a job that is used if the operation is performed asynchronously.

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

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> </dl>

 

 





