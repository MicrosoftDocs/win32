---
title: glEdgeFlagPointer function (Gl.h)
description: The glEdgeFlagPointer function defines an array of edge flags.
ms.assetid: e0e7e442-533d-4c41-addd-a215ce0b1c56
keywords:
- glEdgeFlagPointer function OpenGL
topic_type:
- apiref
api_name:
- glEdgeFlagPointer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glEdgeFlagPointer function

The **glEdgeFlagPointer** function defines an array of edge flags.

## Syntax


```C++
void WINAPI glEdgeFlagPointer(
         GLsizei stride,
   const GLvoid  *pointer
);
```



## Parameters

<dl> <dt>

*stride* 
</dt> <dd>

The byte offset between consecutive edge flags. When *stride* is zero, the edge flags are tightly packed in the array.

</dd> <dt>

*pointer* 
</dt> <dd>

A pointer to the first edge flag in the array.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                             | Meaning                                      |
|--------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl> | *stride* or *count* was negative.<br/> |



## Remarks

The **glEdgeFlagPointer** function specifies the location and data of an array of Boolean edge flags to use when rendering. The *stride* parameter determines the byte offset from one edge flag to the next, which enables the packing of vertices and attributes in a single array or storage in separate arrays. In some implementations, storing the vertices and attributes in a single array can be more efficient than using separate arrays.

An edge-flag array is enabled when you specify the GL\_EDGE\_FLAG\_ARRAY constant with [**glEnableClientState**](glenableclientstate.md). When enabled, [**glDrawArrays**](gldrawarrays.md) or [**glArrayElement**](glarrayelement.md) uses the edge-flag array. By default the edge-flag array is disabled.

Use **glDrawArrays** to construct a sequence of primitives (all of the same type) from prespecified vertex and vertex attribute arrays. Use **glArrayElement** to specify primitives by indexing vertices and vertex attributes, and [**glDrawElements**](gldrawelements.md) to construct a sequence of primitives by indexing vertices and vertex attributes.

You cannot include **glEdgeFlagPointer** in display lists.

When you specify an edge-flag array using **glEdgeFlagPointer**, the values of all the function's edge-flag array parameters are saved in a client-side state and static array elements can be cached. Because the edge-flag array parameters are in a client-side state, [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md) do not save or restore their values.

Although calling **glEdgeFlagPointer** within a [**glBegin**](glbegin.md)/[**glend**](glend.md) pair does not generate an error, the results are undefined.

The following functions retrieve information related to the **glEdgeFlagPointer** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_EDGE\_FLAG\_ARRAY\_STRIDE

**glGet** with argument GL\_EDGE\_FLAG\_ARRAY\_COUNT

[**glGetPointerv**](glgetpointerv.md) with argument GL\_EDGE\_FLAG\_ARRAY\_POINTER

[**glIsEnabled**](glisenabled.md) with argument GL\_EDGE\_FLAG\_ARRAY

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

[**glBegin**](glbegin.md)
</dt> <dt>

[**glColorPointer**](glcolorpointer.md)
</dt> <dt>

[**glDrawArrays**](gldrawarrays.md)
</dt> <dt>

[**glEnableClientState**](glenableclientstate.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
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

[**glPopAttrib**](glpopattrib.md)
</dt> <dt>

[**glPushAttrib**](glpushattrib.md)
</dt> <dt>

[**glTexCoordPointer**](gltexcoordpointer.md)
</dt> <dt>

[**glVertexPointer**](glvertexpointer.md)
</dt> </dl>

 

 





