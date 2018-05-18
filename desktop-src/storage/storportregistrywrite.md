---
title: StorPortRegistryWrite routine
description: The StorPortRegistryWrite routine is called by the miniport driver to convert the registry data contained in a specified buffer from ASCII to Unicode and to then write the data to the miniport driver's per-HBA storage area.
ms.assetid: '9f149e86-7855-4a10-8e0c-8b1aff261946'
keywords: ["StorPortRegistryWrite routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortRegistryWrite
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortRegistryWrite routine

The **StorPortRegistryWrite** routine is called by the miniport driver to convert the registry data contained in a specified buffer from ASCII to Unicode and to then write the data to the miniport driver's per-HBA storage area.

## Syntax


```C++
STORPORT_API BOOLEAN StorPortRegistryWrite(
  _In_ PVOID  HwDeviceExtension,
  _In_ PUCHAR ValueName,
  _In_ ULONG  Global,
  _In_ ULONG  Type,
  _In_ PUCHAR Buffer,
  _In_ ULONG  BufferLength
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device. The miniport driver must be running at IRQL PASSIVE\_LEVEL when it calls this routine.

</dd> <dt>

*ValueName* \[in\]
</dt> <dd>

Pointer to a string that specifies the value name.

</dd> <dt>

*Global* \[in\]
</dt> <dd>

Indicates whether the operation is to be adapter specific or to relate to all adapters.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

One of the following registry data types.



| Type                                         | Meaning                                                                         |
|----------------------------------------------|---------------------------------------------------------------------------------|
| REG\_SZ<br/>                           | Unicode null-terminated string.<br/>                                      |
| REG\_EXPAND\_SZ<br/>                   | Unicode null-terminated string with environment variable references.<br/> |
| REG\_BINARY<br/>                       | Binary data.<br/>                                                         |
| REG\_DWORD<br/>                        | 32-bit double word.<br/>                                                  |
| REG\_DWORD\_LITTLE\_ENDIAN<br/>        | 32-bit double word with a little-endian format.<br/>                      |
| REG\_DWORD\_BIG\_ENDIAN<br/>           | 32-bit double word with a big-endian format.<br/>                         |
| REG\_LINK<br/>                         | Unicode string that specifies a symbolic link.<br/>                       |
| REG\_MULTI\_SZ<br/>                    | Multiple Unicode strings.<br/>                                            |
| REG\_RESOURCE\_LIST<br/>               | Resource list in the resource map.<br/>                                   |
| REG\_FULL\_RESOURCE\_DESCRIPTOR<br/>   | Resource list in the hardware description.<br/>                           |
| REG\_RESOURCE\_REQUIREMENTS\_LIST<br/> | Resource requirement list.<br/>                                           |
| REG\_QWORD<br/>                        | 64-bit quadlet number.<br/>                                               |
| REG\_QWORD\_LITTLE\_ENDIAN<br/>        | 64-bit quadlet number with a little-endian format.<br/>                   |



 

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to a buffer that contains the registry data to be written.

</dd> <dt>

*BufferLength* \[in\]
</dt> <dd>

Specifies the size of the buffer pointed to by *Buffer*.

</dd> </dl>

## Return value

**StorPortRegistryWrite** returns a Boolean value of **TRUE** if the registry data was successfully converted and written; otherwise, this routine returns **FALSE**.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| IRQL<br/>                 | PASSIVE\_LEVEL<br/>                                                                                                               |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



## See also

<dl> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortRegistryWrite%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






