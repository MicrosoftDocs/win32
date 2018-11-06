---
title: Porting Screen and Buffer Clearing Commands
description: OpenGL replaces a variety of IRIS GL clear functions (such as zclear, aclear, sclear, and so on) with a single function, glClear. Specify exactly what you want to clear by passing masks to glClear.
ms.assetid: 52ba503d-e412-4815-a039-a039b41327f4
keywords:
- IRIS GL porting,clear functions
- porting from IRIS GL,clear functions
- porting to OpenGL from IRIS GL,clear functions
- OpenGL porting from IRIS GL,clear functions
- clear functions
- IRIS GL porting,screen clearing commands
- porting from IRIS GL,screen clearing commands
- porting to OpenGL from IRIS GL,screen clearing commands
- OpenGL porting from IRIS GL,screen clearing commands
- screen clearing commands
- IRIS GL porting,buffer clearing commands
- porting from IRIS GL,buffer clearing commands
- porting to OpenGL from IRIS GL,buffer clearing commands
- OpenGL porting from IRIS GL,buffer clearing commands
- buffer clearing commands
ms.topic: article
ms.date: 05/31/2018
---

# Porting Screen and Buffer Clearing Commands

OpenGL replaces a variety of IRIS GL **clear** functions (such as **zclear**, **aclear**, **sclear**, and so on) with a single function, [**glClear**](glclear.md). Specify exactly what you want to clear by passing masks to **glClear**.

Keep the following points in mind when porting screen and buffer commands:

-   OpenGL maintains clearing colors separately from drawing colors, with calls like [**glClearColor**](glclearcolor.md) and [**glClearIndex**](glclearindex.md). Be sure to set the clear color for each buffer before clearing.
-   Instead of using one of several differently named clear calls, you now clear several buffers with one call, [**glClear**](glclear.md), by **OR** ing together buffer masks. For example, **czclear** is replaced by:

    ``` syntax
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    ```

-   IRIS GL references the polygon stipple and the color writemask. OpenGL ignores the polygon stipple but references the color writemask. (The **czclear** function ignores both the polygon stipple and the color writemask.)

The following table lists the various IRIS GL clear functions with their equivalent OpenGL functions.



| IRIS GL call         | OpenGL call                                                               | Meaning                                           |
|----------------------|---------------------------------------------------------------------------|---------------------------------------------------|
| **acbuf**(AC\_CLEAR) | **glClear**( GL\_ACCUM\_BUFFER\_BIT )                                     | Clear the accumulation buffer.                    |
|                      | **glClearColor**                                                          | Set the RGBA clear color.                         |
|                      | **glClearIndex**                                                          | Set the clear-color index.                        |
| **clear**            | **glClear**( GL\_COLOR\_BUFFER\_BIT )                                     | Clear the color buffer.                           |
|                      | **glClearDepth**                                                          | Specify the clear value for the depth buffer.     |
| **zclear**           | **glClear**( GL\_DEPTH\_BUFFER\_BIT )                                     | Clear the depth buffer.                           |
| **czclear**          | **glClear**( GL\_COLOR\_BUFFER\_BIT \|GL\_DEPTH\_BUFFER\_BIT )<br/> | Clear the color buffer and the depth buffer.      |
|                      | **glClearAccum**                                                          | Specify clear values for the accumulation buffer. |
|                      | **glClearStencil**                                                        | Specify the clear value for the stencil buffer.   |
| **sclear**           | **glClear**( GL\_STENCIL\_BUFFER\_BIT )                                   | Clear the stencil buffer.                         |



 

When your IRIS GL code uses both **gclear** and **sclear**, you can combine them into a single **glClear** call; can improve your program's performance.

 

 





