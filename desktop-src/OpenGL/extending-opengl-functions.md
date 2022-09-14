---
title: Extending OpenGL Functions
description: The OpenGL library supports multiple implementations of its functions.
ms.assetid: 9eb08fd4-899a-4610-9491-d7f377a19b46
keywords:
- OpenGL on Windows,extension functions
- extension functions OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Extending OpenGL Functions

The OpenGL library supports multiple implementations of its functions. Extension functions supported in one rendering context aren't necessarily supported in a different rendering context. For a given rendering context in an application using extension functions, use only the function addresses returned by the [**wglGetProcAddress**](/windows/desktop/api/wingdi/nf-wingdi-wglgetprocaddress) function.

 

 




