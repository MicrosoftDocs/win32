---
title: RestoreProperties method of the Msvm\_ShutdownComponent class
description: Restores a previous configuration and state of the logical device.
ms.assetid: 7045a751-e7c9-4701-a763-17a74467638b
keywords:
- RestoreProperties method Hyper-V
- RestoreProperties method Hyper-V , Msvm_ShutdownComponent class
- Msvm_ShutdownComponent class Hyper-V , RestoreProperties method
topic_type:
- apiref
api_name:
- Msvm_ShutdownComponent.RestoreProperties
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

# RestoreProperties method of the Msvm\_ShutdownComponent class

Restores a previous configuration and state of the logical device.

## Syntax


```mof
uint32 RestoreProperties();
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

2 = *value*

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

 

 





