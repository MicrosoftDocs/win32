---
title: StorPortSetBusDataByOffset routine
description: The StorPortSetBusDataByOffset routine writes bus-specific configuration information.
ms.assetid: ec1db013-b630-421b-8d22-385a2d9b9510
keywords:
- StorPortSetBusDataByOffset routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortSetBusDataByOffset
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortSetBusDataByOffset routine

The **StorPortSetBusDataByOffset** routine writes bus-specific configuration information.

## Syntax


```C++
STORPORT_API ULONG StorPortSetBusDataByOffset(
  _In_ PVOID DeviceExtension,
  _In_ ULONG BusDataType,
  _In_ ULONG SystemIoBusNumber,
  _In_ ULONG SlotNumber,
  _In_ PVOID Buffer,
  _In_ ULONG Offset,
  _In_ ULONG Length
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*BusDataType* \[in\]
</dt> <dd>

Contains a value of type [**BUS\_DATA\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff540700) that specifies the type of the bus for which configuration information is to be written. Currently, its value can be **PCIConfiguration**. However, additional types of standardized, dynamically configurable buses will be supported in future. The upper bound on the bus types supported is always **MaximumBusDataType**.

</dd> <dt>

*SystemIoBusNumber* \[in\]
</dt> <dd>

Specifies the system-assigned number of the I/O bus on which the HBA is connected. The miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine obtains this value from the input **PORT\_CONFIGURATION\_INFORMATIONSystemIoBusNumber** member.

</dd> <dt>

*SlotNumber* \[in\]
</dt> <dd>

Indicates the logical slot number of the HBA.

When **PCIConfiguration** is specified as the *BusDataType*, this parameter must be specified as a PCI\_SLOT\_NUMBER-type value.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to a caller-supplied storage area with configuration information specific to *BusDataType*.

When **PCIConfiguration** is specified, the buffer contains some or all of the PCI\_COMMON\_CONFIG information for the given *SlotNumber*. The specified *Offset* and *Length* determine how much information is supplied.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Specifies the byte offset within the PCI\_COMMON\_CONFIG structure at which the caller-supplied configuration values begin. A miniport driver can use PCI\_COMMON\_HDR\_LENGTH to specify the offset of the device-specific area in PCI\_COMMON\_CONFIG.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Indicates the length, in bytes, of the maximum amount of data to return.

</dd> </dl>

## Return value

**StorPortSetBusDataByOffset** returns the number of bytes of configuration data written.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**ScsiPortSetBusDataByOffset**](scsiportsetbusdatabyoffset.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortSetBusDataByOffset%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






