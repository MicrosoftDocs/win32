---
title: AddMember method of the Msvm\_CollectionManagementService class
description: Adds a managed element to a CIM\_CollectionOfMSEs object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dac42e8d-e757-4340-ad17-42a8606f0d43
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddMember method
- AddMember method, Msvm_CollectionManagementService class
- Msvm_CollectionManagementService class, AddMember method
topic_type:
- apiref
api_name:
- Msvm_CollectionManagementService.AddMember
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddMember method of the Msvm\_CollectionManagementService class

Adds a managed element to a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.

## Syntax


```mof
uint32 AddMember(
  [in]  CIM_ManagedElement   REF Member,
  [in]  CIM_CollectionOfMSEs REF Collection,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Member* \[in\]
</dt> <dd>

A reference to the managed element to add.

</dd> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the collection that receives the managed element.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job for the operation. This parameter can be set to NULL if the job is complete.

</dd> </dl>

## Return value

The possible values are:

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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionManagementService**](msvm-collectionmanagementservice.md)
</dt> </dl>

 

 





