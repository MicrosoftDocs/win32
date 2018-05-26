---
title: AtaPortBuildRequestSenseIrb routine
description: The AtaPortBuildRequestSenseIrb routine builds and returns an IRB for operation code SCSIOP\_REQUEST\_SENSE.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: f5083841-a6d7-4437-9941-bd7dca2f1771
keywords:
- AtaPortBuildRequestSenseIrb routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortBuildRequestSenseIrb
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

# AtaPortBuildRequestSenseIrb routine

The **AtaPortBuildRequestSenseIrb** routine builds and returns an IRB for operation code SCSIOP\_REQUEST\_SENSE.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PIDE_REQUEST_BLOCK AtaPortBuildRequestSenseIrb(
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

A pointer to a structure of type [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) that defines the failed IDE request block (IRB) for which the request sense will be issued.

</dd> </dl>

## Return value

If the operation succeeds, the **AtaPortBuildRequestSenseIrb** routine returns a pointer to the request sense IRB that it allocated. If the operation fails, **AtaPortBuildRequestSenseIrb** returns **NULL**.

## Remarks

If the device does not support auto request sense, the miniport driver must build an IRB to gather sense data by using **AtaPortBuildRequestSenseIrb** and then sending it to the device. The miniport driver must not complete the original IRB until the corresponding request sense IRB has completed. Be aware that no request sense data is required for ATA devices.

For an explanation of the SCSIOP\_REQUEST\_SENSE command, see the *SCSI-3* specification.

The miniport driver can have only one outstanding request sense IRB per logical unit.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortReleaseRequestSenseIrb**](ataportreleaserequestsenseirb.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortBuildRequestSenseIrb%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






