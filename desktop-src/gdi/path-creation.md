---
description: To create a path and select it into a DC, it is first necessary to define the points that describe it.
ms.assetid: 3691c3ab-f634-476d-a56b-1c187cb12120
title: Path Creation
ms.topic: article
ms.date: 05/31/2018
---

# Path Creation

To create a path and select it into a DC, it is first necessary to define the points that describe it. This is done by calling the [**BeginPath**](/windows/desktop/api/Wingdi/nf-wingdi-beginpath) function, specifying the appropriate drawing functions, and then by calling the [**EndPath**](/windows/desktop/api/Wingdi/nf-wingdi-endpath) function. This combination of functions (**BeginPath**, drawing functions, and **EndPath**) constitute a *path bracket*. The following is the list of drawing functions that can be used.

-   [**AngleArc**](/windows/desktop/api/Wingdi/nf-wingdi-anglearc)
-   [**Arc**](/windows/desktop/api/Wingdi/nf-wingdi-arc)
-   [**ArcTo**](/windows/desktop/api/Wingdi/nf-wingdi-arcto)
-   [**Chord**](/windows/desktop/api/Wingdi/nf-wingdi-chord)
-   [**CloseFigure**](/windows/desktop/api/Wingdi/nf-wingdi-closefigure)
-   [**Ellipse**](/windows/desktop/api/Wingdi/nf-wingdi-ellipse)
-   [**ExtTextOut**](/windows/desktop/api/Wingdi/nf-wingdi-exttextouta)
-   [**LineTo**](/windows/desktop/api/Wingdi/nf-wingdi-lineto)
-   [**MoveToEx**](/windows/desktop/api/Wingdi/nf-wingdi-movetoex)
-   [**Pie**](/windows/desktop/api/Wingdi/nf-wingdi-pie)
-   [**PolyBezier**](/windows/desktop/api/Wingdi/nf-wingdi-polybezier)
-   [**PolyBezierTo**](/windows/desktop/api/Wingdi/nf-wingdi-polybezierto)
-   [**PolyDraw**](/windows/desktop/api/Wingdi/nf-wingdi-polydraw)
-   [**Polygon**](/windows/desktop/api/Wingdi/nf-wingdi-polygon)
-   [**Polyline**](/windows/desktop/api/Wingdi/nf-wingdi-polyline)
-   [**PolylineTo**](/windows/desktop/api/Wingdi/nf-wingdi-polylineto)
-   [**PolyPolygon**](/windows/desktop/api/Wingdi/nf-wingdi-polypolygon)
-   [**PolyPolyline**](/windows/desktop/api/Wingdi/nf-wingdi-polypolyline)
-   [**Rectangle**](/windows/desktop/api/Wingdi/nf-wingdi-rectangle)
-   [**RoundRect**](/windows/desktop/api/Wingdi/nf-wingdi-roundrect)
-   [**TextOut**](/windows/desktop/api/Wingdi/nf-wingdi-textouta)

When an application calls [**EndPath**](/windows/desktop/api/Wingdi/nf-wingdi-endpath), the system selects the associated path into the specified DC. (If another path had previously been selected into the DC, the system deletes that path without saving it.) After the system selects the path into the DC, an application can operate on the path in one of the following ways:

-   Draw the outline of the path (using the current pen).
-   Paint the interior of the path (using the current brush).
-   Draw the outline and fill the interior of the path.
-   Modify the path (converting curves to line segments).
-   Convert the path into a clip path.
-   Convert the path into a region.
-   Flatten the path by converting each curve in the path into a series of line segments.
-   Retrieve the coordinates of the lines and curves that compose a path.

 

 



