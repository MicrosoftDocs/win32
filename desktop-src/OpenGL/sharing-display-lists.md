---
title: Sharing Display Lists
description: When you create a rendering context, it has its own display-list space.
ms.assetid: 8ace5684-a27b-4d6e-a80b-58a0b7064879
keywords:
- OpenGL on Windows,sharing display lists
- sharing display lists OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Sharing Display Lists

When you create a rendering context, it has its own display-list space. The [**wglShareLists**](/windows/desktop/api/wingdi/nf-wingdi-wglsharelists) function enables a rendering context to share the display-list space of another rendering context. Any number of rendering contexts can share a single display-list space.

 

 




