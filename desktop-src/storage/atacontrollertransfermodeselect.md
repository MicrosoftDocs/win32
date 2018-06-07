---
title: AtaControllerTransferModeSelect routine
description: The AtaControllerTransferModeSelect miniport driver routine selects the transfer mode for all devices on the indicated ATA channel and programs the controller for the selected transfer mode.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 3ee46b54-791f-4eac-84d7-5a0093b6984a
keywords:
- AtaControllerTransferModeSelect routine Storage Devices
- IDE_TRANSFER_MODE_SELECT
topic_type:
- apiref
api_name:
- AtaControllerTransferModeSelect
api_location:
- irb.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AtaControllerTransferModeSelect routine

The ***AtaControllerTransferModeSelect*** miniport driver routine selects the transfer mode for all devices on the indicated ATA channel and programs the controller for the selected transfer mode.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_TRANSFER_MODE_SELECT AtaControllerTransferModeSelect;

BOOLEAN AtaControllerTransferModeSelect(
  _In_    PVOID                         ControllerExtension,
  _Inout_ PIDE_TRANSFER_MODE_PARAMETERS TransferModeParams
)
{ ... }
```



## Parameters

<dl> <dt>

*ControllerExtension* \[in\]
</dt> <dd>

A pointer to the controller extension.

</dd> <dt>

*TransferModeParams* \[in, out\]
</dt> <dd>

A pointer to a structure of type [**IDE\_TRANSFER\_MODE\_PARAMETERS**](ide-transfer-mode-parameters.md) that indicates to the miniport driver the channel on which to set the transfer modes and which transfer modes are available.

</dd> </dl>

## Return value

***AtaControllerTransferModeSelect*** returns **TRUE** to acknowledge the receipt of the transfer mode parameters. The miniport driver ignores a return value of **FALSE**.

## Remarks

The ***AtaControllerTransferModeSelect*** miniport driver routine must select the appropriate timing modes and program the controller for the selected modes. The miniport driver must select at least one programmed input/output (PIO) mode for the indicated channel, and preferably at least one direct memory access (DMA) timing mode also. To communicate to the caller the transfer modes that it selected, the miniport driver sets the appropriate bits in the **TransferModeSelected** member of the IDE\_TRANSFER\_MODE\_PARAMETERS structure.

***AtaControllerTransferModeSelect*** is an optional routine.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_TRANSFER\_MODE\_PARAMETERS**](ide-transfer-mode-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaControllerTransferModeSelect%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






