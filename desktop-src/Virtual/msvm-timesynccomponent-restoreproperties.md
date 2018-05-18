---
title: RestoreProperties method of the Msvm\_TimeSyncComponent class
description: Restores a previous configuration and state of the logical device.
ms.assetid: '10c269a1-5147-4328-acf8-156a7d9c7454'
keywords: ["RestoreProperties method Hyper-V", "RestoreProperties method Hyper-V , Msvm_TimeSyncComponent class", "Msvm_TimeSyncComponent class Hyper-V , RestoreProperties method"]
topic_type:
- apiref
api_name:
- Msvm_TimeSyncComponent.RestoreProperties
api_location:
- Root\virtualization
api_type:
- COM
---

# RestoreProperties method of the Msvm\_TimeSyncComponent class

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

[**Msvm\_TimeSyncComponent**](msvm-timesynccomponent.md)
</dt> </dl>

 

 





