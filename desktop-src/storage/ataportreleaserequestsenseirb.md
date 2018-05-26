---
title: AtaPortReleaseRequestSenseIrb routine
description: The AtaPortReleaseRequestSenseIrb routine frees the request sense IRB tha is allocated by using AtaPortBuildRequestSenseIrb.
ms.assetid: 53e5e234-c256-4581-b109-307f2f17522f
keywords:
- AtaPortReleaseRequestSenseIrb routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortReleaseRequestSenseIrb
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

# AtaPortReleaseRequestSenseIrb routine

The **AtaPortReleaseRequestSenseIrb** routine frees the request sense IRB tha is allocated by using [**AtaPortBuildRequestSenseIrb**](ataportbuildrequestsenseirb.md).

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID AtaPortReleaseRequestSenseIrb(
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

A pointer to a structure of type [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) that defines the request sense IRB.

</dd> </dl>

## Return value

None

## Remarks

The **AtaPortReleaseRequestSenseIrb** routine releases the IRB to the port driver and copies the sense data to the buffer that is pointed to by the **SenseInfoBuffer** member of the original (failed) request's IRB. The miniport driver can then complete the original request by using [**AtaPortCompleteRequest**](ataportcompleterequest.md). The miniport driver must not touch the request sense IRB after it has been released to the port driver.

The miniport driver must call **AtaPortReleaseRequestSenseIrb** for every allocated IRB that is allocated by using [**AtaPortBuildRequestSenseIrb**](ataportbuildrequestsenseirb.md).

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortBuildRequestSenseIrb**](ataportbuildrequestsenseirb.md)
</dt> <dt>

[**AtaPortCompleteRequest**](ataportcompleterequest.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortReleaseRequestSenseIrb%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






