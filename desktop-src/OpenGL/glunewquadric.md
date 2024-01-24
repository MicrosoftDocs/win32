---
title: gluNewQuadric function (Glu.h)
description: The gluNewQuadric function creates a quadric object.
ms.assetid: 5a4289bf-b57a-4c74-b0e3-b7536671e4df
keywords:
- gluNewQuadric function OpenGL
topic_type:
- apiref
api_name:
- gluNewQuadric
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNewQuadric function

The **gluNewQuadric** function creates a quadric object.

## Syntax


```C++
GLUquadric* WINAPI gluNewQuadric(void);
```



## Parameters

This function has no parameters.

## Remarks

The **gluNewQuadric** function creates and returns a pointer to a new quadric object. Refer to this object when calling quadric rendering and control functions. A return value of zero means there is not enough memory to allocate to the object.

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

[**gluCylinder**](glucylinder.md)
</dt> <dt>

[**gluDeleteQuadric**](gludeletequadric.md)
</dt> <dt>

[**gluDisk**](gludisk.md)
</dt> <dt>

[**gluPartialDisk**](glupartialdisk.md)
</dt> <dt>

[*gluQuadricCallback*](gluquadric.md)
</dt> <dt>

[**gluQuadricDrawStyle**](gluquadricdrawstyle.md)
</dt> <dt>

[**gluQuadricNormals**](gluquadricnormals.md)
</dt> <dt>

[**gluQuadricOrientation**](gluquadricorientation.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> <dt>

[**gluSphere**](glusphere.md)
</dt> </dl>

 

 





