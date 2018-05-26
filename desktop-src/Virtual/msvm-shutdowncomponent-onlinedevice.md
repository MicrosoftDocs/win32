---
title: OnlineDevice method of the Msvm\_ShutdownComponent class
description: This method is deprecated. Instead, use the RequestStateChange method.
ms.assetid: 33be6de7-8b8c-4ae5-8d0f-0f9f17fbd834
keywords:
- OnlineDevice method Hyper-V
- OnlineDevice method Hyper-V , Msvm_ShutdownComponent class
- Msvm_ShutdownComponent class Hyper-V , OnlineDevice method
topic_type:
- apiref
api_name:
- Msvm_ShutdownComponent.OnlineDevice
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

# OnlineDevice method of the Msvm\_ShutdownComponent class

This method is deprecated. Instead, use the [**RequestStateChange**](virtual-cim_logicaldevice_requeststatechange) method.

**Deprecated description:** Brings the logical device online so it can accept requests, or offline so it can no longer accept requests.

## Syntax


```mof
uint32 OnlineDevice(
  [in] boolean Online
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

[**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)
</dt> </dl>

 

 





