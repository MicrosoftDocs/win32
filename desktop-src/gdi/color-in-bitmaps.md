---
Description: 'The system handles colors in bitmaps differently than colors in pens, brushes, and text.'
ms.assetid: 'c315dd6e-87ee-4905-b193-186ea580ac0a'
title: Color in Bitmaps
---

# Color in Bitmaps

The system handles colors in bitmaps differently than colors in pens, brushes, and text. Compatible bitmaps, created by using the [**CreateBitmap**](createbitmap.md) or [**CreateCompatibleBitmap**](createcompatiblebitmap.md) function, are device specific and retain color information in a device-dependent format. No color values are used, and the colors are not subject to approximations and dithering.

Device-independent bitmaps (DIBs) retain color information either as color values or color palette indexes. If color values are used, the colors are subject to approximation, but not dithering. Color palette indexes can only be used with devices that support color palettes. Although the system does not approximate or dither colors identified by indexes, the resulting color may be different than that intended, because the indexes yield valid results only in the context of the color palette that was current at the time the bitmap was created. If the palette changes, so do the colors in the bitmap. For more information on palette indexes, see [Default Palette](default-palette.md) and [**PALETTEINDEX**](paletteindex.md).

In addition to referencing the logical palette, an application can also reference a value in a DIB color table. To select a color in a DIB color table, call [**DIBINDEX**](dibindex.md). Note that this is only possible for a device context that has a DIB selected into it.

 

 



