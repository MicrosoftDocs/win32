---
title: ScsiPortGetUncachedExtension routine
description: The ScsiPortGetUncachedExtension routine allocates memory that can be used by both the CPU and a bus-master HBA for DMA or for shared data.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: d32da7d9-7f26-4c99-8c10-3b9e1a7c9c22
keywords:
- ScsiPortGetUncachedExtension routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortGetUncachedExtension
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ScsiPortGetUncachedExtension routine

The **ScsiPortGetUncachedExtension** routine allocates memory that can be used by both the CPU and a bus-master HBA for DMA or for shared data.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PVOID ScsiPortGetUncachedExtension(
  _In_ PVOID                           HwDeviceExtension,
  _In_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
  _In_ ULONG                           NumberOfBytes
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*ConfigInfo* \[in\]
</dt> <dd>

Specifies information about the HBA's DMA capabilities. The following members must be filled in: **DmaChannel** or **DmaPort**, **DmaWidth**, **DmaSpeed**, **MaximumTransferLength**, **ScatterGather**, **Master** set to **TRUE**, **NumberOfPhysicalBreaks**, **AdapterInterfaceType**, **Dma32BitAddresses**, **SystemIoBusNumber**, **AutoRequestSense**, and **SrbExtensionSize.**

Members that are not pertinent to the HBA, such as **DmaChannel** for an EISA bus-master adapter, must be left as is.

</dd> <dt>

*NumberOfBytes* \[in\]
</dt> <dd>

Indicates the size in bytes of the uncached extension to be allocated. Drivers in Windows XP and earlier operating systems must not allocate more than 100 kilobytes of uncached extension, and if they participate in I/O operations on the hibernation file or the crash dump file, they must limit the amount of uncached extension that they allocate to under 32 kilobytes.

</dd> </dl>

## Return value

**ScsiPortGetUncachedExtension** returns a virtual address pointer to the uncached extension. If it cannot allocate the requested memory, it returns **NULL**.

## Remarks

**ScsiPortGetUncachedExtension** can be called only from miniport driver's [*HwScsiFindAdapter*](hwscsifindadapter.md) routine and only for a bus-master HBA. Calls from other miniport driver routines will result in system failure or incorrect operation for the caller.

Because high-end machines have caches and large memories, any memory to be shared between an HBA and the CPU must be specially allocated. Mailboxes or I/O request queues in system memory are examples of this type of shared memory.

A miniport driver must set **SrbExtensionSize.** before calling **ScsiPortGetUncachedExtension** to change the size of its per-request storage based on **NumberOfPhysicalBreaks**.

The [*HwScsiFindAdapter*](hwscsifindadapter.md) routine can call **ScsiPortGetUncachedExtension** only once for each bus-master HBA the miniport driver supports.

To obtain the physical address for the uncached extension that the HBA can use, call [**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md).

The ScsiPort driver will free the memory allocated by **ScsiPortGetUncachedExtension** when the adapter device is stopped.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortGetUncachedExtension%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






