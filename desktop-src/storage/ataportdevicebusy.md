---
title: AtaPortDeviceBusy routine
description: The AtaPortDeviceBusy routine informs the port driver that the indicated device is busy.
ms.assetid: '919f30b1-025d-4526-a1f6-2d14c482e474'
keywords: ["AtaPortDeviceBusy routine Storage Devices"]
topic_type:
- apiref
api_name:
- AtaPortDeviceBusy
api_location:
- irb.h
api_type:
- HeaderDef
---

# AtaPortDeviceBusy routine

The **AtaPortDeviceBusy** routine informs the port driver that the indicated device is busy.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID __inline AtaPortDeviceBusy(
  _In_ PVOID ChannelExtension,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ ULONG BusyTimeout
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Specifies the target identifier of the device.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Specifies the logical unit number (LUN) of the device.

</dd> <dt>

*BusyTimeout* \[in\]
</dt> <dd>

Specifies the time, in seconds, for which the device is presumed to be busy.

</dd> </dl>

## Return value

None

## Remarks

When the port driver receives this call, it pauses the request queue for the indicated device for the time that is indicated by *BusyTimeout*. The caller can pause the channel request queue instead of the request queue for an individual device by assigning the wildcard value of IDE\_UNTAGGED to parameters *TargetId* and *Lun*.

The port driver automatically resumes paused queues after the time-out interval expires.

The miniport driver must not call **AtaPortDeviceBusy** from its [**IdeHwInterrupt**](idehwinterrupt.md) routine.

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IdeHwInterrupt**](idehwinterrupt.md)
</dt> <dt>

[**AtaPortDeviceReady**](ataportdeviceready.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortDeviceBusy%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






