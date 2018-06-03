---
title: Reset method of the Msvm\_TimeSyncComponent class
description: Resets the logical device.
ms.assetid: 5da0c6a4-52f2-4a43-92de-eef0d1de7350
keywords:
- Reset method Hyper-V
- Reset method Hyper-V , Msvm_TimeSyncComponent class
- Msvm_TimeSyncComponent class Hyper-V , Reset method
topic_type:
- apiref
api_name:
- Msvm_TimeSyncComponent.Reset
api_location:
- Root\virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reset method of the Msvm\_TimeSyncComponent class

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

[**Msvm\_TimeSyncComponent**](msvm-timesynccomponent.md)
</dt> </dl>

 

 





