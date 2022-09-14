---
description: Converts a virtual hard disk file by creating a new VHD Set file alongside the existing virtual hard disk.
ms.assetid: 04ae723e-e3c5-4640-a0e5-0e1b75bb2e6d
title: ConvertVirtualHardDiskToVHDSet method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.ConvertVirtualHardDiskToVHDSet
api_type: 
- COM
api_location: 
- vmms.exe
---

# ConvertVirtualHardDiskToVHDSet method of the Msvm\_ImageManagementService class

Converts a virtual hard disk file by creating a new VHD Set file alongside the existing virtual hard disk.

## Syntax


```mof
uint32 ConvertVirtualHardDiskToVHDSet(
  [in]  string              VirtualHardDiskPath,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*VirtualHardDiskPath* \[in\]
</dt> <dd>

String containing the path to the virtual hard disk file. The new VHD Set file will have the same filename but with the .VHDS extension.

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

 

 




