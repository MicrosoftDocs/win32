---
title: PHW\_RESET\_BUS routine
description: HwScsiResetBus resets a given SCSI bus.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: d512fb4e-b1e6-4981-a438-5e49159b178f
keywords:
- HwScsiResetBus routine Storage Devices
- PHW_RESET_BUS
topic_type:
- apiref
api_name:
- HwScsiResetBus
api_location:
- miniport.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PHW\_RESET\_BUS routine

*HwScsiResetBus* resets a given SCSI bus.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PHW_RESET_BUS HwScsiResetBus;

BOOLEAN HwScsiResetBus(
  _In_ PVOID DeviceExtension,
  _In_ ULONG PathId
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus to be reset.

</dd> </dl>

## Return value

If the bus is successfully reset, *HwScsiResetBus* returns **TRUE**.

## Remarks

*HwScsiResetBus* can be called even if the miniport driver is not ready for another request. The miniport driver should complete all pending requests and must reset the given bus.

*HwScsiResetBus* need not call **ScsiPortNotification** to indicate that the bus was reset.

The name *HwScsiResetBus* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
BOOLEAN
(*PHW_RESET_BUS) (
  IN PVOID  DeviceExtension,
  IN ULONG  PathId
  );
```



For more information about the *HwScsiResetBus* routine, see [SCSI Miniport Driver's HwScsiResetBus Routine](https://msdn.microsoft.com/library/windows/hardware/ff565331).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortCompleteRequest**](scsiportcompleterequest.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_RESET_BUS%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






