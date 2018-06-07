---
title: AtaPortGetPhysicalAddress routine
description: The AtaPortGetPhysicalAddress routine converts the virtual address range to the physical address range.
ms.assetid: f6c595f2-a493-453a-a744-7ce6577ae29e
keywords:
- AtaPortGetPhysicalAddress routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortGetPhysicalAddress
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

# AtaPortGetPhysicalAddress routine

The **AtaPortGetPhysicalAddress** routine converts the virtual address range to the physical address range.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_PHYSICAL_ADDRESS AtaPortGetPhysicalAddress(
  _In_      PVOID              ChannelExtension,
  _In_opt_  PIDE_REQUEST_BLOCK Irb,
  _In_opt_  PVOID              VirtualAddress,
  _Out_opt_ ULONG              *Length
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*Irb* \[in, optional\]
</dt> <dd>

A pointer to a structure of type [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) that defines the IDE request block (IRB) for which the address range is converted.

</dd> <dt>

*VirtualAddress* \[in, optional\]
</dt> <dd>

A pointer to the base virtual address to convert.

</dd> <dt>

*Length* \[out, optional\]
</dt> <dd>

Returns the number of mapped bytes starting at the returned physical address.

</dd> </dl>

## Return value

**AtaPortGetPhysicalAddress** returns the corresponding physical address for the virtual address. If the virtual address cannot be converted, it returns **NULL**.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_REQUEST\_BLOCK**](ide-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortGetPhysicalAddress%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






