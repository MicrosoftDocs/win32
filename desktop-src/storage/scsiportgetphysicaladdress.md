---
title: ScsiPortGetPhysicalAddress routine
description: The ScsiPortGetPhysicalAddress routine converts a given virtual address range to a physical address range for a DMA operation.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: 4a0d0b10-9773-40d7-962c-cf2acffcee47
keywords:
- ScsiPortGetPhysicalAddress routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortGetPhysicalAddress
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

# ScsiPortGetPhysicalAddress routine

The **ScsiPortGetPhysicalAddress** routine converts a given virtual address range to a physical address range for a DMA operation.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
SCSI_PHYSICAL_ADDRESS ScsiPortGetPhysicalAddress(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _In_  PVOID               VirtualAddress,
  _Out_ ULONG               *Length
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

Pointer to the SCSI request block if the *VirtualAddress* to be converted comes from that SRB's **DataBuffer** member or, possibly, from the **SenseInfoBuffer**. Otherwise, this parameter must be **NULL**.

</dd> <dt>

*VirtualAddress* \[in\]
</dt> <dd>

Pointer to the base virtual address to be converted. If this virtual address falls within the range for an SRB-supplied **DataBuffer**, the caller also must provide the *Srb* pointer.

</dd> <dt>

*Length* \[out\]
</dt> <dd>

Returns the number of bytes mapped, starting at the returned physical address.

</dd> </dl>

## Return value

**ScsiPortGetPhysicalAddress** returns the corresponding physical address for a given *VirtualAddress*. If the given address cannot be converted, it returns **NULL**.

## Remarks

Miniport drivers of bus-master HBAs call **ScsiPortGetPhysicalAddress** to get mapped physical address ranges to be used during DMA operations. For example, **ScsiPortGetPhysicalAddress** can be used to build a scatter/gather list for data transfers that span pages. Note that the *Length* returned can be greater than the size of the **DataBuffer** in a given SRB.

If a non-**NULL***Srb* is passed, the *VirtualAddress* either must be within the range of the **DataBuffer** of the SRB or must be a pointer from the **SenseInfoBuffer**. Otherwise, the given *VirtualAddress* must be in the miniport driver's uncached extension, the **SrbExtension**, or the **SenseInfoBuffer**.

A miniport driver can call **ScsiPortGetPhysicalAddress** to translate an extension address only if that miniport driver's **DriverEntry** routine set **NeedPhysicalAddresses** to **TRUE** in the HW\_INITIALIZATION\_DATA when it called **ScsiPortInitialize**.

Due to constraints on some buses, such as ISA, the address returned by this routine is not guaranteed to match the address returned by an analogous outside routine (such as **MmGetPhysicalAddress**). A miniport driver should call only **ScsiPort***Xxx* routines to be portable.

**ScsiPortGetPhysicalAddress** uses **SCSI\_PHYSICAL\_ADDRESS** to represent physical addresses.


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

[**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md)
</dt> <dt>

[**DriverEntry of SCSI Miniport Driver**](driverentry-of-scsi-miniport-driver.md)
</dt> <dt>

[**ScsiPortGetUncachedExtension**](scsiportgetuncachedextension.md)
</dt> <dt>

[**ScsiPortGetVirtualAddress**](scsiportgetvirtualaddress.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortGetPhysicalAddress%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






