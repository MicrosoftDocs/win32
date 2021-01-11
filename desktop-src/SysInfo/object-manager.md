---
description: An object consists of a standard header and object-specific attributes. Because all objects have the same structure, there is a single object manager in Windows that maintains all objects.
ms.assetid: 104113f3-bfd1-4ff7-b92f-2f753c0f5185
title: Object Manager
ms.topic: article
ms.date: 05/31/2018
---

# Object Manager

An object consists of a standard header and object-specific attributes. Because all objects have the same structure, there is a single object manager in Windows that maintains all objects.

The object header includes items such as the object name, so that other processes can reference the object by name, and a security descriptor, so that the object manager can control which processes access the system resource.

The tasks that the object manager performs include the following:

-   Creating objects
-   Verifying that a process has the right to use the object
-   Creating object handles and returning them to the caller
-   Maintaining resource quotas
-   Creating duplicate handles
-   Closing handles to objects

 

 



