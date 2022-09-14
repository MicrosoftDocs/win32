---
title: Using Display Lists
description: Using Display Lists
ms.assetid: f5edff21-0928-4ec9-9718-5189bf8ce2d7
keywords:
- OpenGL,display lists
- display lists OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Using Display Lists

A display list is a group of OpenGL functions that has been stored for subsequent execution. The [**glNewList**](glnewlist.md) function begins the creation of a display list, and [**glEndList**](glendlist.md) ends it. With few exceptions, OpenGL functions called between **glNewList** and **glEndList** are appended to the display list. (See **glNewList** for a list of the functions that you can't store and execute from within a display list.) To trigger the execution of a list or set of lists, use [**glCallList**](glcalllist.md) or [**glCallLists**](glcalllists.md) and supply the identifying number of a particular list or lists. You manage the indexes used to identify display lists with [**glGenLists**](glgenlists.md), [**glListBase**](gllistbase.md), and [**glIsList**](glislist.md). To delete a set of display lists, use [**glDeleteLists**](gldeletelists.md).

## Related topics

<dl> <dt>

[Display Lists Reference](display-lists-reference.md)
</dt> </dl>

 

 




