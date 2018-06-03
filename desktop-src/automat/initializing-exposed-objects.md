---
title: Initializing Exposed Objects
description: To initialize OLE and exposed objects, use OleInitialize, CoRegisterClassObject, and RegisterActiveObject.
ms.assetid: c0d5664a-07c7-4d58-a99f-1b9232293269
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Initializing Exposed Objects

To initialize OLE and the exposed objects, use the following functions:

-   [**OleInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms690134) — Initializes OLE.

-   [**CoRegisterClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms693407) — Registers the object's class factory with OLE so other applications can use it to create new objects.

-   [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) — Registers the active object so other applications can connect to an existing object.

 

 




