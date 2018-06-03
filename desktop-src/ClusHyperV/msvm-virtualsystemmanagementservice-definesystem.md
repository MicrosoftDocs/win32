---
title: DefineSystem method of the Msvm\_VirtualSystemManagementService class
description: Defines a virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5f6efb0-c151-4315-9292-4f6de793a10a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DefineSystem method
- DefineSystem method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, DefineSystem method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.DefineSystem
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DefineSystem method of the Msvm\_VirtualSystemManagementService class

Defines a virtual system.

## Syntax


```mof
uint32 DefineSystem(
  [in]  string                           SystemSettings,
  [in]  string                           ResourceSettings[],
  [in]  CIM_VirtualSystemSettingData REF ReferenceConfiguration,
  [out] CIM_ComputerSystem           REF ResultingSystem,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SystemSettings* \[in\]
</dt> <dd>

An embedded instance of [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) that defines attributes of the virtual system to create.

</dd> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array that contains embedded instance of [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) for virtual resource of the new virtual system.

</dd> <dt>

*ReferenceConfiguration* \[in\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that is the top level object of the reference configuration for the new virtual system.

</dd> <dt>

*ResultingSystem* \[out\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) instance that represents the new virtual system.

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

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**DMTF Reserved** (5 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32769)
</dt> <dt>

**Vendor Specific** (32768 65535)
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

 

 





