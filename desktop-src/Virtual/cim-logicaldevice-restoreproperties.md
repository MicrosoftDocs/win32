---
title: RestoreProperties method of the CIM\_LogicalDevice class
description: Restores a previous configuration and state of the logical device.
ms.assetid: '0b905801-494d-4815-8845-e376418d3611'
keywords: ["RestoreProperties method Hyper-V", "RestoreProperties method Hyper-V , CIM_LogicalDevice class", "CIM_LogicalDevice class Hyper-V , RestoreProperties method"]
topic_type:
- apiref
api_name:
- CIM_LogicalDevice.RestoreProperties
api_location:
- Root\virtualization
api_type:
- COM
---

# RestoreProperties method of the CIM\_LogicalDevice class

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
</dt> </dl>

 

 





