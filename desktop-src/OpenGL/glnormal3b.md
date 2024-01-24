---
title: glNormal3b function (Gl.h)
description: Sets the current normal vector. | glNormal3b function (Gl.h)
ms.assetid: b6976143-bc9a-4766-9f7e-5380c3a24173
keywords:
- glNormal3b function OpenGL
topic_type:
- apiref
api_name:
- glNormal3b
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glNormal3b function

Sets the current normal vector.

## Syntax


```C++
void WINAPI glNormal3b(
   GLbyte nx,
   GLbyte ny,
   GLbyte nz
);
```



## Parameters

<dl> <dt>

*nx* 
</dt> <dd>

Specifies the x-coordinate for the new current normal vector.

</dd> <dt>

*ny* 
</dt> <dd>

Specifies the y-coordinate for the new current normal vector.

</dd> <dt>

*nz* 
</dt> <dd>

Specifies the z-coordinate for the new current normal vector.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The current normal is set to the given coordinates whenever you call the **glNormal3b** function.

Byte, short, or integer arguments are converted to floating-point format by using a linear mapping that maps the most positive representable integer value to 1.0, and the most negative representable integer value to -1.0.

Normals specified with **glNormal3b** need not have unit length. If normalization is enabled, then normals specified with **glNormal3b** are normalized after transformation. You can control normalization by using [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) with the argument GL\_NORMALIZE. By default, normalization is disabled. You can update the current normal at any time. In particular, you can call**glNormal3b**between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md). The following functions retrieve information related to **glNormal3b**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_CURRENT\_NORMAL

[**glIsEnable**](glisenabled.md) with argument GL\_NORMALIZE

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

[**glColor**](glcolor-functions.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIndex**](glindex-functions.md)
</dt> <dt>

[**glTexCoord**](gltexcoord-functions.md)
</dt> <dt>

[**glVertex**](glvertex-functions.md)
</dt> </dl>

 

 





