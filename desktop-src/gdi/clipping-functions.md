---
description: The following functions are used with clipping.
ms.assetid: de9e5786-63d8-47be-8522-e96d7c0f8634
title: Clipping Functions
ms.topic: article
ms.date: 05/31/2018
---

# Clipping Functions

The following functions are used with clipping.



| Function                                       | Description                                                                                                                                                                               |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExcludeClipRect**](/windows/desktop/api/Wingdi/nf-wingdi-excludecliprect)     | Creates a new clipping region that consists of the existing clipping region minus the specified rectangle.                                                                                |
| [**ExtSelectClipRgn**](/windows/desktop/api/Wingdi/nf-wingdi-extselectcliprgn)   | Combines the specified region with the current clipping region using the specified mode.                                                                                                  |
| [**GetClipBox**](/windows/desktop/api/Wingdi/nf-wingdi-getclipbox)               | Retrieves the dimensions of the tightest bounding rectangle that can be drawn around the current visible area on the device.                                                              |
| [**GetClipRgn**](/windows/desktop/api/Wingdi/nf-wingdi-getcliprgn)               | Retrieves a handle identifying the current application-defined clipping region for the specified device context.                                                                          |
| [**GetMetaRgn**](/windows/desktop/api/Wingdi/nf-wingdi-getmetargn)               | Retrieves the current metaregion for the specified device context.                                                                                                                        |
| [**GetRandomRgn**](/windows/desktop/api/Wingdi/nf-wingdi-getrandomrgn)           | Copies the system clipping region of a specified device context to a specific region.                                                                                                     |
| [**IntersectClipRect**](/windows/desktop/api/Wingdi/nf-wingdi-intersectcliprect) | Creates a new clipping region from the intersection of the current clipping region and the specified rectangle.                                                                           |
| [**OffsetClipRgn**](/windows/desktop/api/Wingdi/nf-wingdi-offsetcliprgn)         | Moves the clipping region of a device context by the specified offsets.                                                                                                                   |
| [**PtVisible**](/windows/desktop/api/Wingdi/nf-wingdi-ptvisible)                 | Determines whether the specified point is within the clipping region of a device context.                                                                                                 |
| [**RectVisible**](/windows/desktop/api/Wingdi/nf-wingdi-rectvisible)             | Determines whether any part of the specified rectangle lies within the clipping region of a device context.                                                                               |
| [**SelectClipPath**](/windows/desktop/api/Wingdi/nf-wingdi-selectclippath)       | Selects the current path as a clipping region for a device context, combining the new region with any existing clipping region by using the specified mode.                               |
| [**SelectClipRgn**](/windows/desktop/api/Wingdi/nf-wingdi-selectcliprgn)         | Selects a region as the current clipping region for the specified device context.                                                                                                         |
| [**SetMetaRgn**](/windows/desktop/api/Wingdi/nf-wingdi-setmetargn)               | Intersects the current clipping region for the specified device context with the current metaregion and saves the combined region as the new metaregion for the specified device context. |



 

 

 



