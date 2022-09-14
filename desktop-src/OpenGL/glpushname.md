---
title: glPushName function (Gl.h)
description: The glPushName and glPopName functions push and pop the name stack. | glPushName function (Gl.h)
ms.assetid: e4319018-42c0-4567-b67f-31dbdbee9b13
keywords:
- glPushName function OpenGL
topic_type:
- apiref
api_name:
- glPushName
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPushName function

The **glPushName** and [**glPopName**](glpopname.md) functions push and pop the name stack.

## Syntax


```C++
void WINAPI glPushName(
   GLuint name
);
```



## Parameters

<dl> <dt>

*name* 
</dt> <dd>

A name that will be pushed onto the name stack.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_STACK\_OVERFLOW**</dt> </dl>    | The function was called while the current matrix stack was full.<br/>                                                           |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glPushName** function causes name to be pushed onto the name stack, which is initially empty. The [**glPopName**](glpopname.md) function pops one name off the top of the stack. The name stack is used during selection mode to allow sets of rendering commands to be uniquely identified. It consists of an ordered set of unsigned integers.

The name stack is always empty while the render mode is not GL\_SELECT. Calls to **glPushName** or [**glPopName**](glpopname.md) while the render mode is not GL\_SELECT are ignored.

The following functions retrieve information related to **glPushName** and [**glPopName**](glpopname.md):

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_NAME\_STACK\_DEPTH

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAX\_NAME\_STACK\_DEPTH

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

[**glInitNames**](glinitnames.md)
</dt> <dt>

[**glLoadName**](glloadname.md)
</dt> <dt>

[**glRenderMode**](glrendermode.md)
</dt> <dt>

[**glSelectBuffer**](glselectbuffer.md)
</dt> </dl>

 

 





