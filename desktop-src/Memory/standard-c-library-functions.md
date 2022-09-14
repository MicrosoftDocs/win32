---
description: Applications can safely use the memory management features of the C run-time library (malloc, free, and so on) and C++ (new, delete, and so on).
ms.assetid: c58ed263-577d-47c5-93cb-5a7c83604171
title: Standard C Library Functions
ms.topic: article
ms.date: 05/31/2018
---

# Standard C Library Functions

Applications can safely use the memory management features of the C run-time library (**malloc**, **free**, and so on) and C++ (**new**, **delete**, and so on). The C run-time library functions do not have the potential problems they have under 16-bit Windows. Memory management is no longer a problem because the system is free to manage memory by moving pages of physical memory without affecting the virtual addresses. Similarly, the distinction between near and far pointers is no longer relevant. Therefore, you can use the standard C library functions for memory management. However, the memory management functions do provide functionality that is unavailable in the C run-time library.

 

 



