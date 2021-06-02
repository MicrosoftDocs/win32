---
description: 'GDI+ supports several types of curves: ellipses, arcs, cardinal splines, and B&\#233;zier splines.'
ms.assetid: 97a1342c-4edb-4671-b36d-b6992efad498
title: Constructing and Drawing Curves
ms.topic: article
ms.date: 05/31/2018
---

# Constructing and Drawing Curves

GDI+ supports several types of curves: ellipses, arcs, cardinal splines, and Bézier splines. An ellipse is defined by its bounding rectangle; an arc is a portion of an ellipse defined by a starting angle and a sweep angle. A cardinal spline is defined by an array of points and a tension parameter — the curve passes smoothly through each point in the array, and the tension parameter influences the way the curve bends. A Bézier spline is defined by two end points and two control points — the curve does not pass through the control points, but the control points influence the direction and bend as the curve goes from one end point to the other.

The following topics cover cardinal splines and Bézier splines in more detail:

-   [Drawing Cardinal Splines](-gdiplus-drawing-cardinal-splines-use.md)
-   [Drawing Bézier Splines](-gdiplus-drawing-bezier-splines-use.md)

 

 



