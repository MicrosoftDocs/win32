---
title: glGetPolygonStipple function (Gl.h)
description: The glGetPolygonStipple function returns the polygon stipple pattern.
ms.assetid: 95c1ebfa-8465-4bc1-b3f5-eed696a83816
keywords:
- glGetPolygonStipple function OpenGL
topic_type:
- apiref
api_name:
- glGetPolygonStipple
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetPolygonStipple function

The **glGetPolygonStipple** function returns the polygon stipple pattern.

## Syntax


```C++
void WINAPI glGetPolygonStipple(
   GLubyte *mask
);
```



## Parameters

<dl> <dt>

*mask* 
</dt> <dd>

Returns the stipple pattern.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glGetPolygonStipple** function returns a 32x32 polygon stipple pattern through the *mask* parameter. The pattern is packed into memory as if [**glReadPixels**](glreadpixels.md) with both *height* and *width* of 32, *type* of GL\_BITMAP, and *format* of GL\_COLOR\_INDEX were called, and the stipple pattern were stored in an internal 32x32 color-index buffer. Unlike **glReadPixels**, however, pixel-transfer operations (shift, offset, and pixel map) are not applied to the returned stipple image.

If an error is generated, no change is made to the contents of *mask*.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl>         |
| Library<br/>                  | <dl> <dt>Opengl32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Opengl32.dll</dt> </dl> |



## See also

<dl> <dt>

[**glBegin**](glbegin.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glPolygonStipple**](glpolygonstipple.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> </dl>

 

 





