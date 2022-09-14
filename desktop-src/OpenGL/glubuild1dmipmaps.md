---
title: gluBuild1DMipmaps function (Glu.h)
description: The gluBuild1DMipmaps function creates 1-D mipmaps.
ms.assetid: 52ed924f-7a72-4458-b1b8-8e5d3021f60a
keywords:
- gluBuild1DMipmaps function OpenGL
topic_type:
- apiref
api_name:
- gluBuild1DMipmaps
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluBuild1DMipmaps function

The **gluBuild1DMipmaps** function creates 1-D mipmaps.

## Syntax


```C++
void WINAPI gluBuild1DMipmaps(
         GLenum target,
         GLint  components,
         GLint  width,
         GLenum format,
         GLenum type,
   const void   *data
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target texture. Must be GL\_TEXTURE\_1D.

</dd> <dt>

*components* 
</dt> <dd>

The number of color components in the texture. Must be 1, 2, 3, or 4.

</dd> <dt>

*width* 
</dt> <dd>

The width of the texture image.

</dd> <dt>

*format* 
</dt> <dd>

The format of the pixel data. The following values are valid: GL\_COLOR\_INDEX, GL\_RED, GL\_GREEN, GL\_BLUE, GL\_ALPHA, GL\_RGB, GL\_RGBA, GL\_BGR\_EXT, GL\_BGRA\_EXT, GL\_LUMINANCE, or GL\_LUMINANCE\_ALPHA.

</dd> <dt>

*type* 
</dt> <dd>

The data type for *data*. The following values are valid: GL\_UNSIGNED\_BYTE, GL\_BYTE, GL\_BITMAP, GL\_UNSIGNED\_SHORT, GL\_SHORT, GL\_UNSIGNED\_INT, GL\_INT, or GL\_FLOAT.

</dd> <dt>

*data* 
</dt> <dd>

A pointer to the image data in memory.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluBuild1DMipmaps** function obtains the input image and generates all mipmap images (using [**gluScaleImage**](gluscaleimage.md)) so that the input image can be used as a mipmapped texture image. The [**glTexImage1D**](glteximage1d.md) function is then called to load each of the images. If the width of the input image is not a power of two, then the image is scaled to the nearest power of two before the mipmaps are generated.

A return value of zero indicates success. Otherwise, a GLU error code is returned (see [**gluErrorString**](gluerrorstring.md)).

For a description of the acceptable values for the *format* parameter, see **glTexImage1D**. For a description of the acceptable values for the *type* parameter, see [**glDrawPixels**](gldrawpixels.md).

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

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**gluBuild2DMipmaps**](glubuild2dmipmaps.md)
</dt> <dt>

[**gluScaleImage**](gluscaleimage.md)
</dt> </dl>

 

 





