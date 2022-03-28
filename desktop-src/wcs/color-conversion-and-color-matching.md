---
title: Color Conversion and Color Matching
description: The process of converting colors from one color space to another is called color conversion.
ms.assetid: 52f68779-d4d6-4f1e-88a4-f872e9e90054
keywords:
- Windows Color System (WCS),color conversion
- WCS (Windows Color System),color conversion
- image color management,color conversion
- color management,color conversion
- colors,color conversion
- color conversion
- Windows Color System (WCS),color matching
- WCS (Windows Color System),color matching
- image color management,color matching
- color management,color matching
- colors,color matching
- color matching
- Windows Color System (WCS),color mapping
- WCS (Windows Color System),color mapping
- image color management,color mapping
- color management,color mapping
- colors,color mapping
- color mapping
- white point
- colorants
- gamma correction
- gamut


ms.topic: article
ms.date: 05/31/2018
---

# Color Conversion and Color Matching

The process of converting colors from one [color space](c.md) to another is called *color conversion*. All colors in a color space are fixed relative to the color space's [white point](w.md). Since the white point of a color space varies from device to device, a converted color must then be matched to its visually closest color in the destination color space. This process is called *color mapping*.

For example, if you have a digital image that you created on your display, it may be in a device-dependent RGB color space. If you want to print it on a printer, it must be converted to the printer's color space. Since the printer probably uses a device-dependent CMYK color space, all RGB values must be converted to CYMK. This is [color conversion](c.md). Once the values are specified in terms of the CYMK space, they need to be matched to the closest color that the printer can produce. This is called color mapping or [color matching](c.md).

Both color conversion and color mapping must take into account a number of device-specific factors. For instance, the building blocks of screen images are pixels. Each pixel has a set number of bits to store its color or color index value. The number of bits per pixel depends on the type of display and display adapter being used, and the mode to which that the adapter is set. Most every printer type uses different [colorants](c.md) and prints at particular resolutions.

In addition, the physical tone characteristics of a device are often different on different devices. For instance, when colors are produced by computer monitors, they can appear different than they would if they were produced on a printing press. A correction factor, called *gamma correction*, is frequently used to compensate for such differences.

The result of these device-dependent factors is that each color device has a particular set of colors that it can produce. This color set is known as its *gamut*. To perform color conversion and color mapping, the colors in an image must be converted from the color space and gamut of the source device into the color space of the destination device. They are then matched into the gamut of the destination device.

 

 




