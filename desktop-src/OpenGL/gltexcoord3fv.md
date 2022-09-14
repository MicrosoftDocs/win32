---
title: glTexCoord3fv function (Gl.h)
description: Sets the current texture coordinates. | glTexCoord3fv function (Gl.h)
ms.assetid: b37b47f0-ef62-42c9-beec-d1840a888087
keywords:
- glTexCoord3fv function OpenGL
topic_type:
- apiref
api_name:
- glTexCoord3fv
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glTexCoord3fv function

Sets the current texture coordinates.

## Syntax


```C++
void WINAPI glTexCoord3fv(
   const GLfloat *v
);
```



## Parameters

<dl> <dt>

*v* 
</dt> <dd>

A pointer to an array of three elements, which in turn specifies the s, t, and r texture coordinates.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The [**glTexCoord**](gltexcoord-functions.md) function sets the current texture coordinates that are part of the data associated with polygon vertices. The **glTexCoord** function specifies texture coordinates in one, two, three, or four dimensions. The glTexCoord1 function sets the current texture coordinates to (s, 0, 0, 1); a call to glTexCoord2 sets them to (s, t, 0, 1). Similarly, glTexCoord3 specifies the texture coordinates as (s, t, r, 1), and glTexCoord4 defines all four components explicitly as (s, t, r, q). You can update the current texture coordinates at any time. In particular, you can call glTexCoord between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md). The following function retrieves information related to **glTexCoord**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_CURRENT\_TEXTURE\_COORDS

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

[glVertex](glvertex-functions.md)
</dt> </dl>

 

 





