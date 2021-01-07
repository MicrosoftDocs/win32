---
description: 'Windows provides functions that perform the following tasks:'
ms.assetid: 437419c7-d6c5-4cae-b5d0-d552c75d4448
title: Object Interface
ms.topic: article
ms.date: 05/31/2018
---

# Object Interface

Windows provides functions that perform the following tasks:

-   Create an object
-   Get an object handle
-   Get information about the object
-   Set information about the object
-   Close the object handle
-   Destroy the object

Some of these tasks are not necessary for each object. Some of these tasks are combined for certain objects. For example, an application can create an event object. Other applications can open the event to obtain a unique handle to this event object. As each application finishes using the event, it closes its handle to the object. When there are no remaining open handles to the event object, the system destroys the event object. In contrast, an application can obtain a handle to an existing window object. When the window object is no longer needed, the application must destroy the object, which invalidates the window handle.

Occasionally, an object remains in memory after all object handles have been closed. For example, a thread could create an event object and wait on the event handle. While the thread is waiting, another thread could close the same event object handle. The event object remains in memory, without any event object handles, until the event object is set to the signaled state and the wait operation is completed. At this time, the system removes the object from memory.

Handles and objects consume memory. Therefore, to preserve system performance, you should close handles and delete objects as soon as they are no longer needed. If you do not do this, your application can hurt system performance, due to excessive use of the paging file.

When a process terminates, the system automatically closes handles and deletes objects created by the process. However, when a thread terminates, the system usually does not close handles or delete objects. The only exceptions are window, hook, window position, and dynamic data exchange (DDE) conversation objects; these objects are destroyed when the creating thread terminates.

 

 



