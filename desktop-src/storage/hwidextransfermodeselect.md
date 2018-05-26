---
title: HwIdeXTransferModeSelect routine
description: The HwIdeTransferModeSelect routine returns the best PIO mode and the best DMA mode for each device indicated in XferMode.
ms.assetid: a25c05d7-d054-407a-a9c3-5dd24537e434
keywords:
- HwIdeXTransferModeSelect routine Storage Devices
- PCIIDE_TRANSFER_MODE_SELECT_FUNC
topic_type:
- apiref
api_name:
- HwIdeXTransferModeSelect
api_location:
- ide.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HwIdeXTransferModeSelect routine

The *HwIdeTransferModeSelect* routine returns the best PIO mode and the best DMA mode for each device indicated in *XferMode*.

## Syntax


```C++
PCIIDE_TRANSFER_MODE_SELECT_FUNC HwIdeXTransferModeSelect;

NTSTATUS HwIdeXTransferModeSelect(
  _In_    PVOID                        DeviceExtension ,
  _Inout_ PPCIIDE_TRANSFER_MODE_SELECT XferMode 
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Contains a pointer to the IDE controller minidriver's device extension.

</dd> <dt>

*XferMode* \[in, out\]
</dt> <dd>

Contains a pointer to a [**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md) structure supplied by the caller that is used to furnish the IDE controller minidriver with device information and to report which transfer modes the minidriver selects for each device.

</dd> </dl>

## Return value

*HwIdeXChannelTransferMode* returns STATUS\_SUCCESS if the transfer mode data is successfully retrieved; otherwise, returns STATUS\_UNSUCCESSFUL.

## Remarks

*HwIdeTransferModeSelect* queries the IDE controller minidriver to determine what the best available PIO and DMA modes are for each device in a list of devices furnished in the *XferMode* structure. It determines this by considering both the characteristics of each device as specified in *XferMode* and the hardware characteristics of the IDE controller itself. The calling routine must provide the relevant device characteristics, such as the device's best PIO, best single-word DMA, best multiword DMA, and best ultra DMA cycle times, in *XferMode*.

For a detailed summary of the information required by *HwIdeXTransferModeSelect*, see [**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md).

When the controller driver calls minidriver's [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) routine, it passes an [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure to the minidriver. The minidriver must store a pointer to *HwIdeXTransferModeSelect* in this structure.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md)
</dt> <dt>

[**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md)
</dt> <dt>

[**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwIdeXTransferModeSelect%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






