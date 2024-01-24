---
description: To publish an event, simply instantiate an event class object and invoke the desired method; for detailed instructions on how to do this in code, see Publishing an Event.
ms.assetid: 835c3753-fdcc-4afe-94c3-c954aaf1c832
title: Publishing and Delivering Events in COM+
ms.topic: article
ms.date: 05/31/2018
---

# Publishing and Delivering Events in COM+

To publish an event, simply instantiate an [event class](the-com--event-class-object.md) object and invoke the desired method; for detailed instructions on how to do this in code, see [Publishing an Event](publishing-an-event.md).

When a publisher fires an event, the COM+ Events service searches the subscription database to find all the subscribers who have registered subscriptions to the instantiated event class. It connects to those subscribers (by direct creation, monikers, or queued components) and calls the method. To support more than one subscriber notification for an event, methods can contain only in parameters and must return only success or failure **HRESULT** values.

> [!Note]  
> This version of COM+ events does not support a distributed event store. A subscriber must subscribe to an event on each computer from which it wants to receive notification. As an alternative, you can register the event class object and subscriptions on a central computer and instantiate this event class object from the remote computers on which you publish events. Delivery of events is provided either by DCOM or by the COM+ queued components service. For more information about using the COM+ queued components service, see [Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md).

 

By default, the COM+ events service fires events one at a time, in no determined or repeatable order. Publishers that need to control the order in which subscribers receive an event can implement a publisher filter. (For more information, see [Filtering Events in COM+](filtering-events-in-com-.md).)

## Related topics

<dl> <dt>

[Filtering Events in COM+](filtering-events-in-com-.md)
</dt> <dt>

[Subscriptions](subscriptions.md)
</dt> <dt>

[The COM+ Event Class Object](the-com--event-class-object.md)
</dt> <dt>

[Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md)
</dt> </dl>

 

 



