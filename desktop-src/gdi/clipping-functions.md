---
Description: 'The following functions are used with clipping.'
ms.assetid: 'de9e5786-63d8-47be-8522-e96d7c0f8634'
title: Clipping Functions
---

# Clipping Functions

The following functions are used with clipping.



| Function                                       | Description                                                                                                                                                                               |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExcludeClipRect**](excludecliprect.md)     | Creates a new clipping region that consists of the existing clipping region minus the specified rectangle.                                                                                |
| [**ExtSelectClipRgn**](extselectcliprgn.md)   | Combines the specified region with the current clipping region using the specified mode.                                                                                                  |
| [**GetClipBox**](getclipbox.md)               | Retrieves the dimensions of the tightest bounding rectangle that can be drawn around the current visible area on the device.                                                              |
| [**GetClipRgn**](getcliprgn.md)               | Retrieves a handle identifying the current application-defined clipping region for the specified device context.                                                                          |
| [**GetMetaRgn**](getmetargn.md)               | Retrieves the current metaregion for the specified device context.                                                                                                                        |
| [**GetRandomRgn**](getrandomrgn.md)           | Copies the system clipping region of a specified device context to a specific region.                                                                                                     |
| [**IntersectClipRect**](intersectcliprect.md) | Creates a new clipping region from the intersection of the current clipping region and the specified rectangle.                                                                           |
| [**OffsetClipRgn**](offsetcliprgn.md)         | Moves the clipping region of a device context by the specified offsets.                                                                                                                   |
| [**PtVisible**](ptvisible.md)                 | Determines whether the specified point is within the clipping region of a device context.                                                                                                 |
| [**RectVisible**](rectvisible.md)             | Determines whether any part of the specified rectangle lies within the clipping region of a device context.                                                                               |
| [**SelectClipPath**](selectclippath.md)       | Selects the current path as a clipping region for a device context, combining the new region with any existing clipping region by using the specified mode.                               |
| [**SelectClipRgn**](selectcliprgn.md)         | Selects a region as the current clipping region for the specified device context.                                                                                                         |
| [**SetMetaRgn**](setmetargn.md)               | Intersects the current clipping region for the specified device context with the current metaregion and saves the combined region as the new metaregion for the specified device context. |



 

 

 



