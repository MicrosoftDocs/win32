---
title: EnableDevice method of the Msvm\_TimeSyncComponent class
description: This method is deprecated. Instead, use the RequestStateChange method.
ms.assetid: 9ae7128f-2c0b-413c-9023-2f3c820f4944
keywords:
- EnableDevice method Hyper-V
- EnableDevice method Hyper-V , Msvm_TimeSyncComponent class
- Msvm_TimeSyncComponent class Hyper-V , EnableDevice method
topic_type:
- apiref
api_name:
- Msvm_TimeSyncComponent.EnableDevice
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

# EnableDevice method of the Msvm\_TimeSyncComponent class

This method is deprecated. Instead, use the [**RequestStateChange**](virtual-cim_logicaldevice_requeststatechange) method.

**Deprecated description:** Enables or disables the numeric sensor.

## Syntax


```mof
uint32 EnableDevice(
  [in] boolean Enabled
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

[**Msvm\_TimeSyncComponent**](msvm-timesynccomponent.md)
</dt> </dl>

 

 





