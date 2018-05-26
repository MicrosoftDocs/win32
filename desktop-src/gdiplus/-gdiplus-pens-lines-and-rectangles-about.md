---
Description: To draw lines with Windows GDI+ you need to create a Graphics object and a Pen object.
ms.assetid: d91562ab-41e6-4bca-a320-74f490a4f88f
title: Pens, Lines, and Rectangles
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pens, Lines, and Rectangles

To draw lines with Windows GDI+ you need to create a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object and a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object. The **Graphics** object provides the methods that actually do the drawing, and the **Pen** object stores attributes of the line, such as color, width, and style. Drawing a line is simply a matter of calling the [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) method of the **Graphics** object. The address of the **Pen** object is passed as one of the arguments to the DrawLine method. The following example draws a line from the point (4, 2) to the point (12, 6).


```
myGraphics.DrawLine(&amp;myPen, 4, 2, 12, 6);
```



[DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) is an overloaded method of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class, so there are several ways you can supply it with arguments. For example, you can construct two [**Point**](/windows/win32/gdiplustypes/nl-gdiplustypes-point?branch=master) objects and pass references to the **Point** objects as arguments to the DrawLine method.


```
Point myStartPoint(4, 2);
Point myEndPoint(12, 6);
myGraphics.DrawLine(&amp;myPen, myStartPoint, myEndPoint);
```



You can specify certain attributes when you construct a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object. For example, one [Pen](/windows/win32/gdipluspen/nf-gdipluspen-pen-pen(const pen &)?branch=master) constructor allows you to specify color and width. The following example draws a blue line of width 2 from (0, 0) to (60, 30).


```
Pen myPen(Color(255, 0, 0, 255), 2);
myGraphics.DrawLine(&amp;myPen, 0, 0, 60, 30);
```



The [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object also has attributes, such as dash style, that you can use to specify features of the line. For example, the following example draws a dashed line from (100, 50) to (300, 80).


```
myPen.SetDashStyle(DashStyleDash);
myGraphics.DrawLine(&amp;myPen, 100, 50, 300, 80);
```



You can use various methods of the [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object to set many more attributes of the line. The [**Pen::SetStartCap**](/windows/win32/Gdipluspen/nf-gdipluspen-pen-setstartcap?branch=master) and [**Pen::SetEndCap**](/windows/win32/Gdipluspen/nf-gdipluspen-pen-setendcap?branch=master) methods specify the appearance of the ends of the line; the ends can be flat, square, rounded, triangular, or a custom shape. The [**Pen::SetLineJoin**](/windows/win32/Gdipluspen/nf-gdipluspen-pen-setlinejoin?branch=master) method lets you specify whether connected lines are mitered (joined with sharp corners), beveled, rounded, or clipped. The following illustration shows lines with various cap and join styles.

![illustration of a two lines demonstrating rounded and circular ends, rounded and mitered corners, and two arrow styles](images/aboutgdip02-art04.png)

Drawing rectangles with GDI+ is similar to drawing lines. To draw a rectangle, you need a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object and a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object. The **Graphics** object provides a [DrawRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawrectangle(in const pen,in const rect &)?branch=master) method, and the **Pen** object stores attributes, such as line width and color. The address of the **Pen** object is passed as one of the arguments to the DrawRectangle method. The following example draws a rectangle with its upper-left corner at (100, 50), a width of 80, and a height of 40.


```
myGraphics.DrawRectangle(&amp;myPen, 100, 50, 80, 40);
```



[DrawRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawrectangle(in const pen,in const rect &)?branch=master) is an overloaded method of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class, so there are several ways you can supply it with arguments. For example, you can construct a [**Rect**](/windows/win32/gdiplustypes/nl-gdiplustypes-rect?branch=master) object and pass a reference to the **Rect** object as an argument to the DrawRectangle method.


```
Rect myRect(100, 50, 80, 40);
myGraphics.DrawRectangle(&amp;myPen, myRect);
```



A [**Rect**](/windows/win32/gdiplustypes/nl-gdiplustypes-rect?branch=master) object has methods for manipulating and gathering information about the rectangle. For example, the [Inflate](/windows/win32/gdiplustypes/nf-gdiplustypes-rect-inflate(in const point &)?branch=master) and [Offset](/windows/win32/gdiplustypes/nf-gdiplustypes-rect-offset(in int,in int)?branch=master) methods change the size and position of the rectangle. The [**Rect::IntersectsWith**](/windows/win32/Gdiplustypes/nf-gdiplustypes-rect-intersectswith?branch=master) method tells you whether the rectangle intersects another given rectangle, and the [Contains](/windows/win32/gdiplustypes/nf-gdiplustypes-rect-contains(in const point &)?branch=master) method tells you whether a given point is inside the rectangle.

 

 



