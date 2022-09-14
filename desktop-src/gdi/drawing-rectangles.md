---
description: A rectangle is a four-sided polygon whose opposing sides are parallel and equal in length.
ms.assetid: 77d29981-032e-45ba-a06b-c9c992236803
title: Drawing Rectangles
ms.topic: article
ms.date: 05/31/2018
---

# Drawing Rectangles

A rectangle is a four-sided polygon whose opposing sides are parallel and equal in length. Although an application can draw a rectangle by calling the [**Polygon**](/windows/desktop/api/Wingdi/nf-wingdi-polygon) function, supplying the coordinates of each corner, the [**Rectangle**](/windows/desktop/api/Wingdi/nf-wingdi-rectangle) function provides a simpler method. This function requires only the coordinates for the upper-left and the lower-right corners. When an application calls the [**Rectangle**](/windows/win32/api/wingdi/nf-wingdi-rectangle) function, the system draws the rectangle, excluding the right and lower sides if no world transformation is set for the given device context.

If a world transformation has been set by using the [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform) or [**ModifyWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-modifyworldtransform) function, the system includes the right and lower edges.

In addition to drawing a traditional rectangle, you can draw rectangles with rounded corners. The [**RoundRect**](/windows/desktop/api/Wingdi/nf-wingdi-roundrect) function requires that the application supply the coordinates of the lower-left and upper-right corners, as well as the width and height of the ellipse used to round each corner.

Applications can use the following functions to manipulate rectangles.



| Function                         | Description                                                        |
|----------------------------------|--------------------------------------------------------------------|
| [**FillRect**](/windows/desktop/api/Winuser/nf-winuser-fillrect)     | Repaints the interior of a rectangle.                              |
| [**FrameRect**](/windows/desktop/api/Winuser/nf-winuser-framerect)   | Redraws the sides of a rectangle.                                  |
| [**InvertRect**](/windows/desktop/api/Winuser/nf-winuser-invertrect) | Inverts the colors that appear within the interior of a rectangle. |



 

 

 
