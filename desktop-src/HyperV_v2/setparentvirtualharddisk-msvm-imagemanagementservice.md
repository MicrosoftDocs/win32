---
description: Updates the parent for the specified leaf and child virtual hard disk files.
ms.assetid: 5ad41218-bcfd-449a-a66e-2096a1d96bf5
title: SetParentVirtualHardDisk method of the Msvm_ImageManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ImageManagementService.SetParentVirtualHardDisk
api_type: 
- COM
api_location: 
- vmms.exe
---

# SetParentVirtualHardDisk method of the Msvm\_ImageManagementService class

Updates the parent for the specified leaf and child virtual hard disk files. See Remarks for usage restrictions for this method.

## Syntax


```mof
uint32 SetParentVirtualHardDisk(
  [in]  string              ChildPath,
  [in]  string              ParentPath,
  [in]  string              LeafPath,
  [in]  boolean             IgnoreIDMismatch,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*ChildPath* \[in\]
</dt> <dd>

A fully qualified path that specifies the location of the child virtual hard disk file.

</dd> <dt>

*ParentPath* \[in\]
</dt> <dd>

A fully qualified path that specifies the location of the parent virtual hard disk file.

</dd> <dt>

*LeafPath* \[in\]
</dt> <dd>

A fully qualified path that specifies the location of the leaf virtual hard disk file. The parameter can be **Null** if the virtual hard disk is offline, but must be specified if the virtual hard disk is in use.

</dd> <dt>

*IgnoreIDMismatch* \[in\]
</dt> <dd>

Indicates if the parent should be forcibly set when the virtual disk identifiers do not match. This parameter must be used with caution because if the new parent virtual hard disk is not identical to the original parent, data corruption can occur.

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

**File not found** (32779)
</dt> </dl>

## Remarks

Only the following types of virtual hard disks can be used with this method:

-   Differencing VHD
-   Differencing VHDX

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

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

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

