---
title: AtaPortGetBusData routine
description: The AtaPortGetBusData routine retrieves data from the location that is specified by ConfigDataOffset within the device's PCI configuration space.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 'bfff10ab-7e15-4db3-b808-947d61844bc0'
keywords: ["AtaPortGetBusData routine Storage Devices"]
topic_type:
- apiref
api_name:
- AtaPortGetBusData
api_location:
- Pciidex.lib
- Pciidex.dll
api_type:
- LibDef
---

# AtaPortGetBusData routine

The **AtaPortGetBusData** routine retrieves data from the location that is specified by *ConfigDataOffset* within the device's PCI configuration space.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG AtaPortGetBusData(
  _In_ PVOID ControllerExtension,
  _In_ PVOID Buffer,
  _In_ ULONG ConfigDataOffset,
  _In_ ULONG BufferLength
);
```



## Parameters

<dl> <dt>

*ControllerExtension* \[in\]
</dt> <dd>

A pointer to the HBA controller extension.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

A pointer to the buffer where the retrieved data is returned.

</dd> <dt>

*ConfigDataOffset* \[in\]
</dt> <dd>

Specifies an offset into the device's PCI bus configuration space where the return value is found.

</dd> <dt>

*BufferLength* \[in\]
</dt> <dd>

Specifies the length, in bytes, of the buffer.

</dd> </dl>

## Return value

**AtaPortGetBusData** returns the amount of the retrieved data in bytes.

## Remarks

**AtaPortGetBusData** retrieves data from the specified offset in the device's PCI bus configuration space and returns it in the buffer that is provided.

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Pciidex.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**AtaPortSetBusData**](ataportsetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortGetBusData%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






