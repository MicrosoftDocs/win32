---
Description: A rectangle is a four-sided polygon whose opposing sides are parallel and equal in length.
ms.assetid: 77d29981-032e-45ba-a06b-c9c992236803
title: Drawing Rectangles
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drawing Rectangles

A rectangle is a four-sided polygon whose opposing sides are parallel and equal in length. Although an application can draw a rectangle by calling the [**Polygon**](/windows/win32/Wingdi/nf-wingdi-polygon?branch=master) function, supplying the coordinates of each corner, the [**Rectangle**](/windows/win32/Wingdi/nf-wingdi-rectangle?branch=master) function provides a simpler method. This function requires only the coordinates for the upper-left and the lower-right corners. When an application calls the [**Rectangle**](gdi.Rectangle) function, the system draws the rectangle, excluding the right and lower sides if no world transformation is set for the given device context.

If a world transformation has been set by using the [**SetWorldTransform**](/windows/win32/Wingdi/nf-wingdi-setworldtransform?branch=master) or [**ModifyWorldTransform**](/windows/win32/Wingdi/nf-wingdi-modifyworldtransform?branch=master) function, the system includes the right and lower edges.

In addition to drawing a traditional rectangle, you can draw rectangles with rounded corners. The [**RoundRect**](/windows/win32/Wingdi/nf-wingdi-roundrect?branch=master) function requires that the application supply the coordinates of the lower-left and upper-right corners, as well as the width and height of the ellipse used to round each corner.

Applications can use the following functions to manipulate rectangles.



| Function                         | Description                                                        |
|----------------------------------|--------------------------------------------------------------------|
| [**FillRect**](/windows/win32/Winuser/nf-winuser-fillrect?branch=master)     | Repaints the interior of a rectangle.                              |
| [**FrameRect**](/windows/win32/Winuser/nf-winuser-framerect?branch=master)   | Redraws the sides of a rectangle.                                  |
| [**InvertRect**](/windows/win32/Winuser/nf-winuser-invertrect?branch=master) | Inverts the colors that appear within the interior of a rectangle. |



 

 

 



