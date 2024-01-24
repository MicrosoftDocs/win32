---
title: glCallLists function (Gl.h)
description: The glCallLists function executes a list of display lists.
ms.assetid: 7c0a00df-91ee-44ad-9e02-97c1b078e87f
keywords:
- glCallLists function OpenGL
topic_type:
- apiref
api_name:
- glCallLists
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glCallLists function

The **glCallLists** function executes a list of display lists.

## Syntax


```C++
void WINAPI glCallLists(
         GLsizei n,
         GLenum  type,
   const GLvoid  *lists
);
```



## Parameters

<dl> <dt>

*n* 
</dt> <dd>

The number of display lists to be executed.

</dd> <dt>

*type* 
</dt> <dd>

The type of values in *lists*. The following symbolic constants are accepted.



| Value                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_BYTE"></span><span id="gl_byte"></span><dl> <dt>**GL\_BYTE**</dt> </dl>                                | The *lists* parameter is treated as an array of signed bytes, each in the range -128 through 127.<br/>                                                                                                                                                                                                                                                                                       |
| <span id="GL_UNSIGNED_BYTE"></span><span id="gl_unsigned_byte"></span><dl> <dt>**GL\_UNSIGNED\_BYTE**</dt> </dl>    | The *lists* parameter is treated as an array of unsigned bytes, each in the range 0 through 255.<br/>                                                                                                                                                                                                                                                                                        |
| <span id="GL_SHORT"></span><span id="gl_short"></span><dl> <dt>**GL\_SHORT**</dt> </dl>                             | The *lists* parameter is treated as an array of signed 2-byte integers, each in the range -32768 through 32767.<br/>                                                                                                                                                                                                                                                                         |
| <span id="GL_UNSIGNED_SHORT"></span><span id="gl_unsigned_short"></span><dl> <dt>**GL\_UNSIGNED\_SHORT**</dt> </dl> | The *lists* parameter is treated as an array of unsigned 2-byte integers, each in the range 0 through 65535.<br/>                                                                                                                                                                                                                                                                            |
| <span id="GL_INT"></span><span id="gl_int"></span><dl> <dt>**GL\_INT**</dt> </dl>                                   | The *lists* parameter is treated as an array of signed 4-byte integers.<br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="GL_UNSIGNED_INT"></span><span id="gl_unsigned_int"></span><dl> <dt>**GL\_UNSIGNED\_INT**</dt> </dl>       | The *lists* parameter is treated as an array of unsigned 4-byte integers.<br/>                                                                                                                                                                                                                                                                                                               |
| <span id="GL_FLOAT"></span><span id="gl_float"></span><dl> <dt>**GL\_FLOAT**</dt> </dl>                             | The *lists* parameter is treated as an array of 4-byte, floating-point values.<br/>                                                                                                                                                                                                                                                                                                          |
| <span id="GL_2_BYTES"></span><span id="gl_2_bytes"></span><dl> <dt>**GL\_2\_BYTES**</dt> </dl>                      | The *lists* parameter is treated as an array of unsigned bytes. Each pair of bytes specifies a single display-list name. The value of the pair is computed as 256 times the unsigned value of the first byte plus the unsigned value of the second byte.<br/>                                                                                                                                |
| <span id="GL_3_BYTES"></span><span id="gl_3_bytes"></span><dl> <dt>**GL\_3\_BYTES**</dt> </dl>                      | The *lists* parameter is treated as an array of unsigned bytes. Each triplet of bytes specifies a single display list name. The value of the triplet is computed as 65536 times the unsigned value of the first byte, plus 256 times the unsigned value of the second byte, plus the unsigned value of the third byte.<br/>                                                                  |
| <span id="GL_4_BYTES"></span><span id="gl_4_bytes"></span><dl> <dt>**GL\_4\_BYTES**</dt> </dl>                      | The *lists* parameter is treated as an array of unsigned bytes. Each quadruplet of bytes specifies a single display list name. The value of the quadruplet is computed as 16777216 times the unsigned value of the first byte, plus 65536 times the unsigned value of the second byte, plus 256 times the unsigned value of the third byte, plus the unsigned value of the fourth byte.<br/> |



 

</dd> <dt>

*lists* 
</dt> <dd>

The address of an array of name offsets in the display list. The pointer type is void because the offsets can be bytes, shorts, ints, or floats, depending on the value of *type*.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **glCallLists** function causes each display list in the list of names passed as *lists* to be executed. As a result, the functions saved in each display list are executed in order, just as if they were called without using a display list. Names of display lists that have not been defined are ignored.

The **glCallLists** function provides an efficient means for executing display lists. The *n* parameter specifies the number of lists with various name formats (specified by the *type* parameter) **glCallLists** executes.

The list of display list names is not null-terminated. Rather, *n* specifies how many names are to be taken from *lists*.

The [**glListBase**](gllistbase.md) function makes an additional level of indirection available. The **glListBase** function specifies an unsigned offset that is added to each display list name specified in *lists* before that display list is executed.

The **glCallLists** function can appear inside a display list. To avoid the possibility of infinite recursion resulting from display lists calling one another, a limit is placed on the nesting level of display lists during display list execution. This limit must be at least 64, and it depends on the implementation.

The OpenGL state is not saved and restored across a call to **glCallLists**. Thus, changes made to the OpenGL state during the execution of the display lists remain after execution is completed. Use [**glPushAttrib**](glpushattrib.md), [**glPopAttrib**](glpopattrib.md), [**glPushMatrix**](glpushmatrix.md), and [**glPopMatrix**](glpopmatrix.md) to preserve the OpenGL state across **glCallLists** calls.

You can execute display lists between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md), as long as the display list includes only functions that are allowed in this interval.

The following functions retrieve information related to the **glCallLists** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_LIST\_BASE

**glGet** with argument GL\_MAX\_LIST\_NESTING

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

[**glCallList**](glcalllist.md)
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

[**glListBase**](gllistbase.md)
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

 

 





