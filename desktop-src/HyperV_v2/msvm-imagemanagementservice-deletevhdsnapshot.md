---
description: Deletes a VHD Snapshot entry within a VHD Set file.
ms.assetid: 37d55a5f-209d-42ce-8f69-8b494055e263
title: DeleteVHDSnapshot method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.DeleteVHDSnapshot
api_type: 
- COM
api_location: 
- vmms.exe
---

# DeleteVHDSnapshot method of the Msvm\_ImageManagementService class

Deletes a VHD Snapshot entry within a VHD Set file.

## Syntax


```mof
uint32 DeleteVHDSnapshot(
  [in]  string              VHDSetPath,
  [in]  string              SnapshotId,
  [in]  boolean             PersistReferenceSnapshot,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*VHDSetPath* \[in\]
</dt> <dd>

String containing the path to the VHD Set file containing the snapshot in question.

</dd> <dt>

*SnapshotId* \[in\]
</dt> <dd>

A GUID representing the Snapshot ID for the VHD Snapshot entry to be deleted.

</dd> <dt>

*PersistReferenceSnapshot* \[in\]
</dt> <dd>

Whether or not a reference-only snapshot record should be persisted after the snapshot is deleted.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the job (can be null if the task is completed).

</dd> </dl>

## Return value

This method returns one of the following values:

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 




