---
description: The COM+ events service is used to manage the delivery of events from publishers to subscribers.
ms.assetid: 0945163b-1276-47f6-ae7f-9d932a1b586d
title: Using COM+ Events with COM+ Queued Components
ms.topic: article
ms.date: 05/31/2018
---

# Using COM+ Events with COM+ Queued Components

The COM+ events service is used to manage the delivery of events from publishers to subscribers. The COM+ queued components service can be used to make the publisher and subscriber processing time independent by queuing the publisher's message and later replaying it to the subscriber. Whether or not you need to use the queued components service depends on the underlying business logic of your application. If you need to have events that are time independent, you can create them by using the COM+ events service with COM+ queued components service.

> [!Note]  
> For additional information about using the COM+ queued components service, see [COM+ Queued Components](com--queued-components.md).

 

The queued components service maintains order-of-method invocation within a single message. The recorder batches all method invocations into a message, and then the player invokes those methods in order when the message is processed.

A queued components recorder and player can be positioned in either of the following two places:

-   Between the publisher and event object
-   Between the event object and subscriber

If you position the recorder and player between the publisher and event object, you are making the [event class](the-com--event-class-object.md) component queuable. The event class component must be marked for queuing and be activated by the player in a process that is separate from the publisher.

To deliver events asynchronously, compose the recorder and player between the event object and subscriber and set the Queued attribute of the subscription object. This sets SubscriberMoniker as follows: "queue:/new:/{12345678-1234-1234-1234-123456789012}".

There is an order of delivery implication to consider when using queued components in an event situation. Because the queued components service records and plays back all calls within the lifetime of a single object in one message, all calls are replayed in the order in which they were made. However, if there is more than one session with more than one object, order cannot be guaranteed. If order is important, make sure that calls that need to be played back in order reside on the same object instance.

## Related topics

<dl> <dt>

[Filtering Events in COM+](filtering-events-in-com-.md)
</dt> <dt>

[Publishing and Delivering Events in COM+](publishing-and-delivering-events-in-com-.md)
</dt> <dt>

[Subscriptions](subscriptions.md)
</dt> <dt>

[The COM+ Event Class Object](the-com--event-class-object.md)
</dt> </dl>

 

 



