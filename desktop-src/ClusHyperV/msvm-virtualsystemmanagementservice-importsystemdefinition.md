---
title: ImportSystemDefinition method of the Msvm\_VirtualSystemManagementService class
description: Creates a new planned virtual system based on a virtual system definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9eeb3fc5-767e-4d02-9e23-cf5bdc658fba
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ImportSystemDefinition method
- ImportSystemDefinition method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, ImportSystemDefinition method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ImportSystemDefinition
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ImportSystemDefinition method of the Msvm\_VirtualSystemManagementService class

Creates a new planned virtual system based on a virtual system definition.

When this method is run, the files of the virtual system definition must not be in use by the host system or the virtualization platform. The snapshot folder is searched the snapshots referenced by the virtual system definition. Any referenced snapshots not found in this location must be deleted using the [**RemoveVirtualSystemSnapshot**](https://msdn.microsoft.com/library/cc136962) method, or imported using the [**ImportSnapshotDefinitions**](msvm-virtualsystemmanagementservice-importsnapshotdefinitions.md) method before running **ImportSystemDefinition**.

## Syntax


```mof
uint32 ImportSystemDefinition(
  [in]  string                         SystemDefinitionFile,
  [in]  string                         SnapshotFolder,
  [in]  boolean                        GenerateNewSystemIdentifier,
  [out] Msvm_PlannedComputerSystem REF ImportedSystem,
  [out] CIM_ConcreteJob            REF Job
);
```



## Parameters

<dl> <dt>

*SystemDefinitionFile* \[in\]
</dt> <dd>

The fully-qualified path to the XML or EXP file that represents the virtual system definition to import.

</dd> <dt>

*SnapshotFolder* \[in\]
</dt> <dd>

The fully-qualified path to the folder where the snapshot configurations for this virtual machine are located.

</dd> <dt>

*GenerateNewSystemIdentifier* \[in\]
</dt> <dd>

**true** if to create a new unique identifier for the virtual system; otherwise, **false**.

</dd> <dt>

*ImportedSystem* \[out\]
</dt> <dd>

If the operation completes synchronously, a reference to the imported virtual system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is being performed asynchronously, a reference to the job object which can be used to track the progress.

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

 

 





