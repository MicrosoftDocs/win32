---
title: RestoreProperties method of the Msvm\_KvpExchangeComponent class
description: Restores a previous configuration and state of the logical device.
ms.assetid: '29161c9a-1d20-4a92-b714-ef385bf39b1a'
keywords: ["RestoreProperties method Hyper-V", "RestoreProperties method Hyper-V , Msvm_KvpExchangeComponent class", "Msvm_KvpExchangeComponent class Hyper-V , RestoreProperties method"]
topic_type:
- apiref
api_name:
- Msvm_KvpExchangeComponent.RestoreProperties
api_location:
- Root\virtualization
api_type:
- COM
---

# RestoreProperties method of the Msvm\_KvpExchangeComponent class

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

[**Msvm\_KvpExchangeComponent**](msvm-kvpexchangecomponent.md)
</dt> </dl>

 

 





