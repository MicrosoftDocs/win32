---
Description: The StretchBlt function scales a bitmap by performing a bit-block transfer from a rectangle in a source device context into a rectangle in a destination device context.
ms.assetid: 34390ff9-8d5f-497e-87aa-a1019d01bba6
title: Bitmap Scaling
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bitmap Scaling

The [**StretchBlt**](/windows/win32/Wingdi/nf-wingdi-stretchblt?branch=master) function scales a bitmap by performing a bit-block transfer from a rectangle in a source device context into a rectangle in a destination device context. However, unlike the [**BitBlt**](/windows/win32/Wingdi/nf-wingdi-bitblt?branch=master) function, which duplicates the source rectangle dimensions in the destination rectangle, **StretchBlt** allows an application to specify the dimensions of both the source and the destination rectangles. When the destination bitmap is smaller than the source bitmap, the system combines rows or columns of color data (or both) in the bitmap before rendering the corresponding image on the display device. The system combines the color data according to the specified stretch mode, which the application defines by calling the [**SetStretchBltMode**](/windows/win32/Wingdi/nf-wingdi-setstretchbltmode?branch=master) function. When the destination bitmap is larger than the source bitmap, the system scales or magnifies each pixel in the resultant image accordingly.

 

 



