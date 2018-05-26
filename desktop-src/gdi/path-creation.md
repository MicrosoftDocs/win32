---
Description: To create a path and select it into a DC, it is first necessary to define the points that describe it.
ms.assetid: 3691c3ab-f634-476d-a56b-1c187cb12120
title: Path Creation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Path Creation

To create a path and select it into a DC, it is first necessary to define the points that describe it. This is done by calling the [**BeginPath**](/windows/win32/Wingdi/nf-wingdi-beginpath?branch=master) function, specifying the appropriate drawing functions, and then by calling the [**EndPath**](/windows/win32/Wingdi/nf-wingdi-endpath?branch=master) function. This combination of functions (**BeginPath**, drawing functions, and **EndPath**) constitute a *path bracket*. The following is the list of drawing functions that can be used.

-   [**AngleArc**](/windows/win32/Wingdi/nf-wingdi-anglearc?branch=master)
-   [**Arc**](/windows/win32/Wingdi/nf-wingdi-arc?branch=master)
-   [**ArcTo**](/windows/win32/Wingdi/nf-wingdi-arcto?branch=master)
-   [**Chord**](/windows/win32/Wingdi/nf-wingdi-chord?branch=master)
-   [**CloseFigure**](/windows/win32/Wingdi/nf-wingdi-closefigure?branch=master)
-   [**Ellipse**](/windows/win32/Wingdi/nf-wingdi-ellipse?branch=master)
-   [**ExtTextOut**](/windows/win32/Wingdi/nf-wingdi-exttextouta?branch=master)
-   [**LineTo**](/windows/win32/Wingdi/nf-wingdi-lineto?branch=master)
-   [**MoveToEx**](/windows/win32/Wingdi/nf-wingdi-movetoex?branch=master)
-   [**Pie**](/windows/win32/Wingdi/nf-wingdi-pie?branch=master)
-   [**PolyBezier**](/windows/win32/Wingdi/nf-wingdi-polybezier?branch=master)
-   [**PolyBezierTo**](/windows/win32/Wingdi/nf-wingdi-polybezierto?branch=master)
-   [**PolyDraw**](/windows/win32/Wingdi/nf-wingdi-polydraw?branch=master)
-   [**Polygon**](/windows/win32/Wingdi/nf-wingdi-polygon?branch=master)
-   [**Polyline**](/windows/win32/Wingdi/nf-wingdi-polyline?branch=master)
-   [**PolylineTo**](/windows/win32/Wingdi/nf-wingdi-polylineto?branch=master)
-   [**PolyPolygon**](/windows/win32/Wingdi/nf-wingdi-polypolygon?branch=master)
-   [**PolyPolyline**](/windows/win32/Wingdi/nf-wingdi-polypolyline?branch=master)
-   [**Rectangle**](/windows/win32/Wingdi/nf-wingdi-rectangle?branch=master)
-   [**RoundRect**](/windows/win32/Wingdi/nf-wingdi-roundrect?branch=master)
-   [**TextOut**](/windows/win32/Wingdi/nf-wingdi-textouta?branch=master)

When an application calls [**EndPath**](/windows/win32/Wingdi/nf-wingdi-endpath?branch=master), the system selects the associated path into the specified DC. (If another path had previously been selected into the DC, the system deletes that path without saving it.) After the system selects the path into the DC, an application can operate on the path in one of the following ways:

-   Draw the outline of the path (using the current pen).
-   Paint the interior of the path (using the current brush).
-   Draw the outline and fill the interior of the path.
-   Modify the path (converting curves to line segments).
-   Convert the path into a clip path.
-   Convert the path into a region.
-   Flatten the path by converting each curve in the path into a series of line segments.
-   Retrieve the coordinates of the lines and curves that compose a path.

 

 



