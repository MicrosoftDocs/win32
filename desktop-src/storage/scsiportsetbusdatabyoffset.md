---
title: ScsiPortSetBusDataByOffset routine
description: The ScsiPortSetBusDataByOffset routine sets bus-configuration data for an adapter on a dynamically configurable I/O bus with a published, standard interface.
ms.assetid: '64f46049-fbf0-4d9b-b5fe-9877a964755f'
keywords: ["ScsiPortSetBusDataByOffset routine Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiPortSetBusDataByOffset
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
---

# ScsiPortSetBusDataByOffset routine

The **ScsiPortSetBusDataByOffset** routine sets bus-configuration data for an adapter on a dynamically configurable I/O bus with a published, standard interface.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG ScsiPortSetBusDataByOffset(
  _In_ PVOID DeviceExtension,
  _In_ ULONG BusDataType,
  _In_ ULONG SystemIoBusNumber,
  _In_ ULONG SlotNumber,
  _In_ PVOID Buffer,
  _In_ ULONG Offset,
  _In_ ULONG Length
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's device extension.

</dd> <dt>

*BusDataType* \[in\]
</dt> <dd>

Contains a value of type [**BUS\_DATA\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff540700) that specifies the type of bus data to be set. Currently, its value can be **PCIConfiguration**. However, additional types of standardized, dynamically configurable buses will be supported in future. The upper bound on the bus types supported is always **MaximumBusDataType**.

</dd> <dt>

*SystemIoBusNumber* \[in\]
</dt> <dd>

Specifies the system-assigned number of the I/O bus on which the HBA is connected. The miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine obtains this value from the input PORT\_CONFIGURATION\_INFORMATION **SystemIoBusNumber** member.

</dd> <dt>

*SlotNumber* \[in\]
</dt> <dd>

Specifies the logical slot number of the HBA.

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

Specifies the number of bytes in the storage area at *Buffer*.

</dd> </dl>

## Return value

**ScsiPortSetBusDataByOffset** returns the number of bytes of data successfully set for the given *SlotNumber*. If the given *BusDataType* is not valid for the current platform or if the supplied information is invalid, **ScsiPortSetBusDataByOffset** returns zero.

## Remarks

Miniport drivers of HBAs on a PCI bus seldom call **ScsiPortSetBusDataByOffset** unless unusual circumstances or the nature of a particular driver's HBA requires such a call. For example, a miniport driver might call **ScsiPortSetBusDataByOffset** to clear a bit in the PCI status register if its HBA signals a target abort during initialization or to set device-specific configuration data for the HBA.

**ScsiPortSetBusDataByOffset** can be called only from the miniport driver's *HwScsiFindAdapter* routine or from HwScsiAdapterControl when the control type is **ScsiSetRunningConfig**.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**HalSetBusDataByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546633)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**PCI\_COMMON\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff558786)
</dt> <dt>

[**PCI\_SLOT\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff558790)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[**ScsiPortGetBusData**](scsiportgetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortSetBusDataByOffset%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






