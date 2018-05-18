---
title: AtaPortRegistryFreeBuffer routine
description: The AtaPortRegistryFreeBuffer routine frees the registry buffer that was allocated by using AtaPortRegistryAllocateBuffer.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 'a84dffce-977e-412a-a12a-e0e156b943ac'
keywords: ["AtaPortRegistryFreeBuffer routine Storage Devices"]
topic_type:
- apiref
api_name:
- AtaPortRegistryFreeBuffer
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
---

# AtaPortRegistryFreeBuffer routine

The **AtaPortRegistryFreeBuffer** routine frees the registry buffer that was allocated by using [**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md).

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID AtaPortRegistryFreeBuffer(
  _In_ PVOID ChannelExtension,
  _In_ PVOID Buffer
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

A pointer to the buffer to free.

</dd> </dl>

## Return value

None

## Remarks

**AtaPortRegistryFreeBuffer** flushes deferred write operations to the registry.

The miniport driver must call **AtaPortRegistryFreeBuffer** either in its [**AtaChannelInitRoutine**](atachannelinitroutine.md) routine or in its [**IdeHwControl**](idehwcontrol.md) routine. It cannot call **AtaPortRegistryFreeBuffer** from any other routine. Additionally, the miniport driver can only call **AtaPortRegistryFreeBuffer** from its **IdeHwControl** routine if its **IdeHwControl** routine was called and had a value of either **StartChannel** or **StopChannel** in its *ControlAction* parameter.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaChannelInitRoutine**](atachannelinitroutine.md)
</dt> <dt>

[**IdeHwControl**](idehwcontrol.md)
</dt> <dt>

[**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortRegistryFreeBuffer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






