---
Description: 'A rectangle is a four-sided polygon whose opposing sides are parallel and equal in length.'
ms.assetid: '77d29981-032e-45ba-a06b-c9c992236803'
title: Drawing Rectangles
---

# Drawing Rectangles

A rectangle is a four-sided polygon whose opposing sides are parallel and equal in length. Although an application can draw a rectangle by calling the [**Polygon**](polygon.md) function, supplying the coordinates of each corner, the [**Rectangle**](rectangle.md) function provides a simpler method. This function requires only the coordinates for the upper-left and the lower-right corners. When an application calls the [**Rectangle**](gdi.Rectangle) function, the system draws the rectangle, excluding the right and lower sides if no world transformation is set for the given device context.

If a world transformation has been set by using the [**SetWorldTransform**](setworldtransform.md) or [**ModifyWorldTransform**](modifyworldtransform.md) function, the system includes the right and lower edges.

In addition to drawing a traditional rectangle, you can draw rectangles with rounded corners. The [**RoundRect**](roundrect.md) function requires that the application supply the coordinates of the lower-left and upper-right corners, as well as the width and height of the ellipse used to round each corner.

Applications can use the following functions to manipulate rectangles.



| Function                         | Description                                                        |
|----------------------------------|--------------------------------------------------------------------|
| [**FillRect**](fillrect.md)     | Repaints the interior of a rectangle.                              |
| [**FrameRect**](framerect.md)   | Redraws the sides of a rectangle.                                  |
| [**InvertRect**](invertrect.md) | Inverts the colors that appear within the interior of a rectangle. |



 

 

 



