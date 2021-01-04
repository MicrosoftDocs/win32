---
title: glTexCoordPointer function (Gl.h)
description: The glTexCoordPointer function defines an array of texture coordinates.
ms.assetid: c3640a1b-ccc7-4f1a-94a5-a164f7377dbc
keywords:
- glTexCoordPointer function OpenGL
topic_type:
- apiref
api_name:
- glTexCoordPointer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glTexCoordPointer function

The **glTexCoordPointer** function defines an array of texture coordinates.

## Syntax


```C++
void WINAPI glTexCoordPointer(
         GLint   size,
         GLenum  type,
         GLsizei stride,
   const GLvoid  *pointer
);
```



## Parameters

<dl> <dt>

*size* 
</dt> <dd>

The number of coordinates per array element. The value of *size* must be 1, 2, 3, or 4.

</dd> <dt>

*type* 
</dt> <dd>

The data type of each texture coordinate in the array using the following symbolic constants: **GL\_SHORT**, **GL\_INT**, **GL\_FLOAT**, and **GL\_DOUBLE**.

</dd> <dt>

*stride* 
</dt> <dd>

The byte offset between consecutive array elements. When *stride* is zero, the array elements are tightly packed in the array.

</dd> <dt>

*pointer* 
</dt> <dd>

A pointer to the first coordinate of the first element in the array.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                              | Meaning                                      |
|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>  | *type* was not an accepted value.<br/> |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *size* was not 1, 2, 3, or 4.<br/>     |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *stride* was negative.<br/>            |



## Remarks

The **glTexCoordPointer** function specifies the location and data of an array of texture coordinates to use when rendering.The *size* parameter specifies the number of coordinates used for each element of the array.The *type* parameter specifies the data type of each texture coordinate. The *stride* parameter determines the byte offset from one array element to the next, enabling the packing of vertices and attributes in a single array or storage in separate arrays. In some implementations, storing the vertices and attributes in a single array can be more efficient than using separate arrays. For more information, see [**glInterleavedArrays**](glinterleavedarrays.md). When a texture coordinate array is specified, size, type, stride, and pointer are saved client-side state.

A texture coordinate array is enabled when you specify the **GL\_TEXTURE\_COORD\_ARRAY** constant with [**glEnableClientState**](glenableclientstate.md). When enabled, [**glDrawArrays**](gldrawarrays.md), [**glDrawElements**](gldrawelements.md), and [**glArrayElement**](glarrayelement.md) use the texture coordinate array. By default the texture coordinate array is disabled.

You cannot include **glTexCoordPointer** in display lists.

When you specify a texture coordinate array using **glTexCoordPointer**, the values of all the function's texture coordinate array parameters are saved in a client-side state, and static array elements can be cached. Because the texture coordinate array parameters are client-side state, their values are not saved or restored by [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md).

Although no error is generated when you call **glTexCoordPointer** within [**glBegin**](glbegin.md) and [**glEnd**](glend.md) pairs, the results are undefined.

The following functions retrieve information related to **glTexCoordPointer**:

[**glIsEnabled**](glisenabled.md) with argument **GL\_TEXTURE\_COORD\_ARRAY**

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument **GL\_TEXTURE\_COORD\_ARRAY\_SIZE**

**glGet** with argument **GL\_TEXTURE\_COORD\_ARRAY\_STRIDE**

**glGet** with argument **GL\_TEXTURE\_COORD\_ARRAY\_COUNT**

**glGet** with argument **GL\_TEXTURE\_COORD\_ARRAY\_TYPE**

[**glGetPointerv**](glgetpointerv.md) with argument **GL\_TEXTURE\_COORD\_ARRAY\_POINTER**

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

[**glArrayElement**](glarrayelement.md)
</dt> <dt>

[**glColorPointer**](glcolorpointer.md)
</dt> <dt>

[**glDrawArrays**](gldrawarrays.md)
</dt> <dt>

[**glDrawElements**](gldrawelements.md)
</dt> <dt>

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glGetPointerv**](glgetpointerv.md)
</dt> <dt>

[**glGetString**](glgetstring.md)
</dt> <dt>

[**glIndexPointer**](glindexpointer.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glNormalPointer**](glnormalpointer.md)
</dt> <dt>

[**glPopClientAttrib**](glpopclientattrib.md)
</dt> <dt>

[**glPushClientAttrib**](glpushclientattrib.md)
</dt> <dt>

[**glTexCoord**](gltexcoord-functions.md)
</dt> <dt>

[**glVertexPointer**](glvertexpointer.md)
</dt> </dl>

 

 





