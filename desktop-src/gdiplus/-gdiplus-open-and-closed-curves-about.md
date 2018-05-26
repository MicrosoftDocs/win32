---
Description: The following illustration shows two curves one open and one closed.
ms.assetid: e0fb8ba1-1783-4b36-93d8-f1242425d8bd
title: Open and Closed Curves
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Open and Closed Curves

The following illustration shows two curves: one open and one closed.

![illustration of an open curve (a curved line) and a closed curve (the outline of a shape)](images/aboutgdip02-art24.png)

Closed curves have an interior and therefore can be filled with a brush. The [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class in Windows GDI+ provides the following methods for filling closed figures and curves: [FillRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillrectangle(in const brush,in const rect &)?branch=master), [FillEllipse](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillellipse(in const brush,in const rect &)?branch=master), [FillPie](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpie(in const brush,in const rect &,in real,in real)?branch=master), [FillPolygon](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpolygon(in const brush,in const point,in int)?branch=master), [FillClosedCurve](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillclosedcurve(in const brush,in const point,in int)?branch=master), [**Graphics::FillPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpath?branch=master), and [**Graphics::FillRegion**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-fillregion?branch=master). Whenever you call one of these methods, you must pass the address of one of the specific brush types ([**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master), [**HatchBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-hatchbrush?branch=master), [**TextureBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-texturebrush?branch=master), [**LinearGradientBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-lineargradientbrush?branch=master), or [**PathGradientBrush**](/windows/win32/gdipluspath/nl-gdipluspath-pathgradientbrush?branch=master)) as an argument.

The [FillPie](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpie(in const brush,in const rect &,in real,in real)?branch=master) method is a companion to the [DrawArc](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawarc(in const pen,in const rect &,in real,in real)?branch=master) method. Just as the DrawArc method draws a portion of the outline of an ellipse, the FillPie method fills a portion of the interior of an ellipse. The following example draws an arc and fills the corresponding portion of the interior of the ellipse.


```
myGraphics.FillPie(&amp;mySolidBrush, 0, 0, 140, 70, 0, 120);
myGraphics.DrawArc(&amp;myPen, 0, 0, 140, 70, 0, 120);
```



The following illustration shows the arc and the filled pie.

![illustration showing a segment of a filled ellipse](images/aboutgdip02-art25.png)

The [FillClosedCurve](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillclosedcurve(in const brush,in const point,in int)?branch=master) method is a companion to the [DrawClosedCurve](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawclosedcurve(in const pen,in const point,in int)?branch=master) method. Both methods automatically close the curve by connecting the ending point to the starting point. The following example draws a curve that passes through (0, 0), (60, 20), and (40, 50). Then, the curve is automatically closed by connecting (40, 50) to the starting point (0, 0), and the interior is filled with a solid color.


```
Point myPointArray[] =
   {Point(10, 10), Point(60, 20),Point(40, 50)};
myGraphics.DrawClosedCurve(&amp;myPen, myPointArray, 3);
myGraphics.FillClosedCurve(&amp;mySolidBrush, myPointArray, 3, FillModeAlternate)
```



A path can consist of several figures (subpaths). The [**Graphics::FillPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpath?branch=master) method fills the interior of each figure. If a figure is not closed, the **Graphics::FillPath** method fills the area that would be enclosed if the figure were closed. The following example draws and fills a path that consists of an arc, a cardinal spline, a string, and a pie.


```
myGraphics.FillPath(&amp;mySolidBrush, &amp;myGraphicsPath);
myGraphics.DrawPath(&amp;myPen, &amp;myGraphicsPath);
```



The following illustration shows the path before and after it is filled with a solid brush. Note that the text in the string is outlined, but not filled, by the [**Graphics::DrawPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpath?branch=master) method. It is the [**Graphics::FillPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-fillpath?branch=master) method that paints the interiors of the characters in the string.

![illustration that twice shows text and an open and a closed curve; these are empty the first time, and filled the second time](images/aboutgdip02-art26.png)

 

 



