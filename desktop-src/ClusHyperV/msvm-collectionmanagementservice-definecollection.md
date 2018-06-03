---
title: DefineCollection method of the Msvm\_CollectionManagementService class
description: Creates a new CIM\_CollectionOfMSEs object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: abd5869d-affe-4464-8c3e-91bb307374da
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DefineCollection method
- DefineCollection method, Msvm_CollectionManagementService class
- Msvm_CollectionManagementService class, DefineCollection method
topic_type:
- apiref
api_name:
- Msvm_CollectionManagementService.DefineCollection
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DefineCollection method of the Msvm\_CollectionManagementService class

Creates a new CIM\_CollectionOfMSEs object.

## Syntax


```mof
uint32 DefineCollection(
  [in]  string                   Name,
  [in]  string                   Id,
  [in]  uint16                   Type,
  [out] CIM_CollectionOfMSEs REF DefinedCollection,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A user defined name for the new collection. If a name is not specified, the default new collection name is used.

</dd> <dt>

*Id* \[in\]
</dt> <dd>

A **GUID** used to identify the group. The **GUID** must be unique, or the call will fail. If a **GUID** is not specified, the service generates one.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of collection object to create.

<dt>

<span id="Collection_of_Virtual_Systems"></span><span id="collection_of_virtual_systems"></span><span id="COLLECTION_OF_VIRTUAL_SYSTEMS"></span>

**Collection of Virtual Systems** (0)


</dt> <dd></dd> <dt>

<span id="Collection_of_Collections"></span><span id="collection_of_collections"></span><span id="COLLECTION_OF_COLLECTIONS"></span>

**Collection of Collections** (1)


</dt> <dd></dd> </dl> </dd> <dt>

*DefinedCollection* \[out\]
</dt> <dd>

A reference to the new collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job for the operation. This parameter can be set to **NULL** if the job is complete.

</dd> </dl>

## Return value

The possible returns values are:

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

 

 





