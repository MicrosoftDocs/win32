---
title: AtaPortReadPortBufferUshort routine
description: The AtaPortReadPortBufferUshort routine transfers a given number of USHORT values from the HBA to a buffer.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: f118af3b-5a9a-486b-9550-9b48bdfb48cd
keywords:
- AtaPortReadPortBufferUshort routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortReadPortBufferUshort
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AtaPortReadPortBufferUshort routine

The **AtaPortReadPortBufferUshort** routine transfers a given number of USHORT values from the HBA to a buffer.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID AtaPortReadPortBufferUshort(
  _In_ PUSHORT Port,
  _In_ PUSHORT Buffer,
  _In_ ULONG   Count
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

A pointer to the I/O port. The address value that is assigned to this parameter must be within the range of mapped I/O space addresses that are obtained by a call to [**AtaPortGetDeviceBase**](ataportgetdevicebase.md).

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

A pointer to the destination buffer.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Specifies the number of USHORT values to read from the HBA.

</dd> </dl>

## Return value

None

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortGetDeviceBase**](ataportgetdevicebase.md)
</dt> <dt>

[**AtaPortReadPortBufferUchar**](ataportreadportbufferuchar.md)
</dt> <dt>

[**AtaPortReadPortBufferUlong**](ataportreadportbufferulong.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortReadPortBufferUshort%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






