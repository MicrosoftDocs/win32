---
title: glColorPointer function (Gl.h)
description: The glColorPointer function defines an array of colors.
ms.assetid: 4d9d05fb-691d-4b71-b079-c42dc7103055
keywords:
- glColorPointer function OpenGL
topic_type:
- apiref
api_name:
- glColorPointer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glColorPointer function

The **glColorPointer** function defines an array of colors.

## Syntax


```C++
void WINAPI glColorPointer(
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

The number of components per color. The value must be either 3 or 4.

</dd> <dt>

*type* 
</dt> <dd>

The data type of each color component in a color array. Acceptable data types are specified with the following constants: GL\_BYTE, GL\_UNSIGNED\_BYTE, GL\_SHORT, GL\_UNSIGNED\_SHORT, GL\_INT, GL\_UNSIGNED\_INT, GL\_FLOAT, or GL\_DOUBLE.

</dd> <dt>

*stride* 
</dt> <dd>

The byte offset between consecutive colors. When *stride* is zero, the colors are tightly packed in the array.

</dd> <dt>

*pointer* 
</dt> <dd>

A pointer to the first component of the first color element in a color array.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                              | Meaning                                      |
|---------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *size* was not 3 or 4.<br/>            |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>  | *type* was not an accepted value.<br/> |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | *stride* or *count* was negative.<br/> |



## Remarks

The **glColorPointer** function specifies the location and data format of an array of color components to use when rendering. The *stride* parameter determines the byte offset from one color to the next, enabling the packing of vertex attributes in a single array or storage in separate arrays. In some implementations, storing vertex attributes in a single array can be more efficient than the use of separate arrays.

Enabled the color array by specifying the GL\_COLOR\_ARRAY constant with [**glEnableClientState**](glenableclientstate.md). Calling [**glArrayElement**](glarrayelement.md), [**glDrawElements**](gldrawelements.md), or [**glDrawArrays**](gldrawarrays.md) uses the color array that is thus enabled. By default, the color array is disabled. The **glColorPointer** calls cannot by entered in display lists.

When you specify a color array using **glColorPointer**, the values of all the function's color array parameters are saved in a client-side state, and you can cache static array elements. Because the color array parameters are in a client-side state, [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md) do not save or restore the parameters' values.

Although specifying the color array within [**glBegin**](glbegin.md) and [**glend**](glend.md) pairs does not generate an error, the results are undefined.

The following functions retrieve information related to the **glColorPointer** function:

[**glIsEnabled**](glisenabled.md) with argument GL\_COLOR\_ARRAY

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_COLOR\_ARRAY\_SIZE

**glGet** with argument GL\_COLOR\_ARRAY\_TYPE

**glGet** with argument GL\_COLOR\_ARRAY\_STRIDE

**glGet** with argument GL\_COLOR\_ARRAY\_COUNT

[**glGetPointerv**](glgetpointerv.md) with argument GL\_COLOR\_ARRAY\_POINTER

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

[**glDrawArrays**](gldrawarrays.md)
</dt> <dt>

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnableClientState**](glenableclientstate.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glGetString**](glgetstring.md)
</dt> <dt>

[**glGetPointerv**](glgetpointerv.md)
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

 

 





