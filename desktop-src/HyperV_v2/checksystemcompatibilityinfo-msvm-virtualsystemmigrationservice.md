---
description: Checks the compatibility information for compatibility with the hosting computer system.
ms.assetid: 1991c58e-2d0b-4fc3-a04a-c18f358451f6
title: CheckSystemCompatibilityInfo method of the Msvm_VirtualSystemMigrationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemMigrationService.CheckSystemCompatibilityInfo
api_type: 
- COM
api_location: 
- vmms.exe
---

# CheckSystemCompatibilityInfo method of the Msvm\_VirtualSystemMigrationService class

Checks the compatibility information for compatibility with the hosting computer system.

## Syntax


```mof
uint32 CheckSystemCompatibilityInfo(
  [in]  uint8  CompatibilityInfo[],
  [out] string Reasons[]
);
```



## Parameters

<dl> <dt>

*CompatibilityInfo* \[in\]
</dt> <dd>

A blob of data obtained by calling the [**GetSystemCompatibilityInfo**](getsystemcompatibilityinfo-msvm-virtualsystemmigrationservice.md) method on the hosting computer system.

</dd> <dt>

*Reasons* \[out\]
</dt> <dd>

An array of strings that receives the embedded instances of the [**Msvm\_Error**](msvm-error.md) class that represent any warnings or errors.

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

**Not compatible** (32784)
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

 

 




