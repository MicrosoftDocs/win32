---
title: Initializing Persistent Objects
description: Initializing Persistent Objects
ms.assetid: 790cf133-ce86-4d02-b177-a538b4ee3f8b
ms.topic: article
ms.date: 05/31/2018
---

# Initializing Persistent Objects

Several of the persistent object interfaces, [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit), [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), [IPersistMemory](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768210(v=vs.85)), and [IPersistPropertyBag](/windows/win32/api/ocidl/nn-ocidl-ipersistpropertybag), allow clients to initialize objects to a "fresh" or "default" state. This initial state is different from that of a newly created object, which has no state.

Initializing an object's state, even to the default state, may be a compute-intensive or resource-intensive operation. By separating creation from initialization, the initialization can be performed only when it is actually needed and clients can avoid initializing objects to the default state only to immediately load previously stored data.

## Related topics

<dl> <dt>

[Persistent Object Interfaces](persistent-object-interfaces.md)
</dt> </dl>

 

 