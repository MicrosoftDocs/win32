---
title: Matrix Transformations
description: Vertices and normals are transformed by the modelview and projection matrices before they're used to produce an image in the framebuffer.
ms.assetid: 9fd0b236-9152-4494-b5c7-dadb5943269e
keywords:
- OpenGL processing pipeline,matrices
- matrices OpenGL
- modelview matrix
- projection matrix
ms.topic: article
ms.date: 05/31/2018
---

# Matrix Transformations

Vertices and normals are transformed by the modelview and projection matrices before they're used to produce an image in the framebuffer. Use functions such as [**glMatrixMode**](glmatrixmode.md), [**glMultMatrix\***](glmultmatrix.md), [**glRotate\***](glrotate.md), [**glTranslate\***](gltranslate.md), and [**glScale\***](glscale.md) to compose the desired transformations. Or specify matrices directly with [**glLoadMatrix\***](glloadmatrix.md) and [**glLoadIdentity**](glloadidentity.md). Use [**glPushMatrix**](glpushmatrix.md) and [**glPopMatrix**](glpopmatrix.md) to save and restore modelview and projection matrices on their respective stacks.

 

 




