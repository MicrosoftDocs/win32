---
title: Porting Edited Display Lists
description: Although you can't edit OpenGL display lists, you can get similar results by nesting display lists and then destroying and creating new versions of the sublists.
ms.assetid: b7f7ffed-c3de-43d4-bff2-f244faa3a27a
keywords:
- IRIS GL porting,display lists
- porting from IRIS GL,display lists
- porting to OpenGL from IRIS GL,display lists
- OpenGL porting from IRIS GL,display lists
- display lists,porting from IRIS GL
ms.topic: article
ms.date: 05/31/2018
---

# Porting Edited Display Lists

Although you can't edit OpenGL display lists, you can get similar results by nesting display lists and then destroying and creating new versions of the sublists. For example:

``` syntax
glNewList (1, GL_COMPILE); 
    glIndexi(MY_RED); 
glEndlist(); 
 
glNewList(2, GL_COMPILE); 
    glScalef(1.2, 1.2, 1.0); 
glEndList(); 
 
glNewList(3, GL_COMPILE); 
    glCallList(1); 
    glCallList(2); 
glEndList(); 
 
glDeleteLists(1, 2); 
glNewList(1, GL_COMPILE); 
    glIndexi(MY_CYAN); 
glEndList(); 
glNewList(2, GL_COPILE); 
    glScalef(0.5, 0.5, 1.0); 
glEndList;
```

 

 




