---
title: glColor4ui function (Gl.h)
description: Sets the current color. | glColor4ui function (Gl.h)
ms.assetid: 8bcf7c6f-ed40-44eb-91d3-b82cb13c8445
keywords:
- glColor4ui function OpenGL
topic_type:
- apiref
api_name:
- glColor4ui
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glColor4ui function

Sets the current color.

## Syntax


```C++
void WINAPI glColor4ui(
   GLuint red,
   GLuint green,
   GLuint blue,
   GLuint alpha
);
```



## Parameters

<dl> <dt>

*red* 
</dt> <dd>

The new red value for the current color.

</dd> <dt>

*green* 
</dt> <dd>

The new green value for the current color.

</dd> <dt>

*blue* 
</dt> <dd>

The new blue value for the current color.

</dd> <dt>

*alpha* 
</dt> <dd>

The new alpha value for the current color.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The GL stores both a current single-valued color index and a current four-valued RGBA color. **glcolor** sets a new four-valued RGBA color. **glcolor** has two major variants: **glcolor3** and **glcolor4**. **glcolor3** variants specify new red, green, and blue values explicitly and set the current alpha value to 1.0 (full intensity) implicitly. **glcolor4** variants specify all four color components explicitly.

**glcolor3b**, **glcolor4b**, **glcolor3s**, **glcolor4s**, **glcolor3i**, and **glcolor4i** take three or four signed byte, short, or long integers as arguments. When v is appended to the name, the color commands can take a pointer to an array of such values.

Current color values are stored in floating-point format, with unspecified mantissa and exponent sizes. Unsigned integer color components, when specified, are linearly mapped to floating-point values such that the largest representable value maps to 1.0 (full intensity), and 0 maps to 0.0 (zero intensity). Signed integer color components, when specified, are linearly mapped to floating-point values such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. (Note that this mapping does not convert 0 precisely to 0.0.) Floating-point values are mapped directly.

Neither floating-point nor signed integer values are clamped to the range \[0,1\] before the current color is updated. However, color components are clamped to this range before they are interpolated or written into a color buffer.

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

[**glGetBooleanv, glGetDoublev, glGetFloatv, glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIndex**](glindexd.md)
</dt> </dl>

 

 





