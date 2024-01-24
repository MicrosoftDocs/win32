---
description: To create a bitmap, use the CreateBitmap, CreateBitmapIndirect, or CreateCompatibleBitmap function, CreateDIBitmap, and CreateDiscardableBitmap.
ms.assetid: 313072fc-68c9-4ece-95bb-2748ccbd7f57
title: Bitmap Creation
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Creation

To create a bitmap, use the [**CreateBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmap), [**CreateBitmapIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmapindirect), or [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap) function, [**CreateDIBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createdibitmap), and [**CreateDiscardableBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-creatediscardablebitmap).

These functions allow you to specify the width and height, in pixels, of the bitmap. The [**CreateBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmap) and [**CreateBitmapIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmapindirect) function also allow you to specify the number of color planes and the number of bits required to identify the color. On the other hand, the [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap) and [**CreateDiscardableBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-creatediscardablebitmap) functions use a specified device context to obtain the number of color planes and the number of bits required to identify the color.

The [**CreateDIBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createdibitmap) function creates a device-dependent bitmap from a device-independent bitmap. It contains a color table that describes how pixel values correspond to RGB color values. For more information, see [Device-Dependent Bitmaps](device-dependent-bitmaps.md) and [Device-Independent Bitmaps](device-independent-bitmaps.md).

After the bitmap has been created, you cannot change its size, number of color planes, or number of bits required to identify the color.

When you no longer need a bitmap, call the [**DeleteObject**](/windows/desktop/api/Wingdi/nf-wingdi-deleteobject) function to delete it.

 

 



