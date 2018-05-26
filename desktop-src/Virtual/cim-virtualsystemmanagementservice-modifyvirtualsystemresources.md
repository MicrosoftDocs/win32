---
title: ModifyVirtualSystemResources method of the CIM\_VirtualSystemManagementService class
description: Modifies the setting data for existing resources on a virtual computer system.
ms.assetid: 0c90433f-0ebd-4a66-bbed-cbe4cca73d52
keywords:
- ModifyVirtualSystemResources method Hyper-V
- ModifyVirtualSystemResources method Hyper-V , CIM_VirtualSystemManagementService class
- CIM_VirtualSystemManagementService class Hyper-V , ModifyVirtualSystemResources method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.ModifyVirtualSystemResources
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ModifyVirtualSystemResources method of the CIM\_VirtualSystemManagementService class

Modifies the setting data for existing resources on a virtual computer system.

## Syntax


```mof
uint32 ModifyVirtualSystemResources(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 ResourceSettingData[],
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the virtual computer system whose resources are to be modified.

</dd> <dt>

*ResourceSettingData* \[in\]
</dt> <dd>

An array of embedded instances of the [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) class that describe the resources to be modified on the virtual computer system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the *Job* output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

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

**System is in used** (32774)
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



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





