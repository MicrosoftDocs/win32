---
title: ScsiPortConvertPhysicalAddressToUlong routine
description: The ScsiPortConvertPhysicalAddressToUlong routine truncates a SCSI\_PHYSICAL\_ADDRESS to a ULONG.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '55c258d2-922a-430a-ba6b-b05a078b712d'
keywords: ["ScsiPortConvertPhysicalAddressToUlong routine Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiPortConvertPhysicalAddressToUlong
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
---

# ScsiPortConvertPhysicalAddressToUlong routine

The **ScsiPortConvertPhysicalAddressToUlong** routine truncates a SCSI\_PHYSICAL\_ADDRESS to a ULONG.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG ScsiPortConvertPhysicalAddressToUlong(
  _In_ SCSI_PHYSICAL_ADDRESS Address
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

Specifies a value of type SCSI\_PHYSICAL\_ADDRESS.

</dd> </dl>

## Return value

**ScsiPortConvertPhysicalAddressToUlong** returns the low-order part of the given SCSI\_PHYSICAL\_ADDRESS value. A miniport driver cannot call this routine to truncate a 64-bit physical address. Such addresses should be used as quadword values, which contain all 64 bits.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**ACCESS\_RANGE**](access-range.md)
</dt> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> <dt>

[**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortConvertPhysicalAddressToUlong%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






