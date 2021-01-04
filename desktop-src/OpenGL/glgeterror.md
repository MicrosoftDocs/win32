---
title: glGetError function (Gl.h)
description: The glGetError function returns error information.
ms.assetid: 18f0368f-054f-4b84-8397-3f9ee4aa07fa
keywords:
- glGetError function OpenGL
topic_type:
- apiref
api_name:
- glGetError
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetError function

The **glGetError** function returns error information.

## Syntax


```C++
GLenum WINAPI glGetError(void);
```



## Parameters

This function has no parameters.

## Return value

The **glGetError** function returns one of the following error codes.



| Return code                                                                                           | Description                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | An unacceptable value is specified for an enumerated argument. The offending function is ignored, having no side effect other than to set the error flag.<br/>         |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | A numeric argument is out of range. The offending function is ignored, having no side effect other than to set the error flag.<br/>                                    |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The specified operation is not allowed in the current state. The offending function is ignored, having no side effect other than to set the error flag.<br/>           |
| <dl> <dt>**GL\_NO\_ERROR**</dt> </dl>          | No error has been recorded. The value of this symbolic constant is guaranteed to be zero.<br/>                                                                         |
| <dl> <dt>**GL\_STACK\_OVERFLOW**</dt> </dl>    | This function would cause a stack overflow. The offending function is ignored, having no side effect other than to set the error flag.<br/>                            |
| <dl> <dt>**GL\_STACK\_UNDERFLOW**</dt> </dl>   | This function would cause a stack underflow. The offending function is ignored, having no side effect other than to set the error flag.<br/>                           |
| <dl> <dt>**GL\_OUT\_OF\_MEMORY**</dt> </dl>    | There is not enough memory left to execute the function. The state of OpenGL is undefined, except for the state of the error flags, after this error is recorded.<br/> |



 

Note that **glGetError** returns GL\_INVALID\_OPERATION if it is called between a call to [**glBegin**](glbegin.md) and its corresponding call to [**glEnd**](glend.md).

## Remarks

Each detectable error is assigned a numeric code and symbolic name. When an error occurs, the error flag is set to the appropriate error code value. No other errors are recorded until **glGetError** is called, the error code is returned, and the flag is reset to GL\_NO\_ERROR. If a call to **glGetError** returns GL\_NO\_ERROR, there has been no detectable error since the last call to **glGetError**, or since OpenGL was initialized.

To allow for distributed implementations, there may be several error flags. If any single error flag has recorded an error, the value of that flag is returned and that flag is reset to GL\_NO\_ERROR when **glGetError** is called. If more than one flag has recorded an error, **glGetError** returns and clears an arbitrary error flag value. If all error flags are to be reset, you should always call **glGetError** in a loop until it returns GL\_NO\_ERROR.

Initially, all error flags are set to GL\_NO\_ERROR.

When an error flag is set, results of an OpenGL operation are undefined only if GL\_OUT\_OF\_MEMORY has occurred. In all other cases, the function generating the error is ignored and has no effect on the OpenGL state or framebuffer contents.

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

[**glEnd**](glend.md)
</dt> </dl>

 

 





