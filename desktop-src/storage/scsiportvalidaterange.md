---
title: ScsiPortValidateRange routine
description: The ScsiPortValidateRange routine indicates whether the specified access range values have already been claimed in the registry by another driver.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: a9ad58c2-16fc-410a-abc7-01c3f2354b88
keywords:
- ScsiPortValidateRange routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortValidateRange
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

# ScsiPortValidateRange routine

The **ScsiPortValidateRange** routine indicates whether the specified access range values have already been claimed in the registry by another driver.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN ScsiPortValidateRange(
  _In_ PVOID                 HwDeviceExtension,
  _In_ INTERFACE_TYPE        BusType,
  _In_ ULONG                 SystemIoBusNumber,
  _In_ SCSI_PHYSICAL_ADDRESS IoAddress,
  _In_ ULONG                 NumberOfBytes,
  _In_ BOOLEAN               InIoSpace
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*BusType* \[in\]
</dt> <dd>

Specifies the value of the **AdapterInterfaceType** member in the PORT\_CONFIGURATION\_INFORMATION structure when *HwScsiFindAdapter* is called.

</dd> <dt>

*SystemIoBusNumber* \[in\]
</dt> <dd>

Specifies the value of the **SystemIoBusNumber** member in the configuration information when *HwScsiFindAdapter* is called.

</dd> <dt>

*IoAddress* \[in\]
</dt> <dd>

Specifies a bus-relative base address for the range of ports or device memory to be validated *before* the miniport driver's *HwScsiFindAdapter* routine attempts to map the access range for the adapter at that address.

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

Specifies the size in bytes or number of elements in the range.

</dd> <dt>

*InIoSpace* \[in\]
</dt> <dd>

Indicates when TRUE that the range is in I/O space, rather than in memory. When **FALSE**, the range is in memory space.

</dd> </dl>

## Return value

**ScsiPortValidateRange** returns **TRUE** if the HwScsiFindAdapter routine can safely map and use the mapped range to access the adapter. **ScsiPortValidateRange** returns **FALSE** if the specified access range values have already been claimed in the registry by another driver.

## Remarks

**ScsiPortValidateRange** can be called only from a miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine. Calls from other miniport driver routines will result in system failure or incorrect operation for the caller.

If the operating system-specific port driver initializes any **AccessRanges** element of the PORT\_CONFIGURATION\_INFORMATION structure before it calls the miniport driver's *HwScsiFindAdapter* routine, the miniport driver must pass the supplied values to **ScsiPortGetDeviceBase** and use the mapped logical addresses for the range to determine whether an HBA is one that it supports.

The port driver either fills an ACCESS\_RANGE-type element with a complete description of a bus-relative address range for an adapter, or the port driver zeros all members of the element.

For input **AccessRanges** elements set with default zeros, the *HwScsiFindAdapter* routine can attempt to locate an adapter it supports on the given I/O bus. In these circumstances, a miniport driver usually has a set of driver-determined default addresses for its type(s) of HBA. However, a previously loaded driver might already be using an initialized adapter at one of this miniport driver's default address ranges, particularly in x86-only systems in which some devices are initialized in x86 real mode. To prevent such a device from being inadvertently reprogrammed, each miniport driver's *HwScsiFindAdapter* routine should call **ScsiPortValidateRange** before it maps any driver-supplied addresses with **ScsiPortGetDeviceBase** and then uses the mapped logical addresses to interrogate adapters on an I/O bus.

If **ScsiPortValidateRange** returns **FALSE**, *HwScsiFindAdapter* must not attempt to map the input range addresses because another driver has already claimed the range in the registry.

If **ScsiPortValidateRange** returns **TRUE**, *HwScsiFindAdapter* can safely do the following:

1.  Map the bus-relative range addresses to system-space logical range addresses with **ScsiPortGetDeviceBase**.

2.  Use the mapped logical addresses with the **ScsiPortRead/Write***Xxx* to determine whether the adapter actually is an HBA that the driver supports.

If a miniport driver uses a range successfully passed to **ScsiPortValidateRange** for an HBA it supports, that driver must invert the *InIoSpace* value when it sets the **RangeInMemory** member of an **AccessRanges** element in the PORT\_CONFIGURATION\_INFORMATION.

**ScsiPortValidateRange** uses **SCSI\_PHYSICAL\_ADDRESS** to represent bus-relative addresses.


```C++
typedef PHYSICAL_ADDRESS SCSI_PHYSICAL_ADDRESS, *PSCSI_PHYSICAL_ADDRESS;
```



The **SCSI\_PHYSICAL\_ADDRESS** type is an operating system-independent data type that SCSI miniport drivers use to represent either a physical addresses or a bus-relative address.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**ACCESS\_RANGE**](access-range.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortValidateRange%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






