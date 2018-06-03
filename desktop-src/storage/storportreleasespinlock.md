---
title: StorPortReleaseSpinLock routine
description: The StorPortReleaseSpinLock routine releases a spinlock acquired by StorPortAcquireSpinLock.
ms.assetid: ed91d41a-575d-4b26-a7e0-f3ce43db76b4
keywords:
- StorPortReleaseSpinLock routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortReleaseSpinLock
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortReleaseSpinLock routine

The **StorPortReleaseSpinLock** routine releases a spinlock acquired by [**StorPortAcquireSpinLock**](storportacquirespinlock.md).

## Syntax


```C++
VOID StorPortReleaseSpinLock(
  _In_    PVOID             HwDeviceExtension,
  _Inout_ PSTOR_LOCK_HANDLE LockHandle
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to a per-adapter device extension.

</dd> <dt>

*LockHandle* \[in, out\]
</dt> <dd>

Pointer to a lock handle returned by [**StorPortAcquireSpinLock**](storportacquirespinlock.md).

</dd> </dl>

## Return value

None.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| DDI compliance rules<br/> | [**StorPortSpinLock**](https://msdn.microsoft.com/library/windows/hardware/hh454273), [**StorPortSpinLock4**](https://msdn.microsoft.com/library/windows/hardware/hh454272)                  |



## See also

<dl> <dt>

[**StorPortAcquireSpinLock**](storportacquirespinlock.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortReleaseSpinLock%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






