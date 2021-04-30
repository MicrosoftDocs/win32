---
title: gluBuild2DMipmaps function (Glu.h)
description: The gluBuild2DMipmaps function creates 2-D mipmaps.
ms.assetid: ea19a9b0-baf7-436f-afd5-609bc364b3ba
keywords:
- gluBuild2DMipmaps function OpenGL
topic_type:
- apiref
api_name:
- gluBuild2DMipmaps
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluBuild2DMipmaps function

The **gluBuild2DMipmaps** function creates 2-D mipmaps.

## Syntax


```C++
void WINAPI gluBuild2DMipmaps(
         GLenum target,
         GLint  components,
         GLint  width,
         GLInt  height,
         GLenum format,
         GLenum type,
   const void   *data
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target texture. Must be GL\_TEXTURE\_2D.

</dd> <dt>

*components* 
</dt> <dd>

The number of color components in the texture. Must be 1, 2, 3, or 4.

</dd> <dt>

*width* 
</dt> <dd>

The width of the texture image.

</dd> <dt>

*height* 
</dt> <dd>

The height of the texture image.

</dd> <dt>

*format* 
</dt> <dd>

The format of the pixel data. Must be one of the following: GL\_COLOR\_INDEX, GL\_RED, GL\_GREEN, GL\_BLUE, GL\_ALPHA, GL\_RGB, GL\_RGBA, GL\_BGR\_EXT, GL\_BGRA\_EXT, GL\_LUMINANCE, or GL\_LUMINANCE\_ALPHA.

</dd> <dt>

*type* 
</dt> <dd>

The data type for *data*. Must be one of the following: GL\_UNSIGNED\_BYTE, GL\_BYTE, GL\_BITMAP, GL\_UNSIGNED\_SHORT, GL\_SHORT, GL\_UNSIGNED\_INT, GL\_INT, or GL\_FLOAT.

</dd> <dt>

*data* 
</dt> <dd>

A pointer to the image data in memory.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluBuild2DMipmaps** function obtains the input image and generates all mipmap images (using [**gluScaleImage**](gluscaleimage.md)) so the input image can be used as a mipmapped texture image. To load each of the images, call [**glTexImage2D**](glteximage2d.md). If the dimensions of the input image are not powers of two, then the image is scaled so that both the width and height are powers of two before the mipmaps are generated.

A return value of zero indicates success. Otherwise, a GLU error code is returned (see [**gluErrorString**](gluerrorstring.md)).

For a description of the acceptable values for the *format* parameter, see **glTexImage2D**. For a description of the acceptable values for *type*, see [**glDrawPixels**](gldrawpixels.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



## See also

<dl> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**gluBuild1DMipmaps**](glubuild1dmipmaps.md)
</dt> <dt>

[**gluScaleImage**](gluscaleimage.md)
</dt> </dl>

 

 





