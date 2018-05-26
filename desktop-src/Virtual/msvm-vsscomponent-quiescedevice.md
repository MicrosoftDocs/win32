---
title: QuiesceDevice method of the Msvm\_VssComponent class
description: This method is deprecated. Instead, use the RequestStateChange method.
ms.assetid: 4463083b-3619-4dcd-8e79-4e6b8d915831
keywords:
- QuiesceDevice method Hyper-V
- QuiesceDevice method Hyper-V , Msvm_VssComponent class
- Msvm_VssComponent class Hyper-V , QuiesceDevice method
topic_type:
- apiref
api_name:
- Msvm_VssComponent.QuiesceDevice
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# QuiesceDevice method of the Msvm\_VssComponent class

This method is deprecated. Instead, use the [**RequestStateChange**](virtual-cim_logicaldevice_requeststatechange) method.

**Deprecated description:** Temporarily suspends or resumes activity on the numeric sensor.

## Syntax


```mof
uint32 QuiesceDevice(
  [in] boolean Quiesce
);
```



## Parameters

<dl> <dt>

*Quiesce* \[in\]
</dt> <dd>

**true** if the numeric sensor is to temporarily suspend activity or resume activity; **false** to resume activity.

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

[**Msvm\_VssComponent**](msvm-vsscomponent.md)
</dt> </dl>

 

 





