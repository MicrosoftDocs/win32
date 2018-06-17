---
Description: Paths are formed by combining lines, rectangles, and simple curves. Recall from the Overview of Vector Graphics that the following basic building blocks have proven to be the most useful for drawing pictures.
ms.assetid: 88fea2ec-7b53-44bb-841d-486c5c879c68
title: Paths
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Paths

Paths are formed by combining lines, rectangles, and simple curves. Recall from the [Overview of Vector Graphics](-gdiplus-overview-of-vector-graphics-about.md) that the following basic building blocks have proven to be the most useful for drawing pictures.

-   Lines
-   Rectangles
-   Ellipses
-   Arcs
-   Polygons
-   Cardinal splines
-   Bézier splines

In Windows GDI+, the [**GraphicsPath**](/windows/desktop/api/gdipluspath/nl-gdipluspath-graphicspath) object allows you to collect a sequence of these building blocks into a single unit. The entire sequence of lines, rectangles, polygons, and curves can then be drawn with one call to the [**Graphics::DrawPath**](/windows/desktop/api/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpath) method of the [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class. The following illustration shows a path created by combining a line, an arc, a Bézier spline, and a cardinal spline.

![illustration of a path that combines a line, an arc, a bezier spline, and a cardinal spline](images/aboutgdip02-art14.png)

The [**GraphicsPath**](/windows/desktop/api/gdipluspath/nl-gdipluspath-graphicspath) class provides the following methods for creating a sequence of items to be drawn: [AddLine](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addline(in const point &_in const point &)), [AddRectangle](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addrectangle(in const rect &)), [AddEllipse](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addellipse(in const rect &)), [AddArc](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addarc(in const rect &_in real_in real)), [AddPolygon](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addpolygon(in const point_in int)), [AddCurve](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addcurve(in const point_in int)) (for cardinal splines), and [AddBezier](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addbezier(in const point &_in const point &_in const point &_in const point &)). Each of these methods is overloaded; that is, each method comes in several variations with different parameter lists. For example, one variation of the AddLine method receives four integers, and another variation of the AddLine method receives two [**Point**](/windows/desktop/api/gdiplustypes/nl-gdiplustypes-point) objects.

The methods for adding lines, rectangles, and Bézier splines to a path have plural companion methods that add several items to the path in a single call: [AddLines](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addlines(in const point_in int)), [AddRectangles](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addrectangles(in const rect_int)), and [AddBeziers](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addbeziers(in const point_in int)). Also, the [AddCurve](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addcurve(in const point_in int)) method has a companion method, [AddClosedCurve](/windows/desktop/api/gdipluspath/nf-gdipluspath-graphicspath-addclosedcurve(in const point_in int)), that adds a closed curve to the path.

To draw a path, you need a [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object, a [**Pen**](/windows/desktop/api/gdipluspen/nl-gdipluspen-pen) object, and a [**GraphicsPath**](/windows/desktop/api/gdipluspath/nl-gdipluspath-graphicspath) object. The **Graphics** object provides the [**Graphics::DrawPath**](/windows/desktop/api/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpath) method, and the **Pen** object stores attributes of the path, such as line width and color. The **GraphicsPath** object stores the sequence of lines, rectangles, and curves that make up the path. The addresses of the **Pen** object and the **GraphicsPath** object are passed as arguments to the **Graphics::DrawPath** method. The following example draws a path that consists of a line, an ellipse, and a Bézier spline.


```
myGraphicsPath.AddLine(0, 0, 30, 20);
myGraphicsPath.AddEllipse(20, 20, 20, 40);
myGraphicsPath.AddBezier(30, 60, 70, 60, 50, 30, 100, 10);
myGraphics.DrawPath(&amp;myPen, &amp;myGraphicsPath);
```



The following illustration shows the path.

![illustration of a path made up of a line, an ellipse, and a bezier spline](images/aboutgdip02-art15.png)

In addition to adding lines, rectangles, and curves to a path, you can add paths to a path. This allows you to combine existing paths to form large, complex paths. The following code adds **graphicsPath1** and **graphicsPath2** to **myGraphicsPath**. The second parameter of the [**GraphicsPath::AddPath**](/windows/desktop/api/Gdipluspath/nf-gdipluspath-graphicspath-addpath) method specifies whether the added path is connected to the existing path.


```
myGraphicsPath.AddPath(&amp;graphicsPath1, FALSE);
myGraphicsPath.AddPath(&amp;graphicsPath2, TRUE);
```



There are two other items you can add to a path: strings and pies. A pie is a portion of the interior of an ellipse. The following example creates a path from an arc, a cardinal spline, a string, and a pie.


```
myGraphicsPath.AddArc(0, 0, 30, 20, -90, 180);
myGraphicsPath.AddCurve(myPointArray, 3);
myGraphicsPath.AddString(L"a string in a path", 18, &amp;myFontFamily, 
   0, 24, myPointF, &amp;myStringFormat);
myGraphicsPath.AddPie(230, 10, 40, 40, 40, 110);
myGraphics.DrawPath(&amp;myPen, &amp;myGraphicsPath);
```



The following illustration shows the path. Note that a path does not have to be connected; the arc, cardinal spline, string, and pie are separated.

![illustration of a path made up of disconnected lines: an arc, a cardinal spline, a string, and a pie](images/aboutgdip02-art16.png)

 

 



