---
title: PHW\_DMA\_STARTED callback function
description: The PHW\_DMA\_STARTED routine prototype declares a SCSI miniport driver routine that starts DMA for subordinate DMA device.
ms.assetid: 2f989c46-e90e-45e1-a520-98b05ff78e73
keywords:
- ( PHW_DMA_STARTED) callback function Storage Devices
topic_type:
- apiref
api_name:
- ( PHW_DMA_STARTED)
api_location:
- srb.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PHW\_DMA\_STARTED callback function

The PHW\_DMA\_STARTED routine prototype declares a SCSI miniport driver routine that starts DMA for subordinate DMA device.

## Syntax


```C++
typedef VOID (*PHW_DMA_STARTED)(
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

If the HBA is a subordinate DMA device, the SCSI miniport driver's [**HwScsiDmaStarted**](hwscsidmastarted.md) routine is called after the OS-specific port driver has set up the system DMA controller for a DMA transfer.

Miniport drivers that work with the StorPort driver do not support adapters that require subordinate DMA.

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiDmaStarted**](hwscsidmastarted.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_DMA_STARTED%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






