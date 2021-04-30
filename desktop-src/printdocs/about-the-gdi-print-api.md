---
description: One of the chief features of the functions in the GDI print API is their support of device independence.
ms.assetid: 3efcc6d0-14f0-4605-9603-ccc7ad0cc895
title: About the GDI Print API
ms.topic: article
ms.date: 05/31/2018
---

# About the GDI Print API

One of the chief features of the functions in the GDI print API is their support of device independence. Instead of issuing device-specific commands to draw output on a particular printer or plotter, an application calls high-level functions from the graphics device interface (GDI). For example, to print a bitmapped image, an application can call the [**BitBlt**](/windows/desktop/api/wingdi/nf-wingdi-bitblt) function, supplying the coordinates for the bitmap as well as handles identifying the source and destination device contexts (DCs). The call to **BitBlt** is then converted to raw device commands by a printer driver. A device driver is a dynamic-link library (DLL) that supports the device driver interface (DDI). A device driver generates raw device commands when it processes calls to DDI functions made by the graphics engine. The commands are processed by the printer when it prints the image. The syntax, number, and type of these commands vary from device to device.

This overview provides information on the following topics.

<dl>

[Default Printing Interface](default-printing-interface.md)  
[Printer Device Contexts](printer-output.md)  
[Printer Escapes](printer-escapes.md)  
[WYSIWYG Display and Output](wysiwyg-display-and-output.md)  
[Per-User DEVMODE](per-user-devmode.md)  
</dl>

 

 
