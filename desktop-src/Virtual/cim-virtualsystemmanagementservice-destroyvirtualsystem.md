---
title: DestroyVirtualSystem method of the CIM\_VirtualSystemManagementService class
description: Destroys the specified virtual system.
ms.assetid: 75e3c7e0-013c-4f91-bce4-8b2b6e43bf32
keywords:
- DestroyVirtualSystem method Hyper-V
- DestroyVirtualSystem method Hyper-V , CIM_VirtualSystemManagementService class
- CIM_VirtualSystemManagementService class Hyper-V , DestroyVirtualSystem method
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.DestroyVirtualSystem
api_location:
- Root\virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DestroyVirtualSystem method of the CIM\_VirtualSystemManagementService class

Destroys the specified virtual system.

## Syntax


```mof
uint32 DestroyVirtualSystem(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the virtual computer system instance to be destroyed.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of CIM\_ConcreteJob can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the Job output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





