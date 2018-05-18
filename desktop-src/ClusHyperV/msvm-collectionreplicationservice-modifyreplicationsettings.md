---
title: ModifyReplicationSettings method of the Msvm\_CollectionReplicationService class
description: Updates replication setting data for a collection of virtual machines.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5a706a42-aec0-4e56-9b9b-0eae091ddc14'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifyReplicationSettings method", "ModifyReplicationSettings method, Msvm_CollectionReplicationService class", "Msvm_CollectionReplicationService class, ModifyReplicationSettings method"]
topic_type:
- apiref
api_name:
- Msvm_CollectionReplicationService.ModifyReplicationSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# ModifyReplicationSettings method of the Msvm\_CollectionReplicationService class

Updates replication setting data for a collection of virtual machines.

## Syntax


```mof
uint32 ModifyReplicationSettings(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  string                   CollectionReplicationSettingData,
  [out] CIM_ConcreteJob      REF Job
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) instance that represents the collection of virtual machines.

</dd> <dt>

*CollectionReplicationSettingData* \[in\]
</dt> <dd>

The updated setting data for the replication.

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
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> </dl>

 

 





