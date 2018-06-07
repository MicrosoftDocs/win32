---
title: VIRTUAL\_HW\_INITIALIZATION\_DATA structure
description: The VIRTUAL\_HW\_INITIALIZATION\_DATA structure contains information particular to each virtual miniport driver.
ms.assetid: 10e7e097-ed84-4200-b7b6-6a838a058fd2
keywords:
- VIRTUAL_HW_INITIALIZATION_DATA structure Storage Devices
- PVIRTUAL_HW_INITIALIZATION_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- VIRTUAL_HW_INITIALIZATION_DATA
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# VIRTUAL\_HW\_INITIALIZATION\_DATA structure

The **VIRTUAL\_HW\_INITIALIZATION\_DATA** structure contains information particular to each virtual miniport driver.

## Syntax


```C++
typedef struct _VIRTUAL_HW_INITIALIZATION_DATA {
  ULONG                       HwInitializationDataSize;
  INTERFACE_TYPE              AdapterInterfaceType;
  PHW_INITIALIZE              HwInitialize;
  PHW_STARTIO                 HwStartIo;
  PHW_INTERRUPT               HwInterrupt;
  PVIRTUAL_HW_FIND_ADAPTER    HwFindAdapter;
  PHW_RESET_BUS               HwResetBus;
  PHW_DMA_STARTED             HwDmaStarted;
  PHW_ADAPTER_STATE           HwAdapterState;
  ULONG                       DeviceExtensionSize;
  ULONG                       SpecificLuExtensionSize;
  ULONG                       SrbExtensionSize;
  ULONG                       NumberOfAccessRanges;
  PVOID                       Reserved;
  UCHAR                       MapBuffers;
  BOOLEAN                     NeedPhysicalAddresses;
  BOOLEAN                     TaggedQueuing;
  BOOLEAN                     AutoRequestSense;
  BOOLEAN                     MultipleRequestPerLu;
  BOOLEAN                     ReceiveEvent;
  USHORT                      VendorIdLength;
  PVOID                       VendorId;
  union {
    USHORT ReservedUshort;
    USHORT PortVersionFlags;
  };
  USHORT                      DeviceIdLength;
  PVOID                       DeviceId;
  PHW_ADAPTER_CONTROL         HwAdapterControl;
  PHW_BUILDIO                 HwBuildIo;
  PHW_FREE_ADAPTER_RESOURCES  HwFreeAdapterResources;
  PHW_PROCESS_SERVICE_REQUEST HwProcessServiceRequest;
  PHW_COMPLETE_SERVICE_IRP    HwCompleteServiceIrp;
  PHW_INITIALIZE_TRACING      HwInitializeTracing;
  PHW_CLEANUP_TRACING         HwCleanupTracing;
} VIRTUAL_HW_INITIALIZATION_DATA, *PVIRTUAL_HW_INITIALIZATION_DATA;
```



## Members

<dl> <dt>

**HwInitializationDataSize**
</dt> <dd>

Specifies the size of this structure in bytes, as returned by **sizeof**(). This member indicates the version of this structure that is used by the virtual miniport driver. A virtual miniport driver's **DriverEntry** routine should set this member's value for the port driver.

</dd> <dt>

**AdapterInterfaceType**
</dt> <dd>

The Storport driver does not support legacy buses. Therefore, most of the adapter interface types that are used with the SCSI port driver are invalid for Storport drivers. In particular, Storport does not support Isa, Eisa, MicroChannel, and TurboChannel. Furthermore, unlike the SCSI port case, a virtual miniport driver that works with the Storport driver is not required to supply values for the **VendorIdLength**, **VendorId**, **DeviceIdLength**, and **DeviceId** members.

</dd> <dt>

**HwInitialize**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorInitialize**](hwstorinitialize.md) routine, which is a required entry point for all virtual miniport drivers.

</dd> <dt>

**HwStartIo**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorStartIo**](hwstorstartio.md) routine, which is a required entry point for all virtual miniport drivers.

</dd> <dt>

**HwInterrupt**
</dt> <dd>

Not used. Virtual miniport drivers do not process interrupts.

</dd> <dt>

**HwFindAdapter**
</dt> <dd>

A pointer to the virtual miniport driver's [**VirtualHwStorFindAdapter**](virtualhwstorfindadapter.md) routine, which is a required entry point for all virtual miniport drivers.

</dd> <dt>

**HwResetBus**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorResetBus**](hwstorresetbus.md) routine, which is a required entry point for all virtual miniport drivers.

</dd> <dt>

**HwDmaStarted**
</dt> <dd>

Not used. Virtual miniport drivers do not perform DMA.

</dd> <dt>

**HwAdapterState**
</dt> <dd>

The Storport driver does not support legacy drivers. Therefore, this member must be **NULL**.

</dd> <dt>

**DeviceExtensionSize**
</dt> <dd>

Specifies the size, in bytes, that is required by the virtual miniport driver for its per-adapter non-paged device extension. A virtual miniport driver uses its device extension as storage for driver-determined adapter information. The operating system-specific port driver initializes each device extension that it allocates with zeros, and passes a pointer to the adapter-specific device extension in most calls to the virtual miniport driver. The given size does not include any virtual miniport driver-requested per-logical-unit storage.

</dd> <dt>

**SpecificLuExtensionSize**
</dt> <dd>

Specifies the size, in bytes, that is required by the virtual miniport driver for its per-logical-unit non-paged storage, if any. A virtual miniport driver can use its logical unit (LU) extensions as storage for driver-determined LU information about peripherals on the virtual bus. The operating system-specific port driver initializes each LU extension that it allocates with zeros. Leave this member set to zero if the virtual miniport driver does not maintain per-LU information for which it requires storage.

</dd> <dt>

**SrbExtensionSize**
</dt> <dd>

Specifies the size, in bytes, that is required by the virtual miniport driver for its per-request non-paged storage, if any. Because virtual miniport drivers that work with the Storport driver must support scatter/gather lists, and the per-SRB scatter/gather lists are usually allocated in the SRB extension, this member is rarely zero.

</dd> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Not used. Virtual miniport drivers do not support hardware.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**MapBuffers**
</dt> <dd>

Not valid for virtual miniport drivers. The virtual miniport driver must map all data buffers into virtual address space.

</dd> <dt>

**NeedPhysicalAddresses**
</dt> <dd>

Not used. Virtual miniport drivers do not support hardware.

</dd> <dt>

**TaggedQueuing**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the virtual miniport driver supports tagged queuing.

</dd> <dt>

**AutoRequestSense**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the HBA can perform a request-sense operation without requiring an explicit request to do so.

</dd> <dt>

**MultipleRequestPerLu**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the virtual miniport driver can queue multiple requests per logical unit (LU).

</dd> <dt>

**ReceiveEvent**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the virtual miniport driver supports receive events.

</dd> <dt>

**VendorIdLength**
</dt> <dd>

The length, in bytes, of the vendor identifier.

</dd> <dt>

**VendorId**
</dt> <dd>

The vendor identifier.

</dd> <dt>

**ReservedUshort**
</dt> <dd>

Reserved.

</dd> <dt>

**PortVersionFlags**
</dt> <dd>

A bitmap of flags that indicate the features that the port driver supports. Currently, the only flag available is SP\_VER\_TRACE\_SUPPORT, which indicates that the port driver supports tracing.

</dd> <dt>

**DeviceIdLength**
</dt> <dd>

The length, in bytes, of the device identifier.

</dd> <dt>

**DeviceId**
</dt> <dd>

The device identifier.

</dd> <dt>

**HwAdapterControl**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorAdapterControl**](hwstoradaptercontrol.md) routine.

</dd> <dt>

**HwBuildIo**
</dt> <dd>

This member is not used.

</dd> <dt>

**HwFreeAdapterResources**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorFreeAdapterResources**](hwstorfreeadapterresources.md) routine, which is a required entry point for all virtual miniport drivers.

</dd> <dt>

**HwProcessServiceRequest**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorProcessServiceRequest**](hwstorprocessservicerequest.md) routine.

</dd> <dt>

**HwCompleteServiceIrp**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorCompleteServiceIrp**](hwstorcompleteserviceirp.md) routine.

</dd> <dt>

**HwInitializeTracing**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorInitializeTracing**](hwstorinitializetracing.md) routine.

</dd> <dt>

**HwCleanupTracing**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorCleanupTracing**](hwstorcleanuptracing.md) routine.

</dd> </dl>

## Remarks

If a virtual miniport driver will execute only on Windows 8 or later, the driver should use the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure instead of **VIRTUAL\_HW\_INITIALIZATION\_DATA**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> <dt>

[**HwStorCleanupTracing**](hwstorcleanuptracing.md)
</dt> <dt>

[**HwStorCompleteServiceIrp**](hwstorcompleteserviceirp.md)
</dt> <dt>

[**HwStorFreeAdapterResources**](hwstorfreeadapterresources.md)
</dt> <dt>

[**HwStorInitialize**](hwstorinitialize.md)
</dt> <dt>

[**HwStorInitializeTracing**](hwstorinitializetracing.md)
</dt> <dt>

[**HwStorProcessServiceRequest**](hwstorprocessservicerequest.md)
</dt> <dt>

[**HwStorResetBus**](hwstorresetbus.md)
</dt> <dt>

[**HwStorStartIo**](hwstorstartio.md)
</dt> <dt>

[**VirtualHwStorFindAdapter**](virtualhwstorfindadapter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VIRTUAL_HW_INITIALIZATION_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






