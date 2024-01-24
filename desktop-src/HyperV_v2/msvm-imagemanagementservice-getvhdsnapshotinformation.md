---
description: Retrieves information about a VHD Snapshot within a VHD Set file.
ms.assetid: 43745935-9bc3-4a87-8762-54693b2cdef6
title: GetVHDSnapshotInformation method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.GetVHDSnapshotInformation
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetVHDSnapshotInformation method of the Msvm\_ImageManagementService class

Retrieves information about a VHD Snapshot within a VHD Set file.

## Syntax


```mof
uint32 GetVHDSnapshotInformation(
  [in]  string              VHDSetPath,
  [in]  string              SnapshotIds[],
  [in]  uint32              AdditionalInformation[],
  [out] string              SnapshotInformation[],
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*VHDSetPath* \[in\]
</dt> <dd>

A fully-qualified path that specifies the location of the VHD Set file.

</dd> <dt>

*SnapshotIds* \[in\]
</dt> <dd>

A list of GUIDs representing the Snapshot Ids of each Snapshot for which information is being requested. If this parameter is NULL, information for all Snapshots will be retrieved.

</dd> <dt>

*AdditionalInformation* \[in\]
</dt> <dd>

An array specifying what additional information should be gathered about each VHD Snapshot. Each entry in the array is a type of additional information. If this parameter is NULL, no additional information will be retrieved.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Parent_Paths"></span><span id="parent_paths"></span><span id="PARENT_PATHS"></span>

**Parent Paths** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*SnapshotInformation* \[out\]
</dt> <dd>

If successful, an array of information about each requested snapshot. Each element is an embedded instance of [**Msvm\_VHDSnapshotInformation**](msvm-vhdsnapshotinformation.md).

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

 

 




