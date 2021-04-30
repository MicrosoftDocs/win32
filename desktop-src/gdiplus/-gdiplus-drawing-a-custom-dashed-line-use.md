---
description: Windows GDI+ provides several dash styles that are listed in the DashStyle enumeration. If those standard dash styles don't suit your needs, you can create a custom dash pattern.
ms.assetid: 0e75de3b-1006-4c8f-875c-eeb0782f24b0
title: Drawing a Custom Dashed Line
ms.topic: article
ms.date: 05/31/2018
---

# Drawing a Custom Dashed Line

Windows GDI+ provides several dash styles that are listed in the [**DashStyle**](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-dashstyle) enumeration. If those standard dash styles don't suit your needs, you can create a custom dash pattern.

To draw a custom dashed line, put the lengths of the dashes and spaces in an array and pass the address of the array as an argument to the [**Pen::SetDashPattern**](/windows/desktop/api/Gdipluspen/nf-gdipluspen-pen-setdashpattern) method of a [**Pen**](/windows/desktop/api/gdipluspen/nl-gdipluspen-pen) object. The following example draws a custom dashed line based on the array {5, 2, 15, 4}. If you multiply the elements of the array by the pen width of 5, you get {25, 10, 75, 20}. The displayed dashes alternate in length between 25 and 75, and the spaces alternate in length between 10 and 20.


```
REAL dashValues[4] = {5, 2, 15, 4};
Pen blackPen(Color(255, 0, 0, 0), 5);
blackPen.SetDashPattern(dashValues, 4);
stat = graphics.DrawLine(&blackPen, Point(5, 5), Point(405, 5));
```



The following illustration shows the resulting dashed line. Note that the final dash has to be shorter than 25 units so that the line can end at (405, 5).

![illustration showing a dashed line; each segment is a short line followed by a long one](images/pens6.png)

 

 



