---
title: AtaPortRegistryControllerKeyWrite routine
description: The AtaPortRegistryControllerKeyWrite routine writes the data to the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\ service name \\ControllerN, where N is the number of the controller.
ms.assetid: dfe97cce-f349-49a1-9075-c3c3d1a60681
keywords:
- AtaPortRegistryControllerKeyWrite routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortRegistryControllerKeyWrite
api_location:
- irb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaPortRegistryControllerKeyWrite routine

The **AtaPortRegistryControllerKeyWrite** routine writes the data to the indicated value name under the registry key **HKLM\\CurrentControlSet\\Services\\***&lt;service name&gt;***\\Controller***N*, where *N* is the number of the controller.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN __inline AtaPortRegistryControllerKeyWrite(
  _In_ PVOID  ChannelExtension,
  _In_ UCHAR  ControllerNumber,
  _In_ PCHAR  ValueName,
  _In_ UCHAR  ValueType,
  _In_ PUCHAR Buffer,
  _In_ PULONG Length
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

Contains the name of the registry value to write to.

</dd> <dt>

*ValueType* \[in\]
</dt> <dd>

Indicates the type of data that is contained in the registry value. This member should be assigned one of the values indicated in the following table.



| Value                       | Meaning                                        |
|-----------------------------|------------------------------------------------|
| IDE\_REG\_DWORD<br/>  | A 4-byte numeric value. <br/>            |
| IDE\_REG\_BINARY<br/> | Binary data. <br/>                       |
| IDE\_REG\_SZ<br/>     | A null-terminated, Unicode string. <br/> |



 

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

A pointer to the source buffer that contains the data to write to the registry value.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

A pointer to the number of bytes of data to copy. If the operation fails, the location that is pointed to by *Length* will update the length of data that was successfully copied to the registry.

</dd> </dl>

## Return value

**AtaPortRegistryControllerKeyWrite** returns **TRUE** if the operation succeeds. Otherwise, it returns **FALSE**. The routine also returns **FALSE** if the miniport driver does not call it from the correct routine.

## Remarks

The buffer should be allocated by using [**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md).

The miniport driver must call **AtaPortRegistryControllerKeyWrite** during the [**AtaChannelInitRoutine**](atachannelinitroutine.md) routine or the [**IdeHwControl**](idehwcontrol.md) routine.; The miniport driver cannot call **AtaPortRegistryControllerKeyWrite** from any other routine or it will return **FALSE**. Additionally, the miniport driver can only call **AtaPortRegistryControllerKeyWrite** from its **IdeHwControl** routine if its **IdeHwControl** routine was called and had a value of either **StartChannel** or **StopChannel** in its *ControlAction* parameter.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortRegistryControllerKeyWrite%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






