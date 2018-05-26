---
title: StorPortInitializeTimer routine
description: Creates a Storport timer context object.
ms.assetid: 1F43EEDC-5DB4-4ABE-BBC6-A4A51FCAF0B6
keywords:
- StorPortInitializeTimer routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitializeTimer
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortInitializeTimer routine

Creates a Storport timer context object.

## Syntax


```C++
ULONG StorPortInitializeTimer(
  _In_  PVOID HwDeviceExtension,
  _Out_ PVOID *TimerHandle
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*TimerHandle* \[out\]
</dt> <dd>

A pointer to an opaque buffer that holds context information for the timer.

</dd> </dl>

## Return value

The **StorPortInitializeTimer** routine returns one of these status codes:



| Return code                                                                                                          | Description                                                                      |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>           | Current IRQL &gt; DISPATCH\_LEVEL.<br/>                                    |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | Either *HwDeviceExtension* or *TimerHandle* is NULL.<br/>                  |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Insufficient resources are available to initialize the timer context.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The timer context was successfully initialized.<br/>                       |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>            | The number of supported timers is exceeded.<br/>                           |



 

## Remarks

Storport provides a single timer to a miniport driver by using the **RequestTimerCall** notification type in [**StorPortNotification**](storportnotification.md). If a miniport requires more than one timer, additional timers are created with **StorPortInitializeTimer**.

It is recommended that miniports call **StorPortInitializeTimer** in the [**HwStorFindAdapter**](hwstorfindadapter.md) function to ensure that the additional timer resources are available.

Miniports can use this routine to set coalescing timers to create a delay period after an initial timeout.

Prior to Windows 8, a maximum of 4 timers can be created with **StorPortInitializeTimer**. Starting with Windows 8, there is no maximum timers limitation.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> <dt>

[**StorPortFreeTimer**](storportfreetimer.md)
</dt> <dt>

[**StorPortNotification**](storportnotification.md)
</dt> <dt>

[**StorPortRequestTimer**](storportrequesttimer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitializeTimer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






