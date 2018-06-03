---
title: '\_HW\_INITIALIZATION\_DATA structure'
description: Each SCSI miniport driver's DriverEntry routine must initialize with zeros and, then, fill in the relevant HW\_INITIALIZATION\_DATA (SCSI) information for the OS-specific port driver.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 58c80d37-a40d-4839-b516-a78720860cbc
keywords:
- _HW_INITIALIZATION_DATA structure Storage Devices
- HW_INITIALIZATION_DATA structure Storage Devices
- PHW_INITIALIZATION_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HW_INITIALIZATION_DATA
api_location:
- srb.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# \_HW\_INITIALIZATION\_DATA structure

Each SCSI miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine must initialize with zeros and, then, fill in the relevant HW\_INITIALIZATION\_DATA (SCSI) information for the OS-specific port driver.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _HW_INITIALIZATION_DATA {
  ULONG             HwInitializationDataSize;
  INTERFACE_TYPE    AdapterInterfaceType;
  PHW_INITIALIZE    HwInitialize;
  PHW_STARTIO       HwStartIo;
  PHW_INTERRUPT     HwInterrupt;
  PHW_FIND_ADAPTER  HwFindAdapter;
  PHW_RESET_BUS_BUS HwResetBus;
  PHW_DMA_STARTED   HwDmaStarted;
  PHW_ADAPTER_STATE HwAdapterState;
  ULONG             DeviceExtensionSize;
  ULONG             SpecificLuExtensionSize;
  ULONG             SrbExtensionSize;
  ULONG             NumberOfAccessRanges;
  PVOID             Reserved;
  BOOLEAN           MapBuffers;
  BOOLEAN           NeedPhysicalAddresses;
  BOOLEAN           TaggedQueuing;
  BOOLEAN           AutoRequestSense;
  BOOLEAN           MultipleRequestPerLu;
  BOOLEAN           ReceiveEvent;
  USHORT            VendorIdLength;
  PVOID             VendorId;
  USHORT            ReservedUshort;
  USHORT            DeviceIdLength;
  PVOID             DeviceId;
  PHW_STOP_ADAPTER  HwAdapterControl;
} HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA;
```



## Members

<dl> <dt>

**HwInitializationDataSize**
</dt> <dd>

Specifies the size of this structure in bytes, as returned by **sizeof**(). In effect, this member indicates the version of this structure being used by the miniport driver. A miniport driver's **DriverEntry** routine should set this member's value for the port driver.

</dd> <dt>

**AdapterInterfaceType**
</dt> <dd>

Specifies the type of I/O bus to which the HBA is connected, which can be one of the following: **Internal**, **Isa**, **Eisa**, **MicroChannel**, **TurboChannel**, or **PCIBus**. However, additional types of buses will be supported in future. The upper bound on the types of buses supported is always **MaximumInterfaceType**.

<dl> <dd>

If this is set to **PCIBus**, the miniport driver must supply values for the **VendorIdLength**, **VendorId**, **DeviceIdLength**, and **DeviceId** members, described later.

</dd> </dl> </dd> <dt>

**HwInitialize**
</dt> <dd>

Pointer to the miniport driver's [*HwScsiInitialize*](hwscsiinitialize.md) routine, which is a required entry point for all miniport drivers. The prototype for this routine is [**PHW\_INITIALIZE**](phw-initialize.md).

</dd> <dt>

**HwStartIo**
</dt> <dd>

Pointer to the miniport driver's [**HwScsiStartIo**](hwscsistartio.md) routine, which is a required entry point for all miniport drivers. The prototype for this routine is [**PHW\_STARTIO**](phw-startio.md).

</dd> <dt>

**HwInterrupt**
</dt> <dd>

Pointer to the miniport driver's [**HwScsiInterrupt**](hwscsiinterrupt.md) routine, which is a required entry point for any miniport driver of an HBA that generates interrupts. Set this to **NULL** if the miniport driver needs no ISR. The prototype for this routine is [**PHW\_INTERRUPT**](phw-interrupt.md).

</dd> <dt>

**HwFindAdapter**
</dt> <dd>

Pointer to the miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine, which is a required entry point for all miniport drivers. The prototype for this routine is [**PHW\_FIND\_ADAPTER**](phw-find-adapter.md).

</dd> <dt>

**HwResetBus**
</dt> <dd>

Pointer to the miniport driver's [*HwScsiResetBus*](hwscsiresetbus.md) routine, which is a required entry point for all miniport drivers. The prototype for this routine is [**PHW\_RESET\_BUS**](phw-reset-bus.md).

</dd> <dt>

**HwDmaStarted**
</dt> <dd>

Pointer to the miniport driver's [**HwScsiDmaStarted**](hwscsidmastarted.md) routine if its HBA uses system DMA, that is, a system DMA controller. Set this to **NULL** if the HBA is a bus master or uses PIO. The prototype for this routine is [**PHW\_DMA\_STARTED**](phw-dma-started.md).

</dd> <dt>

**HwAdapterState**
</dt> <dd>

Pointer to the miniport driver's [**HwScsiAdapterState**](hwscsiadapterstate.md) routine, which is a required entry point for miniport drivers of HBAs with BIOSs that are linked with an operating system-dependent, x86-platform-only port driver that must switch between x86 protected and real processor modes. If the miniport driver needs no *HwScsiAdapterState* routine, set this member to **NULL**. A miniport driver for an HBA that has a BIOS must have a HwScsiAdapterState routine in order to be compatible with the x86-only port driver and portable to an x86-only operating system environment. The prototype for this routine is [**PHW\_ADAPTER\_STATE**](phw-adapter-state.md).

</dd> <dt>

**DeviceExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-HBA device extension. A miniport driver uses its device extension as storage for driver-determined HBA information. The OS-specific port driver initializes each device extension it allocates with zeros, and passes a pointer to the HBA-specific device extension in every call to a miniport driver except to its **DriverEntry** routine. The given size does not include any miniport driver-requested per-logical-unit storage, described next.

</dd> <dt>

**SpecificLuExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-logical-unit storage, if any. A miniport driver can use its LU extensions as storage for driver-determined logical-unit information about SCSI peripherals on the bus. The OS-specific port driver initializes each LU extension it allocates with zeros. Leave this member set to zero if the miniport driver does not maintain per-LU information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as [**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md).

</dd> <dt>

**SrbExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-request storage, if any. A miniport driver can use SRB extensions as storage for driver-determined, request-specific information, such as data necessary to process a particular request. The OS-specific port driver does not initialize SRB extensions, but sets a pointer to this storage in each SRB it sends to the miniport driver. An SRB extension can be safely accessed by the HBA hardware. Leave this member set to zero if the miniport driver does not maintain per-SRB information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as [**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md).

</dd> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Specifies how many access ranges the adapter uses. Each is a range either of memory addresses or I/O port addresses. A typical HBA uses two ranges, one for its I/O ports and another for its device memory range.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**MapBuffers**
</dt> <dd>

Indicates, when **TRUE**, that all data buffer addresses must be mapped to virtual addresses for access by the miniport driver. When **FALSE**, data buffer addresses do not have to be mapped to virtual addresses.

</dd> <dt>

**NeedPhysicalAddresses**
</dt> <dd>

Indicates, when **TRUE**, that the miniport driver needs to translate its device, any per-LU, and any per-SRB extension addresses, as well as SRB buffer addresses, to physical addresses, as required by the HBA. When **FALSE**, none of these addresses have to be translated to physical addresses.

</dd> <dt>

**TaggedQueuing**
</dt> <dd>

Indicates, when **TRUE**, that miniport driver can support SCSI tagged queuing. When **FALSE**, the miniport driver cannot support SCSI-tagged queuing.

</dd> <dt>

**AutoRequestSense**
</dt> <dd>

Indicates, when **TRUE**, that the HBA can perform a request-sense operation without requiring an explicit request to do so. When **FALSE**, the HBA requires an explicit request before it can perform a request-sense operation. Only miniport drivers driving HBAs with built-in firmware to perform request-sense operations should set this member to **TRUE**.

</dd> <dt>

**MultipleRequestPerLu**
</dt> <dd>

Indicates, when **TRUE**, that the miniport driver can queue multiple requests per logical unit, in particular, within the HBA. When **FALSE**, the miniport driver cannot queue multiple requests per logical unit. Note that an HBA must support auto request sense for its miniport driver to enable this functionality. If a miniport driver sets this member to **TRUE**, it must use each SRB **QueueTag** member for requests of this type, but the SRB\_FLAGS\_QUEUE\_ACTION\_ENABLE is not set in the **SrbFlags** member of the SCSI\_REQUEST\_BLOCK structure.

</dd> <dt>

**ReceiveEvent**
</dt> <dd>

Indicates, when **TRUE**, that the miniport driver drives an HBA that can support the receive-event SRB for SCSI asynchronous events. When **FALSE**, the HBA cannot support the receive-event SRB for SCSI asynchronous events.

</dd> <dt>

**VendorIdLength**
</dt> <dd>

Specifies the size in bytes of the **VendorId** string, described next.

</dd> <dt>

**VendorId**
</dt> <dd>

Pointer to an ASCII byte string identifying the manufacturer of the HBA. This member is irrelevant for Plug and Play drivers.

<dl> <dd>

If the given **AdapterInterfaceType** is **PCIBus**, the vendor ID is a USHORT value allocated by the PCI SIG, which must be converted into a byte string by the miniport driver. For example, if the assigned PCI vendor ID value is 1001, the miniport driver-supplied **VendorId** string would be ('1', '0', '0', '1').

</dd> </dl> </dd> <dt>

**ReservedUshort**
</dt> <dd>

Reserved for system use and is not available for use by miniport drivers.

</dd> <dt>

**DeviceIdLength**
</dt> <dd>

Specifies the size in bytes of the **DeviceId** string, described next.

</dd> <dt>

**DeviceId**
</dt> <dd>

Pointer to an ASCII byte string identifying the HBA model(s) supported by the miniport driver. This member is irrelevant for Plug and Play drivers.

<dl> <dd>

If the given **AdapterInterfaceType** is **PCIBus**, a device ID is a USHORT value assigned by the manufacturer of the HBA. The miniport driver must convert any PCI device ID value(s) for the HBA(s) it can support into **DeviceId** byte string(s), as for the **VendorId** member. For example, if a miniport driver can support HBAs with the PCI device IDs 8040 and 8050, it might set **DeviceId** with a pointer to the byte string ('8', '0').

</dd> </dl> </dd> <dt>

**HwAdapterControl**
</dt> <dd>

Pointer to the miniport driver's [**HwScsiAdapterControl**](hwscsiadaptercontrol.md) routine, which is a required entry point for all PnP miniport drivers. Set this to **NULL** if the miniport driver does not support Plug and Play.

</dd> </dl>

## Remarks

Each miniport driver must initialize the HW\_INITIALIZATION\_DATA structure with zeros before it sets the values of relevant members in this structure and calls **ScsiPortInitialize**.

The **Dma64BitAddresses** member of HW\_INITIALIZATION\_DATA has been eliminated in Windows 2000 (See the discussion under PORT\_CONFIGURATION\_DATA for further details).

Both HW\_INITIALIZATION\_DATA and PORT\_CONFIGURATION\_INFORMATION have a pair of members called **SpecificLuExtensionSize** and **SrbExtensionSize** whose values are handled differently than they were prior to Windows 2000. The miniport driver must calculate the initial values of **SpecificLuExtensionSize** and **SrbExtensionSize** in HW\_INITIALIZATION\_DATA based on the assumption that the HBA is capable of handling 32-bit addresses, regardless of what the controller can actually support. (See the discussion under PORT\_CONFIGURATION\_DATA for further details.)

## Requirements



|                   |                                                                                                               |
|-------------------|---------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Srb.h (include Srb.h or Strmini.h)</dt> </dl> |



## See also

<dl> <dt>

[**DriverEntry of SCSI Miniport Driver**](driverentry-of-scsi-miniport-driver.md)
</dt> <dt>

[*HwScsiInitialize*](hwscsiinitialize.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_HW_INITIALIZATION_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






