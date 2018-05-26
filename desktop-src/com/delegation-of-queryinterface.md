---
title: Delegation of QueryInterface
description: Delegation of QueryInterface
ms.assetid: c5c1b584-9ca3-4dc4-a769-0142e5d8790a
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Delegation of QueryInterface

Handlers that require access to some of the internal interfaces on the proxy manager have to go through the [**IInternalUnknown**](/windows/win32/objidlbase/nn-objidl-iinternalunknown?branch=master) interface. This prevents handlers from blindly delegating and exposing the aggregatee's internal interfaces outside of the aggregate. These interfaces include [**IClientSecurity**](/windows/win32/ObjIdl/nn-objidl-iclientsecurity?branch=master) and [**IMultiQI**](/windows/win32/objidlbase/nn-objidl-imultiqi?branch=master). If the handler wants to expose **IClientSecurity** or **IMultiQI**, it should implement them itself.

In the case of [**IClientSecurity**](/windows/win32/ObjIdl/nn-objidl-iclientsecurity?branch=master), if the client tries to set the security on an interface that the handler has exposed, the handler should set the security on the underlying network interface proxy.

In the case of [**IMultiQI**](/windows/win32/objidlbase/nn-objidl-imultiqi?branch=master), the handler should fill in the interfaces it knows about and then forward the call to the proxy manager to get the rest of the interfaces filled in.

## Related topics

<dl> <dt>

[The Lightweight Client-Side Handler](the-lightweight-client-side-handler.md)
</dt> </dl>

 

 




