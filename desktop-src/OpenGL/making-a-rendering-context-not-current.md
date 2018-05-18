---
title: Making a Rendering Context Not Current
description: To detach a rendering context from a thread, make it not current. You can do this by calling the wglMakeCurrent function with the parameters set to NULL. The following is a sample of this simple task.
ms.assetid: 'fe76e3d3-5480-448d-95aa-a5af0da309f3'
keywords: ["OpenGL on Windows,rendering contexts", "rendering contexts OpenGL"]
---

# Making a Rendering Context Not Current

To detach a rendering context from a thread, make it not current. You can do this by calling the [**wglMakeCurrent**](wglmakecurrent.md) function with the parameters set to **NULL**. The following is a sample of this simple task.

``` syntax
// detach the current rendering context from the thread  
wglMakeCurrent(NULL, NULL);
```

 

 




