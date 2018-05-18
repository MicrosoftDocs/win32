---
title: ScsiPortReadRegisterUshort routine
description: The ScsiPortReadRegisterUshort routine reads a USHORT value from the HBA.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '192a525e-6a42-4bd0-9c50-d13741469a48'
keywords: ["ScsiPortReadRegisterUshort routine Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiPortReadRegisterUshort
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
---

# ScsiPortReadRegisterUshort routine

The **ScsiPortReadRegisterUshort** routine reads a USHORT value from the HBA.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
USHORT ScsiPortReadRegisterUshort(
  _In_ PUSHORT Register
);
```



## Parameters

<dl> <dt>

*Register* \[in\]
</dt> <dd>

Pointer to the register. The given *Register* must be in a mapped memory-space range returned by **ScsiPortGetDeviceBase**.

</dd> </dl>

## Return value

**ScsiPortReadRegisterUshort** returns a USHORT value from the HBA's register.

## Remarks

**ScsiPortReadRegisterUshort** ensures that the data is transferred correctly.

## Requirements



|                            |                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                           |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h, Scsi.h, or Storport.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                                      |



## See also

<dl> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortReadRegisterUshort%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






