---
title: The Lightweight Client-Side Handler
description: Lightweight client-side handlers allow you to create general client-side handlers of any size, to help you do any kind of standard task.
ms.assetid: b712237c-55d7-4f52-9cf6-19c6e5fb3182
ms.topic: article
ms.date: 05/31/2018
---

# The Lightweight Client-Side Handler

Lightweight client-side handlers allow you to create general client-side handlers of any size, to help you do any kind of standard task. As handlers, these are usable by more than one client. They differ from OLE handlers in that they cannot be created before the server is launched, and their lifetime is tied to that of the proxy manager, preventing a possible race condition in which the handler could otherwise be prematurely released.

The proxy manager is the system-created object that implements the [**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal) interface. If you use standard marshaling, the system creates it for you when you call [**CoGetStandardMarshal**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetstandardmarshal) (or [**CoGetStdMarshalEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetstdmarshalex), for creating an aggregated marshaler for lightweight handlers) and also implements the [**IClientSecurity**](/windows/desktop/api/ObjIdl/nn-objidl-iclientsecurity) and [**IMultiQI**](/windows/win32/api/objidlbase/nn-objidlbase-imultiqi) interfaces on the object. On the server side, there is a corresponding system object that also implements **IMarshal**. These objects handle marshaling for you transparently.

There are two general types of these handlers that you may want to implement:

-   A handler that performs a service that requires no extra data from the server
-   A handler that uses extra data from the server

Some potential uses of the extra data in the stream supplied by the server are as follows:

-   Static data from server. Regardless of the particular interface being marshaled, the server writes the same data into the stream.
-   Per-interface data from server. Depending on which particular interface is being marshaled, the server may write different data into the stream.
-   Per-interface helpers. Per-interface COM components aggregated into the client handler and delegating to the standard proxy. For example, to improve network performance, a COM component for [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) could do client-side caching of data, read-ahead, write-behind, op-locking, and so forth.
-   Network version of an interface. The network version of the interface is different from the interface exposed by the client and server application code. It is possible, for example, to multiplex exposed interfaces IA and IB over the same network interface INetAB, the way the embedding server handler does. For example, one could convert a data transfer interface into a network interface that uses pipes for efficient data transfer.

Down-level clients may not have the capability of unmarshaling interfaces that have custom handlers, for two reasons: First, they may not understand the CLSID used in the custom marshaled packet when the server handler is aggregated and the object wants a handler. Second, the handler code may not even run on the client side if it requires new functionality from COM to create the aggregated standard marshaler and to do remote [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) calls.

## Related topics

<dl> <dt>

[The OLE Handler](the-ole-handler.md)
</dt> </dl>

 

 