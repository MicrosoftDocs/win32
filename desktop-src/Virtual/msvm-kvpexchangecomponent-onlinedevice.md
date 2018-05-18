---
title: OnlineDevice method of the Msvm\_KvpExchangeComponent class
description: This method is deprecated. Instead, use the RequestStateChange method.
ms.assetid: '9b050100-0342-49af-8f45-8570d17a930a'
keywords: ["OnlineDevice method Hyper-V", "OnlineDevice method Hyper-V , Msvm_KvpExchangeComponent class", "Msvm_KvpExchangeComponent class Hyper-V , OnlineDevice method"]
topic_type:
- apiref
api_name:
- Msvm_KvpExchangeComponent.OnlineDevice
api_location:
- Root\virtualization
api_type:
- COM
---

# OnlineDevice method of the Msvm\_KvpExchangeComponent class

This method is deprecated. Instead, use the [**RequestStateChange**](virtual-cim_logicaldevice_requeststatechange) method.

**Deprecated description:** Brings the logical device online so it can accept requests, or offline so it can no longer accept requests.

## Syntax


```mof
uint32 OnlineDevice(
  [in] boolean Online
);
```



## Parameters

<dl> <dt>

*Online* \[in\]
</dt> <dd>

**true** to bring the device online, **false** to take the device offline.

</dd> </dl>

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

[**Msvm\_KvpExchangeComponent**](msvm-kvpexchangecomponent.md)
</dt> </dl>

 

 





