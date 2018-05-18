---
title: AtaPortGetDeviceBase routine
description: The AtaPortGetDeviceBase routine returns a mapped logical base address that is used to communicate with an HBA.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '5cad43c7-00f0-4590-997c-f956afe07e55'
keywords: ["AtaPortGetDeviceBase routine Storage Devices"]
topic_type:
- apiref
api_name:
- AtaPortGetDeviceBase
api_location:
- ataport.lib
- ataport.dll
- pciidex.lib
- pciidex.dll
api_type:
- LibDef
---

# AtaPortGetDeviceBase routine

The **AtaPortGetDeviceBase** routine returns a mapped logical base address that is used to communicate with an HBA.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PVOID AtaPortGetDeviceBase(
  _In_ PVOID                ChannelExtension,
  _In_ IDE_PHYSICAL_ADDRESS IoAddress,
  _In_ ULONG                NumberOfBytes
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*IoAddress* \[in\]
</dt> <dd>

Specifies the base address to map.

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the range that the mappings should cover. The value for this parameter can be obtained from the **IdeAccessRange** member of the [**IDE\_MINIPORT\_RESOURCES**](ide-miniport-resources.md) structure.

</dd> </dl>

## Return value

**AtaPortGetDeviceBase** returns a mapped logical base address if the operation succeeds. Otherwise, it returns **NULL**.

## Remarks

Miniport drivers must use logical addresses that have been mapped into system space by **AtaPortGetDeviceBase** instead of bus-relative addresses to communicate with its HBA. Calls to the **AtaPort...Port/Register***Xxx* routines require mapped logical addresses.

## Requirements



|                            |                                                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>Ataport.lib; </dt> <dt>Pciidex.lib</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortReadPortUchar**](ataportreadportuchar.md)
</dt> <dt>

[**AtaPortReadPortUshort**](ataportreadportushort.md)
</dt> <dt>

[**AtaPortReadPortUlong**](ataportreadportulong.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortGetDeviceBase%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






