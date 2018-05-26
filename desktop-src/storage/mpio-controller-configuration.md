---
title: MPIO\_CONTROLLER\_CONFIGURATION structure
description: The MPIO\_CONTROLLER\_CONFIGURATION structure provides a top-level view of the storage controllers and the targets that are connected to them in the system.
ms.assetid: af608197-fa2b-474f-aa87-eb933a57b8cc
keywords:
- MPIO_CONTROLLER_CONFIGURATION structure Storage Devices
- PMPIO_CONTROLLER_CONFIGURATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_CONTROLLER_CONFIGURATION
api_location:
- mpiowmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPIO\_CONTROLLER\_CONFIGURATION structure

The MPIO\_CONTROLLER\_CONFIGURATION structure provides a top-level view of the storage controllers and the targets that are connected to them in the system.

## Syntax


```C++
typedef struct _MPIO_CONTROLLER_CONFIGURATION {
  ULONG                NumberControllers;
  MPIO_CONTROLLER_INFO ControllerInfo[1];
} MPIO_CONTROLLER_CONFIGURATION, *PMPIO_CONTROLLER_CONFIGURATION;
```



## Members

<dl> <dt>

**NumberControllers**
</dt> <dd>

An unsigned 32-bitfield that represents the total number of controllers on the system that are known to MPIO.

</dd> <dt>

**ControllerInfo**
</dt> <dd>

An array with information about all the controllers and all targets in the system. The number of elements of the array is given by *NumberControllers* and each element of the array is an instance of an MPIO\_CONTROLLER\_INFO structure.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_CONTROLLER_CONFIGURATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





