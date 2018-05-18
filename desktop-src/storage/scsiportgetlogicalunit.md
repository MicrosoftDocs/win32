---
title: ScsiPortGetLogicalUnit routine
description: The ScsiPortGetLogicalUnit routine returns a pointer to the miniport driver's per-LU storage area for a given peripheral.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '10088043-fc0b-4df9-a5bf-fdee9740b88a'
keywords: ["ScsiPortGetLogicalUnit routine Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiPortGetLogicalUnit
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
---

# ScsiPortGetLogicalUnit routine

The **ScsiPortGetLogicalUnit** routine returns a pointer to the miniport driver's per-LU storage area for a given peripheral.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PVOID ScsiPortGetLogicalUnit(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Identifies the target controller or device on the bus.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Identifies the logical unit number of the target device.

</dd> </dl>

## Return value

**ScsiPortGetLogicalUnit** returns a pointer to the miniport driver's storage area for the requested logical unit. If the operating system-specific port driver considers this logical unit to be nonexistent, it returns **NULL**.

## Remarks

**ScsiPortGetLogicalUnit** is irrelevant if the miniport driver's **DriverEntry** routine specified zero for the **LuExtensionSize** in the HW\_INITIALIZATION\_DATA when it called **ScsiPortInitialize**. Otherwise, the operating system-specific port driver allocates and initializes with zeros a set of LU extensions of the specified size for the miniport driver to use.

Per-LU storage can be used to store data relevant to a particular peripheral, such as saved data pointers. To access this area, the miniport driver calls **ScsiPortGetLogicalUnit** when the driver is maintaining information about the state of or current operation for any particular peripheral.

The operating system-specific port driver can consider a logical unit to be nonexistent if there is no active request for that logical unit and the device has never been successfully selected.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**DriverEntry of SCSI Miniport Driver**](driverentry-of-scsi-miniport-driver.md)
</dt> <dt>

[**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> <dt>

[**ScsiPortMoveMemory**](scsiportmovememory.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortGetLogicalUnit%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






