---
title: ACCESS\_RANGE structure
description: An ACCESS\_RANGE describes a memory or I/O port range used by an HBA.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: 6009d11b-4f44-4591-bcb8-66e0c42d5689
keywords:
- ACCESS_RANGE structure Storage Devices
- PACCESS_RANGE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ACCESS_RANGE
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

# ACCESS\_RANGE structure

An ACCESS\_RANGE describes a memory or I/O port range used by an HBA.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _ACCESS_RANGE {
  SCSI_PHYSICAL_ADDRESS RangeStart;
  ULONG                 RangeLength;
  BOOLEAN               RangeInMemory;
} ACCESS_RANGE, *PACCESS_RANGE;
```



## Members

<dl> <dt>

**RangeStart**
</dt> <dd>

Contains an address of type [SCSI\_PHYSICAL\_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff565350) that specifies the bus-relative base address of the range. This is an address that can be passed into [**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md).

</dd> <dt>

**RangeLength**
</dt> <dd>

Specifies the size, in bytes, or number of ports in the range. A miniport driver must ensure that this value matches the range actually decoded by the adapter. For example, if the HBA uses seven registers but responds to eight, this member should be set to 8.

</dd> <dt>

**RangeInMemory**
</dt> <dd>

Indicates the range is in memory when **TRUE**, rather than in I/O space. When **FALSE**, the range is in I/O space.

</dd> </dl>

## Remarks

Each ACCESS\_RANGE is an **AccessRanges** array element within the PORT\_CONFIGURATION\_INFORMATION structure that is passed to a miniport driver's HwScsiFindAdapter routine.

If possible, the OS-specific port driver sets up each access range element with a bus-relative HBA range for the miniport driver before calling the miniport driver's HwScsiFindAdapter routine. Otherwise, the port driver zeros range elements for which it cannot supply configuration information.

If the port driver does supply a range, the miniport driver's HwScsiFindAdapter routine should use only the supplied addresses and should *never* attempt to find other HBAs on the same bus using addresses of its own devising. Attempting to access other bus-relative port or memory ranges when the port driver has supplied range information, particularly in x86-only systems in which some devices are initialized in x86 real mode, can cause other devices on the bus to fail initialization or even cause the system to fail the boot process.

Each miniport driver should have a set of bus-relative default ranges to try if the OS-specific port driver cannot supply the information. A miniport driver must call **ScsiPortValidateRange** to check the safety of any miniport driver-supplied access range *before* it attempts to map such a range with **ScsiPortGetDeviceBase** and use the returned logical addresses to access an adapter, particularly if one of its HBAs has a BIOS.

Any access range that a miniport driver fills in for the OS-specific port driver in the PORT\_CONFIGURATION\_INFORMATION must have the **RangeStart** member set to a bus-relative address, such as a value returned by **ScsiPortGetBusData**.

The corresponding base logical address returned by **ScsiPortGetDeviceBase** should be stored, usually in the miniport driver's device extension, as the **RangeStart** address for a mapped range of I/O ports or memory addresses used to call the **ScsiPortRead***Xxx* and **ScsiPortWrite***Xxx* routines.

## Requirements



|                   |                                                                                                                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Srb.h (include Srb.h, Storport.h, or Strmini.h)</dt> </dl> |



## See also

<dl> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[**ScsiPortConvertUlongToPhysicalAddress**](scsiportconvertulongtophysicaladdress.md)
</dt> <dt>

[**ScsiPortGetBusData**](scsiportgetbusdata.md)
</dt> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> <dt>

[**ScsiPortValidateRange**](scsiportvalidaterange.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ACCESS_RANGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






