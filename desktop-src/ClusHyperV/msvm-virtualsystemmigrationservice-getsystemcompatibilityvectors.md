---
title: GetSystemCompatibilityVectors method of the Msvm\_VirtualSystemMigrationService class
description: Gets a list of Msvm\_CompatibilityVector instances that can be used to check for virtual machine (VM) to host compatibility.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '86f6a836-779f-42ad-b68b-dcb466511f2c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSystemCompatibilityVectors method", "GetSystemCompatibilityVectors method, Msvm_VirtualSystemMigrationService class", "Msvm_VirtualSystemMigrationService class, GetSystemCompatibilityVectors method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.GetSystemCompatibilityVectors
api_location:
- VMMS.exe
api_type:
- COM
---

# GetSystemCompatibilityVectors method of the Msvm\_VirtualSystemMigrationService class

Gets a list of [**Msvm\_CompatibilityVector**](https://msdn.microsoft.com/library/windows/desktop/dn280574) instances that can be used to check for virtual machine (VM) to host compatibility.

## Syntax


```mof
uint32 GetSystemCompatibilityVectors(
  [in]  CIM_ComputerSystem   REF ComputerSystem,
  [out] Msvm_CompatibilityVector CompatibilityVectors[]
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represents the VM to retrieve compatibility vectors for. If this parameter refers to the hosting computer system, the data returned in the *CompatibilityVectors* parameter can be used to determine whether any of the VMs on the hosting computer system can be quickly migrated to another hosting computer system.

</dd> <dt>

*CompatibilityVectors* \[out\]
</dt> <dd>

An array of [**Msvm\_CompatibilityVector**](https://msdn.microsoft.com/library/windows/desktop/dn280574) instances that contain the compatibility info for the VMs or hosting computer system.

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



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





