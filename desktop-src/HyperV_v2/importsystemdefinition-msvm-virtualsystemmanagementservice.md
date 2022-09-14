---
description: Creates a new planned computer system based on the specified virtual machine definition.
ms.assetid: 885d399f-5bcf-4f34-b2f1-582cbfcd7c10
title: ImportSystemDefinition method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.ImportSystemDefinition
api_type: 
- COM
api_location: 
- vmms.exe
---

# ImportSystemDefinition method of the Msvm\_VirtualSystemManagementService class

Creates a new planned computer system based on the specified virtual machine definition.

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

The fully qualified path to the system definition file (.xml or .exp) representing the virtual machine which is to be imported. The definition file must not already be in use by the host system or the virtualization platform.

</dd> <dt>

*SnapshotFolder* \[in\]
</dt> <dd>

The fully qualified path to the folder where the snapshot configurations for this virtual machine can be found. This folder will be searched in order to locate any snapshots referenced by the virtual machine definition. Any referenced snapshots not found in this location must be deleted using the [**DestroySnapshot**](destroysnapshot-msvm-virtualsystemsnapshotservice.md) method, or imported using the [**ImportSnapshotDefinitions**](importsnapshotdefinitions-msvm-virtualsystemmanagementservice.md) method prior to realizing the planned computer system.

</dd> <dt>

*GenerateNewSystemIdentifier* \[in\]
</dt> <dd>

Indicates whether to reuse the unique identifier for the virtual machine. If this parameter is **True**, then a new system identifier is generated. If this parameter is **False**, then the existing system identifier is used.

</dd> <dt>

*ImportedSystem* \[out\]
</dt> <dd>

If the operation completes synchronously, a reference to an [**Msvm\_PlannedComputerSystem**](msvm-plannedcomputersystem.md) object that represents the imported virtual machine.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

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
</dt> <dt>

**File in Use** (32779)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

