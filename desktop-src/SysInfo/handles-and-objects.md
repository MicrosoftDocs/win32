---
Description: An object is a data structure that represents a system resource, such as a file, thread, or graphic image.
ms.assetid: 122acb9e-2a1b-480b-9207-5cc6bbe6b6d4
title: Handles and Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Handles and Objects

An *object* is a data structure that represents a system resource, such as a file, thread, or graphic image. An application cannot directly access object data or the system resource that an object represents. Instead, an application must obtain an object *handle*, which it can use to examine or modify the system resource. Each handle has an entry in an internally maintained table. These entries contain the addresses of the resources and the means to identify the resource type.

-   [About Handles and Objects](about-handles-and-objects.md)
-   [Object Categories](object-categories.md)
-   [Handle and Object Reference](handle-and-object-reference.md)

 

 



