---
title: Porting Display Lists
description: The OpenGL implementation of display lists is similar to the IRIS GL implementation, with two exceptions in OpenGL you can't edit display lists once you've created them and you can't call functions from within display lists.
ms.assetid: 617e19ff-6a55-4f7c-b229-075cdee8f1cf
keywords:
- IRIS GL porting,display lists
- porting from IRIS GL,display lists
- porting to OpenGL from IRIS GL,display lists
- OpenGL porting from IRIS GL,display lists
- display lists,porting from IRIS GL
ms.topic: article
ms.date: 05/31/2018
---

# Porting Display Lists

The OpenGL implementation of display lists is similar to the IRIS GL implementation, with two exceptions: in OpenGL you can't edit display lists once you've created them and you can't call functions from within display lists.

Because you can't edit or call functions from within display lists, these IRIS GL functions have no equivalent in OpenGL:

-   **editobj**
-   **objdelete**, **objinsert**, and **objreplace**
-   **maketag**, **gentag**, **istag**, and **deltag**
-   **callfunc**

In IRIS GL, you use the **makeobj** and **closeobj** functions to create display lists. In OpenGL, you use [**glNewList**](glnewlist.md) and [**glEndList**](glendlist.md).

The following table lists the IRIS GL display list functions with their equivalent OpenGL functions.



| IRIS GL function | OpenGL function                                                      | Meaning                                                       |
|------------------|----------------------------------------------------------------------|---------------------------------------------------------------|
| **makeobj**      | **glNewList**                                                        | Creates a new display list.                                   |
| **closeobj**     | **glEndList**                                                        | Signals end of display list.                                  |
| **callobj**      | [**glCallList**](glcalllist.md), [**glCallLists**](glcalllists.md) | Executes display list or lists.                               |
| **isobj**        | [**glIsList**](glislist.md)                                         | Tests for display list existence.                             |
| **delobj**       | [**glDeleteLists**](gldeletelists.md)                               | Deletes contiguous group of display lists.                    |
| **genobj**       | [**glGenLists**](glgenlists.md)                                     | Generates the given number of contiguous empty display lists. |



 

This topic includes information on the following.

-   [Porting the bbox2 Function](porting-the-bbox2-function.md)
-   [Porting Edited Display Lists](porting-edited-display-lists.md)
-   [A Sample Port of a Display List](a-sample-port-of-a-display-list.md)

 

 




