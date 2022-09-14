---
title: Events in COM and Connectable Objects
description: When a program detects something that has happened, it can notify its clients.
ms.assetid: f6ffbd1d-4bc1-4dc2-b3ed-ee12359e3d75
ms.topic: article
ms.date: 05/31/2018
---

# Events in COM and Connectable Objects

When a program detects something that has happened, it can notify its clients. For example, if a stock ticker program detects a change in the price of a stock, it can notify all clients of the change. This notification process is referred to as *firing an event*.

With COM, server objects can use COM events to fire events without any information about what objects will be notified. Objects can also use *connectable objects* to maintain detailed information about clients who have requested notifications.

COM connectable objects provide outgoing interfaces to their clients in addition to their incoming interfaces. As a result, objects and their clients can engage in bidirectional communication. Incoming interfaces are implemented on an object and receive calls from external clients of an object, while outgoing interfaces are implemented on the client's sink and receive calls from the object. The object defines an interface it would like to use, and the client implements it.

An object defines its incoming interfaces and provides implementations of these interfaces. Incoming interfaces are available to clients through the object's [**IUnknown::QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) method. Clients call the methods of an incoming interface on the object, and the object performs desired actions on behalf of the client.

Outgoing interfaces are also defined by an object, but the client provides the implementations of the outgoing interfaces on a sink object that the client creates. The object then calls methods of the outgoing interface on the sink object to notify the client of changes in the object, to trigger events in the client, to request something from the client, or, in fact, for any purpose the object creator comes up with.

An example of an outgoing interface is an IButtonSink interface defined by a push button control to notify its clients of its events. For example, the button object calls IButtonSink::OnClick on the client's sink object when the user clicks the button on the screen. The button control defines the outgoing interface. For a client of the button to handle the event, the client must implement that outgoing interface on a sink object and then connect that sink to the button control. Then, when events occur in the button, the button will call the sink, at which time the client can execute whatever action it wishes to assign to that button click.

Connectable objects provide a general mechanism for object-to-client communication. Any object that wishes to expose events or notifications of any kind can use this technology. In addition to the general connectable object technology, COM provides many special purpose sink and site interfaces used by objects to notify clients of specific events of interest to the client. For example, [**IAdviseSink**](/windows/desktop/api/ObjIdl/nn-objidl-iadvisesink) may be used by objects to notify clients of data and view changes in the object.

For more information, see the following topics:

-   [Architecture of Connectable Objects](architecture-of-connectable-objects.md)
-   [Connectable Object Interfaces](connectable-object-interfaces.md)

 

 




