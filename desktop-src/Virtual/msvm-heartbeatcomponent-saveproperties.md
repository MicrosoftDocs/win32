---
title: SaveProperties method of the Msvm\_HeartbeatComponent class
description: Saves the configuration and state of the logical device.
ms.assetid: ec251ee6-cc25-4688-9793-8463d0d8a50a
keywords:
- SaveProperties method Hyper-V
- SaveProperties method Hyper-V , Msvm_HeartbeatComponent class
- Msvm_HeartbeatComponent class Hyper-V , SaveProperties method
topic_type:
- apiref
api_name:
- Msvm_HeartbeatComponent.SaveProperties
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

# SaveProperties method of the Msvm\_HeartbeatComponent class

Saves the configuration and state of the logical device.

## Syntax


```mof
uint32 SaveProperties();
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

[**Msvm\_HeartbeatComponent**](msvm-heartbeatcomponent.md)
</dt> </dl>

 

 





