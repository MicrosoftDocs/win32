---
Description: The following functions are used with clipping.
ms.assetid: de9e5786-63d8-47be-8522-e96d7c0f8634
title: Clipping Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Clipping Functions

The following functions are used with clipping.



| Function                                       | Description                                                                                                                                                                               |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExcludeClipRect**](/windows/win32/Wingdi/nf-wingdi-excludecliprect?branch=master)     | Creates a new clipping region that consists of the existing clipping region minus the specified rectangle.                                                                                |
| [**ExtSelectClipRgn**](/windows/win32/Wingdi/nf-wingdi-extselectcliprgn?branch=master)   | Combines the specified region with the current clipping region using the specified mode.                                                                                                  |
| [**GetClipBox**](/windows/win32/Wingdi/nf-wingdi-getclipbox?branch=master)               | Retrieves the dimensions of the tightest bounding rectangle that can be drawn around the current visible area on the device.                                                              |
| [**GetClipRgn**](/windows/win32/Wingdi/nf-wingdi-getcliprgn?branch=master)               | Retrieves a handle identifying the current application-defined clipping region for the specified device context.                                                                          |
| [**GetMetaRgn**](/windows/win32/Wingdi/nf-wingdi-getmetargn?branch=master)               | Retrieves the current metaregion for the specified device context.                                                                                                                        |
| [**GetRandomRgn**](/windows/win32/Wingdi/nf-wingdi-getrandomrgn?branch=master)           | Copies the system clipping region of a specified device context to a specific region.                                                                                                     |
| [**IntersectClipRect**](/windows/win32/Wingdi/nf-wingdi-intersectcliprect?branch=master) | Creates a new clipping region from the intersection of the current clipping region and the specified rectangle.                                                                           |
| [**OffsetClipRgn**](/windows/win32/Wingdi/nf-wingdi-offsetcliprgn?branch=master)         | Moves the clipping region of a device context by the specified offsets.                                                                                                                   |
| [**PtVisible**](/windows/win32/Wingdi/nf-wingdi-ptvisible?branch=master)                 | Determines whether the specified point is within the clipping region of a device context.                                                                                                 |
| [**RectVisible**](/windows/win32/Wingdi/nf-wingdi-rectvisible?branch=master)             | Determines whether any part of the specified rectangle lies within the clipping region of a device context.                                                                               |
| [**SelectClipPath**](/windows/win32/Wingdi/nf-wingdi-selectclippath?branch=master)       | Selects the current path as a clipping region for a device context, combining the new region with any existing clipping region by using the specified mode.                               |
| [**SelectClipRgn**](/windows/win32/Wingdi/nf-wingdi-selectcliprgn?branch=master)         | Selects a region as the current clipping region for the specified device context.                                                                                                         |
| [**SetMetaRgn**](/windows/win32/Wingdi/nf-wingdi-setmetargn?branch=master)               | Intersects the current clipping region for the specified device context with the current metaregion and saves the combined region as the new metaregion for the specified device context. |



 

 

 



