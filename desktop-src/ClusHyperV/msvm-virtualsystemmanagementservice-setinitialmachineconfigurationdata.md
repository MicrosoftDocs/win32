---
title: SetInitialMachineConfigurationData method of the Msvm\_VirtualSystemManagementService class
description: Sets the initial machine configuration data for a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18045631-5c30-4481-adb8-72ac6b484adb
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetInitialMachineConfigurationData method
- SetInitialMachineConfigurationData method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, SetInitialMachineConfigurationData method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.SetInitialMachineConfigurationData
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetInitialMachineConfigurationData method of the Msvm\_VirtualSystemManagementService class

Sets the initial machine configuration data for a virtual machine.

## Syntax


```mof
uint32 SetInitialMachineConfigurationData(
  [in]  CIM_ComputerSystem REF TargetSystem,
  [in]  uint8                  ImcData[],
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*TargetSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) instance that represents the virtual machine to update.

</dd> <dt>

*ImcData* \[in\]
</dt> <dd>

An array that contains the initial machine configuration data to set. The first four bytes must be the length of the array in big-endian order.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

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

 

 





