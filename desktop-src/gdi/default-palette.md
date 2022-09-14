---
description: The default palette is an array of color values identifying the colors that can be used with a device context by default.
ms.assetid: 7972d5da-2b73-4cd7-a2ee-fca3a571f611
title: Default Palette
ms.topic: article
ms.date: 05/31/2018
---

# Default Palette

The *default palette* is an array of color values identifying the colors that can be used with a device context by default. the system associates the default palette with a context whenever an application creates a context for a device that supports color palettes. The default palette ensures that colors are available for use by an application without any further action.

The default palette typically has 20 entries (colors), but the exact number of entries may vary from device to device. This number is equal to the NUMCOLORS value returned by the [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function. An application can retrieve the color values for colors in the default palette by enumerating solid pens, the same technique used to discover the colors available on nonpalette devices. The colors in the default palette depend on the device. Display devices, for example, often use the 16 standard colors of the VGA display and 4 other colors defined by Windows. Print devices may use other default colors.

When using the default palette, applications use color values to specify pen and text colors. If the requested color is not in the palette, The system approximates the color by using the closest color in the palette. If an application requests a solid brush color that is not in the palette, the system simulates the color by dithering with colors that are in the palette.

To avoid approximations and dithering, applications can also specify pen, brush, and text colors by using color palette indexes rather than color values. A color palette index is an integer value that identifies a specific palette entry. Applications can use color palette indexes in place of color values but must use the [**PALETTEINDEX**](/windows/desktop/api/Wingdi/nf-wingdi-paletteindex) macro to create the indexes.

Color palette indexes are only useful for devices that support color palettes. To avoid this device dependence, applications that use the same code to draw to both palette and nonpalette devices should use palette-relative color values to specify pen, brush, and text colors. These values are identical to color values except when creating solid brushes. (On palette devices, a solid brush color specified by a palette-relative color value is subject to color approximation instead of dithering.) Applications must use the [**PALETTERGB**](/windows/desktop/api/Wingdi/nf-wingdi-palettergb) macro to create palette-relative color values.

The system does not allow an application to change the entries in the default palette. To use colors other than those in the default palette, an application must create its own logical palette and select the palette into the device context.

 

 



