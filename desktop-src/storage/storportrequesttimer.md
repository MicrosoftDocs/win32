---
title: StorPortRequestTimer routine
description: Schedules a callback event for a Storport timer context object.
ms.assetid: EE5A6D39-EC76-4D97-B2EC-4A43225C2FB5
keywords:
- StorPortRequestTimer routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortRequestTimer
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

# StorPortRequestTimer routine

Schedules a callback event for a Storport timer context object.

## Syntax


```C++
ULONG StorPortRequestTimer(
  _In_     PVOID        HwDeviceExtension,
  _In_     PVOID        TimerHandle,
  _In_     PHW_TIMER_EX TimerCallback,
  _In_opt_ PVOID        CallbackContext,
  _In_     LONGLONG     TimerValue,
  _In_     LONGLONG     TolerableDelay
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*TimerHandle* \[in\]
</dt> <dd>

A pointer to an opaque buffer for the timer context returned by [**StorPortInitializeTimer**](storportinitializetimer.md).

</dd> <dt>

*TimerCallback* \[in\]
</dt> <dd>

A pointer to a timer callback routine supplied by the miniport. The following is the prototype defined for **PHW\_TIMER\_EX**:


```
typedef
VOID
(*PHW_TIMER_EX) (
  _In_ PVOID  DeviceExtension,
  _In_opt_ PVOID Context
  );
```



</dd> <dt>

*CallbackContext* \[in, optional\]
</dt> <dd>

A pointer to a miniport provided context for the timer callback.

</dd> <dt>

*TimerValue* \[in\]
</dt> <dd>

The timeout value for the timer, in microseconds. Setting *TimerValue* to 0 will cancel the timer.

</dd> <dt>

*TolerableDelay* \[in\]
</dt> <dd>

The allowable delay for the timer in microseconds. Values less than 32 microseconds are ignored and *TolerableDelay* defaults to 0.

</dd> </dl>

## Return value

The **StorPortRequestTimer** routine returns one of these status codes:



| Return code                                                                                                          | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Not enough resources available to defer scheduling of the timer.<br/>                                                                |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | *HwDeviceExtension*, *TimerHandle*, or *TimerCallback* is NULL.<br/> The timer context object, *TimerHandle*, is invalid.<br/> |
| <dl> <dt>**STOR\_STATUS\_BUSY**</dt> </dl>                    | A previous timer request is active. *TimerValue* &gt; 0 and *TimerCallback* has not been called.<br/>                                |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The timer request was successfully scheduled.<br/>                                                                                   |



 

## Remarks

The **StorPortRequestTimer** routine is callable at any IRQL. However, if the routine is called when IRQL &gt; DISPATCH\_LEVEL, the timer's scheduling is deferred until IRQL &lt;= DISPATCH\_LEVEL.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**HwStorTimer**](hwstortimer.md)
</dt> <dt>

[**StorPortFreeTimer**](storportfreetimer.md)
</dt> <dt>

[**StorPortInitializeTimer**](storportinitializetimer.md)
</dt> <dt>

[**StorPortNotification**](storportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortRequestTimer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






