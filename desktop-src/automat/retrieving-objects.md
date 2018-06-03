---
title: Retrieving Objects
description: Automation provides several functions to identify and retrieve the active instance of an object or application, so you can make the object available to others.
ms.assetid: 07826983-7cc9-4163-b4d3-46f0d7225984
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Objects

Automation provides several functions to identify and retrieve the active instance of an object or application, so you can make the object available to others.

-   [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) — Sets the active object for an application. Use when the application starts.

-   [**RevokeActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-revokeactiveobject) — Revokes the active object. Use when the application ends.

-   [**GetActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-getactiveobject) — Retrieves a pointer to the active object. In Visual Basic, this pointer is implemented by the **GetObject** function.

Applications can have more than one active object at a time. To be initialized as active, an object must:

-   Have a class factory (that is, the object provides an interface for creating instances of itself).

-   Identify its class factory by a ProgID in the system registry.

-   Be registered by a call to [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) when the object is created, or when it becomes active.

The Application object must be registered as an active object.

 

 




