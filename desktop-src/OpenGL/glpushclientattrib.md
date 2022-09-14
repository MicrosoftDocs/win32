---
title: glPushClientAttrib function (Gl.h)
description: The glPushClientAttrib and glPopClientAttrib functions save and restore groups of client-state variables on the client-attribute stack. | glPushClientAttrib function (Gl.h)
ms.assetid: 69f28af6-1023-4546-95ff-169525c23b07
keywords:
- glPushClientAttrib function OpenGL
topic_type:
- apiref
api_name:
- glPushClientAttrib
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPushClientAttrib function

The **glPushClientAttrib** and [**glPopClientAttrib**](glpopclientattrib.md) functions save and restore groups of client-state variables on the client-attribute stack.

## Syntax


```C++
void WINAPI glPushClientAttrib(
   GLbitfield mask
);
```



## Parameters

<dl> <dt>

*mask* 
</dt> <dd>

A mask that indicates which attributes to save. The following are the symbolic mask constants and their associated OpenGL client states.



| Value                                                                                                                                                                                                                                            | Meaning                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <span id="GL_CLIENT_PIXEL_STORE_BIT"></span><span id="gl_client_pixel_store_bit"></span><dl> <dt>**GL\_CLIENT\_PIXEL\_STORE\_BIT**</dt> </dl>                                             | Pixel storage mode attributes.<br/>         |
| <span id="GL_CLIENT_VERTEX_ARRAY_BIT"></span><span id="gl_client_vertex_array_bit"></span><dl> <dt>**GL\_CLIENT\_VERTEX\_ARRAY\_BIT**</dt> </dl>                                          | Vertex array attributes.<br/>               |
| <span id="GL_CLIENT_ALL_ATTRIB_BITs"></span><span id="gl_client_all_attrib_bits"></span><span id="GL_CLIENT_ALL_ATTRIB_BITS"></span><dl> <dt>**GL\_CLIENT\_ALL\_ATTRIB\_BITs**</dt> </dl> | all stackable client-state attributes.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                               | Meaning                                                                       |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**GL\_STACK\_OVERFLOW**</dt> </dl> | The function was called while the client-attribute stack was full.<br/> |



## Remarks

The **glPushClientAttrib** function uses its mask parameter to determine which groups of client-state variables are saved on the client-attribute stack. You can use the bitwise OR operator to join together accepted symbolic constants to set bits and construct a mask.

The [**glPopClientAttrib**](glpopclientattrib.md) function restores the values of the client-state variables last saved with **glPushclientAttrib**. Client-state variables not previously saved are left unchanged. Pushing attributes onto a full client-attribute stack or popping attributes off an empty stack sets an error flag and no other change is made to the OpenGL state. By default the client attribute stack is empty.

Some OpenGL client-state values cannot be saved on the client-attribute stack. For example, you cannot save the select or feedback states on the client-attribute stack. The depth of the client-attribute stack is at least 16.

The **glPushclientAttrib** and **glPopClientAttrib** functions are not compiled into display lists, but are executed immediately.

The **glPushClientAttrib** and **glPopClientAttrib** functions can only push and pop pixel storage modes and vertex array client states. You must use [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md) to push and pop states that are kept on the server.

> [!Note]  
> The **glPushClientAttrib** and **glPopClientAttrib** functions are only available in OpenGL version 1.1 or later.

 

The following functions retrieve information related to **glPushClientAttrib** and **glPopClientAttrib**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_CLIENT\_ATTRIB\_STACK\_DEPTH

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAX\_CLIENT\_ATTRIB\_STACK\_DEPTH

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

[**glColorPointer**](glcolorpointer.md)
</dt> <dt>

[**glDisableClientState**](gldisableclientstate.md)
</dt> <dt>

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnableClientState**](glenableclientstate.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glGetError**](glgeterror.md)
</dt> <dt>

[**glIndexPointer**](glindexpointer.md)
</dt> <dt>

[**glNormalPointer**](glnormalpointer.md)
</dt> <dt>

[**glNewList**](glnewlist.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPushAttrib**](glpushattrib.md)
</dt> <dt>

[**glTexCoordPointer**](gltexcoordpointer.md)
</dt> <dt>

[**glVertexPointer**](glvertexpointer.md)
</dt> </dl>

 

 





