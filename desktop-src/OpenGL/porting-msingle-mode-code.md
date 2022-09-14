---
title: Porting MSINGLE Mode Code
description: OpenGL has no equivalent for MSINGLE, single-matrix mode.
ms.assetid: 7de933b8-150c-432d-89ee-5f5799ad8443
keywords:
- IRIS GL porting,MSINGLE mode
- porting from IRIS GL,MSINGLE mode
- porting to OpenGL from IRIS GL,MSINGLE mode
- OpenGL porting from IRIS GL,MSINGLE mode
- MSINGLE mode
- IRIS GL porting,single-matrix mode
- porting from IRIS GL,single-matrix mode
- porting to OpenGL from IRIS GL,single-matrix mode
- OpenGL porting from IRIS GL,single-matrix mode
- single-matrix mode
- double-matrix mode
ms.topic: article
ms.date: 05/31/2018
---

# Porting MSINGLE Mode Code

OpenGL has no equivalent for **MSINGLE**, single-matrix mode. Though use of this mode has been discouraged, it is the default for IRIS GL. If your IRIS GL program uses the single-matrix mode, you need to rewrite it to use double-matrix mode only. OpenGL is always in double-matrix mode, and is initially in GL\_MODELVIEW mode.

Most IRIS GL code in MSINGLE mode looks like this:

``` syntax
projectionmatrix();
```

where *projectionmatrix* is one of: **ortho**, **ortho2**, **perspective**, or **window**. To port to OpenGL, replace the **MSINGLE** -mode *projectionmatrix* function with:


```C++
glMatrixMode( GL_PROJECTION ); 
glLoadMatrix( identity matrix ); 
 
/* call one of these functions here: */ 
/* glFrustrum(), glOrtho(), glOrtho2(), gluPerspective()}; */ 
 
glMatrixMode( GL_MODELVIEW ); 
glLoadMatrix( identity matrix );
```



 

 




