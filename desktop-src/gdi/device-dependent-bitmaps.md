---
Description: 'Device-dependent bitmaps (DDBs) are described by using a single structure, the BITMAP structure.'
ms.assetid: '63ff9cd6-cd07-4085-b166-268e4d9b7aad'
title: 'Device-Dependent Bitmaps'
---

# Device-Dependent Bitmaps

Device-dependent bitmaps (DDBs) are described by using a single structure, the [**BITMAP**](bitmap.md) structure. The members of this structure specify the width and height of a rectangular region, in pixels; the width of the array that maps entries from the device palette to pixels; and the device's color format, in terms of color planes and bits per pixel. An application can retrieve the color format of a device by calling the [**GetDeviceCaps**](getdevicecaps.md) function and specifying the appropriate constants. Note that a DDB does not contain color values; instead, the colors are in a device-dependent format. For more information, see [Color in Bitmaps](color-in-bitmaps.md). Because each device can have its own set of colors, a DDB created for one device may not display well on a different device.

To use a DDB in a device context, it must have the color organization of that device context. Thus, a DDB is often called a *compatible bitmap* and it usually has better GDI performance than a DIB. For example, to create a bitmap for video memory, it is best to use a compatible bitmap with the same color format as the primary display. Once in video memory, rendering to the bitmap and displaying it to the screen are significantly faster than from a system memory surface or directly from a DIB.

In addition to enabling better GDI performance, compatible bitmaps are used to capture images (see [Capturing an Image](capturing-an-image.md) ) and to create bitmaps at run time for menus see "Creating the Bitmap" in (see [Using Menus](_win32_Using_Menus_cpp) ).

To transfer a bitmap between devices with different color organization, use [**GetDIBits**](getdibits.md) to convert the compatible bitmap to a DIB and call [**SetDIBits**](setdibits.md) or [**StretchDIBits**](stretchdibits.md) to display the DIB to the second device.

There are two types of DDBs: discardable and nondiscardable. A discardable DDB is a bitmap that the system discards if the bitmap is not selected into a DC and if system memory is low. The [**CreateDiscardableBitmap**](creatediscardablebitmap.md) function creates discardable bitmaps. The [**CreateBitmap**](createbitmap.md), [**CreateCompatibleBitmap**](createcompatiblebitmap.md), and [**CreateBitmapIndirect**](createbitmapindirect.md) functions create nondiscardable bitmaps.

An application can create a DDB from a DIB by initializing the required structures and calling the [**CreateDIBitmap**](createdibitmap.md) function. Specifying CBM\_INIT in the call to **CreateDIBitmap** is equivalent to calling the [**CreateCompatibleBitmap**](createcompatiblebitmap.md) function to create a DDB in the format of the device and then calling the [**SetDIBits**](setdibits.md) function to translate the DIB bits to the DDB. To determine whether a device supports the **SetDIBits** function, call the [**GetDeviceCaps**](getdevicecaps.md) function, specifying RC\_DI\_BITMAP as the RASTERCAPS flag.

 

 



