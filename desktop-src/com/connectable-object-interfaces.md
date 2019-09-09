---
title: Connectable Object Interfaces
description: Connectable Object Interfaces
ms.assetid: 136fb7bd-7a38-4051-b47b-3d08f1dbee79
ms.topic: article
ms.date: 05/31/2018
---

# Connectable Object Interfaces

Support for connectable objects requires support for four interfaces:

-   [**IConnectionPointContainer**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpointcontainer) on the connectable object
-   [**IConnectionPoint**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpoint) on the connection point object
-   [**IEnumConnectionPoints**](/windows/desktop/api/ocidl/nn-ocidl-ienumconnectionpoints) on an enumerator object
-   [**IEnumConnections**](/windows/desktop/api/ocidl/nn-ocidl-ienumconnections) on an enumerator object

The latter two are defined as standard enumerators for the types **IConnectionPoint \*** and [**CONNECTDATA**](/windows/win32/api/ocidl/ns-ocidl-connectdata).

Additionally, the connectable object can optionally support [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) and [**IProvideClassInfo2**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo2) to provide enough information to a client so that the client can provide support for the outgoing interface at run time.

Finally, the client must provide a sink object that implements the outgoing interface, which is a custom COM interface defined by the connectable object.

For more information, see the following topics:

-   [Using IConnectionPointContainer](using-iconnectionpointcontainer.md)
-   [Using IConnectionPoint](using-iconnectionpoint.md)
-   [Using IProvideClassInfo](using-iprovideclassinfo.md)

## Related topics

<dl> <dt>

[Architecture of Connectable Objects](architecture-of-connectable-objects.md)
</dt> </dl>

 

 




