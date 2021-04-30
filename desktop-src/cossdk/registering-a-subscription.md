---
description: After you have registered an event class in the COM+ catalog, you can add subscribers to the event class and subscriptions to the subscribers.
ms.assetid: 101b1075-3724-4508-9c9e-2f12ac6ab65d
title: Registering a Subscription
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Subscription

After you have registered an event class in the COM+ catalog, you can add subscribers to the event class and subscriptions to the subscribers. Subscriptions can subscribe to a single method or to all the methods of an interface. To receive calls on more than one method—but not to every method—of an interface, you must add a subscription for each method to which you want to receive a call. The Component Services administration tool can search the COM+ catalog for registered event classes that support the interfaces implemented by the subscriber and offers you the choice to subscribe. Choose the publisher that offers you the desired events.

To add subscribers to the subscriber component, use the following steps:

1.  After creating a new COM+ application and installing the subscriber component, right-click the **Subscriptions** folder to enable the COM+ New Subscription Wizard.

2.  Choose the event class from which you want to receive events.

3.  Enter a name for the subscription.

4.  Enable the subscription.

5.  Click **OK**.

When a publisher application wants to fire an event, the publisher instantiates the event class object and calls a method on it. COM+ searches the COM+ catalog to find all the subscribers. It creates the subscriber object (directly, queued, or with a moniker) and passes on the method call originally made by the publisher.

## Related topics

<dl> <dt>

[Registering an Event Class](registering-an-event-class.md)
</dt> </dl>

 

 



