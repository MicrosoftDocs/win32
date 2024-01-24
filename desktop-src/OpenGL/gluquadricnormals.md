---
title: gluQuadricNormals function (Glu.h)
description: The gluQuadricNormals function specifies what kind of normals are to be used for quadrics.
ms.assetid: 945759ec-ed4a-480f-8243-49fc785867c1
keywords:
- gluQuadricNormals function OpenGL
topic_type:
- apiref
api_name:
- gluQuadricNormals
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluQuadricNormals function

The **gluQuadricNormals** function specifies what kind of normals are to be used for quadrics.

## Syntax


```C++
void WINAPI gluQuadricNormals(
   GLUquadric *quadObject,
   GLenum     normals
);
```



## Parameters

<dl> <dt>

*quadObject* 
</dt> <dd>

The quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*normals* 
</dt> <dd>

The desired type of normals. The following values are valid.



| Value                                                                                                                                                | Meaning                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="GLU_NONE"></span><span id="glu_none"></span><dl> <dt>**GLU\_NONE**</dt> </dl>       | No normals are generated.<br/>                                                         |
| <span id="GLU_FLAT"></span><span id="glu_flat"></span><dl> <dt>**GLU\_FLAT**</dt> </dl>       | One normal is generated for every facet of a quadric.<br/>                             |
| <span id="GLU_SMOOTH"></span><span id="glu_smooth"></span><dl> <dt>**GLU\_SMOOTH**</dt> </dl> | One normal is generated for every vertex of a quadric. This is the default value.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluQuadricNormals** function specifies what kind of normals are to be used for quadrics rendered with **quadObject**.

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

[**gluQuadricOrientation**](gluquadricorientation.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> </dl>

 

 





