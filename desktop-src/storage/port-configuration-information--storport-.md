---
title: '\_PORT\_CONFIGURATION\_INFORMATION structure'
description: The PORT\_CONFIGURATION\_INFORMATION contains configuration information for a host bus adapter (HBA).
ms.assetid: ef710755-4437-4b17-b0ab-259a94d87545
keywords:
- _PORT_CONFIGURATION_INFORMATION structure Storage Devices
- PORT_CONFIGURATION_INFORMATION structure Storage Devices
- PPORT_CONFIGURATION_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PORT_CONFIGURATION_INFORMATION
api_location:
- Storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# \_PORT\_CONFIGURATION\_INFORMATION structure

The **PORT\_CONFIGURATION\_INFORMATION** contains configuration information for a host bus adapter (HBA).

## Syntax


```C++
typedef struct _PORT_CONFIGURATION_INFORMATION {
  ULONG                                  Length;
  ULONG                                  SystemIoBusNumber;
  INTERFACE_TYPE                         AdapterInterfaceType;
  ULONG                                  BusInterruptLevel;
  ULONG                                  BusInterruptVector;
  KINTERRUPT_MODE                        InterruptMode;
  ULONG                                  MaximumTransferLength;
  ULONG                                  NumberOfPhysicalBreaks;
  ULONG                                  DmaChannel;
  ULONG                                  DmaPort;
  DMA_WIDTH                              DmaWidth;
  DMA_SPEED                              DmaSpeed;
  ULONG                                  AlignmentMask;
  ULONG                                  NumberOfAccessRanges;
  ACCESS_RANGE                           (*AccessRanges)[];
#if (NTDDI_VERSION >= NTDDI_WIN8)
  PVOID                                  MiniportDumpData;
#else 
  PVOID                                  Reserved;
#endif 
  UCHAR                                  NumberOfBuses;
  UCHAR                                  InitiatorBusId[8];
  BOOLEAN                                ScatterGather;
  BOOLEAN                                Master;
  BOOLEAN                                CachesData;
  BOOLEAN                                AdapterScansDown;
  BOOLEAN                                AtdiskPrimaryClaimed;
  BOOLEAN                                AtdiskSecondaryClaimed;
  BOOLEAN                                Dma32BitAddresses;
  BOOLEAN                                DemandMode;
  UCHAR                                  MapBuffers;
  BOOLEAN                                NeedPhysicalAddresses;
  BOOLEAN                                TaggedQueuing;
  BOOLEAN                                AutoRequestSense;
  BOOLEAN                                MultipleRequestPerLu;
  BOOLEAN                                ReceiveEvent;
  BOOLEAN                                RealModeInitialized;
  BOOLEAN                                BufferAccessScsiPortControlled;
  UCHAR                                  MaximumNumberOfTargets;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  UCHAR                                  SrbType;
  UCHAR                                  AddressType;
#else 
  UCHAR                                  ReservedUchars[2];
#endif 
  ULONG                                  SlotNumber;
  ULONG                                  BusInterruptLevel2;
  ULONG                                  BusInterruptVector2;
  KINTERRUPT_MODE                        InterruptMode2;
  ULONG                                  DmaChannel2;
  ULONG                                  DmaPort2;
  DMA_WIDTH                              DmaWidth2;
  DMA_SPEED                              DmaSpeed2;
  ULONG                                  DeviceExtensionSize;
  ULONG                                  SpecificLuExtensionSize;
  ULONG                                  SrbExtensionSize;
  UCHAR                                  Dma64BitAddresses;
  BOOLEAN                                ResetTargetSupported;
  UCHAR                                  MaximumNumberOfLogicalUnits;
  BOOLEAN                                WmiDataProvider;
  STOR_SYNCHRONIZATION_MODEL             SynchronizationModel;
  PHW_MESSAGE_SIGNALED_INTERRUPT_ROUTINE HwMSInterruptRoutine;
  INTERRUPT_SYNCHRONIZATION_MODE         InterruptSynchronizationMode;
  MEMORY_REGION                          DumpRegion;
  ULONG                                  RequestedDumpBufferSize;
  BOOLEAN                                VirtualDevice;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  UCHAR                                  DumpMode;
#endif 
  ULONG                                  ExtendedFlags1;
  ULONG                                  MaxNumberOfIO;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  ULONG                                  MaxIOsPerLun;
  ULONG                                  InitialLunQueueDepth;
  ULONG                                  BusResetHoldTime;
  ULONG                                  FeatureSupport;
#endif 
} PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Specifies the size of the **PORT\_CONFIGURATION\_INFORMATION** structure, in bytes. Initialized by the Storport driver, this member also serves as the structure version.

</dd> <dt>

**SystemIoBusNumber**
</dt> <dd>

Specifies the system-assigned number of the I/O bus to which the HBA is connected. Miniport drivers must not modify this member. This Storport driver assigns this value because the platform might have several I/O buses of the specified **AdapterInterfaceType**.

</dd> <dt>

**AdapterInterfaceType**
</dt> <dd>

Identifies the I/O bus interface. The Storport driver initializes this member to the value specified by the miniport driver in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure. Miniport drivers must not modify this member.

</dd> <dt>

**BusInterruptLevel**
</dt> <dd>

Specifies the bus-relative interrupt request level. The Storport port driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**BusInterruptVector**
</dt> <dd>

Specifies the bus-relative vector returned by the HBA. The Storport driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. This member is irrelevant to drivers that set up the **BusInterruptLevel** member for their HBAs. It is pertinent for HBAs on types of I/O buses that use interrupt vectors, such as **PCIBus**. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**InterruptMode**
</dt> <dd>

Specifies whether the HBA uses **LevelSensitive** or **Latched** (sometimes called "edge-triggered") interrupts. The Storport driver initializes this member to an appropriate value for the bus and the device for example, **LevelSensitive** for **PCIBus**. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**MaximumTransferLength**
</dt> <dd>

Specifies the maximum number of bytes the HBA can transfer in a single transfer operation. By default, the value of this member is SP\_UNINITIALIZED\_VALUE, which indicates an unlimited maximum transfer size. If its HBA has more limited transfer support, a miniport driver must reset this member according to the HBA's transfer capacity. If a miniport driver's [**HwStorInterrupt**](hwstorinterrupt.md) routine cannot disable interrupts on the HBA, this member can be adjusted during driver development to ensure that time spent in that miniport driver's ISR does not degrade overall system performance.

</dd> <dt>

**NumberOfPhysicalBreaks**
</dt> <dd>

Specifies the maximum number of physical pages the storage adapter can manage in a single transfer (in other words, the extent of its scatter/gather support). By default, the value of this member is 0x11. The miniport driver must reset this member according to the storage adapter's capability.

</dd> <dt>

**DmaChannel**
</dt> <dd>

Specifies the DMA channel used by a subordinate HBA. By default, the value of this member is SP\_UNINITIALIZED\_VALUE. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**DmaPort**
</dt> <dd>

Specifies the DMA port used by a subordinate HBA. By default, the value of this member is SP\_UNINITIALIZED\_VALUE. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**DmaWidth**
</dt> <dd>

Specifies the width of DMA transfers if the HBA uses DMA. By default, the value of this member is zero. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**DmaSpeed**
</dt> <dd>

Specifies the DMA data-transfer speed for **Eisa** HBAs. The Storport driver initializes this member and miniport drivers must not modify it.

</dd> <dt>

**AlignmentMask**
</dt> <dd>

Contains a mask indicating the alignment restrictions for buffers required by the HBA for transfer operations. Some example valid mask values are 0 (byte aligned), 1 (word aligned), 3 (DWORD aligned) and 7 (double DWORD aligned). The miniport driver should set this mask if the HBA supports scatter/gather.

The following allowed alignment mask values are defined in *wdm.h*.

<dl> <dt>

<span id="FILE_BYTE_ALIGNMENT"></span><span id="file_byte_alignment"></span>**FILE\_BYTE\_ALIGNMENT** (0x00000000)
</dt> <dt>

<span id="FILE_WORD_ALIGNMENT"></span><span id="file_word_alignment"></span>**FILE\_WORD\_ALIGNMENT** (0x00000001)
</dt> <dt>

<span id="FILE_LONG_ALIGNMENT"></span><span id="file_long_alignment"></span>**FILE\_LONG\_ALIGNMENT** (0x00000003)
</dt> <dt>

<span id="FILE_QUAD_ALIGNMENT"></span><span id="file_quad_alignment"></span>**FILE\_QUAD\_ALIGNMENT** (0x00000007)
</dt> <dt>

<span id="FILE_OCTA_ALIGNMENT"></span><span id="file_octa_alignment"></span>**FILE\_OCTA\_ALIGNMENT** (0x0000000f)
</dt> <dt>

<span id="FILE_32_BYTE_ALIGNMENT"></span><span id="file_32_byte_alignment"></span>**FILE\_32\_BYTE\_ALIGNMENT** (0x0000001f)
</dt> <dt>

<span id="FILE_64_BYTE_ALIGNMENT"></span><span id="file_64_byte_alignment"></span>**FILE\_64\_BYTE\_ALIGNMENT** (0x0000003f)
</dt> <dt>

<span id="FILE_128_BYTE_ALIGNMENT"></span><span id="file_128_byte_alignment"></span>**FILE\_128\_BYTE\_ALIGNMENT** (0x0000007f)
</dt> <dt>

<span id="FILE_256_BYTE_ALIGNMENT"></span><span id="file_256_byte_alignment"></span>**FILE\_256\_BYTE\_ALIGNMENT** (0x000000ff)
</dt> <dt>

<span id="FILE_512_BYTE_ALIGNMENT"></span><span id="file_512_byte_alignment"></span>**FILE\_512\_BYTE\_ALIGNMENT** (0x000001ff)
</dt> </dl> </dd> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Specifies the number of **AccessRanges** elements in the array, described next.

</dd> <dt>

**(\*AccessRanges)**
</dt> <dd>

Pointer to an array of [**ACCESS\_RANGE**](access-range.md)-type elements. The Storport driver allocates memory for the access ranges and initializes this member. Mniport drivers must not modify this member.

</dd> <dt>

**MiniportDumpData**
</dt> <dd>

Pointer to a dump context used during a crashdump or a hibernation.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**NumberOfBuses**
</dt> <dd>

Specifies the number of buses controlled by the adapter. By default, the value of this member is zero. This member has a maximum value of SCSI\_MAXIMUM\_BUSES\_PER\_ADAPTER.

</dd> <dt>

**InitiatorBusId**
</dt> <dd>

Indicates the initiator bus ID. If the input **InitiatorBusId**\[0\] has the value SP\_UNINITIALIZED\_VALUE, the miniport driver can assign a default value if its HBA does not require the use of particular value(s) determined by querying the HBA. Otherwise, the miniport driver should use any nonzero value assigned by the port driver if possible. Typically, this value is bounded by the value set for **MaximumNumberOfTargets**.

</dd> <dt>

**ScatterGather**
</dt> <dd>

Indicates, when **TRUE**, that the HBA supports scatter/gather. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support scatter/gather. Miniport drivers that work with the Storport driver must *not* modify this value.

Starting in Windows Server 2008 R2 and Windows 7, the Storport driver initializes this member to **TRUE**. In prior versions of Windows, however, the value is set to **FALSE**. In this case, miniport drivers must set this member to **TRUE**. Otherwise, not setting this member to **TRUE** will cause the HBA device to fail to start.

</dd> <dt>

**Master**
</dt> <dd>

Indicates, when **TRUE**, that the HBA is a bus master. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support bus-mastering DMA. Miniport drivers that work with the Storport driver must *not* modify this value.

Starting in Windows Server 2008 R2 and Windows 7, the Storport driver initializes this member to **TRUE**. In prior versions of Windows, however, the value is set to **FALSE**. In this case, miniport drivers must set this member to **TRUE**. Otherwise, not setting this member to **TRUE** will cause the HBA device to fail to start.

</dd> <dt>

**CachesData**
</dt> <dd>

Indicates, when **TRUE**, that the HBA caches data or maintains cached state on the peripherals. When **FALSE** the HBA does not cache data or maintain cached state on the peripherals. By default, the value of this member is **FALSE**. If this is reset to **TRUE**, the Storport port driver notifies the miniport driver when certain system events occur, such as file system cache flushes.

</dd> <dt>

**AdapterScansDown**
</dt> <dd>

The Storport driver ignores this member.

</dd> <dt>

**AtdiskPrimaryClaimed**
</dt> <dd>

The Storport driver does not use this member, and its miniport drivers must not set it.

</dd> <dt>

**AtdiskSecondaryClaimed**
</dt> <dd>

The Storport driver does not use this member, and its miniport drivers must not set it.

</dd> <dt>

**Dma32BitAddresses**
</dt> <dd>

Indicates, when **TRUE**, that the HBA has 32 address lines and can access memory with physical addresses greater than 0x00FFFFFF. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support bus-width DMA. Miniport drivers must not modify this value since this the default DMA addressing if a value for **Dma64BitAddresses** is not set.

> [!Note]  
> If only 32 bit addresses are supported by the device hardware, then **Dma64BitAddresses** must be set to 0.

 

</dd> <dt>

**DemandMode**
</dt> <dd>

Indicates the system DMA controller should be programmed for demand-mode rather than single-cycle operations. The Storport driver initializes this member to **FALSE**, because it does not support subordinate-mode DMA. Miniport drivers must not modify this value.

</dd> <dt>

**MapBuffers**
</dt> <dd>

Indicates whether the Storport driver maps SRB data buffer addresses to system virtual addresses. The miniport driver sets this member to one of the following values to control mapping for SRB data buffer addresses.



| Value                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STOR_MAP_NO_BUFFERS"></span><span id="stor_map_no_buffers"></span><dl> <dt>**STOR\_MAP\_NO\_BUFFERS**</dt> </dl>                                                                      | Maps the buffer only for SRB\_FUNCTION\_IO\_CONTROL and SRB\_FUNCTION\_WMI.<br/>                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="STOR_MAP_ALL_BUFFERS"></span><span id="stor_map_all_buffers"></span><dl> <dt>**STOR\_MAP\_ALL\_BUFFERS**</dt> </dl>                                                                   | Obsolete. This value has the same effect as STOR\_MAP\_NON\_READ\_WRITE\_BUFFERS.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| <span id="STOR_MAP_NON_READ_WRITE_BUFFERS"></span><span id="stor_map_non_read_write_buffers"></span><dl> <dt>**STOR\_MAP\_NON\_READ\_WRITE\_BUFFERS**</dt> </dl>                                | Maps the buffer all for IO except for read and write requests.<br/>                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="STOR_MAP_ALL_BUFFERS_INCLUDING_READ_WRITE"></span><span id="stor_map_all_buffers_including_read_write"></span><dl> <dt>**STOR\_MAP\_ALL\_BUFFERS\_INCLUDING\_READ\_WRITE**</dt> </dl> | Maps the buffer all for IO including read and write requests.<br/> Miniports supporting boot must handle a read or write request of PAGE\_SIZE in length. These read or write requests must always complete successfully.<br/> Storport may fail to map the buffer under low system memory conditions. In this case, the **DataBuffer** member in the SRB will be NULL. <br/> This value is valid starting with Windows 8.<br/> |



 

</dd> <dt>

**NeedPhysicalAddresses**
</dt> <dd>

Indicates, when **TRUE**, that the miniport driver must translate virtual addresses to physical addresses, as required by the HBA. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support scatter/gather lists. Miniport must not modify this value.

</dd> <dt>

**TaggedQueuing**
</dt> <dd>

Indicates, when **TRUE**, that the HBA supports queuing of multiple requests with SCSI tags. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support tagged-queuing. Miniport drivers must not modify this value.

</dd> <dt>

**AutoRequestSense**
</dt> <dd>

Indicates, when **TRUE**, that the HBA supports auto request sense. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support auto-request sense. Miniport drivers must not modify this value.

</dd> <dt>

**MultipleRequestPerLu**
</dt> <dd>

Indicates, when **TRUE**, that the HBA supports multiple requests per logical unit. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support multiple requests issued to a logical unit at time. Miniport drivers must not modify this value.

</dd> <dt>

**ReceiveEvent**
</dt> <dd>

The Storport driver does not use this member, and its miniport drivers must not set it.

</dd> <dt>

**RealModeInitialized**
</dt> <dd>

The Storport driver does not use this member, and its miniport drivers must not set it.

</dd> <dt>

**BufferAccessScsiPortControlled**
</dt> <dd>

The Storport driver does not use this member, and its miniport drivers must not set it.

</dd> <dt>

**MaximumNumberOfTargets**
</dt> <dd>

Specifies the number of target peripherals the adapter can control. By default, the value of this member is SCSI\_MAXIMUM\_TARGETS\_PER\_BUS. A miniport driver can reset this member to a lesser value if the HBA has more limited capabilities or to a greater value, indicating that the HBA has extended bus capabilities. The maximum value for this member is 255.

</dd> <dt>

**SrbType**
</dt> <dd>

The type of SRBs to be sent to the miniport driver. This is set to either of these values:



| Value                                                                                                                                                                                                               | Meaning                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="SRB_TYPE_SCSI_REQUEST_BLOCK"></span><span id="srb_type_scsi_request_block"></span><dl> <dt>**SRB\_TYPE\_SCSI\_REQUEST\_BLOCK**</dt> </dl>          | The miniport driver receives standard SRBs.<br/> |
| <span id="SRB_TYPE_STORAGE_REQUEST_BLOCK"></span><span id="srb_type_storage_request_block"></span><dl> <dt>**SRB\_TYPE\_STORAGE\_REQUEST\_BLOCK**</dt> </dl> | The miniport driver receives extended SRBs.<br/> |



 

</dd> <dt>

**AddressType**
</dt> <dd>

The address type used between Storport and the miniport driver. Currently, only on address type is supported and member is set to STORAGE\_ADDRESS\_TYPE\_BTL8.



| Value                                                                                                                                                                                               | Meaning                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="STORAGE_ADDRESS_TYPE_BTL8"></span><span id="storage_address_type_btl8"></span><dl> <dt>**STORAGE\_ADDRESS\_TYPE\_BTL8**</dt> </dl> | Bus, Target, and LUN (BTL) 8-bit addressing.<br/> |



 

</dd> <dt>

**ReservedUchars**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**SlotNumber**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**BusInterruptLevel2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**BusInterruptVector2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**InterruptMode2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**DmaChannel2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**DmaPort2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**DmaWidth2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**DmaSpeed2**
</dt> <dd>

Initialized and reserved for use by the Storport driver. Miniport drivers must not modify this member.

</dd> <dt>

**DeviceExtensionSize**
</dt> <dd>

Specifies the size, in bytes, required by the miniport driver for its per-adapter device extension. A miniport driver uses its device extension as storage for driver-determined host bus adapter (HBA) information. The operating system-specific port driver initializes each device extension one time, when it first allocates the extension, and fills it with zeros. It passes a pointer to the HBA-specific device extension in every call to a miniport driver. The given size does not include any miniport driver-requested per-logical-unit storage. The size of per-logical-unit storage is specified via the **SpecificLuExtensionSize** field, described later in this topic.

Although SCSIPort re-initializes the device extension whenever the adapter is stopped and thus subsequent calls to [**HwScsiFindAdapter**](hwscsifindadapter.md) receive a zeroed-out device extension, Storport does not follow that model. Rather, Storport resets the device extension to zero only when it is first allocated, so only the first call to [**HwStorFindAdapter**](hwstorfindadapter.md) for a given adapter receives a zeroed-out device extension. Subsequent calls to **HwStorFindAdapter** and other miniport functions receive the device extension as last modified by the miniport driver. This allows the miniport driver to maintain knowledge about the state of the adapter between Plug and Play (PnP) stops and restarts, possibly enabling the miniport driver to optimize it's initialization procedure.

</dd> <dt>

**SpecificLuExtensionSize**
</dt> <dd>

This member specifies the size in bytes required by the miniport driver for its per-logical-unit-storage, if any, to handle data transfers larger than 64K. The Storport driver initializes this member to the value in the same member of the [**HW\_INITIALIAZATION\_DATA**](hw-initialization-data--storport-.md) structure sent in the [**StorPortInitialize**](storportinitialize.md) routine. Set this member to zero if the miniport driver does not maintain per-LU information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as [**StorPortGetUncachedExtension**](storportgetuncachedextension.md)

</dd> <dt>

**SrbExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-request storage, if any, to handle data transfers larger than 64K. The Storport driver initializes this member to the value in the same member of the [**HW\_INITIALIAZATION\_DATA**](hw-initialization-data--storport-.md) structure sent in the [**StorPortInitialize**](storportinitialize.md) routine. Set this member before calling [**StorPortGetUncachedExtension**](storportgetuncachedextension.md) to change the size of per-request storage based on **NumberOfPhysicalBreaks**. Set this member to zero if the miniport driver does not maintain per-SRB information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as **StorPortGetUncachedExtension**

</dd> <dt>

**Dma64BitAddresses**
</dt> <dd>

Indicates whether the HBA is able to access addresses greater than 4 GB. Storport adapters are required to support bus-width DMA. Therefore, on a 64-bit or PAE machine, the Storport driver initializes this member to **SCSI\_DMA64\_SYSTEM\_SUPPORTED** indicating that the adapter can access the full range of addresses. When miniport drivers detect this value, they must return one of the values in the following table in the same member to indicate to the port driver that the miniport driver supports 64-bit DMA. If the miniport fails to do this, it might severely degrade the performance of the adapter.

> [!Note]  
> If the device hardware supports only 32 bit addresses, then **Dma64BitAddresses** must be set to 0.

 



| Value                                                                                                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SCSI_DMA64_MINIPORT_SUPPORTED"></span><span id="scsi_dma64_miniport_supported"></span><dl> <dt>**SCSI\_DMA64\_MINIPORT\_SUPPORTED**</dt> </dl>                                                                                   | The miniport driver supports 64-bit physical addresses for I/O transfers.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="SCSI_DMA64_MINIPORT_FULL64BIT_SUPPORTED"></span><span id="scsi_dma64_miniport_full64bit_supported"></span><dl> <dt>**SCSI\_DMA64\_MINIPORT\_FULL64BIT\_SUPPORTED**</dt> </dl>                                                    | The miniport driver supports full 64-bit addressing. This indicates that I/O requests may have physical addresses &gt; 4GB. The uncached extension, SenseInfo, and Srb Extension may exist above 4GB. Allocations are restricted to 4GB boundary alignment in order to prevent them from crossing a 4GB boundary. <br/> This option is defined starting with Windows Server 2003 with SP1. This option is enabled starting in Windows 7 with Hotfix KB2468345 or Windows 7 with SP1 with Hotfix KB2468345.<br/> |
| <span id="SCSI_DMA64_MINIPORT_FULL64BIT_NO_BOUNDARY_REQ_SUPPORTED"></span><span id="scsi_dma64_miniport_full64bit_no_boundary_req_supported"></span><dl> <dt>**SCSI\_DMA64\_MINIPORT\_FULL64BIT\_NO\_BOUNDARY\_REQ\_SUPPORTED**</dt> </dl> | The miniport driver supports full 64-bit addressing. This indicates that I/O requests may have physical addresses &gt; 4GB. The uncached extension, SenseInfo, and Srb Extension may exist above 4GB. Allocations have no boundary alignment requirement. <br/> This option is available in starting with Windows 8.<br/>                                                                                                                                                                                       |
| <span id="SCSI_DMA64_MINIPORT_64BIT_ONE_4GB_SUPPORTED"></span><span id="scsi_dma64_miniport_64bit_one_4gb_supported"></span><dl> <dt>**SCSI\_DMA64\_MINIPORT\_64BIT\_ONE\_4GB\_SUPPORTED**</dt> </dl>                                      | The miniport driver support 64-bit addressing in a single 4GB region. This indicates that I/O requests, uncached extension, **SenseInfo**, and **SrbExtension** may have physical addresses &gt; 4GB in a single 4GB region.<br/> This option is available in starting with Windows 8.<br/>                                                                                                                                                                                                                     |



 

</dd> <dt>

**ResetTargetSupported**
</dt> <dd>

Obsolete. Do not use this member.

</dd> <dt>

**MaximumNumberOfLogicalUnits**
</dt> <dd>

Specifies the maximum number of logical units per target the HBA can control. By default, the value of this member is SCSI\_MAXIMUM\_LOGICAL\_UNITS. A miniport driver can reset this member to a lesser value if the HBA has more limited capabilities or to a greater value, indicating that the HBA has extended capabilities. The maximum value for this member is SCSI\_MAXIMUM\_LUNS\_PER\_TARGET.

</dd> <dt>

**WmiDataProvider**
</dt> <dd>

Indicates, when **TRUE**, that the miniport driver responds to Windows Management Instrumentation (WMI) requests. The Storport driver initializes this member to **TRUE**, because its miniport drivers must support WMI. Additionally, miniport drivers for fibre channel adapters are expected to support the SAN Management HBA API through WMI, and miniport drivers for host-based RAID adapters are required to support the RAID Management Interface.

Miniport drivers must not modify this value.

</dd> <dt>

**SynchronizationModel**
</dt> <dd>

Specifies the I/O synchronization model the miniport driver supports. The possible values are as follows:



| Value                                    | Meaning                       |
|------------------------------------------|-------------------------------|
| **StorSynchronizeFullDuplex**<br/> | Full-duplex mode. <br/> |
| **StorSynchronizeHalfDuplex**<br/> | Half-duplex mode. <br/> |



 

</dd> <dt>

**HwMSInterruptRoutine**
</dt> <dd>

A pointer to the miniport driver's [**HwMSInterruptRoutine**](hwmsinterruptroutine.md). This is a required routine for any miniport driver of an HBA that generates message signaled interrupts (MSIs). A miniport driver sets this member to **NULL** if the HBA does not generate MSIs.

</dd> <dt>

**InterruptSynchronizationMode**
</dt> <dd>

A value of type [**INTERRUPT\_SYNCHRONIZATION\_MODE**](interrupt-synchronization-mode.md) that specifies the interrupt synchronization mode. The interrupt synchronization mode determines how the port driver synchronizes message signaled interrupts.

</dd> <dt>

**DumpRegion**
</dt> <dd>

A structure of type [**MEMORY\_REGION**](memory-region.md) that describes a region of physically contiguous memory that miniport drivers can use during a crash dump or hibernation.

</dd> <dt>

**RequestedDumpBufferSize**
</dt> <dd>

Size of the uncached extension to be allocated for use during dump/hibernation.

</dd> <dt>

**VirtualDevice**
</dt> <dd>

Indicates, when **TRUE**, that there is no real hardware behind this device (for example, no DMA object, interrupt, I/O ports). Storport behaves differently in some circumstances when it supports a "virtual" miniport instead of a miniport that is controlling real hardware.

</dd> <dt>

**DumpMode**
</dt> <dd>

A value indicating the use of the miniport during dump mode. This member is included starting with Windows 8. It can have one of the following values.



| Value                                                                                                                                                                                   | Meaning                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="DUMP_MODE_CRASH"></span><span id="dump_mode_crash"></span><dl> <dt>**DUMP\_MODE\_CRASH**</dt> </dl>                    | The miniport in dump mode is used for a crashdump.<br/>               |
| <span id="DUMP_MODE_HIBER"></span><span id="dump_mode_hiber"></span><dl> <dt>**DUMP\_MODE\_HIBER**</dt> </dl>                    | The miniport in dump mode is used for a hibernation.<br/>             |
| <span id="DUMP_MODE_MARK_MEMORY"></span><span id="dump_mode_mark_memory"></span><dl> <dt>**DUMP\_MODE\_MARK\_MEMORY**</dt> </dl> | The miniport in dump mode is used for marking required memory.<br/>   |
| <span id="DUMP_MODE_RESUME"></span><span id="dump_mode_resume"></span><dl> <dt>**DUMP\_MODE\_RESUME**</dt> </dl>                 | The miniport in dump mode is used for a resume from hibernation.<br/> |



 

</dd> <dt>

**ExtendedFlags1**
</dt> <dd>

Reserved.

</dd> <dt>

**MaxNumberOfIO**
</dt> <dd>

The maximum number of outstanding I/O operations supported by the HBA. The default is set to 1000 by Storport. If the HBA does not support 1000 outstanding I/O operations, the miniport should adjust this to an appropriate smaller value.

If the HBA can support more than 1000 outstanding I/O operations, this value can increase to any value supported by the adapter hardware. To allow more than 1000 outstanding I/O operations, the HBA must support, and set in **Dma64BitAddresses**, to one the following 64 bit DMA addressing methods.

-   SCSI\_DMA64\_MINIPORT\_FULL64BIT\_SUPPORTED
-   SCSI\_DMA64\_MINIPORT\_FULL64BIT\_NO\_BOUNDARY\_REQ\_SUPPORTED
-   SCSI\_DMA64\_MINIPORT\_64BIT\_ONE\_4GB\_SUPPORTED

Prior to Windows 8, this member is reserved.

</dd> <dt>

**MaxIOsPerLun**
</dt> <dd>

The maximum number of I/O requests supported on a LUN. The Storport driver will set this to a default value of 255. If a LUN does not support 255 outstanding I/O requests, the miniport should adjust this to an appropriate smaller value. This member must be &lt;= **MaxNumberOfIO**.

> [!Note]  
> **SrbType** must contain **SRB\_TYPE\_STORAGE\_REQUEST\_BLOCK** to support **MaxIOsPerLun** &gt; 255.

 

</dd> <dt>

**InitialLunQueueDepth**
</dt> <dd>

The initial LUN I/O queue depth. Storport set this to a default value of 20 for physical miniports and to 250 for virtual miniports. This member adjusts the initial queue depth for all LUNs on the adapter. The queue depth for an individual LUN is set by calling [**StorPortSetDeviceQueueDepth**](storportsetdevicequeuedepth.md). This member is typically set to the same value as **MaxIOsPerLun**.

</dd> <dt>

**BusResetHoldTime**
</dt> <dd>

The amount of time, in microseconds, to pause the adapter after a reset is detected. Set this value to 0 if no wait time is needed after a bus reset.

</dd> <dt>

**FeatureSupport**
</dt> <dd>

Storport features requested for the adapter.



| Value                                                                                                                                                                                                                                                                        | Meaning                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <span id="STOR_ADAPTER_FEATURE_RESERVED"></span><span id="stor_adapter_feature_reserved"></span><dl> <dt>**STOR\_ADAPTER\_FEATURE\_RESERVED**</dt> </dl>                                                              | System reserved features are supported. Miniports must not set this feature.<br/> |
| <span id="STOR_ADAPTER_FEATURE_STOP_UNIT_DURING_POWER_DOWN"></span><span id="stor_adapter_feature_stop_unit_during_power_down"></span><dl> <dt>**STOR\_ADAPTER\_FEATURE\_STOP\_UNIT\_DURING\_POWER\_DOWN**</dt> </dl> | The adapter receives the STOP\_UNIT command during system shutdown.<br/>          |



 

Prior to Windows 8, this member is reserved and must be set to 0.

</dd> </dl>

## Remarks

When the PnP Manager notifies the Storport driver to start a device, Storport allocates and initializes this structure, supplies as much HBA-specific configuration information as possible, and passes the structure to the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) routine.

The Storport driver does not support non-PnP devices, so [**HwStorFindAdapter**](hwstorfindadapter.md) does not search for the adapter. Its principal function is to initialize the **PORT\_CONFIGURATION\_INFORMATION** structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HW\_INITIALIAZATION\_DATA**](hw-initialization-data--storport-.md)
</dt> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> <dt>

[**MEMORY\_REGION**](memory-region.md)
</dt> <dt>

[**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md)
</dt> <dt>

[**StorPortGetMSIInfo**](storportgetmsiinfo.md)
</dt> <dt>

[**StorPortReleaseMSISpinLock**](storportreleasemsispinlock.md)
</dt> <dt>

[**StorPortSetDeviceQueueDepth**](storportsetdevicequeuedepth.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_PORT_CONFIGURATION_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






