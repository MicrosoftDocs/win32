---
description: Enables a physical GPU for virtualization.
ms.assetid: 700cb46b-97f1-40cf-88d2-64242f4bd2c6
title: EnableGPUForVirtualization method of the Msvm_Synthetic3DService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_Synthetic3DService.EnableGPUForVirtualization
api_type: 
- COM
api_location: 
- vmms.exe
---

# EnableGPUForVirtualization method of the Msvm\_Synthetic3DService class

Enables a physical GPU for virtualization.

## Syntax


```mof
uint32 EnableGPUForVirtualization(
  [in]  Msvm_Physical3dGraphicsProcessor REF PhysicalGPU,
  [out] CIM_ConcreteJob                  REF Job
);
```



## Parameters

<dl> <dt>

*PhysicalGPU* \[in\]
</dt> <dd>

A reference to an instance of the [**Msvm\_Physical3dGraphicsProcessor**](msvm-physical3dgraphicsprocessor.md) class that represents the physical GPU to be enabled.

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

**Not supported** (1)
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

[**Msvm\_Synthetic3DService**](msvm-synthetic3dservice.md)
</dt> </dl>

 

