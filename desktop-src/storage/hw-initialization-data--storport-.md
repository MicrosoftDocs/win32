---
title: '\_HW\_INITIALIZATION\_DATA structure'
description: The HW\_INITIALIZATION\_DATA (Storport) structure contains information particular to each miniport driver and the hardware that the miniport driver manages.
ms.assetid: 54f460da-2dfb-4a9d-9b25-edb90f3bfdd5
keywords:
- _HW_INITIALIZATION_DATA structure Storage Devices
- HW_INITIALIZATION_DATA structure Storage Devices
- PHW_INITIALIZATION_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HW_INITIALIZATION_DATA
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# \_HW\_INITIALIZATION\_DATA structure

The **HW\_INITIALIZATION\_DATA (Storport)** structure contains information particular to each miniport driver and the hardware that the miniport driver manages.

## Syntax


```C++
typedef struct _HW_INITIALIZATION_DATA {
  ULONG                       HwInitializationDataSize;
  INTERFACE_TYPE              AdapterInterfaceType;
  PHW_INITIALIZE              HwInitialize;
  PHW_STARTIO                 HwStartIo;
  PHW_INTERRUPT               HwInterrupt;
  PHW_FIND_ADAPTER            HwFindAdapter;
  PHW_RESET_BUS               HwResetBus;
  PHW_DMA_STARTED             HwDmaStarted;
  PHW_ADAPTER_STATE           HwAdapterState;
  ULONG                       DeviceExtensionSize;
  ULONG                       SpecificLuExtensionSize;
  ULONG                       SrbExtensionSize;
  ULONG                       NumberOfAccessRanges;
  PVOID                       Reserved;
  BOOLEAN                     MapBuffers;
  BOOLEAN                     NeedPhysicalAddresses;
  BOOLEAN                     TaggedQueuing;
  BOOLEAN                     AutoRequestSense;
  BOOLEAN                     MultipleRequestPerLu;
  BOOLEAN                     ReceiveEvent;
  USHORT                      VendorIdLength;
  PVOID                       VendorId;
  USHORT                      PortVersionFlags;
  USHORT                      DeviceIdLength;
  PVOID                       DeviceId;
  PHW_STOP_ADAPTER            HwAdapterControl;
  PHW_BUILDIO                 HwBuildIo;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  PHW_FREE_ADAPTER_RESOURCES  HwFreeAdapterResources;
  PHW_PROCESS_SERVICE_REQUEST HwProcessServiceRequest;
  PHW_COMPLETE_SERVICE_IRP    HwCompleteServiceIrp;
  PHW_INITIALIZE_TRACING      HwInitializeTracing;
  PHW_CLEANUP_TRACING         HwCleanupTracing;
  PHW_TRACING_ENABLED         HwTracingEnabled;
  ULONG                       FeatureSupport;
  ULONG                       SrbTypeFlags;
  ULONG                       AddressTypeFlags;
  ULONG                       Reserved1;
  PHW_UNIT_CONTROL            HwUnitControl;
#endif 
} HW_INITIALIZATION_DATA, *PHW_INITIALIZATION_DATA;
```



## Members

<dl> <dt>

**HwInitializationDataSize**
</dt> <dd>

Specifies the size of this structure in bytes, as returned by **sizeof**(HW\_INITIALIZATION\_DATA). In effect, this member indicates the version of this structure being used by the miniport driver. A miniport driver's DriverEntry routine should set this member's value for the port driver.

</dd> <dt>

**AdapterInterfaceType**
</dt> <dd>

The Storport driver does not support legacy buses. Therefore, most of the adapter interface types used with the SCSI Port driver are invalid for Storport. In particular, **Isa**, **Eisa**, **MicroChannel**, and **TurboChannel** are not supported. Furthermore, unlike the SCSI Port case, a miniport driver that works with the Storport driver is not required to supply values for the **VendorIdLength**, **VendorId**, **DeviceIdLength**, and **DeviceId** members.

</dd> <dt>

**HwInitialize**
</dt> <dd>

Pointer to the miniport driver's [**HwStorInitialize**](hwstorinitialize.md) routine, which is a required entry point for all miniport drivers.

</dd> <dt>

**HwStartIo**
</dt> <dd>

Pointer to the miniport driver's [**HwStorStartIo**](hwstorstartio.md) routine, which is a required entry point for all miniport drivers.

</dd> <dt>

**HwInterrupt**
</dt> <dd>

Pointer to the miniport driver's [**HwStorInterrupt**](hwstorinterrupt.md) routine, which is a required entry point for all miniport drivers.

</dd> <dt>

**HwFindAdapter**
</dt> <dd>

Pointer to the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine, which is a required entry point for all miniport drivers.

</dd> <dt>

**HwResetBus**
</dt> <dd>

Pointer to the miniport driver's [**HwStorResetBus**](hwstorresetbus.md) routine, which is a required entry point for all miniport drivers.

</dd> <dt>

**HwDmaStarted**
</dt> <dd>

The Storport driver does not support subordinate-mode DMA. Therefore, this member must be **NULL**.

</dd> <dt>

**HwAdapterState**
</dt> <dd>

The Storport driver does not support legacy drivers. Therefore, this member must be **NULL**.

</dd> <dt>

**DeviceExtensionSize**
</dt> <dd>

Specifies the size, in bytes, required by the miniport driver for its per-adapter device extension. A miniport driver uses its device extension as storage for driver-determined host bus adapter (HBA) information. The operating system-specific port driver initializes each device extension one time, when it first allocates the extension and fills it with zeros. It passes a pointer to the HBA-specific device extension in every call to a miniport driver. The given size does not include any miniport driver-requested per-logical-unit storage. The size of per-logical-unit storage is specified via the **SpecificLuExtensionSize** field, described later in this topic.

Although SCSIPort re-initializes the device extension whenever the adapter is stopped and thus subsequent calls to [**HwScsiFindAdapter**](hwscsifindadapter.md) receive a zeroed-out device extension, Storport does not follow that model. Rather, Storport resets the device extension to zero only when it is first allocated, so only the first call to [**HwStorFindAdapter**](hwstorfindadapter.md) for a given adapter receives a zeroed-out device extension. Subsequent calls to **HwStorFindAdapter** and other miniport functions receive the device extension as last modified by the miniport. This allows the miniport driver to maintain knowledge about the state of the adapter between Plug and Play (PnP) stops and restarts, possibly enabling the miniport driver to optimize it's initialization procedure.

</dd> <dt>

**SpecificLuExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-logical-unit storage, if any. A miniport driver can use its LU extensions as storage for driver-determined logical-unit information about peripherals on the bus. The Storport driver initializes each LU extension it allocates with zeros. Leave this member set to zero if the miniport driver does not maintain per-LU information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as [**StorPortGetUncachedExtension**](storportgetuncachedextension.md).

</dd> <dt>

**SrbExtensionSize**
</dt> <dd>

Specifies the size, in bytes, required by the miniport driver for its per-request storage, if any. A miniport driver can use SRB extensions as storage for driver-determined, request-specific information, such as data necessary to process a particular request. The Storport driver does not initialize SRB extensions, but sets a pointer to this storage in each SRB it sends to the miniport driver. An SRB extension can be safely accessed by the HBA hardware. Because miniport drivers that work with the Storport driver must support scatter/gather lists, and the per-SRB scatter/gather lists are usually allocated in the SRB extension, this member is rarely zero. Leave this member set to zero if the miniport driver does not maintain per-SRB information for which it requires storage.

This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as [**StorPortGetUncachedExtension.**](storportgetuncachedextension.md).

</dd> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Specifies how many access ranges the adapter uses. Each is a range either of memory addresses or I/O port addresses.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**MapBuffers**
</dt> <dd>

Indicates whether the Storport driver maps SRB data buffer addresses to system virtual addresses. The **MapBuffers** member can have one of the following values.



| Value                                                                                                                                                                                                                                                  | Meaning                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="STOR_MAP_NO_BUFFERS"></span><span id="stor_map_no_buffers"></span><dl> <dt>**STOR\_MAP\_NO\_BUFFERS**</dt> </dl>                                                                      | Do not map for any SRB except SRB\_FUNCTION\_IO\_CONTROL and SRB\_FUNCTION\_WMI.<br/>                           |
| <span id="STOR_MAP_ALL_BUFFERS"></span><span id="stor_map_all_buffers"></span><dl> <dt>**STOR\_MAP\_ALL\_BUFFERS**</dt> </dl>                                                                   | Obsolete. This value has the same effect as STOR\_MAP\_NON\_READ\_WRITE\_BUFFERS.<br/>                          |
| <span id="STOR_MAP_NON_READ_WRITE_BUFFERS"></span><span id="stor_map_non_read_write_buffers"></span><dl> <dt>**STOR\_MAP\_NON\_READ\_WRITE\_BUFFERS**</dt> </dl>                                | Map the buffer for all I/O except for read or write requests.<br/>                                              |
| <span id="STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE"></span><span id="stor_map_all_buffers_including_read_write"></span><dl> <dt>**STOR\_MAP\_ALL\_BUFFERS\_INCLUDING\_READ\_WRITE**</dt> </dl> | Map the buffer for all I/O including read and write requests. This value is valid starting with Windows 8.<br/> |



 

</dd> <dt>

**NeedPhysicalAddresses**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the miniport driver must translate certain types of addresses to physical addresses. Miniport drivers that work with the Storport driver must support bus-master DMA, so they will always be required to do address translation.

</dd> <dt>

**TaggedQueuing**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the miniport driver supports SCSI tagged queuing. All miniport drivers that work with the Storport driver must support tagged queuing.

</dd> <dt>

**AutoRequestSense**
</dt> <dd>

Must be **TRUE**. A value of **TRUE** indicates that the HBA can perform a request-sense operation without requiring an explicit request to do so. All miniport drivers that work with the Storport driver must support SCSI Auto-Request Sense.

</dd> <dt>

**MultipleRequestPerLu**
</dt> <dd>

Must be set to **TRUE**. A value of **TRUE** indicates that the miniport driver can queue multiple requests per logical unit. Miniport drivers that work with the Storport driver must support multiple requests per logical unit.

</dd> <dt>

**ReceiveEvent**
</dt> <dd>

The Storport driver ignores this member.

</dd> <dt>

**VendorIdLength**
</dt> <dd>

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

</dd> <dt>

**VendorId**
</dt> <dd>

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

</dd> <dt>

**PortVersionFlags**
</dt> <dd>

Flags to indicate supported features.

</dd> <dt>

**DeviceIdLength**
</dt> <dd>

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

</dd> <dt>

**DeviceId**
</dt> <dd>

The Storport driver ignores this member, because miniport drivers that work with the Storport driver must support PnP.

</dd> <dt>

**HwAdapterControl**
</dt> <dd>

Pointer to the miniport driver's [**HwStorAdapterControl**](hwstoradaptercontrol.md) routine. This is a required routine because miniport drivers that work with the Storport driver require PnP support.

</dd> <dt>

**HwBuildIo**
</dt> <dd>

Pointer to an optional [**HwStorBuildIo**](hwstorbuildio.md) routine that the port driver calls to do unsynchronized processing prior to calling the miniport driver's [**HwStorStartIo**](hwstorstartio.md) routine.

</dd> <dt>

**HwFreeAdapterResources**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorFreeAdapterResources**](hwstorfreeadapterresources.md) routine, which is a required entry point for all virtual miniport drivers. This callback is specific to virtual miniports and is set to **NULL** by physical miniports.

This callback is added in Windows 8. Virtual miniports for previous versions of Windows should use [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md) instead of this structure.

</dd> <dt>

**HwProcessServiceRequest**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorProcessServiceRequest**](hwstorprocessservicerequest.md) routine. This callback is specific to virtual miniports and is set to **NULL** by physical miniports.

This callback is added in Windows 8. Virtual miniports for previous versions of Windows should use [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md) instead of this structure.

</dd> <dt>

**HwCompleteServiceIrp**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorCompleteServiceIrp**](hwstorcompleteserviceirp.md) routine. This callback is specific to virtual miniports and is set to **NULL** by physical miniports.

This callback is added in Windows 8. Virtual miniports for previous versions of Windows should use [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md) instead of this structure.

</dd> <dt>

**HwInitializeTracing**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorInitializeTracing**](hwstorinitializetracing.md) routine. This callback is specific to virtual miniports and is set to **NULL** by physical miniports.

This callback is added in Windows 8. Virtual miniports for previous versions of Windows should use [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md) instead of this structure.

</dd> <dt>

**HwCleanupTracing**
</dt> <dd>

A pointer to the virtual miniport driver's [**HwStorCleanupTracing**](hwstorcleanuptracing.md) routine. This callback is specific to virtual miniports and is set to **NULL** by physical miniports.

This callback is added in Windows 8. Virtual miniports for previous versions of Windows should use [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md) instead of this structure.

</dd> <dt>

**HwTracingEnabled**
</dt> <dd>

A pointer to an optional [**HwStorTracingEnabled**](hwstortracingenabled.md) routine that the port driver calls to notify the miniport of whether tracing is enabled or not.

</dd> <dt>

**FeatureSupport**
</dt> <dd>

Flags indicating features that are supported by the miniport. **FeatureSupport** is set to a combination of these values:



| Value                                                                                                                                                                                                                                                                        | Meaning                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STOR_FEATURE_VIRTUAL_MINIPORT"></span><span id="stor_feature_virtual_miniport"></span><dl> <dt>**STOR\_FEATURE\_VIRTUAL\_MINIPORT**</dt> </dl>                                                              | This is a virtual miniport driver.<br/>                                                                                                                                   |
| <span id="STOR_FEATURE_ATA_PASS_THROUGH"></span><span id="stor_feature_ata_pass_through"></span><dl> <dt>**STOR\_FEATURE\_ATA\_PASS\_THROUGH**</dt> </dl>                                                             | The miniport supports ATA pass through.<br/>                                                                                                                              |
| <span id="STOR_FEATURE_FULL_PNP_DEVICE_CAPABILITIES"></span><span id="stor_feature_full_pnp_device_capabilities"></span><dl> <dt>**STOR\_FEATURE\_FULL\_PNP\_DEVICE\_CAPABILITIES**</dt> </dl>                        | The miniport provides complete settings in its **STOR\_DEVICE\_CAPABILITIES\_EX** structure.<br/>                                                                         |
| <span id="STOR_FEATURE_DUMP_POINTERS"></span><span id="stor_feature_dump_pointers"></span><dl> <dt>**STOR\_FEATURE\_DUMP\_POINTERS**</dt> </dl>                                                                       | The miniport supports the dump pointer SRBs.<br/>                                                                                                                         |
| <span id="STOR_FEATURE_DEVICE_NAME_NO_SUFFIX"></span><span id="stor_feature_device_name_no_suffix"></span><dl> <dt>**STOR\_FEATURE\_DEVICE\_NAME\_NO\_SUFFIX**</dt> </dl>                                             | The miniport driver does not want the suffix "SCSI &lt;type&gt; Device" as part of the device friendly name<br/>                                                          |
| <span id="STOR_FEATURE_DUMP_RESUME_CAPABLE"></span><span id="stor_feature_dump_resume_capable"></span><dl> <dt>**STOR\_FEATURE\_DUMP\_RESUME\_CAPABLE**</dt> </dl>                                                    | The miniport's dump capability is functional for resume from hibernation.<br/>                                                                                            |
| <span id="STOR_FEATURE_DEVICE_DESCRIPTOR_FROM_ATA_INFO_VPD"></span><span id="stor_feature_device_descriptor_from_ata_info_vpd"></span><dl> <dt>**STOR\_FEATURE\_DEVICE\_DESCRIPTOR\_FROM\_ATA\_INFO\_VPD**</dt> </dl> | The Storport driver initializes the [**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md) from the ATA Information VPD page instead of from INQUIRY data.<br/> |
| <span id="STOR_FEATURE_SET_ADAPTER_INTERFACE_TYPE"></span><span id="stor_feature_set_adapter_interface_type"></span><dl> <dt>**STOR\_FEATURE\_SET\_ADAPTER\_INTERFACE\_TYPE**</dt> </dl>                              | The Storport driver sets the adapter interface type.<br/>                                                                                                                 |



 

</dd> <dt>

**SrbTypeFlags**
</dt> <dd>

Flags indicating the SRB types supported by the miniport. **SrbTypeFlags** is set to 0 or a combination of the following values:



| Value                                                                                                                                                                                                                               | Meaning                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <span id="SRB_TYPE_FLAG_SCSI_REQUEST_BLOCK"></span><span id="srb_type_flag_scsi_request_block"></span><dl> <dt>**SRB\_TYPE\_FLAG\_SCSI\_REQUEST\_BLOCK**</dt> </dl>          | The miniport uses standard SRBs.<br/>     |
| <span id="SRB_TYPE_FLAG_STORAGE_REQUEST_BLOCK"></span><span id="srb_type_flag_storage_request_block"></span><dl> <dt>**SRB\_TYPE\_FLAG\_STORAGE\_REQUEST\_BLOCK**</dt> </dl> | The miniport supports extended SRBs.<br/> |



 

</dd> <dt>

**AddressTypeFlags**
</dt> <dd>

The address schemes supported by the miniport. Currently, the only one address scheme is supported and the miniport must set this member to ADDRESS\_TYPE\_FLAG\_BTL8.



| Value                                                                                                                                                                                      | Meaning                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="ADDRESS_TYPE_FLAG_BTL8"></span><span id="address_type_flag_btl8"></span><dl> <dt>**ADDRESS\_TYPE\_FLAG\_BTL8**</dt> </dl> | Bus, Target, and LUN (BTL) 8-bit addressing.<br/> |



 

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved, set to 0.

</dd> <dt>

**HwUnitControl**
</dt> <dd>

A pointer the miniport driver's **HwStorUnitControl** routine. The port driver calls this routine with a control request for a storage unit device.

</dd> </dl>

## Remarks

The Storport driver follows the SCSI port driver's PnP initialization model. During the driver's DriverEntry routine, the miniport driver calls the [**StorPortInitialize**](storportinitialize.md) routine with a **HW\_INITIALIZATION\_DATA** structure describing the hardware it supports. Later, when the PnP Manager sends an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request to the port driver, the port driver passes a [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure to the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine. Afterwards, the port driver calls [**HwStorInitialize**](hwstorinitialize.md) to initialize the adapter.

Starting in Windows 8, both physical and virtual Storport miniports use **HW\_INITIALIZATION\_DATA**. See [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md) for more on which members are required for virtual miniports.

If a miniport driver sets the flag, **STOR\_FEATURE\_SET\_ADAPTER\_INTERFACE\_TYPE** in **HW\_INITIALIZATION\_DATA**, it should also set **AdapterInterfaceType** to **InterfaceTypeUndefined**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> <dt>

[**HwStorInitialize**](hwstorinitialize.md)
</dt> <dt>

[**HwStorBuildIo**](hwstorbuildio.md)
</dt> <dt>

[**HwStorStartIo**](hwstorstartio.md)
</dt> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> <dt>

[**HwStorResetBus**](hwstorresetbus.md)
</dt> <dt>

[**HwStorInterrupt**](hwstorinterrupt.md)
</dt> <dt>

[**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_HW_INITIALIZATION_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






