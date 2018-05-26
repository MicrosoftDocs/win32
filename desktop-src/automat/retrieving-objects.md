---
title: Retrieving Objects
description: Automation provides several functions to identify and retrieve the active instance of an object or application, so you can make the object available to others.
ms.assetid: 07826983-7cc9-4163-b4d3-46f0d7225984
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Objects

Automation provides several functions to identify and retrieve the active instance of an object or application, so you can make the object available to others.

-   [**RegisterActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-registeractiveobject?branch=master) — Sets the active object for an application. Use when the application starts.

-   [**RevokeActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-revokeactiveobject?branch=master) — Revokes the active object. Use when the application ends.

-   [**GetActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-getactiveobject?branch=master) — Retrieves a pointer to the active object. In Visual Basic, this pointer is implemented by the **GetObject** function.

Applications can have more than one active object at a time. To be initialized as active, an object must:

-   Have a class factory (that is, the object provides an interface for creating instances of itself).

-   Identify its class factory by a ProgID in the system registry.

-   Be registered by a call to [**RegisterActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-registeractiveobject?branch=master) when the object is created, or when it becomes active.

The Application object must be registered as an active object.

 

 




