---
description: After you create the logical event consumer and the event filter you must link them, which registers the logical consumer to receive notification about the events specified by the filter.
ms.assetid: 2fc3d781-2b93-4e9e-90a1-1b975ab40a01
ms.tgt_platform: multiple
title: Binding an Event Filter with a Logical Consumer
ms.topic: article
ms.date: 05/31/2018
---

# Binding an Event Filter with a Logical Consumer

After you create the logical event consumer and the event filter you must link them, which registers the logical consumer to receive notification about the events specified by the filter.

The following procedure describes how to bind an event filter with a logical consumer.

**To bind an event filter with a logical consumer**

1.  Create an instance of the [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) system class in the WMI repository.

    The [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) class is an association class that links the event filter instance and the logical consumer instance together through the **Filter** and **Consumer** reference properties. For more information, see [Declaring an Association Class](declaring-an-association-class.md).

2.  Set the **Filter** property to the instance of your filter.
3.  Set the **Consumer** property to the instance of your logical consumer.
4.  Set the **DeliverSynchronously** property to determine the type of delivery you want.

    The **DeliverSynchronously** property determines when WMI delivers event notifications synchronously or asynchronously. Setting this property to **TRUE** requests a synchronous delivery. Use synchronous delivery only when the permanent consumer can process events within approximately 100 microseconds.

    > [!Note]  
    > Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

     

5.  When unregistering your logical event consumer, ensure you delete the [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) instance.

    Each [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) instance represents a registration for a specific event notification. When you delete a binding, WMI deactivates the registration. You might have to delete the logical consumer and event filter instances to deactivate registration, depending on the implementation.

The following code example shows you a [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) instance that associates an instance of an [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class with a specific event filter (the instance of the event consumer was created in the [Creating a Logical Consumer](creating-a-logical-consumer.md) topic, and the event filter was created in the [Creating an Event Filter](creating-an-event-filter.md) topic).

``` syntax
instance of __FilterToConsumerBinding
{
    Filter = $FILTER;
    Consumer = $CONSUMER;
    DeliverSynchronously=FALSE;

    // this is the Administrators SID in array of bytes format
    CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0}; 
};
```

Two consumers, [**ActiveScriptEventConsumer**](activescripteventconsumer.md) and [**CommandLineEventConsumer**](commandlineeventconsumer.md), will not work unless their creator is a member of the local Administrators group.

**:** When an administrator creates a subscription, his SID is not used for the **CreatorSID** property, but the SID of the local Administrators group is used instead. Therefore, instances can be created by different administrators and the subscription will still work. For more information, see [Receiving Events Securely](receiving-events-securely.md).

When a filter is bound to a logical consumer the event is recorded by [Event Tracing](/windows/desktop/ETW/event-tracing-portal) for Windows (ETW). For more information, see [Tracing WMI Activity](tracing-wmi-activity.md).

## Related topics

<dl> <dt>

[Receiving Events at All Times](receiving-events-at-all-times.md)
</dt> </dl>

 

 
