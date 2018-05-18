---
title: Reset method of the Msvm\_RdvComponent class
description: Resets the logical device.
ms.assetid: 'ff8d9e38-807e-42be-8b9e-edfbf36c6fbd'
keywords: ["Reset method Hyper-V", "Reset method Hyper-V , Msvm_RdvComponent class", "Msvm_RdvComponent class Hyper-V , Reset method"]
topic_type:
- apiref
api_name:
- Msvm_RdvComponent.Reset
api_location:
- Root\virtualization
api_type:
- COM
---

# Reset method of the Msvm\_RdvComponent class

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

[**Msvm\_RdvComponent**](msvm-rdvcomponent.md)
</dt> </dl>

 

 





