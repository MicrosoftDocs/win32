---
title: glGetPointerv function (Gl.h)
description: The glGetPointerv function returns the address of a vertex data array.
ms.assetid: 6f85c508-9335-4474-8cc5-e67c7421a8e4
keywords:
- glGetPointerv function OpenGL
topic_type:
- apiref
api_name:
- glGetPointerv
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetPointerv function

The **glGetPointerv** function returns the address of a vertex data array.

## Syntax


```C++
void WINAPI glGetPointerv(
   GLenum pname,
   GLvoid **params
);
```



## Parameters

<dl> <dt>

*pname* 
</dt> <dd>

The type of array pointer to return from the following symbolic constants: GL\_COLOR\_ARRAY\_POINTER, GL\_EDGE\_FLAG\_ARRAY\_POINTER, GL\_FEEDBACK\_BUFFER\_POINTER, GL\_INDEX\_ARRAY\_POINTER, GL\_NORMAL\_ARRAY\_POINTER, GL\_TEXTURE\_COORD\_ARRAY\_POINTER, GL\_SELECTION\_BUFFER\_POINTER, and GL\_VERTEX\_ARRAY\_POINTER.

</dd> <dt>

*params* 
</dt> <dd>

Returns the value of the array pointer specified by *pname*.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                             | Meaning                                       |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl> | *pname* was not an accepted value.<br/> |



## Remarks

The **glGetPointerv** function returns array pointer information. The *pname* parameter is a symbolic constant specifying the kind of array pointer to return, and *params* is a pointer to a location to place the returned data.

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

 

 





