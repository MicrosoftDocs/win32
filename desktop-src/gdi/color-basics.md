---
description: The color capabilities of devices, such as displays and printers, can range from monochrome to thousands of colors.
ms.assetid: 3d71c24c-77f4-4344-91c3-439052402fae
title: Color Basics
ms.topic: article
ms.date: 05/31/2018
---

# Color Basics

The color capabilities of devices, such as displays and printers, can range from monochrome to thousands of colors. Because an application may need to generate output for devices throughout this range, it should be prepared to handle varying color capabilities.

An application can discover the number of colors available for a given device by using the [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function to retrieve the NUMCOLORS value. This value specifies the count of colors available for use by the application. Usually, this count corresponds to a physical property of the output device, such as the number of inks in the printer or the number of distinct color signals the display adapter can transmit to the monitor.

Although the NUMCOLORS value specifies the count of colors, it does not identify what the available colors are. An application can discover what colors are available by enumerating all pens having the PS\_SOLID type. Because the device driver that supports a given device usually has a full range of solid pens and because the system requires that solid pens have only colors that the device can generate, enumerating these pens is often equivalent to enumerating the colors. An application can enumerate the pens by using the [**EnumObjects**](/windows/desktop/api/Wingdi/nf-wingdi-enumobjects) function. For a code example, see [Enumerating Colors](enumerating-colors.md).

For more information, see the following topics:

-   [Color Values](color-values.md)
-   [Color Approximations and Dithering](color-approximations-and-dithering.md)
-   [Color in Bitmaps](color-in-bitmaps.md)
-   [Color Mixing](color-mixing.md)

 

 



