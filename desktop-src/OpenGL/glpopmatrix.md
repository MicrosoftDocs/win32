---
title: glPopMatrix function (Gl.h)
description: The glPushMatrix and glPopMatrix functions push and pop the current matrix stack. | glPopMatrix function (Gl.h)
ms.assetid: 7b4fc26e-36c8-4252-aba7-2e8ec6b34f91
keywords:
- glPopMatrix function OpenGL
topic_type:
- apiref
api_name:
- glPopMatrix
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPopMatrix function

The [**glPushMatrix**](glpushmatrix.md) and **glPopMatrix** functions push and pop the current matrix stack.

## Syntax


```C++
void WINAPI glPopMatrix(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Error codes

It is an error to push a full matrix stack, or to pop a matrix stack that contains only a single matrix. In either case, the error flag is set and no other change is made to the OpenGL state.

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_STACK\_UNDERFLOW**</dt> </dl>   | The function was called while the current matrix stack contained only a single matrix.<br/>                                     |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

There is a stack of matrices for each of the matrix modes. In GL\_MODELVIEW mode, the stack depth is at least 32. In the other two modes, GL\_PROJECTION and GL\_TEXTURE, the depth is at least 2. The current matrix in any mode is the matrix on the top of the stack for that mode.

The [**glPushMatrix**](glpushmatrix.md) function pushes the current matrix stack down by one, duplicating the current matrix. That is, after a **glPushMatrix** call, the matrix on the top of the stack is identical to the one below it. The **glPopMatrix** function pops the current matrix stack, replacing the current matrix with the one below it on the stack. Initially, each of the stacks contains one matrix, an identity matrix.

The following functions retrieve information related to [**glPushMatrix**](glpushmatrix.md) and **glPopMatrix**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MATRIX\_MODE

**glGet** with argument GL\_MODELVIEW\_MATRIX

**glGet** with argument GL\_PROJECTION\_MATRIX

**glGet** with argument GL\_TEXTURE\_MATRIX

**glGet** with argument GL\_MODELVIEW\_STACK\_DEPTH

**glGet** with argument GL\_PROJECTION\_STACK\_DEPTH

**glGet** with argument GL\_TEXTURE\_STACK\_DEPTH

**glGet** with argument GL\_MAX\_MODELVIEW\_STACK\_DEPTH

**glGet** with argument GL\_MAX\_PROJECTION\_STACK\_DEPTH

**glGet** with argument GL\_MAX\_TEXTURE\_STACK\_DEPTH

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

[**glFrustum**](glfrustum.md)
</dt> <dt>

[**glLoadIdentity**](glloadidentity.md)
</dt> <dt>

[**glLoadMatrix**](glloadmatrix.md)
</dt> <dt>

[**glMatrixMode**](glmatrixmode.md)
</dt> <dt>

[**glMultMatrix**](glmultmatrix.md)
</dt> <dt>

[**glOrtho**](glortho.md)
</dt> <dt>

[**glPushMatrix**](glpushmatrix.md)
</dt> <dt>

[**glRotate**](glrotate.md)
</dt> <dt>

[**glScale**](glscale.md)
</dt> <dt>

[**glTranslate**](gltranslate.md)
</dt> <dt>

[**glViewport**](glviewport.md)
</dt> </dl>

 

 





