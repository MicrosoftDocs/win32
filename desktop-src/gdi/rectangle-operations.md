---
Description: The SetRect function creates a rectangle, the CopyRect function makes a copy of a given rectangle, and the SetRectEmpty function creates an empty rectangle.
ms.assetid: 982d6283-673b-41a1-abc7-10ef87ff3c6f
title: Rectangle Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Rectangle Operations

The [**SetRect**](/windows/win32/Winuser/nf-winuser-setrect?branch=master) function creates a rectangle, the [**CopyRect**](/windows/win32/Winuser/nf-winuser-copyrect?branch=master) function makes a copy of a given rectangle, and the [**SetRectEmpty**](/windows/win32/Winuser/nf-winuser-setrectempty?branch=master) function creates an empty rectangle. An empty rectangle is any rectangle that has zero width, zero height, or both. The [**IsRectEmpty**](/windows/win32/Winuser/nf-winuser-isrectempty?branch=master) function determines whether a given rectangle is empty. The [**EqualRect**](/windows/win32/Winuser/nf-winuser-equalrect?branch=master) function determines whether two rectangles are identical that is, whether they have the same coordinates.

The [**InflateRect**](/windows/win32/Winuser/nf-winuser-inflaterect?branch=master) function increases or decreases the width or height of a rectangle, or both. It can add or remove width from both ends of the rectangle; it can add or remove height from both the top and bottom of the rectangle.

The [**OffsetRect**](/windows/win32/Winuser/nf-winuser-offsetrect?branch=master) function moves a rectangle by a given amount. It moves the rectangle by adding the given x-amount, y-amount, or x- and y-amounts to the corner coordinates.

The [**PtInRect**](/windows/win32/Winuser/nf-winuser-ptinrect?branch=master) function determines whether a given point lies within a given rectangle. The point is in the rectangle if it lies on the left or top side or is completely within the rectangle. The point is not in the rectangle if it lies on the right or bottom side.

The [**IntersectRect**](/windows/win32/Winuser/nf-winuser-intersectrect?branch=master) function creates a new rectangle that is the intersection of two existing rectangles, as shown in the following figure.

![illustration showing two overlapping rectangles, with darker shading to indicate the intersection ](images/csrec-01.png)

The [**UnionRect**](/windows/win32/Winuser/nf-winuser-unionrect?branch=master) function creates a new rectangle that is the union of two existing rectangles, as shown in the following figure.

![illustration of two overlapping rectangles, with darker shading indicating areas within the union, but not within either rectangle](images/csrec-02.png)

For information about functions that draw ellipses and polygons, see [Filled Shapes](filled-shapes.md).

 

 



