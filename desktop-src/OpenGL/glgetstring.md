---
title: glGetString function (Gl.h)
description: The glGetString function returns a string describing the current OpenGL connection.
ms.assetid: 768e6ec2-3f00-44e6-b3cb-de0f06d6a73d
keywords:
- glGetString function OpenGL
topic_type:
- apiref
api_name:
- glGetString
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetString function

The **glGetString** function returns a string describing the current OpenGL connection.

## Syntax


```C++
const GLubyte* WINAPI glGetString(
   GLenum name
);
```



## Parameters

<dl> <dt>

*name* 
</dt> <dd>

One of the following symbolic constants.



| Value                                                                                                                                                         | Meaning                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_VENDOR"></span><span id="gl_vendor"></span><dl> <dt>**GL\_VENDOR**</dt> </dl>             | Returns the company responsible for this OpenGL implementation. This name does not change from release to release.<br/>                                                  |
| <span id="GL_RENDERER"></span><span id="gl_renderer"></span><dl> <dt>**GL\_RENDERER**</dt> </dl>       | Returns the name of the renderer. This name is typically specific to a particular configuration of a hardware platform. It does not change from release to release.<br/> |
| <span id="GL_VERSION"></span><span id="gl_version"></span><dl> <dt>**GL\_VERSION**</dt> </dl>          | Returns a version or release number.<br/>                                                                                                                                |
| <span id="GL_EXTENSIONS"></span><span id="gl_extensions"></span><dl> <dt>**GL\_EXTENSIONS**</dt> </dl> | Returns a space-separated list of supported extensions to OpenGL.<br/>                                                                                                   |



 

</dd> </dl>

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *name* was not an accepted value.<br/>                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glGetString** function returns a pointer to a static string describing some aspect of the current OpenGL connection.

Because OpenGL does not include queries for the performance characteristics of an implementation, it is expected that some applications will be written to recognize known platforms and will modify their OpenGL usage based on known performance characteristics of these platforms. The strings GL\_VENDOR and GL\_RENDERER together uniquely specify a platform, and will not change from release to release. They should be used as such by platform recognition algorithms.

The format and contents of the string that **glGetString** returns depend on the implementation, except that:

-   Extension names will not include space characters and will be separated by space characters in the GL\_EXTENSIONS string.
-   The GL\_VERSION string begins with a version number. The version number uses one of these forms:

    *major\_number*.*minor\_number*

    *major\_number*.*minor\_number*.*release\_number*

-   Vendor-specific information may follow the version number. Its format depends on the implementation, but a space always separates the version number and the vendor-specific information.
-   All strings are null-terminated.

If an error is generated, **glGetString** returns zero.

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

 

 





