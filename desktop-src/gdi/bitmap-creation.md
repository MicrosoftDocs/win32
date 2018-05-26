---
Description: To create a bitmap, use the CreateBitmap, CreateBitmapIndirect, or CreateCompatibleBitmap function, CreateDIBitmap, and CreateDiscardableBitmap.
ms.assetid: 313072fc-68c9-4ece-95bb-2748ccbd7f57
title: Bitmap Creation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bitmap Creation

To create a bitmap, use the [**CreateBitmap**](/windows/win32/Wingdi/nf-wingdi-createbitmap?branch=master), [**CreateBitmapIndirect**](/windows/win32/Wingdi/nf-wingdi-createbitmapindirect?branch=master), or [**CreateCompatibleBitmap**](/windows/win32/Wingdi/nf-wingdi-createcompatiblebitmap?branch=master) function, [**CreateDIBitmap**](/windows/win32/Wingdi/nf-wingdi-createdibitmap?branch=master), and [**CreateDiscardableBitmap**](/windows/win32/Wingdi/nf-wingdi-creatediscardablebitmap?branch=master).

These functions allow you to specify the width and height, in pixels, of the bitmap. The [**CreateBitmap**](/windows/win32/Wingdi/nf-wingdi-createbitmap?branch=master) and [**CreateBitmapIndirect**](/windows/win32/Wingdi/nf-wingdi-createbitmapindirect?branch=master) function also allow you to specify the number of color planes and the number of bits required to identify the color. On the other hand, the [**CreateCompatibleBitmap**](/windows/win32/Wingdi/nf-wingdi-createcompatiblebitmap?branch=master) and [**CreateDiscardableBitmap**](/windows/win32/Wingdi/nf-wingdi-creatediscardablebitmap?branch=master) functions use a specified device context to obtain the number of color planes and the number of bits required to identify the color.

The [**CreateDIBitmap**](/windows/win32/Wingdi/nf-wingdi-createdibitmap?branch=master) function creates a device-dependent bitmap from a device-independent bitmap. It contains a color table that describes how pixel values correspond to RGB color values. For more information, see [Device-Dependent Bitmaps](device-dependent-bitmaps.md) and [Device-Independent Bitmaps](device-independent-bitmaps.md).

After the bitmap has been created, you cannot change its size, number of color planes, or number of bits required to identify the color.

When you no longer need a bitmap, call the [**DeleteObject**](/windows/win32/Wingdi/nf-wingdi-deleteobject?branch=master) function to delete it.

 

 



