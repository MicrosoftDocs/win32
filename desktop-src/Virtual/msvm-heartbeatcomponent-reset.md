---
title: Reset method of the Msvm\_HeartbeatComponent class
description: Resets the logical device.
ms.assetid: '4f1edd6e-c276-4757-ab22-5c7888b576ee'
keywords: ["Reset method Hyper-V", "Reset method Hyper-V , Msvm_HeartbeatComponent class", "Msvm_HeartbeatComponent class Hyper-V , Reset method"]
topic_type:
- apiref
api_name:
- Msvm_HeartbeatComponent.Reset
api_location:
- Root\virtualization
api_type:
- COM
---

# Reset method of the Msvm\_HeartbeatComponent class

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

[**Msvm\_HeartbeatComponent**](msvm-heartbeatcomponent.md)
</dt> </dl>

 

 





