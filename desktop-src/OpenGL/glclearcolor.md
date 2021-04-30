---
title: glClearColor function (Gl.h)
description: The glClearColor function specifies clear values for the color buffers.
ms.assetid: f938e3f4-9db3-4c24-97ae-531b6799224e
keywords:
- glClearColor function OpenGL
topic_type:
- apiref
api_name:
- glClearColor
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glClearColor function

The **glClearColor** function specifies clear values for the color buffers.

## Syntax


```C++
void WINAPI glClearColor(
   GLclampf red,
   GLclampf green,
   GLclampf blue,
   GLclampf alpha
);
```



## Parameters

<dl> <dt>

*red* 
</dt> <dd>

The red value that [**glClear**](glclear.md) uses to clear the color buffers. The default value is zero.

</dd> <dt>

*green* 
</dt> <dd>

The green value that [**glClear**](glclear.md) uses to clear the color buffers. The default value is zero.

</dd> <dt>

*blue* 
</dt> <dd>

The blue value that [**glClear**](glclear.md) uses to clear the color buffers. The default value is zero.

</dd> <dt>

*alpha* 
</dt> <dd>

The alpha value that [**glClear**](glclear.md) uses to clear the color buffers. The default value is zero.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glClearColor** function specifies the red, green, blue, and alpha values used by [**glClear**](glclear.md) to clear the color buffers. Values specified by **glClearColor** are clamped to the range \[0,1\].

The following functions retrieve information related to the **glClearColor** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_ACCUM\_CLEAR\_VALUE

**glGet** with argument GL\_COLOR\_CLEAR\_VALUE

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

 

 





