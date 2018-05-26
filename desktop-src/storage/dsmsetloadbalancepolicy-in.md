---
title: DsmSetLoadBalancePolicy\_IN structure
description: The DsmSetLoadBalancePolicy\_IN structure provides an input parameter to the DsmSetLoadBalancePolicy method.
ms.assetid: 1a249c0e-1b8d-4c50-9b01-03bfe84e0937
keywords:
- DsmSetLoadBalancePolicy_IN structure Storage Devices
- PDsmSetLoadBalancePolicy_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DsmSetLoadBalancePolicy_IN
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DsmSetLoadBalancePolicy\_IN structure

The DsmSetLoadBalancePolicy\_IN structure provides an input parameter to the DsmSetLoadBalancePolicy method.

## Syntax


```C++
typedef struct _DsmSetLoadBalancePolicy_IN {
  DSM_Load_Balance_Policy LoadBalancePolicy;
} DsmSetLoadBalancePolicy_IN, *PDsmSetLoadBalancePolicy_IN;
```



## Members

<dl> <dt>

**LoadBalancePolicy**
</dt> <dd>

A structure of type DSM\_Load\_Balance\_Policy.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DsmSetLoadBalancePolicy_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





