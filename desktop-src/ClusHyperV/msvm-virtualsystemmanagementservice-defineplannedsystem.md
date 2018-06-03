---
title: DefinePlannedSystem method of the Msvm\_VirtualSystemManagementService class
description: Defines a planned virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 58d56bfc-21aa-4fad-9da6-28526557408f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DefinePlannedSystem method
- DefinePlannedSystem method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, DefinePlannedSystem method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.DefinePlannedSystem
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DefinePlannedSystem method of the Msvm\_VirtualSystemManagementService class

Defines a planned virtual system.

## Syntax


```mof
uint32 DefinePlannedSystem(
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

An embedded instance of [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) that defines attributes of the virtual system.

</dd> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array that contains embedded instances of [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) for the virtual resource of the new virtual system.

</dd> <dt>

*ReferenceConfiguration* \[in\]
</dt> <dd>

A reference to the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance that is the top level object of the reference configuration for the virtual system. The reference configuration is used to complement the configuration of the new virtual system if the **SystemSettings** and **ResourceSettings** parameters do not enough information.

</dd> <dt>

*ResultingSystem* \[out\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) instance that represents the newly defined virtual system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

If a job is used, the [**CIM\_ComputerSystem**](cim-computersystem.md) instance that represents the newly defined virtual system can be retrieved with the **AffectedElement** property of the associated [**CIM\_AffectedJobElement**](cim-affectedjobelement.md) instance.

</dd> </dl>

## Return value

The possible values are:

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

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Remarks

Default values for this class can be applied to properties that aren't specified.

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

 

 





