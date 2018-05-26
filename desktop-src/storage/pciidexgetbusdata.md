---
title: PciIdeXGetBusData routine
description: The PciIdeXGetBusData routine retrieves data from the location specified by ConfigDataOffset within the devices PCI configuration space.
ms.assetid: bc233c05-9412-4bdb-9466-481bf53aff6c
keywords:
- PciIdeXGetBusData routine Storage Devices
topic_type:
- apiref
api_name:
- PciIdeXGetBusData
api_location:
- Pciidex.lib
- Pciidex.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PciIdeXGetBusData routine

The **PciIdeXGetBusData** routine retrieves data from the location specified by *ConfigDataOffset* within the device's PCI configuration space.

## Syntax


```C++
NTSTATUS PciIdeXGetBusData(
  _In_ PVOID DeviceExtension,
  _In_ PVOID Buffer,
  _In_ ULONG ConfigDataOffset,
  _In_ ULONG BufferLength
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Contains a pointer to the device extension of the IDE controller.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Contains a pointer to the buffer in which data from the device's PCI bus configuration space is returned.

</dd> <dt>

*ConfigDataOffset* \[in\]
</dt> <dd>

Specifies an offset into the device's PCI configuration space where the data to be returned can be found.

</dd> <dt>

*BufferLength* \[in\]
</dt> <dd>

Specifies the length in bytes of the buffer.

</dd> </dl>

## Return value

**PciIdeXGetBusData** returns STATUS\_SUCCESS if the data was successfully retrieved from the device's PCI configuration space or STATUS\_UNSUCCESSFUL if the data could not be retrieved.

## Remarks

**PcildeXGetBusData** stores the retrieved data in *Buffer*.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Pciidex.lib</dt> </dl>           |



## See also

<dl> <dt>

[**PciIdeXInitialize**](pciidexinitialize.md)
</dt> <dt>

[**PciIdeXSetBusData**](pciidexsetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PciIdeXGetBusData%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






