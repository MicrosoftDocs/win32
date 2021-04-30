---
title: gluDeleteQuadric function (Glu.h)
description: The gluDeleteQuadric function destroys a quadric object.
ms.assetid: 09efd887-0fe8-4a56-bc6f-2177a4930035
keywords:
- gluDeleteQuadric function OpenGL
topic_type:
- apiref
api_name:
- gluDeleteQuadric
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluDeleteQuadric function

The **gluDeleteQuadric** function destroys a quadric object.

## Syntax


```C++
void WINAPI gluDeleteQuadric(
   GLUquadricObj *state
);
```



## Parameters

<dl> <dt>

*state* 
</dt> <dd>

The quadric object to be destroyed (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluDeleteQuadric** function destroys the quadric object and frees any memory that it used. After you have called **gluDeleteQuadric**, you cannot use *state* again.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



## See also

<dl> <dt>

[**gluNewQuadric**](glunewquadric.md)
</dt> </dl>

 

 





