---
title: RestoreProperties method of the Msvm\_VssComponent class
description: Restores a previous configuration and state of the logical device.
ms.assetid: 7c2e31cb-8344-4890-a3a9-ba95666bb398
keywords:
- RestoreProperties method Hyper-V
- RestoreProperties method Hyper-V , Msvm_VssComponent class
- Msvm_VssComponent class Hyper-V , RestoreProperties method
topic_type:
- apiref
api_name:
- Msvm_VssComponent.RestoreProperties
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

# RestoreProperties method of the Msvm\_VssComponent class

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

[**Msvm\_VssComponent**](msvm-vsscomponent.md)
</dt> </dl>

 

 





