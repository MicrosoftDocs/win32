---
title: AtaPortRegistryControllerKeyWriteDeferred routine
description: The AtaPortRegistryControllerKeyWriteDeferred routine writes the data asynchronously to the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\ service name \\ControllerN, where N is the number of the controller.
ms.assetid: f4297e91-06ae-4c7a-87bc-12e3f5b0238c
keywords:
- AtaPortRegistryControllerKeyWriteDeferred routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortRegistryControllerKeyWriteDeferred
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

# AtaPortRegistryControllerKeyWriteDeferred routine

The **AtaPortRegistryControllerKeyWriteDeferred** routine writes the data asynchronously to the indicated value name under the registry key **HKLM\\CurrentControlSet\\Services\\***&lt;service name&gt;***\\Controller***N*, where *N* is the number of the controller.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN __inline AtaPortRegistryControllerKeyWriteDeferred(
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

Indicates the type of data that is contained in the registry value. This member should be assigned one of values indicated in the following table.



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

A pointer to the number of bytes of data to copy. If the operation fails, the location pointed to by *Length* will update to the length of data that was successfully copied to the registry.

</dd> </dl>

## Return value

**AtaPortRegistryControllerKeyWriteDeferred** returns **TRUE** if the operation succeeds. Otherwise, it returns **FALSE**. The routine also returns **FALSE** if the miniport driver does not call it from the correct routine.

## Remarks

If the value name is not present, the **AtaPortRegistryControllerKeyWriteDeferred** routine creates an entry for the value name and stores the input data under the newly created value name.

The miniport driver can call the **AtaPortRegistryControllerKeyWriteDeferred** routine from any of the routines that are defined in the channel interface.

The buffer pointed to by *Buffer* must be allocated by using [**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md). The miniport driver must not reuse this buffer after it calls **AtaPortRegistryControllerKeyWriteDeferred** because the port driver delays writing the key data. If the miniport driver reuses the buffer, it might overwrite the data in the buffer before the port driver has an opportunity to store it in the registry key. The port driver flushes the buffer when the miniport driver calls [**AtaPortRegistryFreeBuffer**](ataportregistryfreebuffer.md) to free the buffer.

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortRegistryAllocateBuffer**](ataportregistryallocatebuffer.md)
</dt> <dt>

[**AtaPortRegistryFreeBuffer**](ataportregistryfreebuffer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortRegistryControllerKeyWriteDeferred%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






