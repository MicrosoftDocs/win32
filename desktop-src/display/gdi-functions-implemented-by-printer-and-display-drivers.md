---
Description: GDI Functions Implemented by Printer and Display Drivers
ms.assetid: c5480816-eeed-4fbf-bda3-874977b364fb
title: GDI Functions Implemented by Printer and Display Drivers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GDI Functions Implemented by Printer and Display Drivers

## 

This section provides reference information for functions that are implemented by display and/or printer driver writers. Most of these functions are named with a *Drv* prefix. The [Display Devices Design Guide](https://www.bing.com/search?q=Display+Devices+Design+Guide) describes which functions are required, conditionally required, or optional in a graphics driver's implementation.

[Using the Graphics DDI](https://www.bing.com/search?q=Using+the+Graphics+DDI) lists the include files that contain declarations for the graphics driver functions described in this section.

The system-supplied GDI services that can be called by graphics drivers are documented in [GDI Functions Called by Printer and Display Drivers](gdi-functions-called-by-printer-and-display-drivers.md).

Display adapter drivers that run on Windows Vista can adhere to one of two models: the Windows Vista display driver model or the Windows 2000 display driver model. The functions documented in this section are implemented by printer drivers and by drivers in the Windows 2000 display driver model, but they are not implemented by drivers in the Windows Vista display driver model.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdisplay\display%5D:%20GDI%20Functions%20Implemented%20by%20Printer%20and%20Display%20Drivers%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



