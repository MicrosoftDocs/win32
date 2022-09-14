---
title: Entering the Running State
description: Entering the Running State
ms.assetid: 2173eaa9-0e60-4411-81e4-dbabc5fe89b2
ms.topic: article
ms.date: 05/31/2018
---

# Entering the Running State

When an embedded object makes the transition to the running state, the object handler must locate and run the server application in order to utilize the services that only the server provides. Embedded objects are placed in the running state either explicitly through a request by the container, such as a need to draw a format not currently cached, or implicitly by OLE in response to invoking some operation, such as when a user of the container double-clicks the object.

When a linked object makes the transition into the running state, the process is known as *binding*. In the process of binding, the object handler asks its stored moniker to locate the link's data, then runs the server application.

At first glance, binding a linked object appears to be no more complicated than running an embedded object. However, the following points complicate the process:

-   A link can refer to an object, or a portion thereof, that is embedded in another container. This capability implies a potential for nested embeddings. Resolving references to such a hierarchy requires recursively traversing a *composite moniker*, beginning with the rightmost member.
-   When the link source is running, OLE binds to the running instance of the object rather than running another instance. In the case of nested embedded objects, one of which is the link source, OLE must be able to bind to an already running object at any point.
-   Running an object requires accessing the storage area for the object. When an embedded object is run, OLE receives a pointer to the storage during the load process, which it passes on to the OLE server application. For linked objects, however, there is no standard interface for accessing storage. The OLE server application may use the file system interface or some other mechanism.

 

 




