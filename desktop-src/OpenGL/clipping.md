---
title: Clipping (OpenGL)
description: Clipping occurs in two steps
ms.assetid: f6f60135-f43b-4595-bfd3-33e750413e70
keywords:
- OpenGL processing pipeline,clipping
- clipping OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Clipping (OpenGL)

Clipping occurs in two steps:

1.  **View volume clippingApplication-specific clipping.** Immediately after primitives are assembled, they're clipped in eye coordinates as necessary for any clipping planes you've defined with [**glClipPlane**](glclipplane.md). (OpenGL requires support for at least six such application-specific clipping planes.)
2.  Primitives are transformed by the projection matrix into clip coordinates and clipped by the corresponding view volume. This matrix can be controlled by the matrix transformation functions (see [Matrix Transformations](matrix-transformations.md)) but is typically specified by [**glFrustum**](glfrustum.md) or [**glOrtho**](glortho.md).

Points, line segments, and polygons are handled differently during clipping:

-   Points are either retained in their original state (if they're inside the clip volume) or discarded (if they're outside the clip volume).
-   If portions of line segments or polygons are outside the clip volume, new vertices are generated at the clip points.
-   For polygons, an entire edge may need to be constructed between new vertices generated at the clip points.
-   For line segments and polygons that are clipped, the edge flag, color, and texture information is assigned to all new vertices.

 

 




