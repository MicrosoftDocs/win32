---
title: PHW\_INTERRUPT routine
description: HwScsiDisableInterruptsCallback is called after a miniport driver's HwScsiEnableInterruptsCallback routine calls ScsiPortNotification with the NotificationTypeCallDisableInterrupts.
ms.assetid: 'a38f70f0-0bb7-4d9f-b224-5cfe01136487'
keywords: ["HwScsiDisableInterruptsCallback routine Storage Devices", "PHW_INTERRUPT"]
topic_type:
- apiref
api_name:
- HwScsiDisableInterruptsCallback
api_location:
- miniport.h
api_type:
- HeaderDef
---

# PHW\_INTERRUPT routine

*HwScsiDisableInterruptsCallback* is called after a miniport driver's *HwScsiEnableInterruptsCallback* routine calls **ScsiPortNotification** with the *NotificationType***CallDisableInterrupts**. Miniport drivers of HBAs that require interrupt processing that takes more than 50 microseconds in the ISR should have a pair of *HwScsi..InterruptsCallback* routines.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiDisableInterruptsCallback(
  _In_ PVOID DeviceExtension
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

*HwScsiDisableInterruptsCallback* returns **TRUE** if the operation succeeded and **FALSE** if the operation failed.

## Remarks

All system interrupts with a higher hardware priority than the HBA's are enabled when the *HwScsiDisableInterruptsCallback* routine is called. Consequently, a *HwScsiDisableInterruptsCallback* routine should be optimized to run as quickly as possible.

*HwScsiDisableInterruptsCallback* is responsible for reenabling interrupts on the HBA and then returning control.

For more information about the *HwScsiDisableInterruptsCallback* routine, see [SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine](https://msdn.microsoft.com/library/windows/hardware/ff565321).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiEnableInterruptsCallback**](hwscsienableinterruptscallback.md)
</dt> <dt>

[**HwScsiInterrupt**](hwscsiinterrupt.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_INTERRUPT%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






