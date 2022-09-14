---
description: A polygon is a closed figure with three or more straight sides.
ms.assetid: f1155341-83f3-4805-8d42-a1910515db31
title: Polygons
ms.topic: article
ms.date: 05/31/2018
---

# Polygons

A polygon is a closed figure with three or more straight sides. For example, a triangle is a polygon with three sides, a rectangle is a polygon with four sides, and a pentagon is a polygon with five sides. The following illustration shows several polygons.

![illustration showing five polygons of different shapes, sizes, and colors](images/aboutgdip02-art07.png)

To draw a polygon, you need a [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object, a [**Pen**](/windows/win32/api/gdipluspen/nl-gdipluspen-pen) object, and an array of [**Point**](/windows/win32/api/gdiplustypes/nl-gdiplustypes-point) (or [**PointF**](/windows/win32/api/gdiplustypes/nl-gdiplustypes-pointf)) objects. The **Graphics** object provides the [DrawPolygon](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpolygon(inconstpen_inconstpoint_inint)) method. The **Pen** object stores attributes of the polygon, such as line width and color, and the array of **Point** objects stores the points to be connected by straight lines. The addresses of the **Pen** object and the array of **Point** objects are passed as arguments to the DrawPolygon method. The following example draws a three-sided polygon. Note that there are only three points in **myPointArray**: (0, 0), (50, 30), and (30, 60). The DrawPolygon method automatically closes the polygon by drawing a line from (30, 60) back to the starting point (0, 0);


```
Point myPointArray[] =
   {Point(0, 0), Point(50, 30), Point(30, 60)};
myGraphics.DrawPolygon(&myPen, myPointArray, 3);
```



The following illustration shows the polygon.

![illustration showing a triangle against coordinate axes](images/aboutgdip02-art08.png)

 

 



