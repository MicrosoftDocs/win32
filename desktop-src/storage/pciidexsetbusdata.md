---
title: PciIdeXSetBusData routine
description: The PciIdeXSetBusData routine stores data in Buffer at an offset specified in ConfigDataOffset within the devices PCI configuration space.
ms.assetid: 1fd23ba3-aae6-4ae6-9e5c-1f896e3a6198
keywords:
- PciIdeXSetBusData routine Storage Devices
topic_type:
- apiref
api_name:
- PciIdeXSetBusData
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

# PciIdeXSetBusData routine

The **PciIdeXSetBusData** routine stores data in *Buffer* at an offset specified in *ConfigDataOffset* within the device's PCI configuration space.

## Syntax


```C++
NTSTATUS PciIdeXSetBusData(
  _In_ PVOID DeviceExtension,
  _In_ PVOID Buffer,
  _In_ PVOID DataMask,
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

Contains a pointer to the buffer in which data from the device's PCI bus configuration space is written.

</dd> <dt>

*DataMask* \[in\]
</dt> <dd>

Contains a data mask buffer that controls which bits of PCI bus configuration data are to be updated by **PciIdeXSetBusData**. The length of *Datamask* must be the same as the length of *Buffer.*

</dd> <dt>

*ConfigDataOffset* \[in\]
</dt> <dd>

Specifies an offset into the PCI configuration data space where the data to be updated can be found.

</dd> <dt>

*BufferLength* \[in\]
</dt> <dd>

Specifies the length in bytes of the buffer.

</dd> </dl>

## Return value

**PciIdeXSetBusData** returns STATUS\_SUCCESS if the data in the device's PCI configuration space was successfully updated and STATUS\_UNSUCCESSFUL data if the device's PCI configuration space could not be updated.

## Remarks

**PciIdeXSetBusData** replaces each byte of current PCI data, beginning with the byte indicated by *ConfigDataOffest*, with the new data contained in *Buffer*. For each byte, those bits not indicated by the *DataMask* are left untouched. The ith byte of data that follows *ConfigDataOffset*, therefore, is updated as follows:


```
ConfigDataOffest[i] = 
    (ConfigDataOffest[i] & ~DataMask[i]) | (DataMask[i] & Buffer[i])
```



**PciIdeXSetBusData** completes a bitwise OR, one byte at a time, of the current PCI configuration space data with the new data in *Buffer*. For each byte, only the bits indicated by *DataMask* are updated. **PciIdeXSetBusData** then stores the result of the logical OR in the device's PCI configuration space.

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

[**PciIdeXGetBusData**](pciidexgetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PciIdeXSetBusData%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






