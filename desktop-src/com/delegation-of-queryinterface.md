---
title: Delegation of QueryInterface
description: Delegation of QueryInterface
ms.assetid: 'c5c1b584-9ca3-4dc4-a769-0142e5d8790a'
---

# Delegation of QueryInterface

Handlers that require access to some of the internal interfaces on the proxy manager have to go through the [**IInternalUnknown**](iinternalunknown.md) interface. This prevents handlers from blindly delegating and exposing the aggregatee's internal interfaces outside of the aggregate. These interfaces include [**IClientSecurity**](iclientsecurity.md) and [**IMultiQI**](imultiqi.md). If the handler wants to expose **IClientSecurity** or **IMultiQI**, it should implement them itself.

In the case of [**IClientSecurity**](iclientsecurity.md), if the client tries to set the security on an interface that the handler has exposed, the handler should set the security on the underlying network interface proxy.

In the case of [**IMultiQI**](imultiqi.md), the handler should fill in the interfaces it knows about and then forward the call to the proxy manager to get the rest of the interfaces filled in.

## Related topics

<dl> <dt>

[The Lightweight Client-Side Handler](the-lightweight-client-side-handler.md)
</dt> </dl>

 

 




