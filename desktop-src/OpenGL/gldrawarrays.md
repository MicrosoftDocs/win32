---
title: glDrawArrays function (Gl.h)
description: The glDrawArrays function specifies multiple primitives to render.
ms.assetid: 6ebd467b-5a63-43e4-b3fd-242c704d7d13
keywords:
- glDrawArrays function OpenGL
topic_type:
- apiref
api_name:
- glDrawArrays
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glDrawArrays function

The **glDrawArrays** function specifies multiple primitives to render.

## Syntax


```C++
void WINAPI glDrawArrays(
   GLenum  mode,
   GLint   first,
   GLsizei count
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

The kind of primitives to render. The following constants specify acceptable types of primitives: GL\_POINTS, GL\_LINE\_STRIP, GL\_LINE\_LOOP, GL\_LINES, GL\_TRIANGLE\_STRIP, GL\_TRIANGLE\_FAN, GL\_TRIANGLES, GL\_QUAD\_STRIP, GL\_QUADS, and GL\_POLYGON.

</dd> <dt>

*first* 
</dt> <dd>

The starting index in the enabled arrays.

</dd> <dt>

*count* 
</dt> <dd>

The number of indexes to render.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *count* was negative.<br/>                                                                                                      |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was not an accepted value.<br/>                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

With **glDrawArrays**, you can specify multiple geometric primitives to render. Instead of calling separate OpenGL functions to pass each individual vertex, normal, or color, you can specify separate arrays of vertices, normals, and colors to define a sequence of primitives (all the same kind) with a single call to **glDrawArrays**.

When you call **glDrawArrays**, *count* sequential elements from each enabled array are used to construct a sequence of geometric primitives, beginning with the *first* element. The *mode* parameter specifies what kind of primitive to construct and how to use the array elements to construct the primitives.

After **glDrawArrays** returns, the values of vertex attributes that are modified by **glDrawArrays** are undefined. For example, if GL\_COLOR\_ARRAY is enabled, the value of the current color is undefined after **glDrawArrays** returns. Attributes not modified by **glDrawArrays** remain defined. When GL\_VERTEX\_ARRAY is not enabled, no geometric primitives are generated but the attributes corresponding to enabled arrays are modified.

You can include **glDrawArrays** in display lists. When you include **glDrawArrays** in a display list, the necessary array data, determined by the array pointers and the enables, are generated and entered in the display list. The values of array pointers and enables are determined during the creation of display lists.

You can read static array data at any time. If any static array elements are modified and the array is not specified again, the results of any subsequent calls to **glDrawArrays** are undefined.

Although no error is generated when you specify an array more than once within [**glBegin**](glbegin.md) and [**glend**](glend.md) pairs, the results are undefined.

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

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGetPointerv**](glgetpointerv.md)
</dt> <dt>

[**glGetString**](glgetstring.md)
</dt> <dt>

[**glIndexPointer**](glindexpointer.md)
</dt> <dt>

[**glNormalPointer**](glnormalpointer.md)
</dt> <dt>

[**glTexCoordPointer**](gltexcoordpointer.md)
</dt> <dt>

[**glVertexPointer**](glvertexpointer.md)
</dt> </dl>

 

 





