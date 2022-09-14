---
title: Using IConnectionPoint
description: Using IConnectionPoint
ms.assetid: afd50b84-1fd6-47ad-a3ef-e8b4a725b72b
ms.topic: article
ms.date: 05/31/2018
---

# Using IConnectionPoint

When the client has a pointer to a connection point, it can perform the following operations as expressed through [**IConnectionPoint**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpoint):

-   First, [**IConnectionPoint::GetConnectionInterface**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-getconnectioninterface) retrieves the outgoing interface IID supported by the connection point. When used in conjunction with [**IEnumConnectionPoints**](/windows/desktop/api/ocidl/nn-ocidl-ienumconnectionpoints), this method allows the client to examine the IIDs of all outgoing interfaces supported on the connectable object.
-   Second, a client can navigate from the connection point back to the connectable object's [**IConnectionPointContainer**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpointcontainer) interface through the [**IConnectionPoint::GetConnectionPointContainer**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-getconnectionpointcontainer) method.
-   Third, the most interesting methods for the client are [**IConnectionPoint::Advise**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-advise) and [**IConnectionPoint::Unadvise**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-unadvise). When a client wishes to connect its own sink object to the connectable object, the client passes the sink's [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) pointer (or any other interface pointer on the same object) to **Advise**. The connection point queries the sink for the specific outgoing interface that is expected. If that interface is available on the sink, the connection point then stores the interface pointer. From this point until **Unadvise** is called, the connectable object will make calls to the sink through this interface when events occur. To disconnect the sink from the connection point, the client passes a key returned from **Advise** to the **Unadvise** method. **Unadvise** must call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on the sink interface.
-   Finally, a client can ask a connection point to enumerate all the connections to it that exist through [**IConnectionPoint::EnumConnections**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-enumconnections). This method creates an enumerator object (with a separate reference count) returning an [**IEnumConnections**](/windows/desktop/api/ocidl/nn-ocidl-ienumconnections) pointer to it. The client must call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) when the enumerator is no longer needed. Additionally, the enumerator returns a series of [**CONNECTDATA**](/windows/win32/api/ocidl/ns-ocidl-connectdata) structures, one for each connection. Each structure describes one connection using the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) pointer of the sink as well as the connection key originally returned from [**Advise**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-advise). When done with these sink interface pointers, the client must call **Release** on each pointer returned in a **CONNECTDATA** structure.

## Related topics

<dl> <dt>

[Connectable Object Interfaces](connectable-object-interfaces.md)
</dt> </dl>

 

 