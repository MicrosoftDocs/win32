---
title: AtaPortGetScatterGatherList routine
description: The AtaPortGetScatterGatherList routine retrieves the scatter/gather list that is associated with this request.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 11181574-b329-4182-8d17-93d44cb3b839
keywords:
- AtaPortGetScatterGatherList routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortGetScatterGatherList
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

# AtaPortGetScatterGatherList routine

The **AtaPortGetScatterGatherList** routine retrieves the scatter/gather list that is associated with this request.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PIDE_SCATTER_GATHER_LIST AtaPortGetScatterGatherList(
  _In_ PVOID              ChannelExtension,
  _In_ PIDE_REQUEST_BLOCK Irb
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*Irb* \[in\]
</dt> <dd>

A pointer to a structure of type [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) that defines the IDE request block (IRB) for which a scatter/gather list is constructed.

</dd> </dl>

## Return value

If the IRB\_FLAGS\_USE\_DMA flag is set in the **IrbFlags** member of IRB, the **AtaPortGetScatterGatherList** routine returns a pointer to the scatter/gather list that is associated with the IRB. Otherwise, **AtaPortGetScatterGatherList** returns **NULL**.

## Remarks

Every IRB with IRB\_FLAGS\_USE\_DMA set in the **IrbFlags** member has a scatter/gather list associated with it.

The miniport driver must not modify the scatter/gather list.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortGetScatterGatherList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






