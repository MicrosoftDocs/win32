---
title: ATA Controller Interface Routines
description: ATA Controller Interface Routines
ms.assetid: e6d57edc-705c-4c99-850f-83cfde02ff35
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ATA Controller Interface Routines

## 

Every vendor-supplied miniport driver is required to implement a set of routines that define the controller interface. By using these routines, the miniport driver communicates with the system-supplied controller driver, *Pciidex.sys*.

A vendor-supplied miniport driver communicates with the controller driver to initialize both port and miniport drivers and to exchange parameters that are required to configure the host bus adapter (HBA). Some routines in this section are optional. If you choose not to implement an optional routine, you must make sure that the miniport driver sets the corresponding function pointers in the [**IDE\_CONTROLLER\_INTERFACE**](ide-controller-interface.md) structure to **NULL**. If a routine is not explicitly identified in this section as optional, it is required.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

This section describes the following routines:

<dl>

[**DriverEntry**](driverentry.md)  
[**AtaAdapterControl**](ataadaptercontrol.md)  
[**AtaControllerChannelEnabled**](atacontrollerchannelenabled.md)  
[**AtaControllerTransferModeSelect**](atacontrollertransfermodeselect.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA%20Controller%20Interface%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




