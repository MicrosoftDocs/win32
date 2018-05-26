---
title: AtaPortConvertPhysicalAddressToUlong routine
description: The AtaPortConvertPhysicalAddressToUlong routine truncates an address of type IDE\_PHYSICAL\_ADDRESS to a ULONG.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: cd63cb65-701e-46e2-ba32-971f91f9eb29
keywords:
- AtaPortConvertPhysicalAddressToUlong routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortConvertPhysicalAddressToUlong
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaPortConvertPhysicalAddressToUlong routine

The **AtaPortConvertPhysicalAddressToUlong** routine truncates an address of type IDE\_PHYSICAL\_ADDRESS to a ULONG.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG AtaPortConvertPhysicalAddressToUlong(
  _In_ IDE_PHYSICAL_ADDRESS Address
);
```



## Parameters

<dl> <dt>

*Address* \[in\]
</dt> <dd>

Specifies a value of type IDE\_PHYSICAL\_ADDRESS.

</dd> </dl>

## Return value

**AtaPortConvertPhysicalAddressToUlong** returns the lower order part of the given IDE\_PHYSICAL\_ADDRESS value.

## Remarks

A miniport driver must not use this routine to truncate a 64-bit physical address.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortConvertUlongToPhysicalAddress**](ataportconvertulongtophysicaladdress.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortConvertPhysicalAddressToUlong%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






