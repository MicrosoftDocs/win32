---
description: To create a path, construct a GraphicsPath object, and then call methods, such as AddLine and AddCurve, to add primitives to the path.
ms.assetid: 66faeb73-16fb-4b7f-a4d5-a90ec2590d8c
title: Creating Figures from Lines, Curves, and Shapes
ms.topic: article
ms.date: 05/31/2018
---

# Creating Figures from Lines, Curves, and Shapes

To create a path, construct a [**GraphicsPath**](/windows/win32/api/gdipluspath/nl-gdipluspath-graphicspath) object, and then call methods, such as [AddLine](/windows/win32/api/gdipluspath/nf-gdipluspath-graphicspath-addline(inint_inint_inint_inint)) and [AddCurve](/windows/win32/api/gdipluspath/nf-gdipluspath-graphicspath-addcurve(inconstpoint_inint)), to add primitives to the path.

The following example creates a path that has a single arc. The arc has a sweep angle of –180 degrees, which is counterclockwise in the default coordinate system.


```
Pen pen(Color(255, 255, 0, 0));
GraphicsPath path;
path.AddArc(175, 50, 50, 50, 0, -180);
graphics.DrawPath(&pen, &path);
```



The following example creates a path that has two figures. The first figure is an arc followed by a line. The second figure is a line followed by a curve, followed by a line. The first figure is left open, and the second figure is closed.


```
Point points[] = {Point(40, 60), Point(50, 70), Point(30, 90)};

Pen pen(Color(255, 255, 0, 0), 2);
GraphicsPath path;

// The first figure is started automatically, so there is
// no need to call StartFigure here.
path.AddArc(175, 50, 50, 50, 0.0f, -180.0f);
path.AddLine(100, 0, 250, 20);

path.StartFigure();
path.AddLine(50, 20, 5, 90);
path.AddCurve(points, 3);
path.AddLine(50, 150, 150, 180);
path.CloseFigure();

graphics.DrawPath(&pen, &path);
```



In addition to adding lines and curves to paths, you can add closed shapes: rectangles, ellipses, pies, and polygons. The following example creates a path that has two lines, a rectangle, and an ellipse. The code uses a pen to draw the path and a brush to fill the path.


```
GraphicsPath path;
Pen          pen(Color(255, 255, 0, 0), 2);
SolidBrush   brush(Color(255, 0, 0, 200));

path.AddLine(10, 10, 100, 40);
path.AddLine(100, 60, 30, 60);
path.AddRectangle(Rect(50, 35, 20, 40));
path.AddEllipse(10, 75, 40, 30);

graphics.DrawPath(&pen, &path);
graphics.FillPath(&brush, &path);
```



The path in the preceding example has three figures. The first figure consists of the two lines, the second figure consists of the rectangle, and the third figure consists of the ellipse. Even when there are no calls to [**GraphicsPath::CloseFigure**](/windows/win32/api/Gdipluspath/nf-gdipluspath-graphicspath-closefigure) or [**GraphicsPath::StartFigure**](/windows/win32/api/Gdipluspath/nf-gdipluspath-graphicspath-startfigure), intrinsically closed shapes, such as rectangles and ellipses, are considered separate figures.

 

 



