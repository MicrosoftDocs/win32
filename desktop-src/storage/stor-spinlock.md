---
title: STOR\_SPINLOCK enumeration
description: The STOR\_SPINLOCK enumeration is used to specify the type of a spinlock.
ms.assetid: 73e5e994-4133-4651-bb94-1d21386be1cd
keywords:
- STOR_SPINLOCK enumeration Storage Devices
topic_type:
- apiref
api_name:
- STOR_SPINLOCK
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STOR\_SPINLOCK enumeration

The STOR\_SPINLOCK enumeration is used to specify the type of a spinlock.

## Syntax


```C++
typedef enum _STOR_SPINLOCK { 
  DpcLock        = 1,
  StartIoLock    = 2,
  InterruptLock  = 3
} STOR_SPINLOCK;
```



## Constants

<dl> <dt>

<span id="DpcLock"></span><span id="dpclock"></span><span id="DPCLOCK"></span>**DpcLock**
</dt> <dd>

Indicates a DPC spinlock.

</dd> <dt>

<span id="StartIoLock"></span><span id="startiolock"></span><span id="STARTIOLOCK"></span>**StartIoLock**
</dt> <dd>

Indicates a StartIo spinlock.

</dd> <dt>

<span id="InterruptLock"></span><span id="interruptlock"></span><span id="INTERRUPTLOCK"></span>**InterruptLock**
</dt> <dd>

Indicates an Interrupt spinlock.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortAcquireSpinLock**](storportacquirespinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_SPINLOCK%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






