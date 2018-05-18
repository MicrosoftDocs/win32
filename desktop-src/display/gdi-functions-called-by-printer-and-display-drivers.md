---
Description: GDI Functions Called by Printer and Display Drivers
ms.assetid: '1f316fd2-59a2-486c-b58e-c06a3dcd08c1'
title: GDI Functions Called by Printer and Display Drivers
---

# GDI Functions Called by Printer and Display Drivers

## 

This section provides reference information for system-supplied GDI functions that can be called by both display and printer drivers.

Display adapter drivers that run on Windows Vista can adhere to one of two models: the Windows Vista display driver model or the Windows 2000 display driver model. The functions documented in this section are called by printer drivers and by drivers in the Windows 2000 display driver model, but they are not called by drivers in the Windows Vista display driver model.

The set of system-supplied GDI functions can be broken into the following groups:

-   **Eng***Xxx* functions. These are general graphics engine services.

-   ***XXX*OBJ\_***Xxx* functions. These specialized service routines are related to a particular object.

[GDI Support for Graphics Drivers](display.gdi_support_for_graphics_drivers) lists the include files that contain declarations for the functions described in this section.

Reference material for functions that are implemented by printer drivers and display drivers (Windows 2000 model) can be found in [GDI Functions Implemented by Printer and Display Drivers](gdi-functions-implemented-by-printer-and-display-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdisplay\display%5D:%20GDI%20Functions%20Called%20by%20Printer%20and%20Display%20Drivers%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



