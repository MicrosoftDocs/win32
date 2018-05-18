---
title: Connectable Object Interfaces
description: Connectable Object Interfaces
ms.assetid: '136fb7bd-7a38-4051-b47b-3d08f1dbee79'
---

# Connectable Object Interfaces

Support for connectable objects requires support for four interfaces:

-   [**IConnectionPointContainer**](iconnectionpointcontainer.md) on the connectable object
-   [**IConnectionPoint**](iconnectionpoint.md) on the connection point object
-   [**IEnumConnectionPoints**](ienumconnectionpoints.md) on an enumerator object
-   [**IEnumConnections**](ienumconnections.md) on an enumerator object

The latter two are defined as standard enumerators for the types **IConnectionPoint \*** and [**CONNECTDATA**](connectdata.md).

Additionally, the connectable object can optionally support [**IProvideClassInfo**](iprovideclassinfo.md) and [**IProvideClassInfo2**](iprovideclassinfo2.md) to provide enough information to a client so that the client can provide support for the outgoing interface at run time.

Finally, the client must provide a sink object that implements the outgoing interface, which is a custom COM interface defined by the connectable object.

For more information, see the following topics:

-   [Using IConnectionPointContainer](using-iconnectionpointcontainer.md)
-   [Using IConnectionPoint](using-iconnectionpoint.md)
-   [Using IProvideClassInfo](using-iprovideclassinfo.md)

## Related topics

<dl> <dt>

[Architecture of Connectable Objects](architecture-of-connectable-objects.md)
</dt> </dl>

 

 




