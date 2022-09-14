---
description: The Dispatch Mapper is created using COM CoCreateInstance and exposes one interface, ITDispatchMapper.
ms.assetid: 435034e1-d90c-4bad-8758-8a627d88875f
title: Dispatch Mapper
ms.topic: article
ms.date: 05/31/2018
---

# Dispatch Mapper

The Dispatch Mapper is created using COM **CoCreateInstance** and exposes one interface, [**ITDispatchMapper**](/windows/desktop/api/tapi3if/nn-tapi3if-itdispatchmapper). This interface allows an application to retrieve the dispatch pointer of another interface on an object, given the dispatch pointer of one interface and the GUID of another. This interface is provided to assist programmers using scripting applications which do not provide a means of readily polling the interfaces on an object.

The Dispatch Mapper uses an object's **IObjectSafety** interface to make sure the object is safe for scripting on the requested interface. If the object does not implement **IObjectSafety**, or if the object is not safe on this particular interface, the call will fail.

 

 



