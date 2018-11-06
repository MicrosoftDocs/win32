---
title: Persistent Object State
description: Persistent Object State
ms.assetid: 731fef03-d204-48e7-b33a-801e97a9d2c2
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Object State

Some COM objects can save their internal state when asked to do so by a client.

COM defines standards through which clients can request objects to be initialized, loaded, and saved to and from a data store (for example, flat file, structured storage, or memory). It is the client's responsibility to manage the location where the object's persistent data is stored but not the format of the data. COM objects that adhere to these standards are called *persistent objects*.

For more information, see the following topics:

-   [Persistent Object Interfaces](persistent-object-interfaces.md)
-   [Initializing Persistent Objects](initializing-persistent-objects.md)

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> </dl>

 

 




