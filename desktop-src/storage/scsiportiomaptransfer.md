---
title: ScsiPortIoMapTransfer routine
description: The ScsiPortIoMapTransfer routine sets up the system DMA controller for a miniport driver to transfer data through a subordinate HBA.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: 627a2d4c-22c8-48ea-b409-dc246c85a316
keywords:
- ScsiPortIoMapTransfer routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortIoMapTransfer
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

# ScsiPortIoMapTransfer routine

The **ScsiPortIoMapTransfer** routine sets up the system DMA controller for a miniport driver to transfer data through a subordinate HBA.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortIoMapTransfer(
  _In_ PVOID               HwDeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK Srb,
  _In_ PVOID               LogicalAddress,
  _In_ ULONG               Length
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

Pointer to the SCSI request block for the DMA transfer.

</dd> <dt>

*LogicalAddress* \[in\]
</dt> <dd>

Specifies the starting address for the transfer operation. This value can be the base address of a buffer into which or from which data is to be transferred. This value can be an offset within such a buffer.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

Specifies the number of bytes to be transferred.

</dd> </dl>

## Return value

None

## Remarks

Only miniport drivers of HBAs that use a system DMA controller (subordinate DMA) call **ScsiPortIoMapTransfer**. This routine must be called before such a miniport driver sets up its HBA to transfer data. The range specified by the *LogicalAddress* and *Length* must be within the buffer described by the given SRB.

After the operating system-specific port driver programs the system DMA controller, it calls the miniport driver's [**HwScsiDmaStarted**](hwscsidmastarted.md) routine. *HwScsiDmaStarted* should program the HBA to begin the data transfer. Note that an HBA can interrupt between the miniport driver's call to **ScsiPortIoMapTransfer** and the operating system-specific port driver's call to the miniport driver's *HwScsiDmaStarted* routine.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**HwScsiDmaStarted**](hwscsidmastarted.md)
</dt> <dt>

[**ScsiPortFlushDma**](scsiportflushdma.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortIoMapTransfer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






