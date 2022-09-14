---
description: The world transformation is a property of the Graphics class.
ms.assetid: 22f43b29-ea7b-4faf-9795-2242bf704ed3
title: Using the World Transformation
ms.topic: article
ms.date: 05/31/2018
---

# Using the World Transformation

The world transformation is a property of the [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class. The numbers that specify the world transformation are stored in a [**Matrix**](/windows/desktop/api/gdiplusmatrix/nl-gdiplusmatrix-matrix) object, which represents a 3 ×3 matrix. The **Matrix** and **Graphics** classes have several methods for setting the numbers in the world transformation matrix. The examples in this section manipulate rectangles because rectangles are easy to draw and it is easy to see the effects of transformations on rectangles.

We start by creating a 50 by 50 rectangle and locating it at the origin (0, 0). The origin is at the upper-left corner of the client area.


```
Rect rect(0, 0, 50, 50);
Pen pen(Color(255, 255, 0, 0), 0);
graphics.DrawRectangle(&pen, rect);
```



The following code applies a scaling transformation that expands the rectangle by a factor of 1.75 in the x direction and shrinks the rectangle by a factor of 0.5 in the y direction:


```
Rect rect(0, 0, 50, 50);
Pen pen(Color(255, 255, 0, 0), 0);
graphics.ScaleTransform(1.75f, 0.5f);
graphics.DrawRectangle(&pen, rect);
```



The result is a rectangle that is longer in the x direction and shorter in the y direction than the original.

To rotate the rectangle instead of scaling it, use the following code instead of the preceding code:


```
Rect rect(0, 0, 50, 50);
Pen pen(Color(255, 255, 0, 0), 0);
graphics.RotateTransform(28.0f);
graphics.DrawRectangle(&pen, rect);
```



To translate the rectangle, use the following code:


```
Rect rect(0, 0, 50, 50);
Pen pen(Color(255, 255, 0, 0), 0);
graphics.TranslateTransform(150.0f, 150.0f);
graphics.DrawRectangle(&pen, rect);
```



 

 



