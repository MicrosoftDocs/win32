---
title: glLineStipple function (Gl.h)
description: The glLineStipple function specifies the line stipple pattern.
ms.assetid: 256d968c-9e72-4aec-9faf-afe70f1087a8
keywords:
- glLineStipple function OpenGL
topic_type:
- apiref
api_name:
- glLineStipple
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glLineStipple function

The **glLineStipple** function specifies the line stipple pattern.

## Syntax


```C++
void WINAPI glLineStipple(
   GLint    factor,
   GLushort pattern
);
```



## Parameters

<dl> <dt>

*factor* 
</dt> <dd>

A multiplier for each bit in the line stipple pattern. If *factor* is 3, for example, each bit in the pattern will be used three times before the next bit in the pattern is used. The *factor* parameter is clamped to the range \[1, 256\] and defaults to one.

</dd> <dt>

*pattern* 
</dt> <dd>

A 16-bit integer whose bit pattern determines which fragments of a line will be drawn when the line is rasterized. Bit zero is used first, and the default pattern is all ones.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glLineStipple** function specifies the line stipple pattern. Line stippling masks out certain fragments produced by rasterization; those fragments will not be drawn. The masking is achieved by using three parameters: the 16-bit line stipple pattern *pattern*, the repeat count *factor*, and an integer stipple counter *s*.

Counter *s* is reset to zero whenever [**glBegin**](glbegin.md) is called, and before each line segment of a **glBegin**(GL\_LINES)/**glEnd** sequence is generated. It is incremented after each fragment of a unit width aliased line segment is generated, or after each *i* fragments of an *i* width line segment are generated. The *i* fragments associated with count *s* are masked out if *pattern* bit (*s* / *factor*) mod 16 is zero. Otherwise these fragments are sent to the framebuffer. Bit zero of *pattern* is the least significant bit.

Antialiased lines are treated as a sequence of 1x*width* rectangles for purposes of stippling. Rectangle *s* is rasterized or not based on the fragment rule described for aliased lines; it counts rectangles rather than groups of fragments.

Line stippling is enabled or disabled using [**glEnable**](glenable.md) and **glDisable** with argument GL\_LINE\_STIPPLE. When enabled, the line stipple pattern is applied as described above. When disabled, it is as if the pattern were all ones. Initially, line stippling is disabled.

The following functions retrieve information related to **glLineStipple**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_LINE\_STIPPLE\_PATTERN

**glGet** with argument GL\_LINE\_STIPPLE\_REPEAT

[**glIsEnabled**](glisenabled.md) with argument GL\_LINE\_STIPPLE

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

[**glLineWidth**](gllinewidth.md)
</dt> <dt>

[**glPolygonStipple**](glpolygonstipple.md)
</dt> </dl>

 

 





