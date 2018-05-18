---
title: EnableDevice method of the Msvm\_KvpExchangeComponent class
description: This method is deprecated. Instead, use the RequestStateChange method.
ms.assetid: '5c893e7c-57e0-4ab4-ab8f-91335635cf14'
keywords: ["EnableDevice method Hyper-V", "EnableDevice method Hyper-V , Msvm_KvpExchangeComponent class", "Msvm_KvpExchangeComponent class Hyper-V , EnableDevice method"]
topic_type:
- apiref
api_name:
- Msvm_KvpExchangeComponent.EnableDevice
api_location:
- Root\virtualization
api_type:
- COM
---

# EnableDevice method of the Msvm\_KvpExchangeComponent class

This method is deprecated. Instead, use the [**RequestStateChange**](virtual-cim_logicaldevice_requeststatechange) method.

**Deprecated description:** Enables or disables the numeric sensor.

## Syntax


```mof
uint32 EnableDevice(
  [in] boolean Enabled
);
```



## Parameters

<dl> <dt>

*Enabled* \[in\]
</dt> <dd>

Indicates whether to enable the numeric sensor. **true** to enable the sensor; otherwise **false**.

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

 

 





