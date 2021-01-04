---
title: glVertexPointer function (Gl.h)
description: The glVertexPointer function defines an array of vertex data.
ms.assetid: e5f97fdc-9448-4389-8533-3855a3213feb
keywords:
- glVertexPointer function OpenGL
topic_type:
- apiref
api_name:
- glVertexPointer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glVertexPointer function

The **glVertexPointer** function defines an array of vertex data.

## Syntax


```C++
void WINAPI glVertexPointer(
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

The number of coordinates per vertex. The value of *size* must be 2, 3, or 4.

</dd> <dt>

*type* 
</dt> <dd>

The data type of each coordinate in the array using the following symbolic constants: GL\_SHORT, GL\_INT, GL\_FLOAT, and GL\_DOUBLE.

</dd> <dt>

*stride* 
</dt> <dd>

The byte offset between consecutive vertices. When *stride* is zero, the vertices are tightly packed in the array.

</dd> <dt>

*pointer* 
</dt> <dd>

A pointer to the first coordinate of the first vertex in the array.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                              | Meaning                                       |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *size* was not 2, 3, or 4. <br/>        |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>  | *type* was not an accepted value.<br/>  |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *stride* or *count* was negative. <br/> |



## Remarks

The **glVertexPointer** function specifies the location and data of an array of vertex coordinates to use when rendering. The *size* parameter specifies the number of coordinates per vertex. The *type* parameter specifies the data type of each vertex coordinate. The *stride* parameter determines the byte offset from one vertex to the next, enabling the packing of vertices and attributes in a single array or storage in separate arrays. In some implementations, storing the vertices and attributes in a single array can be more efficient than using separate arrays (see [**glInterleavedArrays**](glinterleavedarrays.md)).

A vertex array is enabled when you specify the GL\_VERTEX\_ARRAY constant with [**glEnableClientState**](glenableclientstate.md). When enabled, [**glDrawArrays**](gldrawarrays.md), [**glDrawElements**](gldrawelements.md), and [**glArrayElement**](glarrayelement.md) use the vertex array. By default, the vertex array is disabled.

You cannot include **glVertexPointer** in display lists.

When you specify a vertex array using **glVertexPointer**, the values of all the function's vertex array parameters are saved in a client-side state, and static array elements can be cached. Because the vertex array parameters are client-side state, their values are not saved or restored by [**glPushAttrib**](glpushattrib.md) and **glPopAttrib**.

Although no error is generated if you call **glVertexPointer** within [**glBegin**](glbegin.md) and [**glEnd**](glend.md) pairs, the results are undefined.

The following functions retrieve information related to **glVertexPointer**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_VERTEX\_ARRAY\_SIZE

**glGet** with argument GL\_VERTEX\_ARRAY\_STRIDE

**glGet** with argument GL\_VERTEX\_ARRAY\_COUNT

**glGet** with argument GL\_VERTEX\_ARRAY\_TYPE

[**glGetPointerv**](glgetpointerv.md) with argument GL\_VERTEX\_ARRAY\_POINTER

[**glIsEnabled**](glisenabled.md) with argument GL\_VERTEX\_ARRAY

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

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnableClientState**](glenableclientstate.md)
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

[**glTexCoordPointer**](gltexcoordpointer.md)
</dt> </dl>

 

 





