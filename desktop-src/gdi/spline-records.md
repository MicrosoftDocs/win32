---
description: Spline records represent the quadratic curves (that is, quadratic b-splines) used by TrueType.
ms.assetid: 39b81ffc-382b-467c-83d7-d0754847759a
title: Spline Records
ms.topic: article
ms.date: 05/31/2018
---

# Spline Records

Spline records represent the quadratic curves (that is, quadratic b-splines) used by TrueType. A spline record begins with the last point in the previous record (or for the first record in the contour, with the starting point). For the first spline record, the starting point and the last point in the record are on the glyph outline. For all other spline records, only the last point is on the glyph outline. All other points in the spline records are off the glyph outline and must be rendered as the control points of b-splines.

The last spline or polyline record in a contour always ends with the contour's starting point. This arrangement ensures that every contour is closed.

Because b-splines require three points (one point off the glyph outline between two points that are on the outline), you must perform some calculations when a spline record contains more than one off-curve point.

For example, if a spline record contains three points (A, B, and C) and it is not the first record, points A and B are off the glyph outline. To interpret point A, use the current position (which is always on the glyph outline) and the point on the glyph outline between points A and B. To find the midpoint (M) between A and B, you can perform the following calculation.

M = A + (B A)/2

The midpoint between consecutive off-outline points in a spline record is a point on the glyph outline, according to the definition of the spline format used in TrueType fonts.

If the current position is designated by P, the two quadratic splines defined by this spline record are (P, A, M) and (M, B, C).

 

 



