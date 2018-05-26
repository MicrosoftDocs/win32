---
title: RenameCollection method of the Msvm\_CollectionManagementService class
description: Updates the ElementName property of a CIM\_CollectionOfMSEs object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2c3bf767-c97b-4eec-8321-8265159b493c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RenameCollection method
- RenameCollection method, Msvm_CollectionManagementService class
- Msvm_CollectionManagementService class, RenameCollection method
topic_type:
- apiref
api_name:
- Msvm_CollectionManagementService.RenameCollection
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RenameCollection method of the Msvm\_CollectionManagementService class

Updates the **ElementName** property of a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object.

## Syntax


```mof
uint32 RenameCollection(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  string                   NewName,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the collection to rename.

</dd> <dt>

*NewName* \[in\]
</dt> <dd>

The new name of the collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job for the operation. This parameter can be set to **NULL** if the job is complete.

</dd> </dl>

## Return value

The possible return values are:

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

 

 





