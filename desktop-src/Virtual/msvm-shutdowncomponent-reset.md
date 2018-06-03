---
title: Reset method of the Msvm\_ShutdownComponent class
description: Resets the logical device.
ms.assetid: f12e2b77-2435-4d03-a4dc-5e85453e8b9a
keywords:
- Reset method Hyper-V
- Reset method Hyper-V , Msvm_ShutdownComponent class
- Msvm_ShutdownComponent class Hyper-V , Reset method
topic_type:
- apiref
api_name:
- Msvm_ShutdownComponent.Reset
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

# Reset method of the Msvm\_ShutdownComponent class

Resets the logical device.

## Syntax


```mof
uint32 Reset();
```



## Parameters

This method has no parameters.

## Return value

<dl> <dt>


</dt> <dd>

0

The operation completed successfully.

</dd> <dt>


</dt> <dd>

1

The operation was not completed because it is not supported.

</dd> <dt>


</dt> <dd>

2

The operation is not supported when the device is in the current state.

</dd> <dt>


</dt> <dd>

3 = *value*

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dt>

[**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)
</dt> </dl>

 

 





