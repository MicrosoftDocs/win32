---
title: Using IProvideClassInfo
description: Using IProvideClassInfo
ms.assetid: 16541aab-474f-4ae5-a6b6-fb2fea6d38ab
ms.topic: article
ms.date: 05/31/2018
---

# Using IProvideClassInfo

A connectable object can offer the [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) and [**IProvideClassInfo2**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo2) interfaces so that its clients can easily examine its type information. This capability is important when dealing with outgoing interfaces, which, by definition, are defined by an object but implemented by a client on its own sink object. In some cases, an outgoing interface is known at compile time to both the connectable object and the sink object; such is the case with [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink).

In other cases, however, only the connectable object knows its outgoing interface definitions at compile time. In these cases, the client must obtain the type information for the outgoing interface so that it can dynamically provide a sink supporting the right entry points, as follows:

1.  The client enumerates the connection points and then, to obtain the IIDs of outgoing interfaces supported by the connectable object, calls [**IConnectionPoint::GetConnectionInterface**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-getconnectioninterface) for each connection point.
2.  The client queries the connectable object for one of the [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) interfaces.
3.  The client calls methods in the [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) interfaces to get the type information for the outgoing interface.
4.  The client creates a sink object supporting the outgoing interface.
5.  The process continues, and the client calls [**IConnectionPoint::Advise**](/windows/desktop/api/OCIdl/nf-ocidl-iconnectionpoint-advise) to connect its sink to the connection point.

In the type information, the attribute [**source**](/windows/desktop/Midl/source) marks an [**interface**](/windows/desktop/Midl/interface) or [**dispinterface**](/windows/desktop/Midl/dispinterface) listed under a [**coclass**](/windows/desktop/Midl/coclass) as an outgoing interface. Those listed without this attribute are considered incoming interfaces.

## Related topics

<dl> <dt>

[Connectable Object Interfaces](connectable-object-interfaces.md)
</dt> <dt>

[Providing Class Information](providing-class-information.md)
</dt> </dl>

 

 