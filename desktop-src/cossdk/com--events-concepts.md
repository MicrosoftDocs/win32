---
description: COM+ Events Concepts
ms.assetid: 6bfe4852-4029-4dd4-92ad-3061618b1b23
title: COM+ Events Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Events Concepts

The COM+ events service is an automated, *loosely coupled event* system that stores event information from different publishers in the COM+ catalog. Subscribers can query this event store and select the events that they want to hear about.

> [!Note]  
> An *event* is identified by a method in a COM+ interface, known as an *event method*, and is originated by a publisher and dispatched to the correct subscriber or subscribers through the COM+ events service. Event methods must be uniquely named and can contain only input parameters (no output or input/output parameters). The return value must be an **HRESULT**.

 

The COM+ events service handles most of the event semantics for the publisher and subscriber. Publishers offer to publish event types, and subscribers request event types from publishers. Unlike a *tightly coupled event* system, where publishers must handle the overhead of calling subscribers directly, the COM+ events service maintains subscription data in the COM+ catalog, independent of the publisher and subscriber. This simplifies the programming model for the publisher and subscriber because the COM+ subscriber component does not need to contain the logic for building subscriptions.

Because the life cycle of the COM+ events subscription data is separate from that of either the publisher or the subscriber, subscriptions can be built prior to either the subscriber or the publisher applications being active. This also means that publishers and subscribers can be developed and deployed separately. The publisher can be written without knowledge of the number and location of the subscribers. The subscribers use the COM+ Events service to find the publisher and manage their subscriptions.

The following topics in this section provide detailed information about the core elements of the COM+ events service and how to use them.

-   [The COM+ Event Class Object](the-com--event-class-object.md)
-   [Subscriptions](subscriptions.md)
-   [Publishing and Delivering Events in COM+](publishing-and-delivering-events-in-com-.md)
-   [Filtering Events in COM+](filtering-events-in-com-.md)
-   [Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md)

## Related topics

<dl> <dt>

[COM+ Events Security Considerations](com--events-security-considerations.md)
</dt> <dt>

[COM+ Events Tasks](com--events-tasks.md)
</dt> </dl>

 

 



