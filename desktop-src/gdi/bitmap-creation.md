---
Description: 'To create a bitmap, use the CreateBitmap, CreateBitmapIndirect, or CreateCompatibleBitmap function, CreateDIBitmap, and CreateDiscardableBitmap.'
ms.assetid: '313072fc-68c9-4ece-95bb-2748ccbd7f57'
title: Bitmap Creation
---

# Bitmap Creation

To create a bitmap, use the [**CreateBitmap**](createbitmap.md), [**CreateBitmapIndirect**](createbitmapindirect.md), or [**CreateCompatibleBitmap**](createcompatiblebitmap.md) function, [**CreateDIBitmap**](createdibitmap.md), and [**CreateDiscardableBitmap**](creatediscardablebitmap.md).

These functions allow you to specify the width and height, in pixels, of the bitmap. The [**CreateBitmap**](createbitmap.md) and [**CreateBitmapIndirect**](createbitmapindirect.md) function also allow you to specify the number of color planes and the number of bits required to identify the color. On the other hand, the [**CreateCompatibleBitmap**](createcompatiblebitmap.md) and [**CreateDiscardableBitmap**](creatediscardablebitmap.md) functions use a specified device context to obtain the number of color planes and the number of bits required to identify the color.

The [**CreateDIBitmap**](createdibitmap.md) function creates a device-dependent bitmap from a device-independent bitmap. It contains a color table that describes how pixel values correspond to RGB color values. For more information, see [Device-Dependent Bitmaps](device-dependent-bitmaps.md) and [Device-Independent Bitmaps](device-independent-bitmaps.md).

After the bitmap has been created, you cannot change its size, number of color planes, or number of bits required to identify the color.

When you no longer need a bitmap, call the [**DeleteObject**](deleteobject.md) function to delete it.

 

 



