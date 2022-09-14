---
title: Input Data
description: The OpenGL pipeline requires you to input several types of data
ms.assetid: e820d093-3e39-4feb-ab2a-0c28e298bde4
keywords:
- OpenGL processing pipeline,input data
ms.topic: article
ms.date: 05/31/2018
---

# Input Data

The OpenGL pipeline requires you to input several types of data:

-   **Vertices**. Vertices describe the shape of the desired geometric object. To specify vertices, use [**glVertex\***](glvertex-functions.md) functions in conjunction with [**glBegin**](glbegin.md) and [**glEnd**](glend.md) to create a point, line, or polygon. You can also use [**glRect**](glrect-functions.md) to describe an entire rectangle at one time.
-   **Edge flag**. By default, all edges of polygons are boundary edges. Use [**glEdgeFlag\***](gledgeflag-functions.md) to explicitly set the edge flag.
-   **Current raster position**. Specified with [**glRasterPos\***](glrasterpos-functions.md), the current raster position is used to determine raster coordinates for pixel- and bitmap-drawing operations.
-   **Current normal**. A normal vector associated with a particular vertex determines how a surface at that vertex is oriented in three-dimensional space; this in turn affects how much light that particular vertex receives. Use [**glNormal\***](glnormal-functions.md) to specify a normal vector.
-   **Current color**. The color of a vertex, together with the lighting conditions, determine the final, lit color. Color is specified with [**glColor\***](glcolor-functions.md) if in RGBA mode, or with [**glIndex\***](glindex-functions.md) if in color-index mode.
-   **Current texture coordinates**. Specified with [**glTexCoord\***](gltexcoord-functions.md), texture coordinates determine the location in a texture map to associate with a vertex of an object.

> [!Note]  
> When **glVertex\*** is called, the resulting vertex inherits the current edge flag, normal, color, and texture coordinates. Therefore, **glEdgeFlag\***, **glNormal\***, **glColor\***, and **glTexCoord\*** must be called before **glVertex\***, if they are to affect the resulting vertex.

 

 

 




