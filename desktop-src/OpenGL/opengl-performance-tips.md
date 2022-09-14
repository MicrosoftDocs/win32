---
title: OpenGL Performance Tips
description: OpenGL Performance Tips
ms.assetid: f85bf725-1361-49b9-894c-c803b2dead60
keywords:
- OpenGL,performance tips
- OpenGL,best practices
ms.topic: article
ms.date: 05/31/2018
---

# OpenGL Performance Tips

These programming practices optimize your application's performance:

-   Use [**glColorMaterial**](glcolormaterial.md) when only a single material property is being varied rapidly (at each vertex, for example). Use [**glMaterial**](glmaterial-functions.md) for infrequent changes, or when more than a single material property is being varied rapidly.
-   Use [**glLoadIdentity**](glloadidentity.md) to initialize a matrix, rather than loading your own copy of the identity matrix.
-   Use specific matrix calls such as [**glRotate**](glrotate.md), [**glTranslate**](gltranslate.md), and [**glScale**](glscale.md), rather than composing your own rotation, translation, and scale matrices and calling [**glMultMatrix**](glmultmatrix.md).
-   Use [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md) to save and restore state values. Use query functions only when your application requires the state values for its own computations.
-   Use display lists to encapsulate potentially memory-intensive state changes. For example, place all the [**glTexImage**](glteximage1d.md) calls required to completely specify a texture (and perhaps the associated [**glTexParameter**](gltexparameter-functions.md), [**glPixelStore**](glpixelstore-functions.md), and [**glPixelTransfer**](glpixeltransfer.md) calls as well) into a single display list. Call this display list to select the texture.
-   Use display lists to encapsulate the rendering calls of rigid objects that will be drawn repeatedly.
-   To minimize network bandwidth in client/server environments, use evaluators even for simple surface tessellations.
-   If possible, to avoid the overhead of GL\_NORMALIZE, provide unit-length normals. Because [**glScale**](glscale.md) almost always requires enabling GL\_NORMALIZE, avoid using **glScale** when doing lighting.
-   If smooth shading isn't required, set [**glShadeModel**](glshademodel.md) to GL\_FLAT.
-   Use a single [**glClear**](glclear.md) call per frame, if possible. Do not use **glClear** to clear small subregions of the buffers; use it only to clear the buffer completely or nearly completely.
-   To draw multiple independent triangles, use a single call rather than multiple calls to [**glBegin**](glbegin.md) ( GL\_TRIANGLES ) or a call to **glBegin** ( GL\_POLYGON ). Similarly:

    To draw a single triangle, use GL\_TRIANGLES rather than GL\_POLYGON.

    Use a single call to [**glBegin**](glbegin.md) ( GL\_QUADS ) rather than calling **glBegin** ( GL\_POLYGON ) repeatedly.

    Use a single call to [**glBegin**](glbegin.md) ( GL\_LINES ) to draw multiple independent line segments, rather than calling **glBegin** ( GL\_LINES ) multiple times.

-   In general, use the vector forms of commands to pass precomputed data, and use the scalar forms of commands to pass values that are computed near call time.
-   Avoid making redundant mode changes, such as setting the color to the same value between each vertex of a flat-shaded polygon.
-   When drawing or copying images, disable rasterization and per-fragment operations, to optimize resources. OpenGL can apply textures to pixel images.

 

 




