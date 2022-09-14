---
title: Porting v Functions
description: In IRIS GL, you use variations on the v function to specify vertices. The equivalent OpenGL function is glVertex Below are examples of glVertex.
ms.assetid: b4ac0c41-983a-4387-a69f-530c9094dc33
keywords:
- IRIS GL porting,vertices
- porting from IRIS GL,vertices
- porting to OpenGL from IRIS GL,vertices
- OpenGL porting from IRIS GL,vertices
- drawing functions,vertices
- vertices,porting from IRIS GL
- IRIS GL porting,v functions
- porting from IRIS GL,v functions
- porting to OpenGL from IRIS GL,v functions
- OpenGL porting from IRIS GL,v functions
- drawing functions,v functions
- v functions
ms.topic: article
ms.date: 05/31/2018
---

# Porting v Functions

In IRIS GL, you use variations on the **v** function to specify vertices. The equivalent OpenGL function is [glVertex](glvertex-functions.md): Below are examples of **glVertex**.

``` syntax
glVertex2[d|f|i|s][v]( x, y ); 
glVertex3[d|f|i|s][v]( x, y, z); 
glVertex4[d|f|i|s][v]( x, y, z, w);
```

The **glVertex** function takes suffixes the same way other OpenGL calls do. The vector versions of the call take arrays of the proper size as arguments. In the 2-D version, z=0 and w=1. In the 3-D version, w=1.

 

 




