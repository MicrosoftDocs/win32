---
Description: 'Halftone palettes are intended to be used whenever the stretching mode of a device context is set to HALFTONE.'
ms.assetid: 'ee171379-2ab3-4c38-8e86-ff80fa63a357'
title: Halftone Palette and Color Adjustment
---

# Halftone Palette and Color Adjustment

Halftone palettes are intended to be used whenever the stretching mode of a device context is set to HALFTONE. An application creates a halftone palette by using the [**CreateHalftonePalette**](createhalftonepalette.md) function. The application must select and realize this palette into the device context before calling the [**StretchBlt**](stretchblt.md) or [**StretchDIBits**](stretchdibits.md) function.

The system automatically adjusts the input color of source bitmaps whenever applications call the [**StretchBlt**](stretchblt.md) and [**StretchDIBits**](stretchdibits.md) functions and the stretching mode of a device context is set to HALFTONE. These color adjustments affect certain attributes of the image, such as contrast and brightness. An application can set the color adjustment values by using the [**SetColorAdjustment**](setcoloradjustment.md) function. The application can retrieve the color adjustment values for the specified device context by using the [**GetColorAdjustment**](getcoloradjustment.md) function.

 

 



