---
title: Porting Matrix and Transformation Functions
description: IRIS GL and OpenGL handle matrices and transformations in a similar manner.
ms.assetid: 732ba65a-d776-43ea-a605-0f59209c9a46
keywords:
- IRIS GL porting,matrices
- porting from IRIS GL,matrices
- porting to OpenGL from IRIS GL,matrices
- OpenGL porting from IRIS GL,matrices
- matrices
- IRIS GL porting,transformations
- porting from IRIS GL,transformations
- porting to OpenGL from IRIS GL,transformations
- OpenGL porting from IRIS GL,transformations
- transformations
ms.topic: article
ms.date: 05/31/2018
---

# Porting Matrix and Transformation Functions

IRIS GL and OpenGL handle matrices and transformations in a similar manner. But there are several differences to keep in mind when porting code from IRIS GL:

-   In OpenGL you are always in double-matrix mode; there is no single-matrix mode.
-   Angles are measured in degrees, instead of tenths of degrees.
-   Projection matrix calls, like [**glFrustum**](glfrustum.md) and [**glOrtho**](glortho.md), now multiply onto the current matrix, instead of being loaded onto the current matrix.
-   The OpenGL function, [**glRotate**](glrotate.md), is very different from **rotate**. You can rotate around any arbitrary axis, instead of being confined to the x-, y-, and z- axes. For example, you can translate:

    ```C++
    rotate(200*(i+1), 'z');
    ```

    

    to:

    ```C++
    glRotate(.1*(200*(i+1), 0.0, 0.0, 1.0);
    ```

    

    When translating from **rotate** to **glRotate** you switch to degrees from tenths of degrees and replace 'z' with a vector for the z-axis.

-   OpenGL has no equivalent to the **polarview** function. You can replace it easily with a translation and three rotations. For example, you can translate:

    ```C++
    polarview(distance, azimuth, incidence, twist);
     
    ```

    

    to:

    ```C++
    glTranslatef( 0.0, 0.0, -distance); 
    glRotatef( -twist * 10.0, 0.0, 0.0, 1.0); 
    glRotatef( -incidence * 10.0, 1.0, 0.0, 0.0); 
    glRotatef( -azimuth * 10.0, 0.0, 0.0, 1.0);
    ```

    

The following table lists the OpenGL matrix functions and their equivalent IRIS GL functions.



| IRIS GL function              | OpenGL function                                                                        | Meaning                                                                                                                                                                        |
|-------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **mmode**                     | [**glMatrixMode**](glmatrixmode.md)                                                   | Sets current matrix mode.                                                                                                                                                      |
|                               | [**glLoadIdentity**](glloadidentity.md)                                               | Replaces current matrix with the identity matrix.                                                                                                                              |
| **loadmatrix**                | [**glLoadMatrixf**](glloadmatrix.md),[**glLoadMatrixd**](glloadmatrix.md)<br/> | Replaces current matrix with the specified matrix.                                                                                                                             |
| **multmatrix**                | [**glMultMatrixf**](glmultmatrix.md),[**glMultMatrixd**](glmultmatrix.md)<br/> | Post-multiplies current matrix with the specified matrix (note that **multmatrix** pre-multiplied).                                                                            |
| **mapw**, **mapw2**           | [**gluUnProject**](gluunproject.md)                                                   | Projects world-space coordinates to object space (see also [**gluProject**](gluproject.md)).                                                                                  |
| **ortho**                     | [**glOrtho**](glortho.md)                                                             | Multiplies current matrix by an orthographic projection matrix.                                                                                                                |
| **ortho2**                    | [**gluOrtho2D**](gluortho2d.md)                                                       | Defines a two-dimensional orthographic projection matrix.                                                                                                                      |
| **perspective**               | [**gluPerspective**](gluperspective.md)                                               | Defines a perspective projection matrix.                                                                                                                                       |
| **picksize**                  | [**gluPickMatrix**](glupickmatrix.md)                                                 | Defines a picking region.                                                                                                                                                      |
| **popmatrix**                 | [**glPopMatrix**](glpopmatrix.md)                                                     | Pops current matrix stack, replacing the current matrix with the one below it.                                                                                                 |
| **pushmatrix**                | [**glPushMatrix**](glpushmatrix.md)                                                   | Pushes current matrix stack down by one, duplicating the current matrix.                                                                                                       |
| **rotate**,**rot**<br/> | [**glRotated**](glrotate.md),[**glRotatef**](glrotate.md)<br/>                 | Rotates current coordinate system by the given angle about the vector from the origin through the given point. Note that **rotate** rotated only about the x-, y-, and z-axes. |
| **scale**                     | [**glScaled**](glscale.md),[**glScalef**](glscale.md)<br/>                     | Multiplies current matrix by a scaling matrix.                                                                                                                                 |
| **translate**                 | [**glTranslatef**](gltranslate.md),[**glTranslated**](gltranslate.md)<br/>     | Moves coordinate-system origin to the point specified, by multiplying the current matrix by a translation matrix.                                                              |
| **window**                    | [**glFrustum**](glfrustum.md)                                                         | Given coordinates for clipping planes, multiplies the current matrix by a perspective matrix.                                                                                  |



 

OpenGL has three matrix modes, which are set with [**glMatrixMode**](glmatrixmode.md). The following table lists the modes available as parameters for **glMatrixMode**.



| IRIS GL matrix mode | OpenGL mode    | Meaning                                  | Min stack depth |
|---------------------|----------------|------------------------------------------|-----------------|
| **MTEXTURE**        | GL\_TEXTURE    | Operates on the texture matrix stack.    | 2               |
| **MVIEWING**        | GL\_MODELVIEW  | Operates on the model view matrix stack. | 32              |
| **MPROJECTION**     | GL\_PROJECTION | Operates on the projection matrix stack. | 2               |



 

 

 





