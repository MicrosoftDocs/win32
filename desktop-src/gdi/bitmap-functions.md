---
Description: The following functions are used with bitmaps.
ms.assetid: ef3abc8a-5d95-41d0-8eb6-47719d472414
title: Bitmap Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bitmap Functions

The following functions are used with bitmaps.



| Function                                                 | Description                                                    |
|----------------------------------------------------------|----------------------------------------------------------------|
| [**AlphaBlend**](/windows/win32/WinGdi/nf-wingdi-alphablend?branch=master)                         | Displays a bitmap with transparent or semitransparent pixels.  |
| [**BitBlt**](/windows/win32/Wingdi/nf-wingdi-bitblt?branch=master)                                 | Performs a bit-block transfer.                                 |
| [**CreateBitmap**](/windows/win32/Wingdi/nf-wingdi-createbitmap?branch=master)                     | Creates a bitmap.                                              |
| [**CreateBitmapIndirect**](/windows/win32/Wingdi/nf-wingdi-createbitmapindirect?branch=master)     | Creates a bitmap.                                              |
| [**CreateCompatibleBitmap**](/windows/win32/Wingdi/nf-wingdi-createcompatiblebitmap?branch=master) | Creates a bitmap compatible with a device.                     |
| [**CreateDIBitmap**](/windows/win32/Wingdi/nf-wingdi-createdibitmap?branch=master)                 | Creates a device-dependent bitmap (DDB) from a DIB.            |
| [**CreateDIBSection**](/windows/win32/Wingdi/nf-wingdi-createdibsection?branch=master)             | Creates a DIB that applications can write to directly.         |
| [**ExtFloodFill**](/windows/win32/Wingdi/nf-wingdi-extfloodfill?branch=master)                     | Fills an area of the display surface with the current brush.   |
| [**GetBitmapDimensionEx**](/windows/win32/Wingdi/nf-wingdi-getbitmapdimensionex?branch=master)     | Gets the dimensions of a bitmap.                               |
| [**GetDIBColorTable**](/windows/win32/Wingdi/nf-wingdi-getdibcolortable?branch=master)             | Retrieves RGB color values from a DIB section bitmap.          |
| [**GetDIBits**](/windows/win32/Wingdi/nf-wingdi-getdibits?branch=master)                           | Copies a bitmap into a buffer.                                 |
| [**GetPixel**](/windows/win32/Wingdi/nf-wingdi-getpixel?branch=master)                             | Gets the RGB color value of the pixel at a given coordinate.   |
| [**GetStretchBltMode**](/windows/win32/Wingdi/nf-wingdi-getstretchbltmode?branch=master)           | Gets the current stretching mode.                              |
| [**GradientFill**](/windows/win32/WinGdi/nf-wingdi-gradientfill?branch=master)                     | Fills rectangle and triangle structures.                       |
| [**LoadBitmap**](/windows/win32/Winuser/nf-winuser-loadbitmapa?branch=master)                         | Loads a bitmap from a module's executable file.                |
| [**MaskBlt**](/windows/win32/Wingdi/nf-wingdi-maskblt?branch=master)                               | Combines the color data in the source and destination bitmaps. |
| [**PlgBlt**](/windows/win32/Wingdi/nf-wingdi-plgblt?branch=master)                                 | Performs a bit-block transfer.                                 |
| [**SetBitmapDimensionEx**](/windows/win32/Wingdi/nf-wingdi-setbitmapdimensionex?branch=master)     | Sets the preferred dimensions to a bitmap.                     |
| [**SetDIBColorTable**](/windows/win32/Wingdi/nf-wingdi-setdibcolortable?branch=master)             | Sets RGB values in a DIB.                                      |
| [**SetDIBits**](/windows/win32/Wingdi/nf-wingdi-setdibits?branch=master)                           | Sets the pixels in a bitmap using color data from a DIB.       |
| [**SetDIBitsToDevice**](/windows/win32/Wingdi/nf-wingdi-setdibitstodevice?branch=master)           | Sets the pixels in a rectangle using color data from a DIB.    |
| [**SetPixel**](/windows/win32/Wingdi/nf-wingdi-setpixel?branch=master)                             | Sets the color for a pixel.                                    |
| [**SetPixelV**](/windows/win32/Wingdi/nf-wingdi-setpixelv?branch=master)                           | Sets a pixel to the best approximation of a color.             |
| [**SetStretchBltMode**](/windows/win32/Wingdi/nf-wingdi-setstretchbltmode?branch=master)           | Sets the bitmap stretching mode.                               |
| [**StretchBlt**](/windows/win32/Wingdi/nf-wingdi-stretchblt?branch=master)                         | Copies a bitmap and stretches or compresses it.                |
| [**StretchDIBits**](/windows/win32/Wingdi/nf-wingdi-stretchdibits?branch=master)                   | Copies the color data in a DIB.                                |
| [**TransparentBlt**](/windows/win32/WinGdi/nf-wingdi-transparentblt?branch=master)                 | Performs a bit-block transfer of color data.                   |



 

## Obsolete Functions

The following functions are provided only for compatibility with 16-bit versions of Microsoft Windows:

-   [**CreateDiscardableBitmap**](/windows/win32/Wingdi/nf-wingdi-creatediscardablebitmap?branch=master)
-   [**FloodFill**](/windows/win32/Wingdi/nf-wingdi-floodfill?branch=master)
-   [**GetBitmapBits**](/windows/win32/Wingdi/nf-wingdi-getbitmapbits?branch=master)
-   [**SetBitmapBits**](/windows/win32/Wingdi/nf-wingdi-setbitmapbits?branch=master)

 

 



