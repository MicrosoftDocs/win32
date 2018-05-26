---
title: ImportSnapshotDefinitions method of the Msvm\_VirtualSystemManagementService class
description: Creates snapshots for each snapshot definition files of a planned virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 633c8511-c044-4f84-857b-857587379ff7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ImportSnapshotDefinitions method
- ImportSnapshotDefinitions method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, ImportSnapshotDefinitions method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ImportSnapshotDefinitions
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ImportSnapshotDefinitions method of the Msvm\_VirtualSystemManagementService class

Creates snapshots for each snapshot definition files of a planned virtual machine.

## Syntax


```mof
uint32 ImportSnapshotDefinitions(
  [in]  Msvm_PlannedComputerSystem    REF PlannedSystem,
  [in]  string                            SnapshotFolder,
  [out] Msvm_VirtualSystemSettingData REF ImportedSnapshots[],
  [out] CIM_ConcreteJob               REF Job
);
```



## Parameters

<dl> <dt>

*PlannedSystem* \[in\]
</dt> <dd>

A reference to the planned virtual machine that is associated with the snapshot definition files.

</dd> <dt>

*SnapshotFolder* \[in\]
</dt> <dd>

The fully-qualified path to the folder that contains the snapshot definition files for the virtual machine.

</dd> <dt>

*ImportedSnapshots* \[out\]
</dt> <dd>

If the operation completes synchronously, an array of references to the [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) instances that represent the snapshots that were successfully imported.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

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

**File in Use** (32779)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





