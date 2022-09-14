---
title: In-Process Support
description: The current implementation of Dynamic Annotation is entirely in-process and consequently allows only UI elements to be annotated by the process that owns those UI elements.
ms.assetid: 3d32c444-47fb-49fe-be18-0330fea77926
ms.topic: article
ms.date: 05/31/2018
---

# In-Process Support

The current implementation of Dynamic Annotation is entirely in-process and consequently allows only UI elements to be annotated by the process that owns those UI elements. It is not possible for one process to annotate the UI elements of another process.

Note that this only affects the act of setting an annotation; it does not interfere with the ability of clients to access the properties (annotated or otherwise) of UI elements in other processes.

 

 




