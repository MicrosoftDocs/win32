---
title: gluScaleImage function (Glu.h)
description: The gluScaleImage function scales an image to an arbitrary size.
ms.assetid: f47191e8-b22d-4f6a-949a-9c7782d6d338
keywords:
- gluScaleImage function OpenGL
topic_type:
- apiref
api_name:
- gluScaleImage
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluScaleImage function

The **gluScaleImage** function scales an image to an arbitrary size.

## Syntax


```C++
int WINAPI gluScaleImage(
         GLenum format,
         GLint  widthin,
         GLint  heightin,
         GLenum typein,
   const void   *datain,
         GLint  widthout,
         GLint  heightout,
         GLenum typeout,
         void   *dataout
);
```



## Parameters

<dl> <dt>

*format* 
</dt> <dd>

The format of the pixel data. The following symbolic values are valid: GL\_COLOR\_INDEX, GL\_STENCIL\_INDEX, GL\_DEPTH\_COMPONENT, GL\_RED, GL\_GREEN, GL\_BLUE, GL\_ALPHA, GL\_RGB, GL\_RGBA, GL\_BGR\_EXT, GL\_BGRA\_EXT, GL\_LUMINANCE, and GL\_LUMINANCE\_ALPHA.

</dd> <dt>

*widthin* 
</dt> <dd>

The width of the source image that is scaled.

</dd> <dt>

*heightin* 
</dt> <dd>

The height of the source image that is scaled.

</dd> <dt>

*typein* 
</dt> <dd>

The data type for *datain*. Must be one of the following: GL\_UNSIGNED\_BYTE, GL\_BYTE, GL\_BITMAP, GL\_UNSIGNED\_SHORT, GL\_SHORT, GL\_UNSIGNED\_INT, GL\_INT, or GL\_FLOAT.

</dd> <dt>

*datain* 
</dt> <dd>

A pointer to the source image.

</dd> <dt>

*widthout* 
</dt> <dd>

The width of the destination image.

</dd> <dt>

*heightout* 
</dt> <dd>

The height of the destination image.

</dd> <dt>

*typeout* 
</dt> <dd>

The data type for *dataout*. Must be one of the following: GL\_UNSIGNED\_BYTE, GL\_BYTE, GL\_BITMAP, GL\_UNSIGNED\_SHORT, GL\_SHORT, GL\_UNSIGNED\_INT, GL\_INT, or GL\_FLOAT.

</dd> <dt>

*dataout* 
</dt> <dd>

A pointer to the destination image.

</dd> </dl>

## Return value

If the function succeeds, the return value is zero.

If the function fails, the return value is a GLU error code (see [**gluErrorString**](gluerrorstring.md)).

## Remarks

The **gluScaleImage** function scales a pixel image using the appropriate pixel store modes to unpack data from the source image and pack data into the destination image.

When shrinking an image, **gluScaleImage** uses a box filter to sample the source image and create pixels for the destination image. When magnifying an image, the pixels from the source image are linearly interpolated to create the destination image.

For a description of the acceptable values for the *format*, *typein*, and *typeout* parameters, see [**glReadPixels**](glreadpixels.md).

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

[**glReadPixels**](glreadpixels.md)
</dt> <dt>

[**gluBuild1DMipmaps**](glubuild1dmipmaps.md)
</dt> <dt>

[**gluBuild2DMipmaps**](glubuild2dmipmaps.md)
</dt> <dt>

[**gluErrorString**](gluerrorstring.md)
</dt> </dl>

 

 





