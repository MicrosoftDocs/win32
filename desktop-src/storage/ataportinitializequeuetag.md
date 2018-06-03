---
title: AtaPortInitializeQueueTag routine
description: The AtaPortInitializeQueueTag routine initializes the queue tag list for the specified device.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: f6d40f3e-4bc9-4b30-97ac-600a33280305
keywords:
- AtaPortInitializeQueueTag routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortInitializeQueueTag
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

# AtaPortInitializeQueueTag routine

The **AtaPortInitializeQueueTag** routine initializes the queue tag list for the specified device.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN AtaPortInitializeQueueTag(
  _In_ PVOID ChannelExtension,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ UCHAR MaxQueueTag
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Specifies the target identifier of the device.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Specifies the logical unit number (LUN) of the device.

</dd> <dt>

*MaxQueueTag* \[in\]
</dt> <dd>

Specifies the maximum allowed value for the queue tag.

</dd> </dl>

## Return value

**AtaPortInitializeQueueTag** returns **TRUE** if the operation succeeds. Otherwise, it returns **FALSE**.

## Remarks

The miniport driver should call **AtaPortInitializeQueueTag** before it uses [**AtaPortAllocateQueueTag**](ataportallocatequeuetag.md) and [**AtaPortReleaseQueueTag**](ataportreleasequeuetag.md) to allocate and release queue tags respectively.

The values in the *TargetId* and *Lun* parameters specify the device to which the queue tag belongs. To generate channel specific queue tags, the miniport driver should set the *TargetId* and *Lun* parameters to IDE\_UNTAGGED.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortAllocateQueueTag**](ataportallocatequeuetag.md)
</dt> <dt>

[**AtaPortReleaseQueueTag**](ataportreleasequeuetag.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortInitializeQueueTag%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






