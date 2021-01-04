---
title: gluQuadricOrientation function (Glu.h)
description: The gluQuadricOrientation function specifies inside or outside orientation for quadrics.
ms.assetid: 4e3fc6d3-5a39-455b-bd24-8eb497333096
keywords:
- gluQuadricOrientation function OpenGL
topic_type:
- apiref
api_name:
- gluQuadricOrientation
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluQuadricOrientation function

The **gluQuadricOrientation** function specifies inside or outside orientation for quadrics.

## Syntax


```C++
void WINAPI gluQuadricOrientation(
   GLUquadric *quadObject,
   GLenum     orientation
);
```



## Parameters

<dl> <dt>

*quadObject* 
</dt> <dd>

The quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*orientation* 
</dt> <dd>

The desired orientation. The following values are valid.



| Value                                                                                                                                                   | Meaning                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="GLU_OUTSIDE"></span><span id="glu_outside"></span><dl> <dt>**GLU\_OUTSIDE**</dt> </dl> | Draw quadrics with normals pointing outward. This is the default value.<br/> |
| <span id="GLU_INSIDE"></span><span id="glu_inside"></span><dl> <dt>**GLU\_INSIDE**</dt> </dl>    | Draw quadrics with normals pointing inward.<br/>                             |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluQuadricOrientation** function specifies what kind of orientation is desired for quadrics rendered with **quadObject**. The interpretation of outward and inward depends on the quadric being drawn.

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
</dt> <dt>

[**gluQuadricDrawStyle**](gluquadricdrawstyle.md)
</dt> <dt>

[**gluQuadricNormals**](gluquadricnormals.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> </dl>

 

 





