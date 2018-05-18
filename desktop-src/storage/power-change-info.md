---
title: POWER\_CHANGE\_INFO structure
description: The POWER\_CHANGE\_INFO structure is used in conjunction with the IDE\_REQUEST\_BLOCK to request a power state change.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '10f6c449-f0f8-4261-825e-127c477c06eb'
keywords: ["POWER_CHANGE_INFO structure Storage Devices", "IDE_POWER_INFO structure Storage Devices", "PIDE_POWER_INFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_POWER_INFO
api_location:
- irb.h
api_type:
- HeaderDef
---

# POWER\_CHANGE\_INFO structure

The POWER\_CHANGE\_INFO structure is used in conjunction with the [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) to request a power state change.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_POWER_INFO {
  IDE_POWER_STATE CurrentPowerState;
  IDE_POWER_STATE DesiredPowerState;
} IDE_POWER_INFO, *PIDE_POWER_INFO;
```



## Members

<dl> <dt>

**CurrentPowerState**
</dt> <dd>

Contains an enumeration value of type [**IDE\_POWER\_STATE**](ide-power-state.md) that indicates the current power state of the device.

</dd> <dt>

**DesiredPowerState**
</dt> <dd>

Contains an enumeration value of type IDE\_POWER\_STATE that indicates the power state to which the device will be changed.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_REQUEST\_BLOCK**](ide-request-block.md)
</dt> <dt>

[**IDE\_POWER\_STATE**](ide-power-state.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20POWER_CHANGE_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






