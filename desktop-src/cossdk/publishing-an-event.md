---
description: Publishing an Event
ms.assetid: b40d10aa-43bc-4c53-9e89-94c585d34238
title: Publishing an Event
ms.topic: article
ms.date: 05/31/2018
---

# Publishing an Event

To publish an event, just instantiate an event object by calling [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) or the Microsoft Visual Basic **CreateObject** method using EventClassID or EventClassName as an argument. The publisher calls [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the event object to obtain the interfaces supported by the event class object and invokes a method on the event object through the interface to publish the event. The event system then publishes events on the event class CLSID\_EventObjectChange with the interface ID IID\_IEventObjectChange.

To support delivery of events to multiple subscribers, event class methods should contain only in parameters.

By using the FireInParallel property of the [event class](the-com--event-class-object.md) object, publishers can request that the event system use multiple threads to deliver an event to more than one subscriber. Selecting an in-parallel delivery mechanism does not guarantee simultaneous delivery of the event to multiple subscribers, but it instructs the COM+ events service to permit this to happen.

## Related topics

<dl> <dt>

[Publishing and Delivering Events in COM+](publishing-and-delivering-events-in-com-.md)
</dt> </dl>

 

 
