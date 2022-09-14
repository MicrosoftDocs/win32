---
title: Monikers
description: A moniker in COM is not only a way to identify an object \ 8212;a moniker is also implemented as an object.
ms.assetid: 'ae0cd2f3-8ac0-4388-8781-e86fc4a26b3b'
ms.topic: article
ms.date: 05/31/2018
---

# Monikers

A moniker in COM is not only a way to identify an object—a moniker is also implemented as an object. This object provides services allowing a component to obtain a pointer to the object identified by the moniker. This process is referred to as *binding*.

Monikers are objects that implement the [**IMoniker**](/windows/desktop/api/ObjIdl/nn-objidl-imoniker) interface and are generally implemented in DLLs as component objects. There are two ways of viewing the use of monikers: as a moniker client, a component that uses a moniker to get a pointer to another object; and as a moniker provider, a component that supplies monikers identifying its objects to moniker clients.

OLE uses monikers to connect to and activate objects, whether they are in the same machine or across a network. A very important use is for network connections. They are also used to identify, connect to, and run OLE compound document link objects. In this case, the link source acts as the moniker provider and the container holding the link object acts as the moniker client.

For more information, see the following topics:

-   [Moniker Clients](moniker-clients.md)
-   [Moniker Providers](moniker-providers.md)
-   [OLE Moniker Implementations](ole-moniker-implementations.md)

## Related topics

<dl> <dt>

[The Component Object Model](the-component-object-model.md)
</dt> </dl>

 

 




