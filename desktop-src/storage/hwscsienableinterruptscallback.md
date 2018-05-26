---
title: PHW\_INTERRUPT routine
description: HwScsiEnableInterruptsCallback is called after a miniport drivers HwScsiInterrupt routine disables interrupts on the HBA and calls ScsiPortNotification with the NotificationTypeCallEnableInterrupts.
ms.assetid: b62709b2-aa90-4bb1-9c17-edb3b489b696
keywords:
- HwScsiEnableInterruptsCallback routine Storage Devices
- PHW_INTERRUPT
topic_type:
- apiref
api_name:
- HwScsiEnableInterruptsCallback
api_location:
- miniport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PHW\_INTERRUPT routine

*HwScsiEnableInterruptsCallback* is called after a miniport driver's *HwScsiInterrupt* routine disables interrupts on the HBA and calls **ScsiPortNotification** with the *NotificationType***CallEnableInterrupts**. Miniport drivers of HBAs that require interrupt processing that takes more than 50 microseconds in the ISR should have a pair of *HwScsi..InterruptsCallback* routines.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiEnableInterruptsCallback(
  _In_ PVOID DeviceExtension
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

*HwScsiEnableInterruptsCallback* returns **TRUE**.

## Remarks

All system interrupts are enabled when the *HwScsiEnableInterruptsCallback* routine gets control, except for interrupts from the HBA. Because the miniport driver's *HwScsiInterrupt* routine disables interrupts on the HBA before it calls **ScsiPortNotification**, the *HwScsiEnableInterruptsCallback* routine should be optimized to run as quickly as possible.

*HwScsiEnableInterruptsCallback* is responsible for completing the interrupt-driven I/O processing deferred by the *HwScsiInterrupt* routine, using the information it saved in the *DeviceExtension*. That is, *HwScsiEnableInterruptsCallback* completes the request that caused the interrupt to occur.

Then, *HwScsiEnableInterruptsCallback* calls **ScsiPortNotification** again with the *NotificationType***CallDisableInterrupts** before it returns control.

For more information about the *HwScsiEnableInterruptsCallback* routine, see [SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine](https://msdn.microsoft.com/library/windows/hardware/ff565323).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiDisableInterruptsCallback**](hwscsidisableinterruptscallback.md)
</dt> <dt>

[**HwScsiInterrupt**](hwscsiinterrupt.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_INTERRUPT%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






