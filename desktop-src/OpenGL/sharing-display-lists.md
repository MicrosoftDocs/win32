---
title: Sharing Display Lists
description: When you create a rendering context, it has its own display-list space.
ms.assetid: 8ace5684-a27b-4d6e-a80b-58a0b7064879
keywords:
- OpenGL on Windows,sharing display lists
- sharing display lists OpenGL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sharing Display Lists

When you create a rendering context, it has its own display-list space. The [**wglShareLists**](/windows/win32/wingdi/nf-wingdi-wglsharelists?branch=master) function enables a rendering context to share the display-list space of another rendering context. Any number of rendering contexts can share a single display-list space.

 

 




