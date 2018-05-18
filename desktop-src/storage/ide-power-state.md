---
title: IDE\_POWER\_STATE enumeration
description: The IDE\_POWER\_STATE enumeration type indicates that power state of the device.
ms.assetid: 'b54655ac-b7ac-4026-9d9d-75dd139ac059'
keywords: ["IDE_POWER_STATE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_POWER_STATE
api_location:
- irb.h
api_type:
- HeaderDef
---

# IDE\_POWER\_STATE enumeration

The IDE\_POWER\_STATE enumeration type indicates that power state of the device.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum  { 
  IdePowerUnSpecified  = 0,
  IdePowerD0           = 1,
  IdePowerD3           = 2
} IDE_POWER_STATE;
```



## Constants

<dl> <dt>

<span id="IdePowerUnSpecified"></span><span id="idepowerunspecified"></span><span id="IDEPOWERUNSPECIFIED"></span>**IdePowerUnSpecified**
</dt> <dd>

Indicates that the power level is unspecified.

</dd> <dt>

<span id="IdePowerD0"></span><span id="idepowerd0"></span><span id="IDEPOWERD0"></span>**IdePowerD0**
</dt> <dd>

Indicates a device power level of 0.

</dd> <dt>

<span id="IdePowerD3"></span><span id="idepowerd3"></span><span id="IDEPOWERD3"></span>**IdePowerD3**
</dt> <dd>

Indicates a device power level of 3.

</dd> </dl>

## Remarks

The IDE\_POWER\_STATE enumeration type is used in conjunction with the [**AtaPortRequestPowerStateChange**](ataportrequestpowerstatechange.md) routine to request a power state transition for a device.

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortRequestPowerStateChange**](ataportrequestpowerstatechange.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_POWER_STATE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






