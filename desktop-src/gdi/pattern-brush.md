---
Description: 'A pattern (or custom) brush is created from an application-defined bitmap or device-independent bitmap (DIB). The following rectangles were painted by using different pattern brushes.'
ms.assetid: '0de89a6f-d9c7-4f33-8088-c24a48a3ceee'
title: Pattern Brush
---

# Pattern Brush

A pattern (or custom) brush is created from an application-defined bitmap or device-independent bitmap (DIB). The following rectangles were painted by using different pattern brushes.

![illustration showing three boxes, each filled with a different pattern](images/csbru-05.png)

To create a logical pattern brush, an application must first create a bitmap. After creating the bitmap, the application can create the logical pattern brush by calling the [**CreatePatternBrush**](createpatternbrush.md) or [**CreateDIBPatternBrushPt**](createdibpatternbrushpt.md) function, supplying a handle that identifies the bitmap (or DIB). The brushes that appear in the preceding illustration were created from monochrome bitmaps. For a description of bitmaps, DIBs, and the functions that create them, see [Bitmaps](bitmaps.md).

 

 



