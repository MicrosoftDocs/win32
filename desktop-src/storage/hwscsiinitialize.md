---
title: PHW\_INITIALIZE routine
description: HwScsiInitialize initializes the HBA after a reboot or a power failure occurs.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '19bcd646-1b0a-4e10-aef2-25103d645a53'
keywords: ["HwScsiInitialize routine Storage Devices", "PHW_INITIALIZE"]
topic_type:
- apiref
api_name:
- HwScsiInitialize
api_location:
- miniport.h
api_type:
- UserDefined
---

# PHW\_INITIALIZE routine

*HwScsiInitialize* initializes the HBA after a reboot or a power failure occurs.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PHW_INITIALIZE HwScsiInitialize;

BOOLEAN HwScsiInitialize(
  _In_ PVOID DeviceExtension
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

If the initialization succeeds, *HwScsiInitialize* returns **TRUE**.

## Remarks

*HwScsiInitialize* must initialize the HBA but should avoid resetting the SCSI bus or buses if possible. Interrupts can occur before this routine is called. If *HwScsiInitialize* resets a bus, it must call **ScsiPortNotification** to report that the bus was reset.

If *HwScsiInitialize* cannot initialize the HBA, this routine should call **ScsiPortLogError** before returning **FALSE** when it returns control.

The name *HwScsiInitialize* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
BOOLEAN
(*PHW_INITIALIZE) (
  IN PVOID  DeviceExtension
  );
```



For more information about *HwScsiInitialize* see [SCSI Miniport Driver's HwScsiInitialize Routine](https://msdn.microsoft.com/library/windows/hardware/ff565328).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortLogError**](scsiportlogerror.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_INITIALIZE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






