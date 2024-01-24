---
description: A clipping region is one of the graphic objects that an application can select into a device context (DC).
ms.assetid: d9238ee5-3305-4e85-aef3-2c5c8b74aacd
title: Clipping Regions
ms.topic: article
ms.date: 05/31/2018
---

# Clipping Regions

A clipping region is one of the graphic objects that an application can select into a device context (DC). It is typically rectangular. Some device contexts provide a predefined or default clipping region while others do not. For example, if you obtain a device context handle from the [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) function, the DC contains a predefined rectangular clipping region that corresponds to the invalid rectangle that requires repainting. However, when you obtain a device context handle by calling the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) function with a **NULL***hWnd* parameter, or by calling the [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca) function, the DC does not contain a default clipping region. For more information about device contexts returned by the **BeginPaint** function, see [Painting and Drawing](painting-and-drawing.md) . For more information about device contexts returned by the **CreateDC** and **GetDC** functions, see [Device Contexts](device-contexts.md).

Applications can perform a variety of operations on clipping regions. Some of these operations require a handle identifying the region and some do not. For example, an application can perform the following operations directly on a device context's clipping region.

-   Determine whether graphics output appears within the region's borders by passing coordinates of the corresponding line, arc, bitmap, text, or filled shape to the [**PtVisible**](/windows/desktop/api/Wingdi/nf-wingdi-ptvisible) function.
-   Determine whether part of the client area intersects a region by calling the [**RectVisible**](/windows/desktop/api/Wingdi/nf-wingdi-rectvisible) function.
-   Move the existing region by a specified offset by calling the [**OffsetClipRgn**](/windows/desktop/api/Wingdi/nf-wingdi-offsetcliprgn) function.
-   Exclude a rectangular part of the client area from the current clipping region by calling the [**ExcludeClipRect**](/windows/desktop/api/Wingdi/nf-wingdi-excludecliprect) function.
-   Combine a rectangular part of the client area with the current clipping region by calling the [**IntersectClipRect**](/windows/desktop/api/Wingdi/nf-wingdi-intersectcliprect) function.

After obtaining a handle identifying the clipping region, an application can perform any operation that is common with regions, such as:

-   Combining a copy of the current clipping region with a second region by calling the [**CombineRgn**](/windows/desktop/api/Wingdi/nf-wingdi-combinergn) function.
-   Compare a copy of the current clipping region to a second region by calling the [**EqualRgn**](/windows/desktop/api/Wingdi/nf-wingdi-equalrgn) function.
-   Determine whether a point lies within the interior of a copy of the current clipping region by calling the [**PtInRegion**](/windows/desktop/api/Wingdi/nf-wingdi-ptinregion) function.

 

 



