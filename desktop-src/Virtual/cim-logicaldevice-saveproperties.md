---
title: SaveProperties method of the CIM\_LogicalDevice class
description: Saves the configuration and state of the logical device.
ms.assetid: '24784c71-ec33-4516-87de-cf9fd9613c61'
keywords: ["SaveProperties method Hyper-V", "SaveProperties method Hyper-V , CIM_LogicalDevice class", "CIM_LogicalDevice class Hyper-V , SaveProperties method"]
topic_type:
- apiref
api_name:
- CIM_LogicalDevice.SaveProperties
api_location:
- Root\virtualization
api_type:
- COM
---

# SaveProperties method of the CIM\_LogicalDevice class

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
</dt> </dl>

 

 





