---
title: glClearAccum function (Gl.h)
description: The glClearAccum function specifies the clear values for the accumulation buffer.
ms.assetid: 77d8f340-be47-43f4-96fc-31025a4c8b4e
keywords:
- glClearAccum function OpenGL
topic_type:
- apiref
api_name:
- glClearAccum
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glClearAccum function

The **glClearAccum** function specifies the clear values for the accumulation buffer.

## Syntax


```C++
void WINAPI glClearAccum(
   GLfloat red,
   GLfloat green,
   GLfloat blue,
   GLfloat alpha
);
```



## Parameters

<dl> <dt>

*red* 
</dt> <dd>

The red value used when the accumulation buffer is cleared. The default value is zero.

</dd> <dt>

*green* 
</dt> <dd>

The green value used when the accumulation buffer is cleared. The default value is zero.

</dd> <dt>

*blue* 
</dt> <dd>

The blue value used when the accumulation buffer is cleared. The default value is zero.

</dd> <dt>

*alpha* 
</dt> <dd>

The alpha value used when the accumulation buffer is cleared. The default value is zero.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glClearAccum** function specifies the red, green, blue, and alpha values used by [**glClear**](glclear.md) to clear the accumulation buffer.

Values specified by **glClearAccum** are clamped to the range \[1,1\].

The following function retrieves information related to **glClearAccum**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_ACCUM\_CLEAR\_VALUE

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

[**glClear**](glclear.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> </dl>

 

 





