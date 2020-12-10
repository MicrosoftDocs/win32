---
title: gluProject function (Glu.h)
description: The gluProject function maps object coordinates to window coordinates.
ms.assetid: cfd8bc5b-b684-4207-8bdb-bf086858da13
keywords:
- gluProject function OpenGL
topic_type:
- apiref
api_name:
- gluProject
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluProject function

The **gluProject** function maps object coordinates to window coordinates.

## Syntax


```C++
int WINAPI gluProject(
         GLdouble objx,
         GLdouble objy,
         GLdouble objz,
   const GLdouble modelMatrix[16],
   const GLdouble projMatrix[16],
   const GLint    viewport[4],
         GLdouble *winx,
         GLdouble *winy,
         GLdouble *winz
);
```



## Parameters

<dl> <dt>

*objx* 
</dt> <dd>

The x object coordinate.

</dd> <dt>

*objy* 
</dt> <dd>

The y object coordinate.

</dd> <dt>

*objz* 
</dt> <dd>

The z object coordinate.

</dd> <dt>

*modelMatrix* 
</dt> <dd>

The current modelview matrix (as from a [**glGetDoublev**](glgetdoublev.md) call).

</dd> <dt>

*projMatrix* 
</dt> <dd>

The current projection matrix (as from a **glGetDoublev** call).

</dd> <dt>

*viewport* 
</dt> <dd>

The current viewport (as from a [**glGetIntegerv**](glgetintegerv.md) call).

</dd> <dt>

*winx* 
</dt> <dd>

The computed x window coordinate.

</dd> <dt>

*winy* 
</dt> <dd>

The computed y window coordinate.

</dd> <dt>

*winz* 
</dt> <dd>

The computed z window coordinate.

</dd> </dl>

## Return value

If the function succeeds, the return value is GL\_TRUE.

If the function fails, the return value is GL\_FALSE.

## Remarks

The **gluProject** function transforms the specified object coordinates into window coordinates using *modelMatrix*, *projMatrix*, and *viewport*. The result is stored in *winx*, *winy*, and *winz*.

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

[**glGetDoublev**](glgetdoublev.md)
</dt> <dt>

[**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**gluUnProject**](gluunproject.md)
</dt> </dl>

 

 





