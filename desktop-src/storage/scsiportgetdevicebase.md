---
title: ScsiPortGetDeviceBase routine
description: The ScsiPortGetDeviceBase routine returns a mapped, logical base address that can be used to communicate with an HBA.
ms.assetid: d8d14818-4b84-4c65-a29e-2cd97e8bfbe9
keywords:
- ScsiPortGetDeviceBase routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortGetDeviceBase
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

# ScsiPortGetDeviceBase routine

The **ScsiPortGetDeviceBase** routine returns a mapped, logical base address that can be used to communicate with an HBA. Every miniport driver must pass mapped, logical access range addresses to the **ScsiPort..Port***Xxx* and **ScsiPort..Register***Xxx* routines to communicate with its HBA(s).

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PVOID ScsiPortGetDeviceBase(
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

Specifies the interface type of the I/O bus on which the HBA is connected. The miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine obtains the value for this parameter from the **AdapterInterfaceType** member of the input PORT\_CONFIGURATION\_INFORMATION.

</dd> <dt>

*SystemIoBusNumber* \[in\]
</dt> <dd>

Specifies the system-assigned number of the I/O bus on which the HBA is connected. The *HwScsiFindAdapter* routine obtains the value for this parameter from the **SystemIoBusNumber** member of the input PORT\_CONFIGURATION\_INFORMATION.

</dd> <dt>

*IoAddress* \[in\]
</dt> <dd>

Specifies the bus-relative base address of a range used by the HBA. The *HwScsiFindAdapter* routine obtains the value for this parameter from one of the **AccessRanges** elements in the PORT\_CONFIGURATION\_INFORMATION if the port driver supplies range-configuration information. Otherwise, this address can be a value returned by **ScsiPortGetBusData** or a miniport driver-supplied default value. Avoid using a base address of zero because its successful return status can conflict with the error status (**NULL**).

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

Specifies the size in bytes of the range that the mapping should cover. The *HwScsiFindAdapter* routine obtains the value of this parameter from the same **AccessRanges** element as *IoAddress* if the port driver supplies range configuration information. Otherwise, this value can be returned by **ScsiPortGetBusData** or a miniport driver-supplied default. In any case, the driver must not access the hardware outside of the returned, mapped range.

</dd> <dt>

*InIoSpace* \[in\]
</dt> <dd>

**TRUE** indicates the range to be mapped is in I/O space, and the miniport driver will pass mapped addresses in this range to the **ScsiPort...Port***Xxx* to communicate with the HBA. The *HwScsiFindAdapter* routine obtains the value of this parameter from the same **AccessRanges** element as *IoAddress*. Note that a miniport driver *must invert* the value of the **InMemorySpace** member in an ACCESS\_RANGE-type element before it is passed to **ScsiPortGetDeviceBase** as the *InIoSpace* argument. **FALSE** indicates that the range to be mapped is in memory space.

</dd> </dl>

## Return value

**ScsiPortGetDeviceBase** returns a mapped logical base address for the given *IoAddress* if it successfully mapped the given range from *IoAddress* to *NumberOfBytes*. If a given range cannot be mapped, **ScsiPortGetDeviceBase** returns **NULL**.

## Remarks

NT-based operating system platforms can have several types of I/O buses and several I/O buses of the same type. Moreover, the HAL can map I/O space to memory in some platforms.

Consequently, a miniport driver cannot use bus-relative access range addresses to communicate with its HBA. To maintain miniport driver portability across CISC- and RISC-based machines, the addresses they use to access HBAs must be translated with **ScsiPortGetDeviceBase**.

Every miniport driver must use system-space logical range addresses, mapped by **ScsiPortGetDeviceBase**, to communicate with its HBA(s). Calls to the **ScsiPort...Port/Register***Xxx* routines require these mapped, logical addresses.

**ScsiPortGetDeviceBase** can be called several times, depending on how many HBAs the miniport driver supports and how many access ranges each HBA requires. Each mapped range corresponds to a range of bus-relative device addresses specified in an ACCESS\_RANGE-type element of the **AccessRanges** array.

**ScsiPortGetDeviceBase** can be called only from a miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine or from HwScsiAdapterControl when the control type is **ScsiSetRunningConfig**. Calls from other miniport driver routines will result in system failure or in incorrect operation for the caller.

Follow these guidelines for calling **ScsiPortGetDeviceBase**:

-   If *HwScsiFindAdapter* is using a miniport driver-supplied set of default bus-relative access ranges or values returned by **ScsiPortGetBusData**, it should call [**ScsiPortValidateRange**](scsiportvalidaterange.md) before attempting to call **ScsiPortGetDeviceBase**.

-   If *HwScsiFindAdapter* determines that a particular HBA is not one that the miniport driver supports, it must call **ScsiPortFreeDeviceBase** to release the mapping(s) it set up to communicate with that HBA.

The logical address returned by **ScsiPortGetDeviceBase** should be used for all subsequent references made to the hardware but should *not* be added to any **AccessRanges** specification in the PORT\_CONFIGURATION\_INFORMATION. Miniport driver writers should make no assumptions about how many bits are used in the logical base address returned by **ScsiPortGetDeviceBase**.

**ScsiPortGetDeviceBase** uses **SCSI\_PHYSICAL\_ADDRESS** to represent bus-relative addresses.


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

[**ScsiPortFreeDeviceBase**](scsiportfreedevicebase.md)
</dt> <dt>

[**ScsiPortGetBusData**](scsiportgetbusdata.md)
</dt> <dt>

[**ScsiPortValidateRange**](scsiportvalidaterange.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortGetDeviceBase%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






