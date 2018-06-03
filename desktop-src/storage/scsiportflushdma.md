---
title: ScsiPortFlushDma routine
description: The ScsiPortFlushDma routine flushes any data cached in the system DMA controller at the end of a transfer or terminates a system DMA transfer.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: 9cf4286b-1ff7-4113-a2dc-d8813c633dd6
keywords:
- ScsiPortFlushDma routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortFlushDma
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

# ScsiPortFlushDma routine

The **ScsiPortFlushDma** routine flushes any data cached in the system DMA controller at the end of a transfer or terminates a system DMA transfer.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortFlushDma(
  _In_ PVOID DeviceExtension
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

None

## Remarks

Only miniport drivers of subordinate HBAs that use a system DMA controller call this routine.

**ScsiPortFlushDma** must be called after a subordinate DMA transfer operation is completed but before the SRB is completed or the next call is made to [**ScsiPortIoMapTransfer**](scsiportiomaptransfer.md) for the current buffer.

**ScsiPortFlushDma** also must be called after **ScsiPortIoMapTransfer** to cancel a DMA operation, even if no transfer has occurred and the driver's [**HwScsiDmaStarted**](hwscsidmastarted.md) routine has not yet been called.

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

[**ScsiPortIoMapTransfer**](scsiportiomaptransfer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortFlushDma%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






