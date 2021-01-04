---
title: glColorMask function (Gl.h)
description: The glColorMask function enables and disables writing of frame-buffer color components.
ms.assetid: 23d7f94e-f290-423c-a841-f86caf94009d
keywords:
- glColorMask function OpenGL
topic_type:
- apiref
api_name:
- glColorMask
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glColorMask function

The **glColorMask** function enables and disables writing of frame-buffer color components.

## Syntax


```C++
void WINAPI glColorMask(
   GLboolean red,
   GLboolean green,
   GLboolean blue,
   GLboolean alpha
);
```



## Parameters

<dl> <dt>

*red* 
</dt> <dd>

Specify whether red can or cannot be written into the framebuffer. The default values is GL\_TRUE, indicating that the color component can be written.

</dd> <dt>

*green* 
</dt> <dd>

Specify whether green can or cannot be written into the framebuffer. The default value is GL\_TRUE, indicating that the color component can be written.

</dd> <dt>

*blue* 
</dt> <dd>

Specify whether blue can or cannot be written into the framebuffer. The default value is GL\_TRUE, indicating that the color component can be written.

</dd> <dt>

*alpha* 
</dt> <dd>

Specify whether alpha can or cannot be written into the framebuffer. The default value is GL\_TRUE, indicating that the color component can be written.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glColorMask** function specifies whether the individual color components in the framebuffer can or cannot be written. If *red* is GL\_FALSE, for example, no change is made to the red component of any pixel in any of the color buffers, regardless of the drawing operation attempted.

Changes to individual bits of components cannot be controlled. Rather, changes are either enabled or disabled for entire color components.

The following functions retrieve information related to **glColorMask**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_COLOR\_WRITEMASK

**glGet** with argument GL\_RGBA\_MODE

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

[**glDepthMask**](gldepthmask.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIndex**](glindex-functions.md)
</dt> <dt>

[**glIndexMask**](glindexmask.md)
</dt> <dt>

[**glStencilMask**](glstencilmask.md)
</dt> </dl>

 

 





