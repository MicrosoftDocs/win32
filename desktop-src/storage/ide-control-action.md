---
title: IDE\_CONTROL\_ACTION enumeration
description: The IDE\_CONTROL\_ACTION enumeration type indicates the control action to be performed by a IdeHwControl routine.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 'a63d1a2f-d560-492f-9b73-198e42cb4300'
keywords: ["IDE_CONTROL_ACTION enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_CONTROL_ACTION
api_location:
- irb.h
api_type:
- HeaderDef
---

# IDE\_CONTROL\_ACTION enumeration

The IDE\_CONTROL\_ACTION enumeration type indicates the control action to be performed by a [**IdeHwControl**](idehwcontrol.md) routine.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum  { 
  IdeStart          = 0,
  IdeStop           = 1,
  IdePowerUp        = 2,
  IdePowerDown      = 3,
  IdeVendorDefined  = 4
} IDE_CONTROL_ACTION;
```



## Constants

<dl> <dt>

<span id="IdeStart"></span><span id="idestart"></span><span id="IDESTART"></span>**IdeStart**
</dt> <dd>

Indicates that the miniport driver should start the channel.

</dd> <dt>

<span id="IdeStop"></span><span id="idestop"></span><span id="IDESTOP"></span>**IdeStop**
</dt> <dd>

Indicates that the miniport driver should stop the channel.

</dd> <dt>

<span id="IdePowerUp"></span><span id="idepowerup"></span><span id="IDEPOWERUP"></span>**IdePowerUp**
</dt> <dd>

Indicates that the miniport driver should power up the channel.

</dd> <dt>

<span id="IdePowerDown"></span><span id="idepowerdown"></span><span id="IDEPOWERDOWN"></span>**IdePowerDown**
</dt> <dd>

Indicates that the miniport driver should power down the channel.

</dd> <dt>

<span id="IdeVendorDefined"></span><span id="idevendordefined"></span><span id="IDEVENDORDEFINED"></span>**IdeVendorDefined**
</dt> <dd>

Indicates that the miniport driver should perform a vendor-defined control action.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IdeHwControl**](idehwcontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_CONTROL_ACTION%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






