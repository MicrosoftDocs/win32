---
title: AtaPortSetBusData routine
description: The AtaPortSetBusData routine stores the data at Buffer in the indicated devices PCI configuration space at an offset that is specified in ConfigDataOffset.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 5cc65ef9-7447-4775-bf5d-6dadd78f166c
keywords:
- AtaPortSetBusData routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortSetBusData
api_location:
- Pciidex.lib
- Pciidex.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaPortSetBusData routine

The **AtaPortSetBusData** routine stores the data at *Buffer* in the indicated device's PCI configuration space at an offset that is specified in *ConfigDataOffset*.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG AtaPortSetBusData(
   IN PVOID ControllerExtension,
   IN PVOID Buffer,
   IN PVOID DataMask,
   IN ULONG ConfigDataOffset,
   IN ULONG BufferLength
);
```



## Parameters

<dl> <dt>

*ControllerExtension* 
</dt> <dd>

A pointer to the controller extension.

</dd> <dt>

*Buffer* 
</dt> <dd>

A pointer to the buffer that contains the data to write to the device's PCI bus configuration space.

</dd> <dt>

*DataMask* 
</dt> <dd>

Contains a data mask buffer that controls which bits of PCI bus configuration data must be updated. The length of *Datamask* must be the same length as *Buffer.*

</dd> <dt>

*ConfigDataOffset* 
</dt> <dd>

Specifies an offset into the device's PCI bus configuration data space where the data is updated.

</dd> <dt>

*BufferLength* 
</dt> <dd>

Specifies the length, in bytes, of the buffer.

</dd> </dl>

## Return value

**AtaPortSetBusData** returns the amount of the data that was written in bytes.

## Remarks

**AtaPortSetBusData** completes a bitwise OR, one byte at a time, of the current PCI configuration space data with the new data in *Buffer*. Only those bits not indicated by *DataMask* are left untouched. The byte of data that follows *ConfigDataOffset*, therefore, is updated as follows:


```
ConfigDataOffest[i] = 
    (ConfigDataOffest[i] & ~DataMask[i]) | 
    (DataMask[i] & Buffer[i])
```



## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Pciidex.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**AtaPortGetBusData**](ataportgetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortSetBusData%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






