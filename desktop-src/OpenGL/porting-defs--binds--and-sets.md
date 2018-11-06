---
title: Porting Defs, Binds, and Sets
description: Porting Defs, Binds, and Sets
ms.assetid: 971feb14-ed39-4492-a62b-9930bdc506e9
keywords:
- IRIS GL porting,definitions
- porting from IRIS GL,definitions
- porting to OpenGL from IRIS GL,definitions
- OpenGL porting from IRIS GL,definitions
- IRIS GL porting,binds
- porting from IRIS GL,binds
- porting to OpenGL from IRIS GL,binds
- OpenGL porting from IRIS GL,binds
- IRIS GL porting,sets
- porting from IRIS GL,sets
- porting to OpenGL from IRIS GL,sets
- OpenGL porting from IRIS GL,sets
- definitions
- binds
- sets
ms.topic: article
ms.date: 05/31/2018
---

# Porting Defs, Binds, and Sets

OpenGL doesn't have tables of stored definitions; you can't define lighting models, material, textures, line styles, or patterns as separate objects as you can in IRIS GL. Thus OpenGL has no direct equivalents to the following IRIS GL functions:

-   **Imdef** and **Imbind**
-   **tevdef** and **tevbind**
-   **textdef** and **textbind**
-   **definestyle** and **setstyle**
-   **defpattern** and **setpattern**

You can use OpenGL display lists to mimic the IRIS GL def/bind mechanism. For example, here is a material definition in IRIS GL:


```C++
float mat() = { 
    AMBIENT, .1, .1, .1, 
    DIFFUSE, 0, .369, .165, 
    SPECULAR, .5, .5, .5, 
    SHININESS, 10, 
    LMNULL 
}; 
lmdef(DEFMATERIAL, 1, 0, mat); 
lmbind(MATERIAL, 1);
```



The following OpenGL code sample defines the same material in a display list that is referred to by the list number defined by **MYMATERIAL**.


```C++
#define MYMATERIAL 10 
 
GLfloat        mat_amb[] = {.1, .1, .1, 1.0}; 
GLfloat        mat_dif[] = {0, .369, .165, 1.0}; 
GLfloat        mat_spec[] = {.5, .5, .5, 1.0}; 
 
glNewList(MYMATERIAL, GL_COMPILE); 
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb); 
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif); 
    glMaterialfv(GL_FRONT, GL_SHININESS, 10); 
glEndList(); 
 
glCallList( MYMATERIAL );
```



 

 




