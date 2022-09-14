---
title: Managing Modes and Execution
description: Managing Modes and Execution
ms.assetid: 6a1ecc42-194a-4d8f-94f6-fd59696d87cf
keywords:
- OpenGL,modes
ms.topic: article
ms.date: 05/31/2018
---

# Managing Modes and Execution

The effect of many OpenGL functions depends on whether a particular mode is in effect. The [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) functions set such modes; [**glIsEnabled**](glisenabled.md) determines whether a particular mode is set.

You can control the execution of previously issued OpenGL functions with [**glFinish**](glfinish.md), which forces all such functions to finish, or [**glFlush**](glflush.md), which ensures that all such functions will be completed in a finite time.

In a particular implementation of OpenGL, you may be able to control certain behaviors with hints by using [**glHint**](glhint.md). Such behaviors are the quality of color and texture coordinate interpolation; the accuracy of fog calculations; and the sampling quality of antialiased points, lines, or polygons.

## Related topics

<dl> <dt>

[Modes and Execution Reference](modes-and-execution-reference.md)
</dt> </dl>

 

 




