---
Description: A clipping region is one of the graphic objects that an application can select into a device context (DC).
ms.assetid: d9238ee5-3305-4e85-aef3-2c5c8b74aacd
title: Clipping Regions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Clipping Regions

A clipping region is one of the graphic objects that an application can select into a device context (DC). It is typically rectangular. Some device contexts provide a predefined or default clipping region while others do not. For example, if you obtain a device context handle from the [**BeginPaint**](/windows/win32/Winuser/nf-winuser-beginpaint?branch=master) function, the DC contains a predefined rectangular clipping region that corresponds to the invalid rectangle that requires repainting. However, when you obtain a device context handle by calling the [**GetDC**](/windows/win32/Winuser/nf-winuser-getdc?branch=master) function with a **NULL***hWnd* parameter, or by calling the [**CreateDC**](/windows/win32/Wingdi/nf-wingdi-createdca?branch=master) function, the DC does not contain a default clipping region. For more information about device contexts returned by the **BeginPaint** function, see [Painting and Drawing](painting-and-drawing.md) . For more information about device contexts returned by the **CreateDC** and **GetDC** functions, see [Device Contexts](device-contexts.md).

Applications can perform a variety of operations on clipping regions. Some of these operations require a handle identifying the region and some do not. For example, an application can perform the following operations directly on a device context's clipping region.

-   Determine whether graphics output appears within the region's borders by passing coordinates of the corresponding line, arc, bitmap, text, or filled shape to the [**PtVisible**](/windows/win32/Wingdi/nf-wingdi-ptvisible?branch=master) function.
-   Determine whether part of the client area intersects a region by calling the [**RectVisible**](/windows/win32/Wingdi/nf-wingdi-rectvisible?branch=master) function.
-   Move the existing region by a specified offset by calling the [**OffsetClipRgn**](/windows/win32/Wingdi/nf-wingdi-offsetcliprgn?branch=master) function.
-   Exclude a rectangular part of the client area from the current clipping region by calling the [**ExcludeClipRect**](/windows/win32/Wingdi/nf-wingdi-excludecliprect?branch=master) function.
-   Combine a rectangular part of the client area with the current clipping region by calling the [**IntersectClipRect**](/windows/win32/Wingdi/nf-wingdi-intersectcliprect?branch=master) function.

After obtaining a handle identifying the clipping region, an application can perform any operation that is common with regions, such as:

-   Combining a copy of the current clipping region with a second region by calling the [**CombineRgn**](/windows/win32/Wingdi/nf-wingdi-combinergn?branch=master) function.
-   Compare a copy of the current clipping region to a second region by calling the [**EqualRgn**](/windows/win32/Wingdi/nf-wingdi-equalrgn?branch=master) function.
-   Determine whether a point lies within the interior of a copy of the current clipping region by calling the [**PtInRegion**](/windows/win32/Wingdi/nf-wingdi-ptinregion?branch=master) function.

 

 



