---
Description: 'To create a path and select it into a DC, it is first necessary to define the points that describe it.'
ms.assetid: '3691c3ab-f634-476d-a56b-1c187cb12120'
title: Path Creation
---

# Path Creation

To create a path and select it into a DC, it is first necessary to define the points that describe it. This is done by calling the [**BeginPath**](beginpath.md) function, specifying the appropriate drawing functions, and then by calling the [**EndPath**](endpath.md) function. This combination of functions (**BeginPath**, drawing functions, and **EndPath**) constitute a *path bracket*. The following is the list of drawing functions that can be used.

-   [**AngleArc**](anglearc.md)
-   [**Arc**](arc.md)
-   [**ArcTo**](arcto.md)
-   [**Chord**](chord.md)
-   [**CloseFigure**](closefigure.md)
-   [**Ellipse**](ellipse.md)
-   [**ExtTextOut**](exttextout.md)
-   [**LineTo**](lineto.md)
-   [**MoveToEx**](movetoex.md)
-   [**Pie**](pie.md)
-   [**PolyBezier**](polybezier.md)
-   [**PolyBezierTo**](polybezierto.md)
-   [**PolyDraw**](polydraw.md)
-   [**Polygon**](polygon.md)
-   [**Polyline**](polyline.md)
-   [**PolylineTo**](polylineto.md)
-   [**PolyPolygon**](polypolygon.md)
-   [**PolyPolyline**](polypolyline.md)
-   [**Rectangle**](rectangle.md)
-   [**RoundRect**](roundrect.md)
-   [**TextOut**](textout.md)

When an application calls [**EndPath**](endpath.md), the system selects the associated path into the specified DC. (If another path had previously been selected into the DC, the system deletes that path without saving it.) After the system selects the path into the DC, an application can operate on the path in one of the following ways:

-   Draw the outline of the path (using the current pen).
-   Paint the interior of the path (using the current brush).
-   Draw the outline and fill the interior of the path.
-   Modify the path (converting curves to line segments).
-   Convert the path into a clip path.
-   Convert the path into a region.
-   Flatten the path by converting each curve in the path into a series of line segments.
-   Retrieve the coordinates of the lines and curves that compose a path.

 

 



