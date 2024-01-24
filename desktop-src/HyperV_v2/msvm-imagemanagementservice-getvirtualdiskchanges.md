---
description: Retrieves a list of changes in the specified region of a virtual disk since the provided Resilient Change Tracking Id or VHDSet Snapshot Id.
ms.assetid: c1dac403-96e0-4c0d-ad71-858f04bf07cd
title: GetVirtualDiskChanges method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.GetVirtualDiskChanges
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetVirtualDiskChanges method of the Msvm\_ImageManagementService class

Retrieves a list of changes in the specified region of a virtual disk since the provided Resilient Change Tracking Id or VHDSet Snapshot Id.

## Syntax


```mof
uint32 GetVirtualDiskChanges(
  [in]  string              Path,
  [in]  string              LimitId,
  [in]  string              TargetSnapshotId,
  [in]  uint64              ByteOffset,
  [in]  uint64              ByteLength,
  [out] uint64              ProcessedByteLength,
  [out] uint64              ChangedByteOffsets[],
  [out] uint64              ChangedByteLengths[],
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

A fully-qualified path that specifies the location of the Virtual Hard Disk file.

</dd> <dt>

*LimitId* \[in\]
</dt> <dd>

A Resilient Change Tracking Id or VHD Set Snapshot Id indicating the baseline for changes in the virtual disk.

</dd> <dt>

*TargetSnapshotId* \[in\]
</dt> <dd>

A VHDSet Snapshot Id indicating the snapshot to compare to the baseline when determing changes in the virtual hard disk. This parameter is only valid for VHD Set files.

</dd> <dt>

*ByteOffset* \[in\]
</dt> <dd>

The byte offset of the region in the virtual disk to query changes for.

</dd> <dt>

*ByteLength* \[in\]
</dt> <dd>

The byte length of the region in the virtual disk to query changes for. This must be less than the size of the Virtual Disk.

</dd> <dt>

*ProcessedByteLength* \[out\]
</dt> <dd>

The total byte length that was processed. This may be equal to ByteLength or less.

</dd> <dt>

*ChangedByteOffsets* \[out\]
</dt> <dd>

The list of byte offsets into the virtual disk indicating the beginning of each changed range.

</dd> <dt>

*ChangedByteLengths* \[out\]
</dt> <dd>

The list of byte lengths of the changed ranges in the virtual disk.

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

 

 




