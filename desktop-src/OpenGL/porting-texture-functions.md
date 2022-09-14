---
title: Porting Texture Functions
description: Porting Texture Functions
ms.assetid: 03e0b0fc-3812-4744-a0f1-3dcb466d679d
keywords:
- IRIS GL porting,texture
- porting from IRIS GL,texture
- porting to OpenGL from IRIS GL,texture
- OpenGL porting from IRIS GL,texture
- texture
ms.topic: article
ms.date: 05/31/2018
---

# Porting Texture Functions

When porting IRIS GL texture functions to OpenGL, keep the following points in mind:

-   OpenGL doesn't maintain tables of textures; it uses either 1-D texture and 2-D texture only. To reuse the textures from your IRIS GL code, put them in a display list.
-   OpenGL doesn't automatically generate mipmaps. If you're using mipmaps, you must first call the [**gluBuild2DMipmaps**](glubuild2dmipmaps.md) function.
-   In OpenGL, you use [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) to turn texturing capabilities on and off.
-   In OpenGL, texture size is more strictly regulated than in IRIS GL. The size of an OpenGL texture must be:

    2*n* + 2*b*

    where *n* is an integer and *b* is:

    -   0, if the texture has no border
    -   1, if the texture has a border pixel (OpenGL textures can have 1-pixel borders.)

The following table lists IRIS GL texture functions and their general OpenGL equivalents.



| IRIS GL function | OpenGL function                                                                                                                                                                                                                                                       | Meaning                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **textdef2d**    | [**glTexImage2D**](glteximage2d.md)[**glTexParameter**](gltexparameter-functions.md)<br/> [**gluBuild2DMipmaps**](glubuild2dmipmaps.md)<br/>                                                                                                           | Specifies a 2-D texture image.                                                              |
| **textbind**     | **glTexImage2DglTexParameter**<br/> **gluBuild2DMipmaps**<br/>                                                                                                                                                                                            | Selects a texture function.                                                                 |
| **tevdef**       | [**glTexEnv**](gltexenv-functions.md)                                                                                                                                                                                                                                | Defines a texture-mapping environment.                                                      |
| **tevbind**      | **glTexEnv**[**glTexImage1D**](glteximage1d.md)<br/>                                                                                                                                                                                                           | Selects a texture environment.                                                              |
| **t2**           | [**glTexCoord**](gltexcoord-functions.md)                                                                                                                                                                                                                            | Sets the current texture coordinates.                                                       |
| **texgen**       | [**glTexGen**](gltexgen-functions.md)[**glGetTexParameter**](glgettexparameter.md)<br/> [**gluBuild1DMipmaps**](glubuild1dmipmaps.md)<br/> [**gluBuild2DMipmaps**](glubuild2dmipmaps.md)<br/> [**gluScaleImage**](gluscaleimage.md)<br/> | Controls generation of texture coordinates.Scales an image to an arbitrary size.<br/> |



 

For more information on texturing, see the *OpenGL Programming Guide*.

This topic includes information on the following.

-   [Translating tevdef](translating-tevdef.md)
-   [Translating texdef](translating-texdef.md)
-   [Translating texgen](translating-texgen.md)

 

 





