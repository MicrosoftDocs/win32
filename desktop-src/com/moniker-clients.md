---
title: Moniker Clients
description: Moniker clients must start by getting a moniker, and there are several ways for a moniker client to get a moniker.
ms.assetid: ab1758c4-8dfc-47f6-8e1b-875e033a54d6
ms.topic: article
ms.date: 05/31/2018
---

# Moniker Clients

Moniker clients must start by getting a moniker, and there are several ways for a moniker client to get a moniker. For example, in OLE compound documents, when the end user creates a linked item (either using **Insert Object** dialog, the clipboard, or drag-and drop), a moniker is embedded as part of the linked item. In that case, the programmer has minimal contact with monikers. Programmatically, if you have an interface pointer to an object that implements the [**IMoniker**](/windows/desktop/api/ObjIdl/nn-objidl-imoniker) interface, you can use that to get a moniker, and there are methods on other interfaces that are defined to return monikers.

There are different kinds of monikers, which are used to identify different kinds of objects, but to a moniker client, all monikers look the same. A moniker client simply calls [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) on a moniker and gets an interface pointer to the object that the moniker identifies. Whether the moniker identifies an object as large as an entire spreadsheet or as small as a single cell within a spreadsheet, calling **BindToObject** will return a pointer to that object. If the object is already running, **BindToObject** will find it in memory. If the object is stored passively on disk, **BindToObject** will locate a server for that object, run the server, and have the server bring the object into the running state. All the details of the binding process are hidden from the moniker client. Thus, for a moniker client, using the moniker is very simple.

## Related topics

<dl> <dt>

[Moniker Providers](moniker-providers.md)
</dt> <dt>

[OLE Moniker Implementations](ole-moniker-implementations.md)
</dt> </dl>

 

 




