---
title: '\_PORT\_CONFIGURATION\_INFORMATION structure'
description: PORT\_CONFIGURATION\_INFORMATION (SCSI) contains configuration information for an HBA.
ms.assetid: f3c9d851-d30d-4757-82a3-225ee67528c1
keywords:
- _PORT_CONFIGURATION_INFORMATION structure Storage Devices
- PORT_CONFIGURATION_INFORMATION structure Storage Devices
- PPORT_CONFIGURATION_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PORT_CONFIGURATION_INFORMATION
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

# \_PORT\_CONFIGURATION\_INFORMATION structure

PORT\_CONFIGURATION\_INFORMATION (SCSI) contains configuration information for an HBA. The OS-specific port driver allocates and initializes this structure, supplies as much HBA-specific configuration information as possible, and passes the structure to the miniport driver's *HwScsiFindAdapter* routine. The port driver gets some of the information for this structure from the miniport driver's HW\_INITIALIZATION\_DATA structure. The miniport driver's *HwScsiFindAdapter* routine is responsible for determining whether the miniport driver can support the HBA and, if so, for filling in the pertinent remaining information in the PORT\_CONFIGURATION\_INFORMATION structure.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _PORT_CONFIGURATION_INFORMATION {
  ULONG           Length;
  ULONG           SystemIoBusNumber;
  INTERFACE_TYPE  AdapterInterfaceType;
  ULONG           BusInterruptLevel;
  ULONG           BusInterruptVector;
  KINTERRUPT_MODE InterruptMode;
  ULONG           MaximumTransferLength;
  ULONG           NumberOfPhysicalBreaks;
  ULONG           DmaChannel;
  ULONG           DmaPort;
  DMA_WIDTH       DmaWidth;
  DMA_SPEED       DmaSpeed;
  ULONG           AlignmentMask;
  ULONG           NumberOfAccessRanges;
  ACCESS_RANGE    (*AccessRanges)[];
  PVOID           Reserved;
  UCHAR           NumberOfBuses;
  UCHAR           InitiatorBusId[8];
  BOOLEAN         ScatterGather;
  BOOLEAN         Master;
  BOOLEAN         CachesData;
  BOOLEAN         AdapterScansDown;
  BOOLEAN         AtdiskPrimaryClaimed;
  BOOLEAN         AtdiskSecondaryClaimed;
  BOOLEAN         Dma32BitAddresses;
  BOOLEAN         DemandMode;
  BOOLEAN         MapBuffers;
  BOOLEAN         NeedPhysicalAddresses;
  BOOLEAN         TaggedQueuing;
  BOOLEAN         AutoRequestSense;
  BOOLEAN         MultipleRequestPerLu;
  BOOLEAN         ReceiveEvent;
  BOOLEAN         RealModeInitialized;
  BOOLEAN         BufferAccessScsiPortControlled;
  UCHAR           MaximumNumberOfTargets;
  UCHAR           ReservedUchars[2];
  ULONG           SlotNumber;
  ULONG           BusInterruptLevel2;
  ULONG           BusInterruptVector2;
  KINTERRUPT_MODE InterruptMode2;
  ULONG           DmaChannel2;
  ULONG           DmaPort2;
  DMA_WIDTH       DmaWidth2;
  DMA_SPEED       DmaSpeed2;
  ULONG           DeviceExtensionSize;
  ULONG           SpecificLuExtensionSize;
  ULONG           SrbExtensionSize;
  UCHAR           Dma64BitAddresses;
  BOOLEAN         ResetTargetSupported;
  UCHAR           MaximumNumberOfLogicalUnits;
  BOOLEAN         WmiDataProvider;
} PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Specifies the size of this structure in bytes, as returned by **sizeof**(). In effect, this member, which is always initialized by the OS-specific port driver, indicates the version of this structure used by the port driver.

</dd> <dt>

**SystemIoBusNumber**
</dt> <dd>

Specifies the system-assigned number of the I/O bus to which the HBA is connected. The OS-specific port driver always initializes this member. Its value is system-assigned because the platform might have several I/O buses of the given **AdapterInterfaceType**.

</dd> <dt>

**AdapterInterfaceType**
</dt> <dd>

Identifies the I/O bus interface. The OS-specific port driver always sets this member to the value specified by the miniport driver in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure.

</dd> <dt>

**BusInterruptLevel**
</dt> <dd>

Specifies the bus-relative interrupt request level. The OS-specific port driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. Depending on the given **AdapterInterfaceType** and HBA, the value set for this member can correspond to the IRQL for the bus, such as for **Isa** and **MicroChannel** type buses. Drivers of **Eisa** HBAs must set this value to the bus-relative IRQL for the HBA if the adapter is configured for level-sensitive interrupts.

</dd> <dt>

**BusInterruptVector**
</dt> <dd>

Specifies the bus-relative vector returned by the HBA. The OS-specific port driver makes no assumptions about the HBA's interrupt usage, so the default value is zero. This member is irrelevant to drivers that set up the **BusInterruptLevel** member for their HBAs. It is pertinent for HBAs on types of I/O buses that use interrupt vectors, such as **PCIBus**.

</dd> <dt>

**InterruptMode**
</dt> <dd>

Specifies whether the HBA uses **LevelSensitive** or **Latched** (sometimes called "edge-triggered") interrupts. The OS-specific port driver initializes this member to an appropriate value for the bus and the device--for example, **LevelSensitive** for **PCIBus**. Drivers of **Eisa** HBAs must reset this value if the adapter is configured for level-sensitive interrupts, as must drivers of HBAs on I/O buses that use level-sensitive interrupts, such as **MicroChannel** type buses.

</dd> <dt>

**MaximumTransferLength**
</dt> <dd>

Specifies the maximum number of bytes the HBA can transfer in a single transfer operation. By default, the value of this member is SP\_UNINITIALIZED\_VALUE, which indicates an unlimited maximum transfer size. If its HBA has more limited transfer support, a miniport driver must reset this member according to the HBA's transfer capacity. If a miniport driver's HwScsiInterrupt routine cannot disable interrupts on the HBA, this member can be adjusted during driver development to ensure that time spent in that miniport driver's ISR does not cause the mouse to "jump" or serial/parallel throughput to drop to a user-noticeable level.

</dd> <dt>

**NumberOfPhysicalBreaks**
</dt> <dd>

Specifies the maximum number of breaks between address ranges that a data buffer can have if the HBA supports scatter/gather. In other words, the number of scatter/gather lists minus one. By default, the value of this member is SP\_UNINITIALIZED\_VALUE, which indicates the HBA can support an unlimited number of physical discontiguities. If the port driver sets a value for this member, the miniport driver can adjust the value lower but no higher. If this member is SP\_UNINITIALIZED\_VALUE, the miniport driver must reset this member according to the HBA's scatter/gather capacity, with zero representing no scatter/gather support.

</dd> <dt>

**DmaChannel**
</dt> <dd>

Specifies the DMA channel used by a subordinate HBA. By default, the value of this member is SP\_UNINITIALIZED\_VALUE. If the HBA uses a system DMA controller and the given **AdapterInterfaceType** is any value except **MicroChannel**, the miniport driver must reset this member.

</dd> <dt>

**DmaPort**
</dt> <dd>

Specifies the DMA port used by a subordinate HBA. By default, the value of this member is SP\_UNINITIALIZED\_VALUE. If the HBA uses a system DMA controller and the given **AdapterInterfaceType** is **MicroChannel**, the miniport driver must set this member.

</dd> <dt>

**DmaWidth**
</dt> <dd>

Specifies the width of DMA transfers if the HBA uses DMA. By default, the value of this member is zero. If its HBA does DMA, the miniport driver must reset this member to one of the following: **Width8Bits**, **Width16Bits**, or **Width32Bits**.

</dd> <dt>

**DmaSpeed**
</dt> <dd>

Specifies the DMA data-transfer speed for **Eisa** HBAs. By default, the value of this member specifies compatibility timing. Acceptable values for this member are any of the following: **Compatible**, **TypeA**, **TypeB**, or **TypeC**.

</dd> <dt>

**AlignmentMask**
</dt> <dd>

Contains a mask indicating the alignment restrictions for buffers required by the HBA for transfer operations. Valid mask values are also restricted by characteristics of the memory managers on different versions of Windows. The mask values that are permitted under Windows 95 or Windows 98 are 0 (byte aligned), 1 (word aligned) or 3 (DWORD aligned). Under Windows NT and Windows 2000 the valid mask values are 0 (byte aligned), 1 (word aligned), 3 (DWORD aligned) and 7 (double DWORD aligned). The miniport driver should set this mask if the HBA supports scatter/gather.

</dd> <dt>

**NumberOfAccessRanges**
</dt> <dd>

Specifies the number of **AccessRanges** elements in the array, described next. The OS-specific port driver always sets this member to the value passed in the HW\_INITIALIZATION\_DATA structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md).

</dd> <dt>

**(\*AccessRanges)**
</dt> <dd>

Pointer to an array of [**ACCESS\_RANGE**](access-range.md)-type elements. The given **NumberOfAccessRanges** determines how many elements must be configured with bus-relative range values. The **AccessRanges** pointer must be **NULL** if **NumberOfAccessRanges** is zero. If possible, the OS-specific port driver initializes this member's elements, possibly from the registry or possibly by interrogating an I/O bus, for an HBA it found by using the miniport driver's specified [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md). Otherwise, the port driver initializes all values within array elements to zero.

<dl> <dd>

If any access range element is set to nonzero values on entry to the miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine, the miniport driver *must* map the supplied addresses with [**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md) and use the corresponding logical addresses to verify whether that HBA is one it supports. If the input **AccessRanges** have nonzero values supplied, a miniport driver *should neverattempt* to scan the I/O bus for HBAs it supports using a set of driver-devised port/memory addresses that its HBA(s) might use.

</dd> </dl> </dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**NumberOfBuses**
</dt> <dd>

Specifies the number of SCSI buses controlled by the HBA. By default, the value of this member is zero.

</dd> <dt>

**InitiatorBusId**
</dt> <dd>

Indicates the initiator bus ID. If the input **InitiatorBusId**\[0\] has the value zero, the miniport driver can assign a default value if its HBA does not require the use of particular value(s) determined by querying the HBA. Otherwise, the miniport driver should use any nonzero value assigned by the port driver if possible. Every miniport driver must update **InitiatorBusId** specifications to match what its HBA uses, if necessary querying the HBA to determine the appropriate values(s).

<dl> <dd>

A miniport driver must set an entry for each SCSI bus supported by the HBA, as indicated by the value of **NumberOfBuses**.

</dd> </dl> </dd> <dt>

**ScatterGather**
</dt> <dd>

Indicates when **TRUE** that the HBA supports scatter/gather. When **FALSE** the HBA does not support scatter/gather. By default, the value of this member is **FALSE**.

</dd> <dt>

**Master**
</dt> <dd>

Indicates when **TRUE** that the HBA is a bus master. When **FALSE**, the HBA is not a bus master. By default, the value of this member is **FALSE**.

</dd> <dt>

**CachesData**
</dt> <dd>

Indicates when **TRUE** that the HBA caches data or maintains cached state on the peripherals. When **FALSE** the HBA does not cache data or maintain cached state on the peripherals. By default, the value of this member is **FALSE**. If this is reset to **TRUE**, the OS-specific port driver notifies the miniport driver when certain system events occur, such as file system cache flushes and system shutdown. For example, if a controller on the bus mirrors two disks, the miniport driver would normally set this member to **TRUE**.

</dd> <dt>

**AdapterScansDown**
</dt> <dd>

Indicates when **TRUE** that the BIOS for the HBA scans for SCSI bus targets from seven to zero. When **FALSE**, the BIOS for the HBA looks for SCSI bus targets, starting with an ID zero and scanning upwards to (but not including) **MaximumTargetIds**. By default, the value of **AdapterScansDown** is **FALSE**.

</dd> <dt>

**AtdiskPrimaryClaimed**
</dt> <dd>

Indicates when **TRUE** that the primary "AT" (WD1003-compatible) disk address range, 0x1F0 to 0x1FF, has been claimed in the registry by another driver for its device. The OS-specific port driver always initializes this member. If the input value of this member is **TRUE**, a miniport driver should assume that an already loaded driver has claimed the device range. If the input value is **FALSE**, a miniport driver can claim the address range for an HBA that emulates an "AT" disk controller and reset this member to **TRUE**, thereby preventing access to this range by the "AT" disk driver or subsequently loaded miniport drivers.

</dd> <dt>

**AtdiskSecondaryClaimed**
</dt> <dd>

Indicates when **TRUE** that the secondary AT disk address range, 0x170 to 0x17F has been claimed in the registry by another driver for its device. When **FALSE** the secondary AT disk address range has not been claimed in the registry by another driver. The OS-specific port driver always initializes this member. Miniport drivers should treat this member as for **AtdiskPrimaryClaimed**.

</dd> <dt>

**Dma32BitAddresses**
</dt> <dd>

Indicates when **TRUE** that the HBA has 32 address lines and can access memory with physical addresses greater than 0x00FFFFFF. When **FALSE** the HBA has either a number of DMA address lines other than 32. By default, the value of this member is **FALSE**. If the miniport driver sets **Dma64BitAddresses**, this member must be **FALSE**.

</dd> <dt>

**DemandMode**
</dt> <dd>

Indicates when **TRUE** that the system DMA controller should be programmed for demand-mode rather than single-cycle operations. If the HBA is not a subordinate device, this member should be **FALSE**.

</dd> <dt>

**MapBuffers**
</dt> <dd>

Indicates when **TRUE** that data buffers must be mapped to system virtual address ranges. When **FALSE** the data buffers do not have to be mapped to system virtual addresses. The OS-specific port driver always sets this member to the value passed in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md). A miniport driver can reset this value for any particular HBA it controls. If **FALSE**, the miniport driver must not access **Srb.DataBuffer** directly.

</dd> <dt>

**NeedPhysicalAddresses**
</dt> <dd>

Indicates when **TRUE** that the miniport driver must translate virtual addresses to physical addresses, as required by the HBA. When **FALSE**, the miniport driver does not have to translate virtual addresses to physical addresses. The OS-specific port driver always sets this member to the value passed in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md). A miniport driver can reset this value for any particular HBA it controls.

</dd> <dt>

**TaggedQueuing**
</dt> <dd>

Indicates when **TRUE** that the HBA supports queuing of multiple requests with SCSI tags. When **FALSE**, the HBA does not support SCSI-tagged queuing. The OS-specific port driver always sets this member to the value passed in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md). A miniport driver can reset this value for any particular HBA it controls.

</dd> <dt>

**AutoRequestSense**
</dt> <dd>

Indicates when **TRUE** that the HBA supports auto request sense. When **FALSE** the HBA does not support auto request sense. The OS-specific port driver always sets this member to the value passed in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md). A miniport driver can reset this value for any particular HBA it controls. This member must be set to **TRUE** before the driver of a bus-master HBA calls [**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md).

</dd> <dt>

**MultipleRequestPerLu**
</dt> <dd>

Indicates when **TRUE** that the HBA supports multiple requests per logical unit. When **FALSE** the HBA does not support multiple requests per logical unit. The mechanism by which the adapter caches the requests is adapter-defined. The OS-specific port driver always sets this member to the value passed in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md). A miniport driver can reset this value for any particular HBA it controls.

</dd> <dt>

**ReceiveEvent**
</dt> <dd>

Indicates when **TRUE** that the HBA supports SCSI receive-event operations. When **FALSE** the HBA does not support SCSI receive-event operations. The OS-specific port driver always sets this member to the value passed in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called [**ScsiPortInitialize**](scsiportinitialize.md). A miniport driver can reset this value for any particular HBA it controls.

</dd> <dt>

**RealModeInitialized**
</dt> <dd>

Indicates when **TRUE** that an (x86-only) real-mode driver has already initialized the HBA. When **FALSE** the HBA has not been previously initialized by a real-mode driver. The OS-dependent port driver always initializes this member. If this is set to **TRUE**, the miniport driver must not initialize its HBA if the driver's initialization sequence is identical to real-mode HBA initialization; not reinitializing the HBA in these circumstances makes the miniport driver load much faster. The value of this member is irrelevant to any miniport driver that always initializes its HBA while running in protected mode on x86-based platforms and to all miniport drivers for which it is immaterial whether they are running on a CISC- or RISC-based platform.

</dd> <dt>

**BufferAccessScsiPortControlled**
</dt> <dd>

Indicates when **TRUE** that the miniport driver always calls **ScsiPort***Xxx* to access data buffers and/or request-sense information in SRBs, thereby allowing the OS-specific port driver to optimize I/O request processing. When **FALSE** the miniport driver does not have to call **ScsiPort***Xxx* routines to access data buffers or request-sense information. Setting this member to **FALSE** can degrade the I/O performance of the HBA. Calling routines other than the **ScsiPort***Xxx* makes a miniport driver nonportable across Microsoft operating systems.

</dd> <dt>

**MaximumNumberOfTargets**
</dt> <dd>

Specifies the number of target peripherals the HBA can control. By default, the value of this member is SCSI\_MAXIMUM\_TARGETS, according to the SCSI standard. A miniport driver can reset this member to a lesser value if the HBA has more limited capabilities or to a greater value, indicating that the HBA has wide-SCSI or Fibre Channel capabilities. This value is limited to SCSI\_MAXIMUM\_TARGETS\_PER\_BUS.

</dd> <dt>

**ReservedUchars**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**SlotNumber**
</dt> <dd>

Specifies the slot number of an HBA with matching values to the **VendorId** and **DeviceId** that were specified in the [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md) structure when the miniport driver called **ScsiPortInitialize**.

</dd> <dt>

**BusInterruptLevel2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**BusInterruptVector2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**InterruptMode2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**DmaChannel2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**DmaPort2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**DmaWidth2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**DmaSpeed2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**DeviceExtensionSize**
</dt> <dd>

Specifies the size in bytes required by a miniport driver for its per-HBA device extension to handle data transfers larger than 64K, which might require larger scatter/gather lists than the size defined in the registry for this driver.

</dd> <dt>

**SpecificLuExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-logical-unit-storage, if any, to handle data transfers larger than 64K. Leave this member set to zero if the miniport driver does not maintain per-LU information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as [**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md).

</dd> <dt>

**SrbExtensionSize**
</dt> <dd>

Specifies the size in bytes required by the miniport driver for its per-request storage, if any, to handle data transfers larger than 64K. Set this member before calling [**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md) to change the size of per-request storage based on **NumberOfPhysicalBreaks**. Leave this member set to zero if the miniport driver does not maintain per-SRB information for which it requires storage. This value is based on the assumption that the HBA is able to receive 32-bit addresses, regardless of what the controller can actually support. If additional space is needed in the LUN or SRB extensions to handle 64-bit addresses, then appropriate adjustments must be made to this value before using it with routines such as **ScsiPortGetUncachedExtension**.

</dd> <dt>

**Dma64BitAddresses**
</dt> <dd> <dl> <dd>

Indicates that the HBA is able to access addresses greater than 4 GB, or 0x0FFFFFFFF if **Dma64BitAddresses** contains a value of SCSI\_DMA64\_MINIPORT\_SUPPORTED. Prior to Windows 2000 the ScsiPort set this value based on the contents of [**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md). This is no longer the case. In Windows 2000 the value of **Dma64BitAddresses** is determined by the miniport driver callback [*HwScsiFindAdapter*](hwscsifindadapter.md) alone. If the operating system supports a 64-bit address space, the port driver passes a value of SCSI\_DMA64\_SYSTEM\_SUPPORTED to the miniport driver in this member. If the HBA described by PORT\_CONFIGURATION\_INFORMATION also supports address spaces greater than 32-bits then the port/miniport driver is required to support full 64-bit addressing, and the miniport driver's callback *HwScsiFindAdapter* indicates this by assigning a value of SCSI\_DMA64\_MINIPORT\_SUPPORTED to **Dma64BitAddresses**, writing over any previous value assigned by the port driver. The correct value must be assigned to the **Dma64BitAddresses** member before the miniport driver calls [**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md).

</dd> </dl> </dd> <dt>

**ResetTargetSupported**
</dt> <dd>

Obsolete. ScsiPort driver no longer sends SRB\_FUNCTION\_RESET\_DEVICE requests to its miniport drivers. Do not use this member.

</dd> <dt>

**MaximumNumberOfLogicalUnits**
</dt> <dd>

Specifies the maximum number of logical units per target the HBA can control. By default, the value of this member is SCSI\_MAXIMUM\_LOGICAL\_UNITS. A miniport driver can reset this member to a lesser value if the HBA has more limited capabilities or to a greater value, indicating that the HBA has SCSI-3 capabilities.

</dd> <dt>

**WmiDataProvider**
</dt> <dd>

Indicates when **TRUE** that the miniport driver responds to Windows Management Instrumentation (WMI) requests. When **FALSE** the miniport driver does not respond to Windows Management Instrumentation (WMI) requests. By default, the value of this member is **FALSE**.

</dd> </dl>

## Remarks

The specific members initialized depend on the HBA miniport driver and on the configuration information available to the OS-specific port driver. The OS-specific port driver sets default values in all members for which it cannot supply configuration information to the miniport driver's *HwScsiFindAdapter* routine.

All HBA miniport drivers should have at least one set of defaults to use for relevant members if the OS-specific port driver does not pass in all initialized values.

The *HwScsiFindAdapter* routine must update all members relevant to an HBA that the driver supports.

Windows NT storage class drivers, which load later than miniport drivers, depend on the information supplied by each miniport driver's *HwScsiFindAdapter* routine to set up their subsequent I/O requests. For example, the **MaximumTransferLength** and **NumberOfPhysicalBreaks** values supplied by each miniport driver control whether a class driver must split large transfer requests into a set of partial transfers to suit the limits of the HBA.

Prior to Windows 2000, both the PORT\_CONFIGURATION\_INFORMATION and the HW\_INITIALIZATION\_DATA structures had a member called **Dma64BitAddresses**. In Windows 2000, **Dma64BitAddresses** has been eliminated from the HW\_INITIALIZATION\_DATA structure, and its definition has changed somewhat in PORT\_CONFIGURATION\_INFORMATION. The port driver no longer consults HW\_INITIALIZATION\_DATA in order to initialize **Dma64BitAddresses** in PORT\_CONFIGURATION\_INFORMATION.

The **Dma64BitAddresses** member of PORT\_CONFIGURATION\_INFORMATION should no longer be thought of as a BOOLEAN value. A value of SCSI\_DMA64\_SYSTEM\_SUPPORTED indicates that the port/miniport driver is required to support 64-bit addressing, but the **ScsiPortGetUncachedExtension** routine still interprets any nonzero value of **Dma64BitAddresses** as indicating that 64-bit support is required. This means that **ScsiPortGetUncachedExtension** still functions properly when called by a legacy driver that assigns BOOLEAN values to **Dma64BitAddresses**.

In addition to **Dma64BitAddresses**, both PORT\_CONFIGURATION\_INFORMATION and HW\_INITIALIZATION\_DATA have a pair of members called **SpecificLuExtensionSize** and **SrbExtensionSize** whose values must now be handled differently. The miniport driver must calculate the initial values of **SpecificLuExtensionSize** and **SrbExtensionSize** in HW\_INITIALIZATION\_DATA based on the assumption that the HBA is capable of receiving 32-bit addresses, regardless of what the controller can actually support. The default values for **SpecificLuExtensionSize** and **SrbExtensionSize** in PORT\_CONFIGURATION\_INFORMATION will also be based on an assumption of 32-bit addressing, since the values in PORT\_CONFIGURATION\_INFORMATION are derived from the values in HW\_INITIALIZATION\_DATA.

This means that if the miniport driver needs additional space in either the LUN extension or the SRB extension in order to handle 64 bit physical addresses, it must modify the values for **SpecificLuExtensionSize** and **SrbExtensionSize** in PORT\_CONFIGURATION\_INFORMATION to account for this before passing PORT\_CONFIGURATION\_INFORMATION to **ScsiPortGetUncachedExtension**.

## Requirements



|                   |                                                                                                                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Srb.h (include Srb.h, Storport.h, or Strmini.h)</dt> </dl> |



## See also

<dl> <dt>

[**ACCESS\_RANGE**](access-range.md)
</dt> <dt>

[**DriverEntry of SCSI Miniport Driver**](driverentry-of-scsi-miniport-driver.md)
</dt> <dt>

[**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> <dt>

[**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> <dt>

[**ScsiPortValidateRange**](scsiportvalidaterange.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_PORT_CONFIGURATION_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






