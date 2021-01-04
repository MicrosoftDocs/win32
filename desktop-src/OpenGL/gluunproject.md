---
title: gluUnProject function (Glu.h)
description: The gluUnProject function maps window coordinates to object coordinates.
ms.assetid: 6a719fc2-ad40-4b22-9c99-5753f5dbb8a0
keywords:
- gluUnProject function OpenGL
topic_type:
- apiref
api_name:
- gluUnProject
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluUnProject function

The **gluUnProject** function maps window coordinates to object coordinates.

## Syntax


```C++
int WINAPI gluUnProject(
         GLdouble winx,
         GLdouble winy,
         GLdouble winz,
   const GLdouble modelMatrix[16],
   const GLdouble projMatrix[16],
   const GLint    viewport[4],
         GLdouble *objx,
         GLdouble *objy,
         GLdouble *objz
);
```



## Parameters

<dl> <dt>

*winx* 
</dt> <dd>

The x window coordinate to be mapped.

</dd> <dt>

*winy* 
</dt> <dd>

The y window coordinate to be mapped.

</dd> <dt>

*winz* 
</dt> <dd>

The z window coordinate to be mapped.

</dd> <dt>

*modelMatrix* 
</dt> <dd>

The modelview matrix (as from a [**glGetDoublev**](glgetdoublev.md) call).

</dd> <dt>

*projMatrix* 
</dt> <dd>

The projection matrix (as from a **glGetDoublev** call).

</dd> <dt>

*viewport* 
</dt> <dd>

The viewport (as from a [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) call).

</dd> <dt>

*objx* 
</dt> <dd>

The computed x object coordinate.

</dd> <dt>

*objy* 
</dt> <dd>

The computed y object coordinate.

</dd> <dt>

*objz* 
</dt> <dd>

The computed z object coordinate.

</dd> </dl>

## Return value

If the function succeeds, the return value is GL\_TRUE.

If the function fails, the return value is GL\_FALSE.

## Remarks

The **gluUnProject** function maps the specified window coordinates into object coordinates using *modelMatrix*, *projMatrix*, and *viewport*. The result is stored in *objx*, *objy*, and *objz*.

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

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glGetDoublev**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**gluProject**](gluproject.md)
</dt> </dl>

 

 





