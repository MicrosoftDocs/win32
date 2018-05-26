---
title: Using IConnectionPointContainer
description: Using IConnectionPointContainer
ms.assetid: a87afb25-4d45-4ce2-9b27-840da5107bce
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using IConnectionPointContainer

A connectable object implements [**IConnectionPointContainer**](/windows/win32/OCIdl/nn-ocidl-iconnectionpointcontainer?branch=master) (and exposes it through [**QueryInterface**](/windows/win32/Unknwn/nf-unknwn-iunknown-queryinterface(q,)?branch=master)) to indicate the existence of outgoing interfaces. For each outgoing interface, the connectable object manages a connection point sub-object, which itself implements [**IConnectionPoint**](/windows/win32/OCIdl/nn-ocidl-iconnectionpoint?branch=master). The connectable object therefore contains the connection points, hence the naming of **IConnectionPointContainer** and **IConnectionPoint**.

Through [**IConnectionPointContainer**](/windows/win32/OCIdl/nn-ocidl-iconnectionpointcontainer?branch=master), a client can perform two operations. First, if the client already has the IID for an outgoing interface that it supports, it can locate the corresponding connection point for the IID using [**IConnectionPointContainer::FindConnectionPoint**](/windows/win32/OCIdl/nf-ocidl-iconnectionpointcontainer-findconnectionpoint?branch=master). The client cannot query for the connection point directly because of the container/contained relationship between the connectable object and its contained connection points. Basically, **FindConnectionPoint** is the [**QueryInterface**](/windows/win32/Unknwn/nf-unknwn-iunknown-queryinterface(q,)?branch=master) for outgoing interfaces when the IID is known to the client.

Second, the client can enumerate all connection points within the connectable object through [**IConnectionPointContainer::EnumConnectionPoints**](/windows/win32/OCIdl/nf-ocidl-iconnectionpointcontainer-enumconnectionpoints?branch=master). This method returns an [**IEnumConnectionPoints**](/windows/win32/ocidl/nn-ocidl-ienumconnectionpoints?branch=master) interface pointer for a separate enumerator object. Through [**IEnumConnectionPoints::Next**](/windows/win32/ocidl/nf-ocidl-ienumconnectionpoints-next?branch=master), the client can obtain [**IConnectionPoint**](/windows/win32/OCIdl/nn-ocidl-iconnectionpoint?branch=master) interface pointers to each connection point.

After the client obtains the [**IConnectionPoint**](/windows/win32/OCIdl/nn-ocidl-iconnectionpoint?branch=master) interface, it must call [**IConnectionPoint::GetConnectionInterface**](/windows/win32/OCIdl/nf-ocidl-iconnectionpoint-getconnectioninterface?branch=master) to determine the IID of the outgoing interface supported by each connection point. If the client already supports that outgoing interface, it can establish a connection. Otherwise, it may still be able to support the outgoing interface by using information from the connectable object's type library to provide support at run time. This technique requires that the connectable object support the [**IProvideClassInfo**](/windows/win32/OCIdl/nn-ocidl-iprovideclassinfo?branch=master) interface. (See [Using IProvideClassInfo](using-iprovideclassinfo.md).)

Because the enumerator is a separate object, the client must call **IEnumConnectionPoints::Release** when the enumerator is no longer needed. In addition, each connection point is an object with a separate reference count from the containing connectable object. Therefore, the client must also call IConnectionPoint::Release for each connection point accessed either through the enumerator or through [**FindConnectionPoint**](/windows/win32/OCIdl/nf-ocidl-iconnectionpointcontainer-findconnectionpoint?branch=master).

## Related topics

<dl> <dt>

[Connectable Object Interfaces](connectable-object-interfaces.md)
</dt> </dl>

 

 




