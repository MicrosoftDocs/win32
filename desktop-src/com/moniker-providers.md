---
title: Moniker Providers
description: Moniker Providers
ms.assetid: 4d4820d2-bf5f-4543-b318-59481dcc51de
ms.topic: article
ms.date: 05/31/2018
---

# Moniker Providers

In general, a component should be a moniker provider when it allows access to one of its objects, while still controlling the object's storage. If a component is going to hand out monikers that identify its objects, it must be capable of performing the following tasks:

-   On request, create a moniker that identifies an object.
-   Enable the moniker to be bound when a client calls [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) on it.

A moniker provider must create a moniker of an appropriate *moniker class* to identify an object. The moniker class refers to a specific implementation of the [**IMoniker**](/windows/desktop/api/ObjIdl/nn-objidl-imoniker) interface that defines the type of moniker created. While you can implement **IMoniker** to create a new moniker class, it is frequently unnecessary because OLE provides implementations of several different moniker classes, each with its own CLSID. See [OLE Moniker Implementations](ole-moniker-implementations.md) for descriptions of moniker classes that OLE provides.

## Related topics

<dl> <dt>

[Moniker Clients](moniker-clients.md)
</dt> <dt>

[OLE Moniker Implementations](ole-moniker-implementations.md)
</dt> </dl>

 

 




