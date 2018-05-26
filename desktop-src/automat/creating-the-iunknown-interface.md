---
title: Creating the IUnknown Interface
description: The IUnknown interface defines three member functions that must be implemented for each object that is exposed.
ms.assetid: 6cf53e96-fe7c-4702-9729-9eafbee8d89c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the IUnknown Interface

The **IUnknown** interface defines three member functions that must be implemented for each object that is exposed. The prototypes for these functions reside in the header file, Ole2.h.

-   [QueryInterface](54D5FF80-18DB-43F2-B636-F93AC053146D) — Identifies which OLE interfaces the object supports.

-   [AddRef](B4316EFD-73D4-4995-B898-8025A316BA63) — Increments a member variable that tracks the number of references to the object.

-   [Release](4B494C6F-F0EE-4C35-AE45-ED956F40DC7A) — Decrements the member variable that tracks the instances of the object. If an object has zero references, **Release** frees the object.

These functions provide the fundamental interface through which OLE can access objects. The *COM Programmer's Reference* describes in detail how to implement the functions.

 

 




