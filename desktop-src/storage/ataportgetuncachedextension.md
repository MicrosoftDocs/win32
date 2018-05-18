---
title: AtaPortGetUnCachedExtension routine
description: The AtaPortGetUncachedExtension routine allocates an uncached common buffer that is shared by the CPU and the device.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '7b81fc29-4906-4095-b197-6b63f5f01ac0'
keywords: ["AtaPortGetUnCachedExtension routine Storage Devices"]
topic_type:
- apiref
api_name:
- AtaPortGetUnCachedExtension
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
---

# AtaPortGetUnCachedExtension routine

The **AtaPortGetUncachedExtension** routine allocates an uncached common buffer that is shared by the CPU and the device.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PVOID AtaPortGetUnCachedExtension(
  _In_ PVOID ChannelExtension,
  _In_ ULONG UncachedExtensionSize,
  _In_ ULONG IrbExtensionSize
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*UncachedExtensionSize* \[in\]
</dt> <dd>

Specifies the length, in bytes, of the uncached common buffer. Set this parameter to 0 if the miniport driver does not require an uncached extension.

</dd> <dt>

*IrbExtensionSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, that is required by the miniport driver for its per request storage, if any.

Set this parameter set to 0 if the miniport driver does not maintain per IRB information for which it requires storage.

</dd> </dl>

## Return value

**AtaPortGetUncachedExtension** returns a virtual address pointer to the uncached extension. If it cannot allocate the requested memory, or if the memory was previously allocated, it returns **NULL**.

## Remarks

The miniport driver can use IRB extensions as storage for driver-determined, request-specific information, such as data that is necessary to process a particular request.

The port driver does not initialize IRB extensions, but sets a pointer to an extension in each IRB that it sends to the miniport driver.

HBA hardware can safely access an IRB extension.

The miniport driver must not call **AtaPortGetUncachedExtension** from any routine other than its [**IdeHwControl**](idehwcontrol.md) routine, and only when it is processing a control action of **StartChannel**. Calls of **AtaPortGetUncachedExtension** from other miniport driver routines result in incorrect operation or even system failure. The port driver automatically frees the uncached extension after it invokes **IdeHwControl** with the **StopChannel** control action.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**IdeHwControl**](idehwcontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortGetUnCachedExtension%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






