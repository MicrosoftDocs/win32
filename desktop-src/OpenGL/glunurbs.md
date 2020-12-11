---
title: gluNurbsCallback function (Glu.h)
description: The gluNurbsCallback function defines a callback for a Non-Uniform Rational B-Spline (NURBS) object.
ms.assetid: 1e9afc00-57c6-459e-a9fc-463f45df2084
keywords:
- gluNurbsCallback function OpenGL
topic_type:
- apiref
api_name:
- gluNurbsCallback
api_location:
- Glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNurbsCallback function

The **gluNurbsCallback** function defines a callback for a Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) object.

## Syntax


```C++
void WINAPI gluNurbsCallback(
   GLUnurbs *nobj,
   GLenum   which,
   void (CALLBACK *fn)()
);
```



## Parameters

<dl> <dt>

*nobj* 
</dt> <dd>

The NURBS object (created with [**gluNewNurbsRenderer**](glunewnurbsrenderer.md)).

</dd> <dt>

*which* 
</dt> <dd>

The callback being defined. The only valid value is GLU\_ERROR. The meaning of GLU\_ERROR means that the error function is called when an error is encountered. Its single argument is of type **GLenum**, and it indicates the specific error that occurred. There are 37 errors unique to NURBS, named GLU\_NURBS\_ERROR1 through GLU\_NURBS\_ERROR37. Character strings describing these errors can be retrieved with [**gluErrorString**](gluerrorstring.md).

</dd> <dt>

*fn* 
</dt> <dd>

A pointer to the callback function.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use **gluNurbsCallback** to define a callback to be used by a NURBS object. If the specified callback is already defined, it is replaced. If *fn* is **NULL**, then any existing callback is erased.

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

[**gluErrorString**](gluerrorstring.md)
</dt> <dt>

[**gluNewNurbsRenderer**](glunewnurbsrenderer.md)
</dt> </dl>

 

 





