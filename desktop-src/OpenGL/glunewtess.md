---
title: gluNewTess function (Glu.h)
description: The gluNewTess function creates a tessellation object.
ms.assetid: dfc9fce8-ecab-493b-85ee-6d7487814186
keywords:
- gluNewTess function OpenGL
topic_type:
- apiref
api_name:
- gluNewTess
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNewTess function

The **gluNewTess** function creates a tessellation object.

## Syntax


```C++
GLUtesselator* WINAPI gluNewTess(void);
```



## Parameters

This function has no parameters.

## Remarks

The **gluNewTess** function creates and returns a pointer to a new tessellation object. Refer to this object when calling tessellation functions. A return value of zero means there is not enough memory to allocate to the object.

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

[**gluDeleteTess**](gludeletetess.md)
</dt> <dt>

[**gluTessBeginPolygon**](glubeginpolygon.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> </dl>

 

 





