---
title: Manipulating Images for Use in Texturing
description: The OpenGL Utility library (GLU) provides image scaling and automatic mipmapping functions to simplify the specification of texture images.
ms.assetid: 20edf665-1fed-4761-b8b1-beee02c78b0d
keywords:
- OpenGL Utility (GLU),image scaling
- GLU (OpenGL Utility),image scaling
- OpenGL Utility (GLU),automatic mipmapping
- GLU (OpenGL Utility),automatic mipmapping
- OpenGL Utility (GLU),texture images
- GLU (OpenGL Utility),texture images
- GLU library,texture images
ms.topic: article
ms.date: 05/31/2018
---

# Manipulating Images for Use in Texturing

The OpenGL Utility library (GLU) provides image scaling and automatic mipmapping functions to simplify the specification of texture images. The [**gluScaleImage**](gluscaleimage.md) function scales a specified image to an accepted texture size; you can pass the resulting image to OpenGL as a texture. The automatic mipmapping functions, [**gluBuild1DMipmaps**](glubuild1dmipmaps.md) and [**gluBuild2DMipmaps**](glubuild2dmipmaps.md), create mipmapped texture images from a specified image and pass them to [**glTexImage1D**](glteximage1d.md) and [**glTexImage2D**](glteximage2d.md), respectively.

 

 




