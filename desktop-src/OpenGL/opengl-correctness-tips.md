---
title: OpenGL Correctness Tips
description: OpenGL Correctness Tips
ms.assetid: 48397fbf-823d-4ea0-adfd-2c639e20e38f
keywords:
- OpenGL,correctness tips
- OpenGL,best practices
ms.topic: article
ms.date: 05/31/2018
---

# OpenGL Correctness Tips

Follow these guidelines to create OpenGL applications that perform as you intend:

-   Assume error behavior on the part of an OpenGL implementation may change in a future release of OpenGL. OpenGL error semantics may change in future revisions.
-   Use the projection matrix to collapse all geometry to a single plane. If the modelview matrix is used, OpenGL features that operate in eye coordinates (such as lighting and application-defined clipping planes) might fail.
-   Do not make extensive changes to a single matrix. For example, do not animate a rotation by continually calling [**glRotate**](glrotate.md) with an incremental angle. Rather, use [**glLoadIdentity**](glloadidentity.md) to initialize the given matrix for each frame, and then call **glRotate** with the desired complete angle for that frame.
-   Expect multiple passes through a rendering database to generate the same pixel fragments only if this behavior is guaranteed by the invariance rules established for a compliant OpenGL implementation. Otherwise, multiple passes might generate varying sets of fragments.
-   Do not expect errors to be reported while a display list is being defined. The commands within a display list generate errors only when the list is executed.
-   To optimize the operation of the depth buffer, place the near frustum plane as far from the viewpoint as possible.
-   Call [**glFlush**](glflush.md) to force execution of all previous OpenGL commands. Do not count on [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) or [**glIsEnabled**](glisenabled.md) to flush the rendering stream. Query commands flush as much of the stream as is required to return valid data but don't necessarily complete all pending rendering commands.
-   Turn off dithering when rendering predithered images (for example, when [**glCopyPixels**](glcopypixels.md) is called).
-   Make use of the full range of the accumulation buffer. For example, if accumulating four images, scale each by one-quarter as it is accumulated.
-   To obtain exact two-dimensional rasterization, carefully specify both the orthographic projection and the vertices of the primitives that are to be rasterized. Specify the orthographic projection with integer coordinates, as shown in the following example.

    ``` syntax
    gluOrtho2D(0, width, 0, height); 
    ```

    The parameters *width* and *height* are the dimensions of the viewport. Given this projection matrix, place polygon vertices and pixel image positions at integer coordinates to rasterize predictably. For example, [glRecti](glrect-functions.md)( 0, 0, 1, 1 ) reliably fills the lower-left pixel of the viewport, and [glRasterPos2i](glrasterpos-functions.md)( 0, 0 ) reliably positions an unzoomed image at the lower-left pixel of the viewport. However, point vertices, line vertices, and bitmap positions should be placed at half-integer locations. For example, a line drawn from (*x* (1) , 0.5) to (*x* (2) , 0.5) will be reliably rendered along the bottom row of pixels in the viewport, and a point drawn at (0.5, 0.5) will reliably fill the same pixel as glRecti( 0, 0, 1, 1 ).

    An optimum compromise that allows all primitives to be specified at integer positions, while still ensuring predictable rasterization, is to translate *x* and *y* by 0.375, as shown in the following code sample. Such a translation keeps polygon and pixel image edges safely away from the centers of pixels, while moving line vertices close enough to the pixel centers.

    ``` syntax
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity( );
    gluOrtho2D(0, width, 0, height);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity( );
    glTranslatef(0.375, 0.375, 0.0);
    /* render all primitives at integer positions */
    ```

-   Avoid using negative *w* vertex coordinates and negative *q* texture coordinates. OpenGL might not clip such coordinates correctly and can make interpolation errors when shading primitives defined by such coordinates.

 

 




