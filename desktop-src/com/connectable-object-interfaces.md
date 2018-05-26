---
title: Connectable Object Interfaces
description: Connectable Object Interfaces
ms.assetid: 136fb7bd-7a38-4051-b47b-3d08f1dbee79
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Connectable Object Interfaces

Support for connectable objects requires support for four interfaces:

-   [**IConnectionPointContainer**](/windows/win32/OCIdl/nn-ocidl-iconnectionpointcontainer?branch=master) on the connectable object
-   [**IConnectionPoint**](/windows/win32/OCIdl/nn-ocidl-iconnectionpoint?branch=master) on the connection point object
-   [**IEnumConnectionPoints**](/windows/win32/ocidl/nn-ocidl-ienumconnectionpoints?branch=master) on an enumerator object
-   [**IEnumConnections**](/windows/win32/ocidl/nn-ocidl-ienumconnections?branch=master) on an enumerator object

The latter two are defined as standard enumerators for the types **IConnectionPoint \*** and [**CONNECTDATA**](/windows/win32/Ocidl/ns-ocidl-tagconnectdata?branch=master).

Additionally, the connectable object can optionally support [**IProvideClassInfo**](/windows/win32/OCIdl/nn-ocidl-iprovideclassinfo?branch=master) and [**IProvideClassInfo2**](/windows/win32/OCIdl/nn-ocidl-iprovideclassinfo2?branch=master) to provide enough information to a client so that the client can provide support for the outgoing interface at run time.

Finally, the client must provide a sink object that implements the outgoing interface, which is a custom COM interface defined by the connectable object.

For more information, see the following topics:

-   [Using IConnectionPointContainer](using-iconnectionpointcontainer.md)
-   [Using IConnectionPoint](using-iconnectionpoint.md)
-   [Using IProvideClassInfo](using-iprovideclassinfo.md)

## Related topics

<dl> <dt>

[Architecture of Connectable Objects](architecture-of-connectable-objects.md)
</dt> </dl>

 

 




