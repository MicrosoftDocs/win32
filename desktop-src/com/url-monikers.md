---
title: URL Monikers
description: The OLE moniker architecture provides a convenient programming model for working with URLs.
ms.assetid: '8e0e2bad-9275-4b96-a96b-35d9c933ae31'
---

# URL Monikers

The OLE moniker architecture provides a convenient programming model for working with URLs. The moniker architecture supports extensible and complete name parsing through the [**MkParseDisplayName**](mkparsedisplayname.md) function and the [**IParseDisplayName**](iparsedisplayname.md) and [**IMoniker**](imoniker.md) interfaces, as well as printable names through the [**IMoniker::GetDisplayName**](imoniker-getdisplayname.md) method. The **IMoniker** interface is the way you actually use URLs you encounter, and building components that fit into the moniker architecture is the way to actually extend URL namespaces in practice.

A system-provided moniker class, the URL moniker, provides a framework for building and using certain URLs. Because URLs frequently see resources across high-latency networks, the URL moniker supports asynchronous as well as synchronous binding. The URL moniker does not currently support [asynchronous storage](https://msdn.microsoft.com/library/windows/desktop/aa378862).

The following diagram shows the components involved in using URL monikers. All these components should be familiar. (See [Asynchronous Monikers](asynchronous-monikers.md).)

![](images/bb10975a-9cb5-418e-872e-1e1add0b58ed.png)

Like all moniker clients, a user of URL Monikers typically creates and holds a reference to the moniker as well as to the bind context to be used during binding ([**IMoniker::BindToStorage**](imoniker-bindtostorage.md) or [**IMoniker::BindToObject**](imoniker-bindtoobject.md)). To support asynchronous binding, the client can implement a bind-status-callback object, which implements the [**IBindStatusCallback**](_inet_IBindStatusCallback_Interface_cpp) interface, and register it with the bind context using the [**RegisterBindStatusCallback**](_inet_RegisterBindStatusCallback_Function_cpp) function. This object will receive the transport's [**IBinding**](_inet_IBinding_Interface_cpp) interface during calls to [**IBindStatusCallback::OnStartBinding**](_inet_IBindStatusCallback_OnStartBinding_Method).

The URL Moniker identifies the protocol being used by parsing the URL prefix and then retrieves the [**IBinding**](_inet_IBinding_Interface_cpp) interface from the transport layer. The client uses **IBinding** to support pausing, cancellation, and prioritization of the binding operation. The callback object also receives progress notification through [**IBindStatusCallback::OnProgress**](_inet_IBindStatusCallback_OnProgress_Method), data availability notification through [**IBindStatusCallback::OnDataAvailable**](_inet_IBindStatusCallback_OnDataAvailable_Method), and various, other transport-layer notifications about the status of the binding. The URL moniker or specific transport layers may also request extended information from the client through **IBindStatusCallback::QueryInterface**, allowing the client to provide protocol-specific information that will affect the bind operation.

For more information, see the following topics:

-   [Callback Synchronization](callback-synchronization.md)
-   [Media-Type Negotiation](media-type-negotiation.md)
-   [URL Moniker Functions](url-moniker-api-functions.md)

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> <dt>

[About URL Monikers](https://msdn.microsoft.com/library/ms775149)
</dt> </dl>

 

 




