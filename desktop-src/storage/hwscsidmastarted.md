---
title: PHW\_DMA\_STARTED routine
description: If the HBA is a subordinate DMA device, the miniport driver's HwScsiDmaStarted routine is called after the operating system-specific port driver has set up the system DMA controller for a DMA transfer.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: e4fdb22b-d88c-4544-947f-4d0c3836404c
keywords:
- HwScsiDmaStarted routine Storage Devices
- PHW_DMA_STARTED
topic_type:
- apiref
api_name:
- HwScsiDmaStarted
api_location:
- miniport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PHW\_DMA\_STARTED routine

If the HBA is a subordinate DMA device, the miniport driver's *HwScsiDmaStarted* routine is called after the operating system-specific port driver has set up the system DMA controller for a DMA transfer.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PVOID HwScsiDmaStarted(
  _In_ PVOID HwDeviceExtension
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

None.

## Remarks

Only miniport drivers of subordinate DMA adapters must have a *HwScsiDmaStarted* routine.

*HwScsiDmaStarted* is responsible for programming the HBA for the transfer operation.

Miniport drivers of HBAs that are busmasters or use programmed I/O do not supply this routine.

The name *HwScsiDmaStarted* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
VOID
(*PHW_DMA_STARTED) (
  IN PVOID  DeviceExtension
  );
```



For more information about the *HwScsiDmaStarted* routine, see [SCSI Miniport Driver's HwScsiDmaStarted Routine](https://msdn.microsoft.com/library/windows/hardware/ff565322).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortFlushDma**](scsiportflushdma.md)
</dt> <dt>

[**ScsiPortIoMapTransfer**](scsiportiomaptransfer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_DMA_STARTED%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






