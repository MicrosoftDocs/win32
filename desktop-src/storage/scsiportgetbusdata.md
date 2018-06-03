---
title: ScsiPortGetBusData routine
description: The ScsiPortGetBusData routine returns bus-type-specific configuration information that a miniport driver's HwScsiFindAdapter routine might use to determine whether it supports a particular adapter on a particular I/O bus, and to configure the HBA if it does.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 43d30c99-9f9e-4516-8c50-e096f760a774
keywords:
- ScsiPortGetBusData routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortGetBusData
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiPortGetBusData routine

The **ScsiPortGetBusData** routine returns bus-type-specific configuration information that a miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine might use to determine whether it supports a particular adapter on a particular I/O bus, and to configure the HBA if it does.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG ScsiPortGetBusData(
  _In_ PVOID DeviceExtension,
  _In_ ULONG BusDataType,
  _In_ ULONG SystemIoBusNumber,
  _In_ ULONG SlotNumber,
  _In_ PVOID Buffer,
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

Contains a value of type [**BUS\_DATA\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff540700) that specifies the type of bus-specific configuration data to be returned. Currently, this value can be one of the following: **Cmos**, **EisaConfiguration**, **Pos**, or **PCIConfiguration**. However, additional types of bus configuration will be supported in the future. The upper bound on the types supported is always **MaximumBusDataType**.

</dd> <dt>

*SystemIoBusNumber* \[in\]
</dt> <dd>

Specifies the system-assigned number of the I/O bus. The miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine obtains this value from the input PORT\_CONFIGURATION\_INFORMATION **SystemIoBusNumber** member.

</dd> <dt>

*SlotNumber* \[in\]
</dt> <dd>

Specifies the logical slot number or location of the device.

If **PCIConfiguration** is specified as the *BusDataType*, this parameter must be specified as a PCI\_SLOT\_NUMBER-type value.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to a buffer or area to which the configuration data is returned or, if the given *Length* is zero, points to a location to which the operating system-specific port driver returns a pointer to a buffer that it allocates.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Specifies the maximum number of bytes to return at *Buffer*, or zero if the caller requires the operating system-specific port driver to allocate a buffer to contain the data.

</dd> </dl>

## Return value

**ScsiPortGetBusData** returns the number of bytes of configuration information it stored in the buffer. When the input BusDataType is PCIConfiguration, ScsiPortGetBusData can return either of the following values to indicate an error.



| Return code                                                                             | Description                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**0 (zero)**</dt> </dl> | The PCI bus does not exist.<br/>                                                                                                                                                        |
| <dl> <dt>**2**</dt> </dl>        | The PCI bus exists, but there is no device at the given PCI *SlotNumber*. The *Buffer* contains the value PCI\_INVALID\_VENDOR\_ID at the PCI\_COMMON\_CONFIG **VendorId** member.<br/> |



 

## Remarks

**ScsiPortGetBusData** can be called only from a miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine or from *HwScsiAdapterControl* when the control type is **ScsiSetRunningConfig**. Calls from other miniport driver routines will result in system failure or incorrect operation for the caller.

Configuration data returned by **ScsiPortGetBusData** is valid only until the miniport driver calls **ScsiPortGetBusData** again. As soon as the caller's *HwScsiFindAdapter* routine returns control, any returned configuration data becomes invalid.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**PCI\_COMMON\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff558786)
</dt> <dt>

[**PCI\_SLOT\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff558790)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortGetBusData%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






