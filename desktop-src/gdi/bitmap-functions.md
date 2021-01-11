---
description: The following functions are used with bitmaps.
ms.assetid: ef3abc8a-5d95-41d0-8eb6-47719d472414
title: Bitmap Functions (Windows GDI)
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Functions (Windows GDI)

The following functions are used with bitmaps.



| Function                                                 | Description                                                    |
|----------------------------------------------------------|----------------------------------------------------------------|
| [**AlphaBlend**](/windows/desktop/api/WinGdi/nf-wingdi-alphablend)                         | Displays a bitmap with transparent or semitransparent pixels.  |
| [**BitBlt**](/windows/desktop/api/Wingdi/nf-wingdi-bitblt)                                 | Performs a bit-block transfer.                                 |
| [**CreateBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmap)                     | Creates a bitmap.                                              |
| [**CreateBitmapIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmapindirect)     | Creates a bitmap.                                              |
| [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap) | Creates a bitmap compatible with a device.                     |
| [**CreateDIBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createdibitmap)                 | Creates a device-dependent bitmap (DDB) from a DIB.            |
| [**CreateDIBSection**](/windows/desktop/api/Wingdi/nf-wingdi-createdibsection)             | Creates a DIB that applications can write to directly.         |
| [**ExtFloodFill**](/windows/desktop/api/Wingdi/nf-wingdi-extfloodfill)                     | Fills an area of the display surface with the current brush.   |
| [**GetBitmapDimensionEx**](/windows/desktop/api/Wingdi/nf-wingdi-getbitmapdimensionex)     | Gets the dimensions of a bitmap.                               |
| [**GetDIBColorTable**](/windows/desktop/api/Wingdi/nf-wingdi-getdibcolortable)             | Retrieves RGB color values from a DIB section bitmap.          |
| [**GetDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-getdibits)                           | Copies a bitmap into a buffer.                                 |
| [**GetPixel**](/windows/desktop/api/Wingdi/nf-wingdi-getpixel)                             | Gets the RGB color value of the pixel at a given coordinate.   |
| [**GetStretchBltMode**](/windows/desktop/api/Wingdi/nf-wingdi-getstretchbltmode)           | Gets the current stretching mode.                              |
| [**GradientFill**](/windows/desktop/api/WinGdi/nf-wingdi-gradientfill)                     | Fills rectangle and triangle structures.                       |
| [**LoadBitmap**](/windows/desktop/api/Winuser/nf-winuser-loadbitmapa)                         | Loads a bitmap from a module's executable file.                |
| [**MaskBlt**](/windows/desktop/api/Wingdi/nf-wingdi-maskblt)                               | Combines the color data in the source and destination bitmaps. |
| [**PlgBlt**](/windows/desktop/api/Wingdi/nf-wingdi-plgblt)                                 | Performs a bit-block transfer.                                 |
| [**SetBitmapDimensionEx**](/windows/desktop/api/Wingdi/nf-wingdi-setbitmapdimensionex)     | Sets the preferred dimensions to a bitmap.                     |
| [**SetDIBColorTable**](/windows/desktop/api/Wingdi/nf-wingdi-setdibcolortable)             | Sets RGB values in a DIB.                                      |
| [**SetDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-setdibits)                           | Sets the pixels in a bitmap using color data from a DIB.       |
| [**SetDIBitsToDevice**](/windows/desktop/api/Wingdi/nf-wingdi-setdibitstodevice)           | Sets the pixels in a rectangle using color data from a DIB.    |
| [**SetPixel**](/windows/desktop/api/Wingdi/nf-wingdi-setpixel)                             | Sets the color for a pixel.                                    |
| [**SetPixelV**](/windows/desktop/api/Wingdi/nf-wingdi-setpixelv)                           | Sets a pixel to the best approximation of a color.             |
| [**SetStretchBltMode**](/windows/desktop/api/Wingdi/nf-wingdi-setstretchbltmode)           | Sets the bitmap stretching mode.                               |
| [**StretchBlt**](/windows/desktop/api/Wingdi/nf-wingdi-stretchblt)                         | Copies a bitmap and stretches or compresses it.                |
| [**StretchDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-stretchdibits)                   | Copies the color data in a DIB.                                |
| [**TransparentBlt**](/windows/desktop/api/WinGdi/nf-wingdi-transparentblt)                 | Performs a bit-block transfer of color data.                   |



 

## Obsolete Functions

The following functions are provided only for compatibility with 16-bit versions of Microsoft Windows:

-   [**CreateDiscardableBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-creatediscardablebitmap)
-   [**FloodFill**](/windows/desktop/api/Wingdi/nf-wingdi-floodfill)
-   [**GetBitmapBits**](/windows/desktop/api/Wingdi/nf-wingdi-getbitmapbits)
-   [**SetBitmapBits**](/windows/desktop/api/Wingdi/nf-wingdi-setbitmapbits)

 

 



