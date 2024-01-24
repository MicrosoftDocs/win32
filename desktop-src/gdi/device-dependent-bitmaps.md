---
description: Device-dependent bitmaps (DDBs) are described by using a single structure, the BITMAP structure.
ms.assetid: 63ff9cd6-cd07-4085-b166-268e4d9b7aad
title: Device-Dependent Bitmaps
ms.topic: article
ms.date: 05/31/2018
---

# Device-Dependent Bitmaps

Device-dependent bitmaps (DDBs) are described by using a single structure, the [**BITMAP**](/windows/win32/api/wingdi/ns-wingdi-bitmap) structure. The members of this structure specify the width and height of a rectangular region, in pixels; the width of the array that maps entries from the device palette to pixels; and the device's color format, in terms of color planes and bits per pixel. An application can retrieve the color format of a device by calling the [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function and specifying the appropriate constants. Note that a DDB does not contain color values; instead, the colors are in a device-dependent format. For more information, see [Color in Bitmaps](color-in-bitmaps.md). Because each device can have its own set of colors, a DDB created for one device may not display well on a different device.

To use a DDB in a device context, it must have the color organization of that device context. Thus, a DDB is often called a *compatible bitmap* and it usually has better GDI performance than a DIB. For example, to create a bitmap for video memory, it is best to use a compatible bitmap with the same color format as the primary display. Once in video memory, rendering to the bitmap and displaying it to the screen are significantly faster than from a system memory surface or directly from a DIB.

In addition to enabling better GDI performance, compatible bitmaps are used to capture images (see [Capturing an Image](capturing-an-image.md) ) and to create bitmaps at run time for menus see "Creating the Bitmap" in (see [Using Menus](../menurc/using-menus.md) ).

To transfer a bitmap between devices with different color organization, use [**GetDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-getdibits) to convert the compatible bitmap to a DIB and call [**SetDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-setdibits) or [**StretchDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-stretchdibits) to display the DIB to the second device.

There are two types of DDBs: discardable and nondiscardable. A discardable DDB is a bitmap that the system discards if the bitmap is not selected into a DC and if system memory is low. The [**CreateDiscardableBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-creatediscardablebitmap) function creates discardable bitmaps. The [**CreateBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmap), [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap), and [**CreateBitmapIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmapindirect) functions create nondiscardable bitmaps.

An application can create a DDB from a DIB by initializing the required structures and calling the [**CreateDIBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createdibitmap) function. Specifying CBM\_INIT in the call to **CreateDIBitmap** is equivalent to calling the [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap) function to create a DDB in the format of the device and then calling the [**SetDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-setdibits) function to translate the DIB bits to the DDB. To determine whether a device supports the **SetDIBits** function, call the [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function, specifying RC\_DI\_BITMAP as the RASTERCAPS flag.

 

 
