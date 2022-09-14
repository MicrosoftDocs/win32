---
title: gluQuadricTexture function (Glu.h)
description: The gluQuadricTexture function specifies whether quadrics are to be textured.
ms.assetid: 11681497-f099-4856-a0ac-6a44abd3e1a1
keywords:
- gluQuadricTexture function OpenGL
topic_type:
- apiref
api_name:
- gluQuadricTexture
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluQuadricTexture function

The **gluQuadricTexture** function specifies whether quadrics are to be textured.

## Syntax


```C++
void WINAPI gluQuadricTexture(
   GLUquadric *quadObject,
   GLboolean  textureCoords
);
```



## Parameters

<dl> <dt>

*quadObject* 
</dt> <dd>

The quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*textureCoords* 
</dt> <dd>

A flag indicating whether texture coordinates are to be generated. The following values are valid.



| Value                                                                                                                                          | Meaning                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <span id="GL_TRUE"></span><span id="gl_true"></span><dl> <dt>**GL\_TRUE**</dt> </dl>    | Generate texture coordinates.<br/>                                   |
| <span id="GL_FALSE"></span><span id="gl_false"></span><dl> <dt>**GL\_FALSE**</dt> </dl> | Do not generate texture coordinates. This is the default value.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluQuadricTexture** function specifies whether texture coordinates are to be generated for quadrics rendered with **quadObject**.

The manner in which texture coordinates are generated depends upon the specific quadric rendered.

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
</dt> </dl>

 

 





