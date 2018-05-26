---
title: Initializing Exposed Objects
description: To initialize OLE and exposed objects, use OleInitialize, CoRegisterClassObject, and RegisterActiveObject.
ms.assetid: c0d5664a-07c7-4d58-a99f-1b9232293269
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Initializing Exposed Objects

To initialize OLE and the exposed objects, use the following functions:

-   [**OleInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms690134) — Initializes OLE.

-   [**CoRegisterClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms693407) — Registers the object's class factory with OLE so other applications can use it to create new objects.

-   [**RegisterActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-registeractiveobject?branch=master) — Registers the active object so other applications can connect to an existing object.

 

 




