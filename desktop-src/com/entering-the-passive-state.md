---
title: Entering the Passive State
description: Entering the Passive State
ms.assetid: 544760e6-1706-4384-8e17-8971f0e0c5f1
ms.topic: article
ms.date: 05/31/2018
---

# Entering the Passive State

Object closure forces an embedded or linked object into the passive state. It is typically initiated from the OLE server application's user interface, such as when the user selects the File Close command. In this case, the OLE server application notifies the container, which releases its reference count on the object. When all references to the object have been released, the object can be freed. When all objects have been freed, the OLE server application can safely terminate.

A container application can also initiate object closure. To close an object, the container releases its reference count after completing an optional save operation. You can design containers to release objects when they are deactivating after an in-place activation session, allowing the user to click outside the object without losing the active editing session.

 

 




