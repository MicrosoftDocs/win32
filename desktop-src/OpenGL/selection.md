---
title: Selection
description: Selection returns the current contents of the name stack, which is an array of names with integer values.
ms.assetid: 66902d2c-0cd7-49b3-a685-5c0bdba0df1c
keywords:
- selection mode OpenGL
- selection hits OpenGL
- hit records OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Selection

Selection returns the current contents of the name stack, which is an array of names with integer values. You assign the names and build the name stack within the modeling code that specifies the geometry of objects you want to draw. Then, in selection mode, whenever a primitive intersects the clip volume, a selection hit occurs. The hit record, which is written into the selection array you've supplied with [**glSelectBuffer**](glselectbuffer.md), contains information about the contents of the name stack at the time of the hit.

> [!Note]  
> Call [**glSelectBuffer**](glselectbuffer.md) before you put OpenGL into selection mode with [**glRenderMode**](glrendermode.md). The entire contents of the name stack aren't guaranteed to be returned until you call **glRenderMode** to take OpenGL out of selection mode.

 

Manipulate the name stack with [**glInitNames**](glinitnames.md), [**glLoadName**](glloadname.md), [**glPushName**](glpushname.md), and [**glPopName**](glpopname.md). You can also use [**gluPickMatrix**](glupickmatrix.md) for selection.

 

 




