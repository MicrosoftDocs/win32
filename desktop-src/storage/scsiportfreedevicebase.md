---
title: ScsiPortFreeDeviceBase routine
description: The ScsiPortFreeDeviceBase routine frees a range of device I/O or memory space addresses previously mapped into the system address space with ScsiPortGetDeviceBase.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 391f3b20-175f-4b27-b30f-34ccc43ca650
keywords:
- ScsiPortFreeDeviceBase routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortFreeDeviceBase
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

# ScsiPortFreeDeviceBase routine

The **ScsiPortFreeDeviceBase** routine frees a range of device I/O or memory space addresses previously mapped into the system address space with **ScsiPortGetDeviceBase**.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortFreeDeviceBase(
  _In_ PVOID HwDeviceExtension,
  _In_ PVOID MappedAddress
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*MappedAddress* \[in\]
</dt> <dd>

Pointer to the base address of the range to be freed. This address must be the same as that returned by [**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md).

</dd> </dl>

## Return value

None

## Remarks

If a miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine determines that the driver does not need a particular mapped base address for an adapter, it must release the mapping by calling this routine. For example, when a miniport driver determines there are no supported HBAs on a particular I/O bus, it must call **ScsiPortFreeDeviceBase** with each mapped address returned by **ScsiPortGetDeviceBase**, if any calls to this routine were made.

**ScsiPortFreeDeviceBase** can be called only from miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine. Calls from other miniport driver routines will result in system failure or incorrect operation for the caller.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**ScsiPortGetDeviceBase**](scsiportgetdevicebase.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortFreeDeviceBase%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






