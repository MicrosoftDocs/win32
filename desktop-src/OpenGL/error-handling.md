---
title: Error Handling (OpenGL)
description: When OpenGL detects an error, it records a current error code.
ms.assetid: 8e40e382-14fd-44df-8e1c-ebceb34af19c
keywords:
- error handling OpenGL
- OpenGL error handling
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling (OpenGL)

When OpenGL detects an error, it records a current error code. The function that caused the error is ignored, so it has no effect on the OpenGL state or on the framebuffer contents. (If the error recorded was GL\_OUT\_OF\_MEMORY, however, the results of the function are undefined.) Once recorded, the current error code isn't cleared until you call the [**glGetError**](glgeterror.md) query function, which returns the current error code.

Implementations of OpenGL may return multiple current error codes, each of which remains set until queried. The **glGetError** function returns GL\_NO\_ERROR once you've queried all the current error codes or if there is no error. Therefore, if you obtain an error code, call **glGetError** until GL\_NO\_ERROR is returned to be sure you've discovered all the errors. For the list of error codes, see [OpenGL error codes](opengl-error-codes.md).

You can use the [**gluErrorString**](gluerrorstring.md) GLU function to obtain a descriptive string corresponding to the error code passed in. For more information on **gluErrorString**, see [Handling Errors](handling-errors.md).

> [!Note]  
> GLU functions often return error values if an error is detected. Also, the OpenGL Utility library defines the error codes GLU\_INVALID\_ENUM, GLU\_INVALID\_VALUE, and GLU\_OUT\_OF\_MEMORY, which have the same meaning as the related OpenGL error codes.

 

 

 




