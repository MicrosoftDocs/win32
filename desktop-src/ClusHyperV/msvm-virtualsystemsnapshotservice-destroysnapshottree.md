---
title: DestroySnapshotTree method of the Msvm\_VirtualSystemSnapshotService class
description: Deletes a tree that contains snapshots of a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4c308034-f691-4e33-82ca-e2bf4c6cb92e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DestroySnapshotTree method", "DestroySnapshotTree method, Msvm_VirtualSystemSnapshotService class", "Msvm_VirtualSystemSnapshotService class, DestroySnapshotTree method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemSnapshotService.DestroySnapshotTree
api_location:
- VMMS.exe
api_type:
- COM
---

# DestroySnapshotTree method of the Msvm\_VirtualSystemSnapshotService class

Deletes a tree that contains snapshots of a virtual machine.

## Syntax


```mof
uint32 DestroySnapshotTree(
  [in]  CIM_VirtualSystemSettingData REF SnapshotSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SnapshotSettingData* \[in\]
</dt> <dd>

A reference to a [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that represents the virtual machine snapshot tree to delete.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

This method returns one of the following values.

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

[**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md)
</dt> </dl>

 

 





