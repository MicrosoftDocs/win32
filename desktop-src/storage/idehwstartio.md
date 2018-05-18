---
title: IdeHwStartIo routine
description: The IdeHwStartIo miniport driver routine processes the synchronized aspects of an I/O request.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '9172e62e-263c-471c-bcc2-9be4e1d6b1a2'
keywords: ["IdeHwStartIo routine Storage Devices", "IDE_HW_STARTIO"]
topic_type:
- apiref
api_name:
- IdeHwStartIo
api_location:
- irb.h
api_type:
- UserDefined
---

# IdeHwStartIo routine

The ***IdeHwStartIo*** miniport driver routine processes the synchronized aspects of an I/O request.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_HW_STARTIO IdeHwStartIo;

BOOLEAN IdeHwStartIo(
  _In_ PVOID              ChannelExtension,
  _In_ PIDE_REQUEST_BLOCK Irb
)
{ ... }
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver per channel device extension.

</dd> <dt>

*Irb* \[in\]
</dt> <dd>

A pointer to a structure of type [**IDE\_REQUEST\_BLOCK**](ide-request-block.md) that defines the IDE request block (IRB) to process.

</dd> </dl>

## Return value

***IdeHwStartIo*** returns **TRUE** to acknowledge the receipt of an IRB. The port driver ignores a return value of **FALSE**.

## Remarks

Miniport drivers must provide an ***IdeHwStartIo*** routine to process the aspects of an I/O request that must be handled synchronously. For information about how the miniport driver processes the unsynchronized aspects of an I/O request, see [**IdeHwBuildIo**](idehwbuildio.md).

After the miniport driver receives the ***IdeHwStartIo*** call, it owns the request and must complete it.

After this routine returns, the miniport driver should be prepared to receive the next request from the port driver immediately.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IdeHwBuildIo**](idehwbuildio.md)
</dt> <dt>

[**IDE\_REQUEST\_BLOCK**](ide-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IdeHwStartIo%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






