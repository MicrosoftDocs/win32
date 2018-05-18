---
Description: 'A line join is the common area that is formed by two lines whose ends meet or overlap.'
ms.assetid: '4ec3e76a-2531-4869-a5b0-c595198e8345'
title: Joining Lines
---

# Joining Lines

A line join is the common area that is formed by two lines whose ends meet or overlap. Windows GDI+ provides four line join styles: miter, bevel, round, and miter clipped. Line join style is a property of the [**Pen**](-gdiplus-class-pen-class.md) class. When you specify a line join style for a pen and then use that pen to draw a path, the specified join style is applied to all the connected lines in the path.

You can specify the line join style by using the [**Pen::SetLineJoin**](-gdiplus-class-pen-setlinejoin-linejoin-.md) method of the [**Pen**](-gdiplus-class-pen-class.md) class. The following example demonstrates a beveled line join between a horizontal line and a vertical line:


```
GraphicsPath path;
Pen penJoin(Color(255, 0, 0, 255), 8);

path.StartFigure();
path.AddLine(Point(50, 200), Point(100, 200));
path.AddLine(Point(100, 200), Point(100, 250));

penJoin.SetLineJoin(LineJoinBevel);
graphics.DrawPath(&amp;penJoin, &amp;path);
```



The following illustration shows the resulting beveled line join.

![illustration that shows two lines meeting at a right angle, with a bevelled join](images/pens5.png)

In the preceding example, the value (**LineJoinBevel**) passed to the [**Pen::SetLineJoin**](-gdiplus-class-pen-setlinejoin-linejoin-.md) method is an element of the [**LineJoin**](-gdiplus-enum-linejoin.md) enumeration.

 

 



