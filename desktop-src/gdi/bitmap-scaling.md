---
Description: 'The StretchBlt function scales a bitmap by performing a bit-block transfer from a rectangle in a source device context into a rectangle in a destination device context.'
ms.assetid: '34390ff9-8d5f-497e-87aa-a1019d01bba6'
title: Bitmap Scaling
---

# Bitmap Scaling

The [**StretchBlt**](stretchblt.md) function scales a bitmap by performing a bit-block transfer from a rectangle in a source device context into a rectangle in a destination device context. However, unlike the [**BitBlt**](bitblt.md) function, which duplicates the source rectangle dimensions in the destination rectangle, **StretchBlt** allows an application to specify the dimensions of both the source and the destination rectangles. When the destination bitmap is smaller than the source bitmap, the system combines rows or columns of color data (or both) in the bitmap before rendering the corresponding image on the display device. The system combines the color data according to the specified stretch mode, which the application defines by calling the [**SetStretchBltMode**](setstretchbltmode.md) function. When the destination bitmap is larger than the source bitmap, the system scales or magnifies each pixel in the resultant image accordingly.

 

 



