---
description: Device independence is one of the chief features of Microsoft Windows.
ms.assetid: f2a4c4cf-55e9-4129-8067-256552af49d2
title: About Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# About Device Contexts

Device independence is one of the chief features of Microsoft Windows. Applications can draw and print output on a variety of devices. The software that supports this device independence is contained in two dynamic-link libraries. The first, Gdi.dll, is referred to as the graphics device interface (GDI); the second is referred to as a device driver. The name of the second depends on the device where the application draws output. For example, if the application draws output in the client area of its window on a VGA display, this library is Vga.dll; if the application prints output on an Epson FX-80 printer, this library is Epson9.dll.

An application must inform GDI to load a particular device driver and, once the driver is loaded, to prepare the device for drawing operations (such as selecting a line color and width, a brush pattern and color, a font typeface, a clipping region, and so on). These tasks are accomplished by creating and maintaining a device context (DC). A DC is a structure that defines a set of graphic objects and their associated attributes, and the graphic modes that affect output. The graphic objects include a pen for line drawing, a brush for painting and filling, a bitmap for copying or scrolling parts of the screen, a palette for defining the set of available colors, a region for clipping and other operations, and a path for painting and drawing operations. Unlike most of the structures, an application never has direct access to the DC; instead, it operates on the structure indirectly by calling various functions.

This overview provides information on the following topics:

-   [Graphic Objects](graphic-objects.md)
-   [Graphic Modes](graphic-modes.md)
-   [Device Context Types](device-context-types.md)
-   [Device Context Operations](device-context-operations.md)
-   [ICM-Enabled Device Context Functions](icm-enabled-device-context-functions.md)

An important concept is the layout of a DC or a window, which describes the order in which GDI objects and text are revealed (either left-to-right or right-to-left). For more information, see "Window Layout and Mirroring" in [**Window Features**](../winmsg/window-features.md) and the [**GetLayout**](/windows/desktop/api/Wingdi/nf-wingdi-getlayout) and [**SetLayout**](/windows/desktop/api/Wingdi/nf-wingdi-setlayout) functions.

 

 
