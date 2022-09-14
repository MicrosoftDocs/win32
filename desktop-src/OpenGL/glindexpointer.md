---
title: glIndexPointer function (Gl.h)
description: The glIndexPointer function defines an array of color indexes.
ms.assetid: b435d950-1f87-4041-93e4-f1f8786cabdb
keywords:
- glIndexPointer function OpenGL
topic_type:
- apiref
api_name:
- glIndexPointer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glIndexPointer function

The **glIndexPointer** function defines an array of color indexes.

## Syntax


```C++
void WINAPI glIndexPointer(
         GLenum  type,
         GLsizei stride,
   const GLvoid  *pointer
);
```



## Parameters

<dl> <dt>

*type* 
</dt> <dd>

The data type of each color index in the array using the following symbolic constants: GL\_SHORT, GL\_INT, GL\_FLOAT, GL\_DOUBLE.

</dd> <dt>

*stride* 
</dt> <dd>

The byte offset between consecutive color indexes. When *stride* is zero, the color indexes are tightly packed in the array.

</dd> <dt>

*pointer* 
</dt> <dd>

A pointer to the first color index in the array.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                              | Meaning                                      |
|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>  | *type* was not an accepted value.<br/> |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *stride* or *count* was negative.<br/> |



## Remarks

The **glIndexPointer** function specifies the location and data of an array of color indexes to use when rendering. The *type* parameter specifies the data type of each color index and *stride* determines the byte offset from one color index to the next, enabling the packing of vertices and attributes in a single array or storage in separate arrays. In some implementations, storing the vertices and attributes in a single array can be more efficient than using separate arrays. For more information, see [**glInterleavedArrays**](glinterleavedarrays.md).

A color-index array is enabled when you specify the GL\_INDEX\_ARRAY constant with [**glEnableClientState**](glenableclientstate.md). When enabled, [**glDrawArrays**](gldrawarrays.md) and [**glArrayElement**](glarrayelement.md) use the color-index array. By default the color-index array is disabled.

You cannot include **glIndexPointer** in display lists.

When you specify a color-index array using **glIndexPointer**, the values of all the function's color-index array parameters are saved in a client-side state and static array elements can be cached. Because the color-index array parameters are client-side state, their values are not saved or restored by [**glPushAttrib**](glpushattrib.md) and **glPopAttrib**.

Although no error is generated when you call **glIndexPointer** within [**glBegin**](glbegin.md) and **glEnd** pairs, the results are undefined.

The following functions retrieve information related to **glIndexPointer**:

[**glIsEnabled**](glisenabled.md) with argument GL\_INDEX\_ARRAY

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_INDEX\_ARRAY\_STRIDE

**glGet** with argument GL\_INDEX\_ARRAY\_COUNT

**glGet** with argument GL\_INDEX\_ARRAY\_TYPE

**glGet** with argument GL\_INDEX\_ARRAY\_SIZE

[**glGetPointerv**](glgetpointerv.md) with argument GL\_INDEX\_ARRAY\_POINTER

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

[**glGetPointerv**](glgetpointerv.md)
</dt> <dt>

[**glGetString**](glgetstring.md)
</dt> <dt>

[**glNormalPointer**](glnormalpointer.md)
</dt> <dt>

[**glPushAttrib**](glpushattrib.md)
</dt> <dt>

[**glTexCoordPointer**](gltexcoordpointer.md)
</dt> <dt>

[**glVertexPointer**](glvertexpointer.md)
</dt> </dl>

 

 





