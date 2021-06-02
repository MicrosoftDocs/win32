---
description: Subscription data resides in the subscription COM+ catalog. A subscription can be created either by using the Component Services administrative tool or programmatically by using the ICOMAdminCatalog::InstallComponent interface.
ms.assetid: '190e88f3-1d87-4c27-9451-0a633cbae829'
title: Subscriptions
ms.topic: article
ms.date: 05/31/2018
---

# Subscriptions

Subscription data resides in the subscription COM+ catalog. A subscription can be created either by using the Component Services administrative tool or programmatically by using the [**ICOMAdminCatalog::InstallComponent**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-installcomponent) interface.

The [**SubscriptionsForComponent**](subscriptionsforcomponent.md) collection is used to add, delete, or change information pertaining to subscriptions. The **SubscriptionsForComponent** collection is a child collection to a component. To add a subscription, get the component's **SubscriptionsForComponent** collection and use the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) method to add an entry to the collection. To set up the various properties of the subscription object, use the [**Value**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_value) property. To save the changes, use [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) on the **SubscriptionsForComponent** collection object.

You can also use the Component Services administration tool to modify some, but not all, of the subscription properties. Subscriptions specify the following information:

-   Identity and location of the subscriber
-   Delivery method
-   Event methods to deliver
-   Event class object and PublisherID property of an event class component from which the subscriber wants to receive events

Subscriptions exist independently from event class objects. You can disable a subscription by setting the Enabled property to False. A disabled subscription is not called by COM+ Events.

The three types of subscriptions are as follows:

<dl> <dt>

<span id="Persistent"></span><span id="persistent"></span><span id="PERSISTENT"></span>Persistent
</dt> <dd>

Persistent subscriptions reside in the COM+ catalog and are independent from the subscriber's lifetime. Persistent subscriptions survive a system restart. Generally, a persistent subscription is created when an application is installed on a subscriber's computer and removed when the application is removed. After a persistent subscription is created, COM+ Events activates the subscriber each time an event should be delivered to it.

When a publisher instantiates and makes a call on an [event class](the-com--event-class-object.md) object, the object looks for all the persistent subscriptions in the COM+ catalog and creates a new instance of each object. The creation process can be either direct or through a moniker for queued components. Specify the subscriber object by the [**SubscriberMoniker**](subscriptionsforcomponent.md) property of the subscription. Subscriber objects created by a persistent subscription are always released after each event call.

</dd> <dt>

<span id="Transient"></span><span id="transient"></span><span id="TRANSIENT"></span>Transient
</dt> <dd>

For transient subscriptions, you can use the [**TransientSubscriptions**](transientsubscriptions.md) collection, whose parent object is the root catalog object. Transient subscriptions request an event for a specific subscriber object that already exists. Transient subscriptions are stored in the COM+ catalog, but the subscription is deleted if the event system or operating system is stopped. Unlike persistent subscriptions, transient subscriptions are tied to a particular object and are stored only in the event system. Transient subscriptions can be more efficient than persistent subscriptions, but you must manage their object life cycles. For information about registering a transient subscription, see [Registering a Transient Subscription](registering-a-transient-subscription.md).

</dd> <dt>

<span id="Per_user"></span><span id="per_user"></span><span id="PER_USER"></span>Per user
</dt> <dd>

Per User subscriptions can deliver events only when the subscriber is logged on to the event system's computer. When the subscriber logs on, the event system enables all subscriptions on which the *PerUser* flag is set to **TRUE** and *UserName* is set to the name of the user who is logged on. When the subscriber logs off, the subscriptions are disabled.

Per User subscriptions are effective only when the publisher and subscriber are on the same computer. Logon and logoff are detected only at the publisher's computer—not the computer on which the subscriber object resides.

</dd> </dl>

The event system uses meta-events to notify interested subscribers whenever event class objects or subscriptions are created, modified, or removed. To receive meta-events from the event system, applications must create a subscription that resides on the event system's computer and that specifies the firing interface ID (IID\_IEventObjectChange).

## Related topics

<dl> <dt>

[Filtering Events in COM+](filtering-events-in-com-.md)
</dt> <dt>

[Publishing and Delivering Events in COM+](publishing-and-delivering-events-in-com-.md)
</dt> <dt>

[The COM+ Event Class Object](the-com--event-class-object.md)
</dt> <dt>

[Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md)
</dt> </dl>

 

 



