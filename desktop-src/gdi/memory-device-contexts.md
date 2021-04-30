---
description: To enable applications to place output in memory rather than sending it to an actual device, use a special device context for bitmap operations called a memory device context.
ms.assetid: 0a682dc4-31a4-43c8-b0b1-ab01986b1dac
title: Memory Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Memory Device Contexts

To enable applications to place output in memory rather than sending it to an actual device, use a special device context for bitmap operations called a *memory device context*. A memory DC enables the system to treat a portion of memory as a virtual device. It is an array of bits in memory that an application can use temporarily to store the color data for bitmaps created on a normal drawing surface. Because the bitmap is compatible with the device, a memory DC is also sometimes referred to as a *compatible device context*.

The memory DC stores bitmap images for a particular device. An application can create a memory DC by calling the [**CreateCompatibleDC**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatibledc) function.

The original bitmap in a memory DC is simply a placeholder. Its dimensions are one pixel by one pixel. Before an application can begin drawing, it must select a bitmap with the appropriate width and height into the DC by calling the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function. To create a bitmap of the appropriate dimensions, use the [**CreateBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmap), [**CreateBitmapIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmapindirect), or [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap) function. After the bitmap is selected into the memory DC, the system replaces the single-bit array with an array large enough to store color information for the specified rectangle of pixels.

When an application passes the handle returned by [**CreateCompatibleDC**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatibledc) to one of the drawing functions, the requested output does not appear on a device's drawing surface. Instead, the system stores the color information for the resultant line, curve, text, or region in the array of bits. The application can copy the image stored in memory back onto a drawing surface by calling the [**BitBlt**](/windows/desktop/api/Wingdi/nf-wingdi-bitblt) function, identifying the memory DC as the source device context and a window or screen DC as the target device context.

When displaying a DIB or a DDB created from a DIB on a palette device, you can improve the speed at which the image is drawn by arranging the logical palette to match the layout of the system palette. To do this, call [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) with the NUMRESERVED value to get the number of reserved colors in the system. Then call [**GetSystemPaletteEntries**](/windows/desktop/api/Wingdi/nf-wingdi-getsystempaletteentries) and fill in the first and last NUMRESERVED/2 entries of the logical palette with the corresponding system colors. For example, if NUMRESERVED is 20, you would fill in the first and last 10 entries of the logical palette with the system colors. Then fill in the remaining 256-NUMRESERVED colors of the logical palette (in our example, the remaining 236 colors) with colors from the DIB and set the PC\_NOCOLLAPSE flag on each of these colors.

For more information about color and palettes, see [Colors](colors.md). For more information about bitmaps and bitmap operations, see [Bitmaps](bitmaps.md).

 

 



