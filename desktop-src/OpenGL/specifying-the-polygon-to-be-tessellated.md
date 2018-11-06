---
title: Specifying the Polygon to Be Tessellated
description: You specify a polygon (possibly containing holes) to be tessellated using
ms.assetid: 23e56d3e-c26c-4158-b0ce-cf8fcea22927
ms.topic: article
ms.date: 05/31/2018
---

# Specifying the Polygon to Be Tessellated

You specify a polygon (possibly containing holes) to be tessellated using:

-   [**gluBeginPolygon**](glubeginpolygon.md)
-   [**gluTessVertex**](glutessvertex.md)
-   [**gluNextContour**](glunextcontour.md)
-   [**gluEndPolygon**](gluendpolygon.md)

For polygons without holes, the specification process is exactly as in OpenGL:

1.  Start with [**gluBeginPolygon**](glubeginpolygon.md).
2.  Call [**gluTessVertex**](glutessvertex.md) for each vertex in the boundary.
3.  End the polygon with a call to [**gluEndPolygon**](gluendpolygon.md).

If a polygon consists of multiple contours, including holes and holes within holes, you specify the contours one after the other, preceding each by [**gluNextContour**](glunextcontour.md). When you call [**gluEndPolygon**](gluendpolygon.md), it signals the end of the final contour and starts the tessellation. You can omit the call to **gluNextContour** before the first contour. The [**gluBeginPolygon**](glubeginpolygon.md) function begins the specification of a polygon to be tessellated and associates a tessellation object, **tessobj**, with it. The callback functions to be used are those that you bind to the tessellation object with [*gluTessCallback*](glutess.md).

The [**gluTessVertex**](glutessvertex.md) function specifies a vertex in the polygon to be tessellated. Call **gluTessVertex** for each vertex in the polygon. The function's *tessobj* parameter is the tessellation object to use, *v* contains the three-dimensional vertex coordinates, and *data* is an arbitrary pointer that is sent to the callback associated with **GLU\_VERTEX**. Typically, *data* contains vertex data, texture coordinates, color information, or whatever else the application may require.

The [**gluNextContour**](glunextcontour.md) function marks the beginning of the next contour when multiple contours make up the boundary of the polygon to be tessellated. The function's *type* parameter can be **GLU\_EXTERIOR**, **GLU\_INTERIOR**, **GLU\_CCW**, **GLU\_CW**, or **GLU\_UNKNOWN**. These constants serve only as hints to the tessellation. If you get them right, the tessellation might go faster. If you get them wrong, they're ignored, and the tessellation still works.

For a polygon with holes, one contour is the exterior contour, and the others are interior. If you don't call **gluNextContour** immediately after [**gluBeginPolygon**](glubeginpolygon.md), the first contour is assumed to be of type **GLU\_EXTERIOR**.

**GLU\_CW** and **GLU\_CCW** indicate clockwise- and counterclockwise-oriented polygons. Choosing which are clockwise and which are counterclockwise is arbitrary in three dimensions, but in any plane, there are two different orientations; use the **GLU\_CW** and **GLU\_CCW** types consistently. Use **GLU\_UNKNOWN** if you don't know which to use.

The [**gluEndPolygon**](gluendpolygon.md) function indicates the end of the polygon specification. It also indicates that the tessellation can begin using the tessellation object *tessobj*.

 

 




