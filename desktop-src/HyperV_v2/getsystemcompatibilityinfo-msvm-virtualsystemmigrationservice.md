---
description: Generates an opaque blob of data that contains compatibility information for the specified system.
ms.assetid: 5cfb50c4-d695-4867-ac6a-234ce5120a6d
title: GetSystemCompatibilityInfo method of the Msvm_VirtualSystemMigrationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemMigrationService.GetSystemCompatibilityInfo
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetSystemCompatibilityInfo method of the Msvm\_VirtualSystemMigrationService class

Generates an opaque blob of data that contains compatibility information for the specified system. This method is used in conjunction with the [**CheckSystemCompatibilityInfo**](checksystemcompatibilityinfo-msvm-virtualsystemmigrationservice.md) method to determine whether a quick or live migration of a virtual machine to another hosting computer system is possible without actually attempting the migration.

## Syntax


```mof
uint32 GetSystemCompatibilityInfo(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [out] uint8                  CompatibilityInfo[]
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represents the virtual machine to retrieve compatibility information for. If this parameter refers to the hosting computer system, the data returned in the *CompatibilityInfo* parameter can be used to determine whether any of the virtual machines on the hosting computer system can be quickly migrated to another hosting computer system.

</dd> <dt>

*CompatibilityInfo* \[out\]
</dt> <dd>

An opaque blob of data that can be passed to the [**CheckSystemCompatibilityInfo**](checksystemcompatibilityinfo-msvm-virtualsystemmigrationservice.md) method on another hosting computer system to confirm compatibility.

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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 




