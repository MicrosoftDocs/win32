---
title: Porting the bbox2 Function
description: There is no OpenGL equivalent for the IRIS GL bbox2 function.
ms.assetid: 2d8082bf-c2c3-41d9-9bf7-b4ac2fdefbd6
keywords:
- IRIS GL porting,bbox2 function
- porting from IRIS GL,bbox2 function
- porting to OpenGL from IRIS GL,bbox2 function
- OpenGL porting from IRIS GL,bbox2 function
ms.topic: article
ms.date: 05/31/2018
---

# Porting the bbox2 Function

There is no OpenGL equivalent for the IRIS GL **bbox2** function.

**To port code that contains bbox2 functions**

1.  Create a new (OpenGL) display list that contains everything in the equivalent IRIS GL display list except the call to **bbox2**.
2.  Use appropriate Windows code to draw a rectangle the same size as the IRIS GL **bbox**.

 

 




