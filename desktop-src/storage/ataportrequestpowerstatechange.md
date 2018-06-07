---
title: AtaPortRequestPowerStateChange routine
description: The AtaPortRequestPowerStateChange routine requests a power state transition for the indicated device.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 37cf1552-2cbe-4b80-b220-cfa853674e1b
keywords:
- AtaPortRequestPowerStateChange routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortRequestPowerStateChange
api_location:
- Irb.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AtaPortRequestPowerStateChange routine

The **AtaPortRequestPowerStateChange** routine requests a power state transition for the indicated device.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID AtaPortRequestPowerStateChange(
   IN PVOID           ChannelExtension,
   IN UCHAR           TargetId,
   IN UCHAR           Lun,
   IN IDE_POWER_STATE DesiredPowerState
);
```



## Parameters

<dl> <dt>

*ChannelExtension* 
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*TargetId* 
</dt> <dd>

Specifies the target identifier of the device.

</dd> <dt>

*Lun* 
</dt> <dd>

Specifies the logical unit number (LUN).

</dd> <dt>

*DesiredPowerState* 
</dt> <dd>

Contains an enumerator value of type [**IDE\_POWER\_STATE**](ide-power-state.md) that indicates the power state to which the indicated device should be changed.

</dd> </dl>

## Return value

None

## Remarks

The **AtaPortRequestPowerStateChange** routine is used when a miniport driver might have to initiate a power state change, such as when a hot-plug operation occurs.

> [!Note]  
> The practice of doing idle detection from an ATA miniport driver is discouraged.

 

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_POWER\_STATE**](ide-power-state.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortRequestPowerStateChange%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






