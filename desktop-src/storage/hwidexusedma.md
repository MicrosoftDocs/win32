---
title: HwIdeXUseDma routine
description: The IDE controller driver calls the minidriver routine HwIdeXUseDma prior to an I/O operation, in order to determine whether I/O can be done by means of DMA.
ms.assetid: '718af7c3-0c57-4397-9fe0-3cdc4b578f53'
keywords: ["HwIdeXUseDma routine Storage Devices", "PCIIDE_USEDMA_FUNC"]
topic_type:
- apiref
api_name:
- HwIdeXUseDma
api_location:
- ide.h
api_type:
- UserDefined
---

# HwIdeXUseDma routine

The IDE controller driver calls the minidriver routine *HwIdeXUseDma* prior to an I/O operation, in order to determine whether I/O can be done by means of DMA.

## Syntax


```C++
PCIIDE_USEDMA_FUNC HwIdeXUseDma;

ULONG HwIdeXUseDma(
  _In_ PVOID DeviceExtension,
  _In_ PVOID CdbCommand,
  _In_ UCHAR Subordinate
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Contains a pointer to the IDE controller minidriver's device extension.

</dd> <dt>

*CdbCommand* \[in\]
</dt> <dd>

Contains a pointer to a control data block (CDB) structure containing the I/O operation to be requested.

</dd> <dt>

*Subordinate* \[in\]
</dt> <dd>

Specifies whether the IDE device is a secondary (subordinate) or a primary (master) device. This parameter must be set to one (1) if the device is a subordinate and to zero (0) if the device is a master.

</dd> </dl>

## Return value

*HwIdeXUseDma* returns one (1) if DMA is allowed and zero (0) if DMA is not allowed.

## Remarks

*HwIdeXUseDma* determines whether DMA is appropriate, based on the sort of command indicated in *CdbCommand* and the type of IDE controller chipset that the minidriver manages.

If *HwIdeXUseDma* returns zero, the controller driver must complete the data transfer in PIO mode instead of DMA mode.

When the controller driver calls minidriver's [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) routine, it passes an [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure to the minidriver. The minidriver must store a pointer to *HwIdeXUseDma* in this structure.

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
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwIdeXUseDma%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






