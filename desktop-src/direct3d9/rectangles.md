---
description: Throughout Direct3D and Window programming, objects on the screen are referred to in terms of bounding rectangles.
ms.assetid: 9e271652-1673-42ea-b1f4-31ac63c397c5
title: Rectangles (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Rectangles (Direct3D 9)

Throughout Direct3D and Window programming, objects on the screen are referred to in terms of bounding rectangles. The sides of a bounding rectangle are always parallel to the sides of the screen, so the rectangle can be described by two points, the upper-left corner and lower-right corner. Most applications use the [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure to carry information about a bounding rectangle to use when blitting to the screen or performing hit detection.

In C++, the [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure has the following definition.


```
typedef struct tagRECT { 
    LONG    left;    // This is the upper-left corner x-coordinate.
    LONG    top;     // The upper-left corner y-coordinate.
    LONG    right;   // The lower-right corner x-coordinate.
    LONG    bottom;  // The lower-right corner y-coordinate.
} RECT, *PRECT, NEAR *NPRECT, FAR *LPRECT; 
```



In the preceding example, the left and top members are the x- and y-coordinates of a bounding rectangle's upper-left corner. Similarly, the right and bottom members make up the coordinates of the lower-right corner. The following illustration shows how you can visualize these values.

![illustration of the rectangle bounded by the left, top, right, and bottom values](images/rect.png)

The column of pixels at the right edge and the row of pixels at the bottom edge are not included in the RECT. For example, locking a RECT with members {10, 10, 138, 138} results in an object 128 pixels in width and height.

In the interest of efficiency, consistency, and ease of use, all Direct3D presentation functions work with rectangles.

## Related topics

<dl> <dt>

[Coordinate Systems and Geometry](coordinate-systems-and-geometry.md)
</dt> </dl>

 

 
