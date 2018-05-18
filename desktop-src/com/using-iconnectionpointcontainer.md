---
title: Using IConnectionPointContainer
description: Using IConnectionPointContainer
ms.assetid: 'a87afb25-4d45-4ce2-9b27-840da5107bce'
---

# Using IConnectionPointContainer

A connectable object implements [**IConnectionPointContainer**](iconnectionpointcontainer.md) (and exposes it through [**QueryInterface**](iunknown-queryinterface.md)) to indicate the existence of outgoing interfaces. For each outgoing interface, the connectable object manages a connection point sub-object, which itself implements [**IConnectionPoint**](iconnectionpoint.md). The connectable object therefore contains the connection points, hence the naming of **IConnectionPointContainer** and **IConnectionPoint**.

Through [**IConnectionPointContainer**](iconnectionpointcontainer.md), a client can perform two operations. First, if the client already has the IID for an outgoing interface that it supports, it can locate the corresponding connection point for the IID using [**IConnectionPointContainer::FindConnectionPoint**](iconnectionpointcontainer-findconnectionpoint.md). The client cannot query for the connection point directly because of the container/contained relationship between the connectable object and its contained connection points. Basically, **FindConnectionPoint** is the [**QueryInterface**](iunknown-queryinterface.md) for outgoing interfaces when the IID is known to the client.

Second, the client can enumerate all connection points within the connectable object through [**IConnectionPointContainer::EnumConnectionPoints**](iconnectionpointcontainer-enumconnectionpoints.md). This method returns an [**IEnumConnectionPoints**](ienumconnectionpoints.md) interface pointer for a separate enumerator object. Through [**IEnumConnectionPoints::Next**](ienumconnectionpoints-next.md), the client can obtain [**IConnectionPoint**](iconnectionpoint.md) interface pointers to each connection point.

After the client obtains the [**IConnectionPoint**](iconnectionpoint.md) interface, it must call [**IConnectionPoint::GetConnectionInterface**](iconnectionpoint-getconnectioninterface.md) to determine the IID of the outgoing interface supported by each connection point. If the client already supports that outgoing interface, it can establish a connection. Otherwise, it may still be able to support the outgoing interface by using information from the connectable object's type library to provide support at run time. This technique requires that the connectable object support the [**IProvideClassInfo**](iprovideclassinfo.md) interface. (See [Using IProvideClassInfo](using-iprovideclassinfo.md).)

Because the enumerator is a separate object, the client must call **IEnumConnectionPoints::Release** when the enumerator is no longer needed. In addition, each connection point is an object with a separate reference count from the containing connectable object. Therefore, the client must also call IConnectionPoint::Release for each connection point accessed either through the enumerator or through [**FindConnectionPoint**](iconnectionpointcontainer-findconnectionpoint.md).

## Related topics

<dl> <dt>

[Connectable Object Interfaces](connectable-object-interfaces.md)
</dt> </dl>

 

 




