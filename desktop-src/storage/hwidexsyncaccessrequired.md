---
title: HwIdeXSyncAccessRequired routine
description: The HwIdeXSyncAccessRequired routine indicates whether both channels of its controller can be accessed at once.
ms.assetid: 0e330c05-708b-4b36-944a-c8bfdc6bde56
keywords:
- HwIdeXSyncAccessRequired routine Storage Devices
- PCIIDE_SYNC_ACCESS_REQUIRED
topic_type:
- apiref
api_name:
- HwIdeXSyncAccessRequired
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

# HwIdeXSyncAccessRequired routine

The *HwIdeXSyncAccessRequired* routine indicates whether both channels of its controller can be accessed at once.

## Syntax


```C++
PCIIDE_SYNC_ACCESS_REQUIRED HwIdeXSyncAccessRequired;

BOOLEAN HwIdeXSyncAccessRequired(
  _In_ PVOID DeviceExtension
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Contains a pointer to the IDE controller minidriver's device extension.

</dd> </dl>

## Return value

*HwIdeXSyncAccessRequired* returns **TRUE** if the controller only allows one channel to be accessed at a time; otherwise it returns **FALSE**.

## Remarks

*HwIdeXSyncAccessRequired* determines whether both channels of its controller can be accessed at once by comparing the controller's Vendor ID and Device ID with a list of the Vendor ID and Device ID of IDE controllers that are known to be single FIFO controllers. The Vendor ID and Device ID of the IDE controller is obtained by consulting the PCI configuration data stored in *DeviceExtension*.

When the controller driver calls minidriver's [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) routine, it passes an [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure to the minidriver. The minidriver must store a pointer to *HwIdeXSyncAccessRequired* in this structure.

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

[**PciIdeXGetBusData**](pciidexgetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwIdeXSyncAccessRequired%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






