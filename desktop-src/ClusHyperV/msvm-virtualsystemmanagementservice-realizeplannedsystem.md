---
title: RealizePlannedSystem method of the Msvm\_VirtualSystemManagementService class
description: Validates the configuration of a planned virtual machine and converts it new virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: caf69805-0534-4c11-9071-0b5aaeb7fd4a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RealizePlannedSystem method
- RealizePlannedSystem method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, RealizePlannedSystem method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RealizePlannedSystem
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RealizePlannedSystem method of the Msvm\_VirtualSystemManagementService class

Validates the configuration of a planned virtual machine and converts it new virtual machine. Any runtime or saved state files that are associated with the virtual machine are copied from the import directory to the root data directory.

## Syntax


```mof
uint32 RealizePlannedSystem(
  [in]  Msvm_PlannedComputerSystem REF PlannedSystem,
  [out] CIM_ComputerSystem         REF ResultingSystem,
  [out] CIM_ConcreteJob            REF Job
);
```



## Parameters

<dl> <dt>

*PlannedSystem* \[in\]
</dt> <dd>

A reference to the [**Msvm\_PlannedComputerSystem**](https://msdn.microsoft.com/library/windows/desktop/hh850187) instance that is to be converted into a realized virtual system.

</dd> <dt>

*ResultingSystem* \[out\]
</dt> <dd>

If the operation is completed synchronously, this method receives a [**CIM\_ComputerSystem**](cim-computersystem.md) reference to the new virtual system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A [**CIM\_ConcreteJob**](cim-concretejob.md) reference to an optional job for the operation if the operation is run asynchronously.

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

 

 





