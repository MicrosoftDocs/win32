---
title: SaveProperties method of the Msvm\_VssComponent class
description: Saves the configuration and state of the logical device.
ms.assetid: 'e81403dd-b6df-4df7-95af-5b70e72ee91c'
keywords: ["SaveProperties method Hyper-V", "SaveProperties method Hyper-V , Msvm_VssComponent class", "Msvm_VssComponent class Hyper-V , SaveProperties method"]
topic_type:
- apiref
api_name:
- Msvm_VssComponent.SaveProperties
api_location:
- Root\virtualization
api_type:
- COM
---

# SaveProperties method of the Msvm\_VssComponent class

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

[**Msvm\_VssComponent**](msvm-vsscomponent.md)
</dt> </dl>

 

 





