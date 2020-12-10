---
title: glGenLists function (Gl.h)
description: The glGenLists function generates a contiguous set of empty display lists.
ms.assetid: 07a97e89-1fbe-4405-b1b0-c4c47b098633
keywords:
- glGenLists function OpenGL
topic_type:
- apiref
api_name:
- glGenLists
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGenLists function

The **glGenLists** function generates a contiguous set of empty display lists.

## Syntax


```C++
GLuint WINAPI glGenLists(
   GLsizei range
);
```



## Parameters

<dl> <dt>

*range* 
</dt> <dd>

The number of contiguous empty display lists to be generated.

</dd> </dl>

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *range* was negative.<br/>                                                                                                      |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glGenLists** function has one argument, *range*. It returns an integer *n* such that *range* contiguous empty display lists, named *n*, *n* + 1, . . ., *n* + (*range* - 1), are created. If *range* is zero, if there is no group of *range* contiguous names available, or if any error is generated, then no display lists are generated and zero is returned.

The following function retrieves information related to **glGenLists**:

[**glIsList**](glislist.md)

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

[**glCallList**](glcalllist.md)
</dt> <dt>

[**glCallLists**](glcalllists.md)
</dt> <dt>

[**glDeleteLists**](gldeletelists.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIsList**](glislist.md)
</dt> <dt>

[**glNewList**](glnewlist.md)
</dt> </dl>

 

 





