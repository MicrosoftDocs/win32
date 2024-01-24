---
title: gluGetTessProperty function (Glu.h)
description: The gluGetTessProperty function gets a tessellation object property.
ms.assetid: 6aa565d8-2257-4259-a959-b7d806a7ed96
keywords:
- gluGetTessProperty function OpenGL
topic_type:
- apiref
api_name:
- gluGetTessProperty
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluGetTessProperty function

The **gluGetTessProperty** function gets a tessellation object property.

## Syntax


```C++
void WINAPI gluGetTessProperty(
   GLUtesselator *tess,
   GLenum        which,
   GLdouble      *value
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*which* 
</dt> <dd>

The property whose value is to be retrieved. The following values are valid: GLU\_TESS\_WINDING\_RULE, GLU\_TESS\_BOUNDARY\_ONLY, and GLU\_TESS\_TOLERANCE.

</dd> <dt>

*value* 
</dt> <dd>

A pointer to the location where the value of the named property is written.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use **gluGetTessProperty** to retrieve properties stored in a tessellation object. These properties affect the way tessellation objects are interpreted and rendered. For information about what the properties are and what they do, see [**gluTessProperty**](glutessproperty.md).

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

[**gluNewTess**](glunewtess.md)
</dt> <dt>

[**gluTessProperty**](glutessproperty.md)
</dt> </dl>

 

 





