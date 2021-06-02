---
title: gluQuadricCallback function (Glu.h)
description: The gluQuadricCallback function defines a callback for a quadric object.
ms.assetid: 1f1e9fe9-7239-419c-92b6-af2534850ac5
keywords:
- gluQuadricCallback function OpenGL
topic_type:
- apiref
api_name:
- gluQuadricCallback
api_location:
- Glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluQuadricCallback function

The **gluQuadricCallback** function defines a callback for a quadric object.

## Syntax


```C++
void WINAPI gluQuadricCallback(
   GLUquadric *qobj,
   GLenum     which,
   void (CALLBACK *fn)()
);
```



## Parameters

<dl> <dt>

*qobj* 
</dt> <dd>

The quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*which* 
</dt> <dd>

The callback being defined. The only valid value is GLU\_ERROR.



| Value                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GLU_ERROR"></span><span id="glu_error"></span><dl> <dt>**GLU\_ERROR**</dt> </dl> | The **gluQuadricCallback** function is called when an error is encountered. Its single argument is of type **GLenum**, and it indicates the specific error that occurred. Character strings describing these errors can be retrieved with the [**gluErrorString**](gluerrorstring.md) call.<br/> |



 

</dd> <dt>

*fn* 
</dt> <dd>

The function to be called.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use **gluQuadricCallback** to define a new callback to be used by a quadric object. If the specified callback is already defined, it is replaced. If *fn* is **NULL**, any existing callback is erased.

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

[**gluNewQuadric**](glunewquadric.md)
</dt> </dl>

 

 





