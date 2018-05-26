---
title: PHW\_TIMER routine
description: HwScsiTimer is called after the interval specified when the miniport driver called ScsiPortNotification with the RequestTimerCallNotificationType value.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: cd8c0699-c9ec-45cd-9e51-c8a3d4ffc8db
keywords:
- HwScsiTimer routine Storage Devices
- PHW_TIMER
topic_type:
- apiref
api_name:
- HwScsiTimer
api_location:
- miniport.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PHW\_TIMER routine

*HwScsiTimer* is called after the interval specified when the miniport driver called **ScsiPortNotification** with the **RequestTimerCall***NotificationType* value.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PHW_TIMER HwScsiTimer;

VOID HwScsiTimer(
  _In_ PVOID DeviceExtension
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

None.

## Remarks

A miniport driver that does not have an *HwScsiInterrupt* routine because it manages all HBA I/O operations by polling should have an *HwScsiTimer* routine.

A miniport driver should use *HwScsiTimer* instead of **ScsiPortStallExecution** whenever a wait longer than a millisecond is required.

The name *HwScsiTimer* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
VOID
(*PHW_TIMER) (
  IN PVOID  DeviceExtension
  );
```



For a discussion of when and how to use *HwScsiTimer* see [SCSI Miniport Driver's HwScsiTimer Routine](https://msdn.microsoft.com/library/windows/hardware/ff565340).

A *HwScsiTimer* routine is optional.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_TIMER%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






