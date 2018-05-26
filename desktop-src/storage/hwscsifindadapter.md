---
title: PHW\_FIND\_ADAPTER routine
description: HwScsiFindAdapter uses supplied configuration information to determine whether it supports a particular HBA and, if so, returns information about its HBA in the given ConfigInfo buffer.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 794710ef-f90f-4759-a379-542bd7fcfb03
keywords:
- HwScsiFindAdapter routine Storage Devices
- PHW_FIND_ADAPTER
topic_type:
- apiref
api_name:
- HwScsiFindAdapter
api_location:
- miniport.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PHW\_FIND\_ADAPTER routine

*HwScsiFindAdapter* uses supplied configuration information to determine whether it supports a particular HBA and, if so, returns information about its HBA in the given *ConfigInfo* buffer.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PHW_FIND_ADAPTER HwScsiFindAdapter;

ULONG HwScsiFindAdapter(
  _In_    PVOID                           DeviceExtension,
  _In_    PVOID                           HwContext,
  _In_    PVOID                           BusInformation,
  _In_    PCHAR                           ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
  _Out_   PBOOLEAN                        Again
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area. The operating system-specific port driver allocates memory for and initializes this extension with zeros before it calls the miniport driver's *HwScsiFindAdapter* routine.

</dd> <dt>

*HwContext* \[in\]
</dt> <dd>

Points to a context value.

Legacy (non-PnP) miniport drivers that scan for supported adapters can define the context in their [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine and pass its address to [**ScsiPortInitialize**](scsiportinitialize.md). **ScsiPortInitialize** passes the context pointer to *HwScsiFindAdapter*. Such a miniport driver can use *HwContext* to store state between calls to *HwScsiFindAdapter*.

Miniport drivers that use configuration information provided by the port driver, rather than by scanning the I/O bus, must not use this pointer. Even if the miniport driver does scan the I/O bus for other configuration information, if *HwScsiFindAdapter* receives nonzero access range values from the port driver it must not use the *HwContext* pointer.

</dd> <dt>

*BusInformation* \[in\]
</dt> <dd>

Points to bus-type-specific information that the operating system-specific port driver has gathered. The format of this information depends on the particular bus type, which the miniport driver determines by setting the **AdapterInterfaceType** value in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--scsi-.md) structure. This parameter is meaningful only for legacy (non-PnP) miniport drivers.

</dd> <dt>

*ArgumentString* \[in\]
</dt> <dd>

Points to a null-terminated ASCII string. This string originates from the user and, if supplied, contains device information such as a base parameter or an interrupt level from the registry.

</dd> <dt>

*ConfigInfo* \[in, out\]
</dt> <dd>

Points to the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md) structure. The operating system-specific port driver initializes this structure with any known configuration information, such as values the miniport driver set in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--scsi-.md) and the **SystemIoBusNumber**. *HwScsiFindAdapter* must use any supplied information to determine if the HBA it describes is one that the miniport driver supports, and, if so, to initialize and configure that HBA and to fill in any missing relevant configuration information for that HBA. If possible, each miniport driver should have a set of default configuration values for each type of HBA it supports, in case the operating system-dependent port driver cannot supply additional configuration information to that provided by the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

</dd> <dt>

*Again* \[out\]
</dt> <dd>

Points to a BOOLEAN variable to be set by *HwScsiFindAdapter* before it returns control. **TRUE** indicates that the miniport driver wants the operating system-specific port driver to call its *HwScsiFindAdapter* routine again with a new *DeviceExtension* and the same *ConfigInfo*. This member is set to **TRUE** by miniport drivers that can support more than one HBA on an I/O bus. This parameter is meaningful only for legacy (non-PnP) miniport drivers.

</dd> </dl>

## Return value

*HwScsiFindAdapter* must return one of the following status values:



| Return code                                                                                            | Description                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SP\_RETURN\_FOUND**</dt> </dl>       | Indicates a supported HBA was found and that the HBA-relevant configuration information was successfully determined and set in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md) structure.<br/> |
| <dl> <dt>**SP\_RETURN\_ERROR**</dt> </dl>       | Indicates an HBA was found but there was error obtaining the configuration information. If possible, such an error should be logged with [**ScsiPortLogError**](scsiportlogerror.md).<br/>                                          |
| <dl> <dt>**SP\_RETURN\_BAD\_CONFIG**</dt> </dl> | Indicates the supplied configuration information was invalid for the adapter.<br/>                                                                                                                                                   |
| <dl> <dt>**SP\_RETURN\_NOT\_FOUND**</dt> </dl>  | Indicates no supported HBA was found for the supplied configuration information.<br/>                                                                                                                                                |



 

## Remarks

For a legacy miniport driver, [**ScsiPortInitialize**](scsiportinitialize.md) calls the *HwScsiFindAdapter* routine after allocating storage according to the **DeviceExtensionSize** that the miniport driver specified in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--scsi-.md) structure. For a Plug and Play miniport driver, the port driver calls *HwScsiFindAdapter* when the Plug and Play manager has detected an adapter for that miniport driver.

First, every *HwScsiFindAdapter* routine should check the value of **Length** in the input [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md) to determine whether the port driver has allocated a structure with all the configuration information the miniport driver would need to find and configure its HBA(s).

Next, every *HwScsiFindAdapter* routine should check the **AccessRanges** in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md) to determine whether the operating system-specific port driver collected and set bus-relative range-configuration information for an HBA. If *HwScsiFindAdapter* finds nonzero access-range values, it must map the supplied values with [**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md) and use the returned logical range addresses to access the HBA.

If the input [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md) contains **AccessRanges** elements filled with default zeros, the *HwScsiFindAdapter* routine can use any appropriate search logic, such as calling [**ScsiPortGetBusData**](scsiportgetbusdata.md), or use a set of driver-supplied bus-relative default values, to fill in each such access range element and determine its validity.

*HwScsiFindAdapter* should call [**ScsiPortValidateRange**](scsiportvalidaterange.md) before it maps any miniport driver-supplied access range values with [**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md) and uses the mapped logical addresses to access an adapter. **ScsiPortValidateRange** verifies that the device range has not already been claimed by another driver. If **ScsiPortValidateRange** returns **FALSE**, *HwScsiFindAdapter* cannot map and use that range and must not attempt to do so.

*HwScsiFindAdapter* must check the value of **NumberOfPhysicalBreaks** in the input [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md). The port driver usually sets this member to a particular value. The miniport driver can set **NumberOfPhysicalBreaks** to a lower value if its HBA supports fewer breaks between scatter/gather lists, but the miniport driver must not set it to a higher value than that supplied by the port driver. If **NumberOfPhysicalBreaks** is set to SP\_UNINITIALIZED\_VALUE, the miniport driver must fill in the actual number of breaks between scatter/gather lists that its underlying adapter can support.

*HwScsiFindAdapter* should also check the input port configuration information for additional port-driver-supplied values, such as interrupt vector or level, and DMA channel or port. Usually, the operating system-specific port driver supplies additional configuration information if it supplies nonzero, bus-relative values for **AccessRanges** elements.

A miniport driver must use any valid configuration information it finds in the input [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md) to configure the HBA.

The port driver is responsible for doing bus-level configuration programming, particularly of dynamically configurable I/O buses with published standard interfaces, such as PCI and PCMCIA. For an HBA on such an I/O bus, the miniport driver can simply accept the interrupt configuration information provided as values reserved for system use. For an HBA on other types of I/O buses, a miniport driver should program its HBA to use any supplied interrupt value if its HBA supports programmable interrupt configuration. If no interrupt configuration is supplied, as indicated either by the value zero or the value SP\_UNINITIALIZED\_VALUE, the miniport driver should either query its HBA if the HBA supports interrupt selection using jumpers or should supply a nonzero default interrupt configuration unless the HBA does not use interrupts. The miniport driver should set the interrupt configuration value to zero if it controls its HBA in a polled mode.

A miniport driver's *HwScsiFindAdapter* routine should return with the *Again* parameter set to **TRUE** so the operating system-specific SCSI port driver will search for additional HBAs on the I/O bus. Although *Again* is irrelevant when a miniport driver is loaded as a Plug and Play driver, *Again* must be set appropriately so the system can run a Plug and Play miniport driver as a legacy driver if necessary.

The name *HwScsiFindAdapter* is just a placeholder. The actual prototype of this routine is defined in srb.h as follows:


```
typedef
ULONG
(*PHW_FIND_ADAPTER) (
  IN PVOID  DeviceExtension,
  IN PVOID  HwContext,
  IN PVOID  BusInformation,
  IN PCHAR  ArgumentString,
  IN OUT PPORT_CONFIGURATION_INFORMATION  ConfigInfo,
  OUT PBOOLEAN Again
  );
```



For more information about the *HwScsiFindAdapter* routine, see [SCSI Miniport Driver's HwScsiFindAdapter Routine](https://msdn.microsoft.com/library/windows/hardware/ff565326).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ACCESS\_RANGE**](access-range.md)
</dt> <dt>

[**DriverEntry**](driverentry-of-scsi-miniport-driver.md)
</dt> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--scsi-.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--scsi-.md)
</dt> <dt>

[**ScsiPortGetBusData**](scsiportgetbusdata.md)
</dt> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> <dt>

[**ScsiPortLogError**](scsiportlogerror.md)
</dt> <dt>

[**ScsiPortValidateRange**](scsiportvalidaterange.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_FIND_ADAPTER%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






