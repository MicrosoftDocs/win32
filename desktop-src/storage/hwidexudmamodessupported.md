---
title: HwIdeXUdmaModesSupported routine
description: The HwIdeXUdmaModeSupported routine indicates which ultra direct memory access (UDMA) transfer mode is current and which is best for the device indicated by IdentifyData.
ms.assetid: 'afc0d7f7-b8cd-41ed-8c96-84461bb11a06'
keywords: ["HwIdeXUdmaModesSupported routine Storage Devices", "PCIIDE_UDMA_MODES_SUPPORTED"]
topic_type:
- apiref
api_name:
- HwIdeXUdmaModesSupported
api_location:
- ide.h
api_type:
- UserDefined
---

# HwIdeXUdmaModesSupported routine

The *HwIdeXUdmaModeSupported* routine indicates which ultra direct memory access (UDMA) transfer mode is current and which is best for the device indicated by *IdentifyData*.

## Syntax


```C++
PCIIDE_UDMA_MODES_SUPPORTED HwIdeXUdmaModesSupported;

NTSTATUS HwIdeXUdmaModesSupported(
   IDENTIFY_DATA IdentifyData,
   PULONG        BestXferMode,
   PULONG        CurrentXferMode
)
{ ... }
```



## Parameters

<dl> <dt>

*IdentifyData* 
</dt> <dd>

Specifies a structure containing the IDENTIFY DEVICE information defined in the *ATA/ATAPI-5 specification*. Minidrivers retrieve this data in the [**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md) structure with a call to *HwIdeXTransferModeSelect*. For further information about the contents of this structure, see the *ATA/ATAPI-5 specification*.

</dd> <dt>

*BestXferMode* 
</dt> <dd>

Indicates the highest UDMA mode supported by this device.

</dd> <dt>

*CurrentXferMode* 
</dt> <dd>

Indicates the currently active UDMA mode on this device.

</dd> </dl>

## Return value

*HwIdeXUdmaModesSupported* returns STATUS\_SUCCESS if the operation was a success; otherwise, it returns STATUS\_UNSUCCESSFUL.

## Remarks

*HwIdeXUdmaModesSupported* interprets the identify data for a device and determines both the currently active UDMA mode and the best possible UDMA mode supported by the device. For example, if UDMA mode four is the best transfer mode that the device supports and UDMA mode two is the currently active UDMA mode, the routine should return *BestXferMode* = 4 and *CurrentXferMode* = 2.

This routine makes IDE controller drivers more extensible. If a new UDMA mode is added to the *ATA/ATAPI specification*, you only need to change this routine to interpret the new information in the identify data.

When the controller driver calls the minidriver's [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) routine, it passes a [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure to the minidriver. The minidriver must store a pointer to *HwIdeXUdmaModesSupported* in this structure.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |



## See also

<dl> <dt>

[**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md)
</dt> <dt>

[**HwIdeXTransferModeSelect**](hwidextransfermodeselect.md)
</dt> <dt>

[**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md)
</dt> <dt>

[**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwIdeXUdmaModesSupported%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






