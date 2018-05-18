---
title: Reset method of the Msvm\_VssComponent class
description: Resets the logical device.
ms.assetid: '03af6b63-39c5-47b8-8260-7cbdb8904636'
keywords: ["Reset method Hyper-V", "Reset method Hyper-V , Msvm_VssComponent class", "Msvm_VssComponent class Hyper-V , Reset method"]
topic_type:
- apiref
api_name:
- Msvm_VssComponent.Reset
api_location:
- Root\virtualization
api_type:
- COM
---

# Reset method of the Msvm\_VssComponent class

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

[**Msvm\_VssComponent**](msvm-vsscomponent.md)
</dt> </dl>

 

 





