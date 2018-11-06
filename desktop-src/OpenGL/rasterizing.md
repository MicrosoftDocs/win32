---
title: Rasterizing
description: Rasterizing is the process by which a primitive is converted to a two-dimensional image.
ms.assetid: 8d4e3033-2afe-4526-8862-799c45ea9a6a
keywords:
- OpenGL processing pipeline,rasterizing
- rasterizing OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Rasterizing

*Rasterizing* is the process by which a primitive is converted to a two-dimensional image. Each point of this image contains such information as color, depth, and texture data. A point and its associated information are called a *fragment*. The current raster position, as specified with [**glRasterPos\***](glrasterpos-functions.md), is used in various ways during this stage for drawing pixels and bitmaps. Different issues arise when rasterizing points, line segments, and polygons. In addition, pixel rectangles and bitmaps need to be rasterized.

With OpenGL you control rasterizing by using the following functions:

-   Primitives. Control how primitives are rasterized using functions that determine dimensions and stipple patterns: [**glPointSize**](glpointsize.md), [**glLineWidth**](gllinewidth.md), [**glLineStipple**](gllinestipple.md), and [**glPolygonStipple**](glpolygonstipple.md). Control how the front and back faces of polygons are rasterized with [**glCullFace**](glcullface.md), [**glFrontFace**](glfrontface.md), and [**glPolygonMode**](glpolygonmode.md).
-   Pixels. Several functions control pixel storage and transfer modes. The function [**glPixelStore\***](glpixelstore-functions.md) controls the encoding of pixels in client memory, and [**glPixelTransfer\***](glpixeltransfer.md) and [**glPixelMap\***](glpixelmap.md) control how pixels are processed before being placed in the framebuffer. Specify a pixel rectangle with [**glDrawPixels**](gldrawpixels.md); control its rasterization with [**glPixelZoom**](glpixelzoom.md).
-   Bitmaps. Bitmaps are rectangles of zeros and ones specifying a particular pattern of fragments to be produced. Each of these fragments has the same associated data. The [**glBitmap**](glbitmap.md) function specifies a bitmap.
-   Texture Memory. When texturing is enabled, texturing maps a portion of a specified texture image onto each primitive. This mapping is accomplished by using the color of the texture image at the location indicated by a fragment's texture coordinates to modify the fragment's RGBA color. Specify a texture image with [**glTexImage2D**](glteximage2d.md) or [**glTexImage1D**](glteximage1d.md). The [**glTexParameter\***](gltexparameter-functions.md) and [**glTexEnv\***](gltexenv-functions.md) functions control how texture values are interpreted and applied to a fragment.
-   Fog. To blend a fog color with a rasterized fragment's post-texturing color, use a blending factor that depends on the distance between the eyepoint and the fragment. Use [**glFog\***](glfog.md) to specify the fog color and blending factor.

 

 




