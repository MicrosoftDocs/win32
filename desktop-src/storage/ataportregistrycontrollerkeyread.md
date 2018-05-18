---
title: AtaPortRegistryControllerKeyRead routine
description: The AtaPortRegistryControllerKeyRead routine reads the data that is associated with the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\ service name \\ControllerN, where N is the number of the controller.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: '7db22027-49ac-4ee5-8da7-bbd16c97a35b'
keywords: ["AtaPortRegistryControllerKeyRead routine Storage Devices"]
topic_type:
- apiref
api_name:
- AtaPortRegistryControllerKeyRead
api_location:
- irb.h
api_type:
- HeaderDef
---

# AtaPortRegistryControllerKeyRead routine

The **AtaPortRegistryControllerKeyRead** routine reads the data that is associated with the indicated value name under the registry key **HKLM\\CurrentControlSet\\Services\\***&lt;service name&gt;***\\Controller***N*, where *N* is the number of the controller.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN __inline AtaPortRegistryControllerKeyRead(
  _In_      PVOID  ChannelExtension,
  _In_      UCHAR  ControllerNumber,
  _In_      PCHAR  ValueName,
  _In_      UCHAR  ValueType,
  _Out_opt_ PUCHAR Buffer,
  _Inout_   PULONG Length
);
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the channel extension.

</dd> <dt>

*ControllerNumber* \[in\]
</dt> <dd>

Contains the controller number.

</dd> <dt>

*ValueName* \[in\]
</dt> <dd>

Contains the name of the registry value to read.

</dd> <dt>

*ValueType* \[in\]
</dt> <dd>

Indicates the type of the data that is contained in the registry value. This parameter should be assigned one of values indicated in the following table.



| Value type                  | Meaning                                        |
|-----------------------------|------------------------------------------------|
| IDE\_REG\_DWORD<br/>  | A 4-byte numeric value. <br/>            |
| IDE\_REG\_BINARY<br/> | Binary data. <br/>                       |
| IDE\_REG\_SZ<br/>     | A null-terminated, Unicode string. <br/> |



 

</dd> <dt>

*Buffer* \[out, optional\]
</dt> <dd>

A pointer to the buffer where the results are to be copied.

</dd> <dt>

*Length* \[in, out\]
</dt> <dd>

A pointer to the number of bytes of data to copy. If the operation fails because of an insufficient buffer, the location that is pointed to by *Length* will update to the actual length of the data in the registry.

</dd> </dl>

## Return value

**AtaPortRegistryControllerKeyRead** returns **TRUE** if the operation succeeds. Otherwise, it returns **FALSE**. The **AtaPortRegistryControllerKeyRead** routine also returns **FALSE** if the miniport driver does not call it from the correct routine.

## Remarks

The buffer at *Buffer* must be allocated by using [**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md).

The miniport driver must call **AtaPortRegistryControllerKeyRead** either in its [**AtaChannelInitRoutine**](atachannelinitroutine.md) routine or in its [**IdeHwControl**](idehwcontrol.md) routine. It cannot call **AtaPortRegistryControllerKeyRead** from any other routine. Additionally, the miniport driver can only call **AtaPortRegistryControllerKeyRead** from its **IdeHwControl** routine if its **IdeHwControl** routine was called and had a value of either **StartChannel** or **StopChannel** in its *ControlAction* parameter.

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaChannelInitRoutine**](atachannelinitroutine.md)
</dt> <dt>

[**IdeHwControl**](idehwcontrol.md)
</dt> <dt>

[**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortRegistryControllerKeyRead%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






