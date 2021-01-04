---
title: glCallList function (Gl.h)
description: The glCallList function executes a display list.
ms.assetid: 9373d32e-b11e-4a80-8713-da2c1d8d9368
keywords:
- glCallList function OpenGL
topic_type:
- apiref
api_name:
- glCallList
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glCallList function

The **glCallList** function executes a display list.

## Syntax


```C++
void WINAPI glCallList(
   GLuint list
);
```



## Parameters

<dl> <dt>

*list* 
</dt> <dd>

The integer name of the display list to be executed.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Invoking the **glCallList** function begins execution of the named display list. The functions saved in the display list are executed in order, just as if you called them without using a display list. If *list* has not been defined as a display list, **glCallList** is ignored.

The **glCallList** function can appear inside a display list. To avoid the possibility of infinite recursion resulting from display lists calling one another, a limit is placed on the nesting level of display lists during display-list execution. This limit is at least 64, however, it depends on the implementation.

The OpenGL state is not saved and restored across a call to **glCallList**. Thus, changes made to the OpenGL state during the execution of a display list remain after execution of the display list is completed. To preserve the OpenGL state across **glCallList** calls, use [**glPushAttrib**](glpushattrib.md), [**glPopAttrib**](glpopattrib.md), [**glPushMatrix**](glpushmatrix.md), and [**glPopMatrix**](glpopmatrix.md).

You can execute display lists between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md), as long as the display list includes only functions that are allowed in this interval.

The following functions retrieve information related to **glCallList**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAX\_LIST\_NESTING

[**glIsList**](glislist.md)

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

[**glCallLists**](glcalllists.md)
</dt> <dt>

[**glDeleteLists**](gldeletelists.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGenLists**](glgenlists.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIsList**](glislist.md)
</dt> <dt>

[**glNewList**](glnewlist.md)
</dt> <dt>

[**glPopAttrib**](glpopattrib.md)
</dt> <dt>

[**glPopMatrix**](glpopmatrix.md)
</dt> <dt>

[**glPushAttrib**](glpushattrib.md)
</dt> <dt>

[**glPushMatrix**](glpushmatrix.md)
</dt> </dl>

 

 





