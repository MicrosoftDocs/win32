---
description: To draw lines and rectangles, you need a Graphics object and a Pen object. The Graphics object provides the DrawLine method, and the Pen object stores features of the line, such as color and width.
ms.assetid: f2e4144f-f2f1-49db-bfdf-ffce3023b4cb
title: Using a Pen to Draw Lines and Rectangles
ms.topic: article
ms.date: 05/31/2018
---

# Using a Pen to Draw Lines and Rectangles

To draw lines and rectangles, you need a [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object and a [**Pen**](/windows/win32/api/gdipluspen/nl-gdipluspen-pen) object. The **Graphics** object provides the [DrawLine](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(inconstpen_inint_inint_inint_inint)) method, and the **Pen** object stores features of the line, such as color and width.

The following example draws a line from (20, 10) to (300, 100). Assume **graphics** is an existing [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object.


```
Pen pen(Color(255, 0, 0, 0));
graphics.DrawLine(&pen, 20, 10, 300, 100);
```



The first statement of code uses the [**Pen**](/windows/win32/api/gdipluspen/nl-gdipluspen-pen) class constructor to create a black pen. The one argument passed to the **Pen** constructor is a [**Color**](/windows/win32/api/gdipluscolor/nl-gdipluscolor-color) object. The values used to construct the **Color** object — (255, 0, 0, 0) — correspond to the alpha, red, green, and blue components of the color. These values define an opaque black pen.

The following example draws a rectangle with its upper-left corner at (10, 10). The rectangle has a width of 100 and a height of 50. The second argument passed to the [**Pen**](/windows/win32/api/gdipluspen/nl-gdipluspen-pen) constructor indicates that the pen width is 5 pixels.


```
Pen blackPen(Color(255, 0, 0, 0), 5);
stat = graphics.DrawRectangle(&blackPen, 10, 10, 100, 50);
```



When the rectangle is drawn, the pen is centered on the rectangle's boundary. Because the pen width is 5, the sides of the rectangle are drawn 5 pixels wide, such that 1 pixel is drawn on the boundary itself, 2 pixels are drawn on the inside, and 2 pixels are drawn on the outside. For more details on pen alignment, see [Setting Pen Width and Alignment](-gdiplus-setting-pen-width-and-alignment-use.md).

The following illustration shows the resulting rectangle. The dotted lines show where the rectangle would have been drawn if the pen width had been one pixel. The enlarged view of the upper-left corner of the rectangle shows that the thick black lines are centered on those dotted lines.

![illustration of a rectangle drawn with a thick black line that surrounds a thin, grey, dashed line](images/pens1.png)

 

 



