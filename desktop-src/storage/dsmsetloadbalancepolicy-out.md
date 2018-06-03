---
title: DsmSetLoadBalancePolicy\_OUT structure
description: The DsmSetLoadBalancePolicy\_OUT structure reports the output parameter of the DsmSetLoadBalancePolicy method.
ms.assetid: d3479656-310f-4e2d-a671-296bc3e2f1ab
keywords:
- DsmSetLoadBalancePolicy_OUT structure Storage Devices
- PDsmSetLoadBalancePolicy_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DsmSetLoadBalancePolicy_OUT
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DsmSetLoadBalancePolicy\_OUT structure

The **DsmSetLoadBalancePolicy\_OUT** structure reports the output parameter of the [**DsmSetLoadBalancePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff552670) method.

## Syntax


```C++
typedef struct _DsmSetLoadBalancePolicy_OUT {
  ULONG Status;
} DsmSetLoadBalancePolicy_OUT, *PDsmSetLoadBalancePolicy_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

The status of the [**DsmSetLoadBalancePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff552670) operation.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DsmSetLoadBalancePolicy_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





