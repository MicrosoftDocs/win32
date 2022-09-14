---
title: glArrayElement function (Gl.h)
description: The glArrayElement function specifies the array elements used to render a vertex.
ms.assetid: 2c4d76bb-e4c9-4baa-a190-66298b8a4335
keywords:
- glArrayElement function OpenGL
topic_type:
- apiref
api_name:
- glArrayElement
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glArrayElement function

The **glArrayElement** function specifies the array elements used to render a vertex.

## Syntax


```C++
void WINAPI glArrayElement(
   GLint index
);
```



## Parameters

<dl> <dt>

*index* 
</dt> <dd>

An index in the enabled arrays.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use the **glArrayElement** function within [**glBegin**](glbegin.md) and [**glEnd**](glend.md) pairs to specify vertex and attribute data for point, line, and polygon primitives. The **glArrayElement** function specifies the data for a single vertex using vertex and attribute data located at the *index* of the enabled vertex arrays.

You can use **glArrayElement** to construct primitives by indexing vertex data, rather than by streaming through arrays of data in first-to-last order. Because **glArrayElement** specifies a single vertex only, you can explicitly specify attributes for individual primitives. For example, you can set a single normal for each individual triangle.

When you include calls to **glArrayElement** in display lists, the necessary array data, determined by the array pointers and enable values, is entered in the display list also. Array pointer and enable values are determined when display lists are created, not when display lists are executed.

You can read and cache static array data at any time with **glArrayElement**. When you modify the elements of a static array without specifying the array again, the results of any subsequent calls to **glArrayElement** are undefined.

When you call **glArrayElement** without first calling **glEnableClientState**(GL\_VERTEX\_ARRAY), no drawing occurs, but the attributes corresponding to enabled arrays are modified. Although no error is generated when you specify an array within **glBegin** and **glEnd** pairs, the results are undefined.

> [!Note]  
> The **glArrayElement** function is only available in OpenGL version 1.1 or later.

 

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

[**glColorPointer**](glcolorpointer.md)
</dt> <dt>

[**glDrawArrays**](gldrawarrays.md)
</dt> <dt>

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnableClientState**](glenableclientstate.md)
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

 

 





