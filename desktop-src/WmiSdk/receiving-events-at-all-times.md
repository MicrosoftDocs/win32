---
description: You may want to write an application that can react to events at any time.
ms.assetid: 475dca47-b1e5-4362-ab00-9ab9383e92f9
ms.tgt_platform: multiple
title: Receiving Events at All Times
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Events at All Times

You may want to write an application that can react to events at any time. For example, an administrator may want to receive an email message when specific performance measures decline on network servers. In this case, your application should run at all times. However, running an application continuously is not an efficient use of system resources. Instead, WMI allows you to create a permanent event consumer. Permanent event consumers must meet special security requirements. For more information, see [Securing WMI Events](securing-wmi-events.md).

A permanent event consumer receives events until its registration is explicitly canceled.

A permanent event consumer is a combination of the following WMI classes, filters, and COM objects that reside on your system:

-   A COM object called a physical consumer. WMI supplies several standard permanent consumers. For example, the Active Script Event consumer [runs a script when an event occurs](running-a-script-based-on-an-event.md).
-   A new permanent consumer class.
-   An instance of the permanent consumer class called a logical consumer.
-   A filter that contains the query for events.
-   A linkage between the consumer and the filter.

The properties of a logical event consumer specify the actions to perform when notified of an event, but do not define the event queries with which they are associated. When signaled, WMI automatically loads the COM object that represents the permanent event consumer into active memory. Typically, this occurs during startup or in response to a triggering event. After being activated, the permanent event consumer acts as a normal event consumer, but remains until specifically unloaded by the operating system.

You can write your own permanent event consumer or use the WMI preinstalled [Standard Consumer Classes](standard-consumer-classes.md), such as [**ActiveScriptEventConsumer**](activescripteventconsumer.md). For more information, see [Standard Consumer Classes](standard-consumer-classes.md), [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md), and [Monitoring Events](monitoring-events.md).

The following procedure describes how to create your own permanent event consumer.

**To create your own permanent event consumer**

1.  Determine what kind of events you want to receive.

    WMI supports intrinsic and extrinsic events. An intrinsic event is an event predefined by WMI, whereas an extrinsic event is an event defined by a third party provider. For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

2.  [Implement a physical consumer](implementing-a-physical-consumer.md).

    The main difference between a management application and a [*physical consumer*](gloss-p.md) is that a user loads and unloads a management application, whereas WMI loads and unloads a physical consumer. Most of your coding should be in the physical consumer.

    > [!Note]  
    > This step is first in the procedure for ease of explanation. In terms of coding, you should actually create the physical consumer last. That way you can lay out your parameters and logic for your permanent event provider before you start lengthy coding. However, there is no restriction against writing the physical consumer first.

     

3.  [Create a new consumer class describing the physical consumer](creating-a-new-permanent-event-consumer-class.md).

    Like any class, the consumer class describes the general parameters of a permanent event consumer to WMI.

4.  [Create an instance of the consumer class](creating-a-logical-consumer.md).

    Like any other WMI class, you must create an instance of the consumer class if you want to implement the class. An instance of a consumer class is also known as a [*logical consumer*](gloss-l.md). The logical consumer represents the physical consumer to WMI.

5.  [Create an event filter](creating-an-event-filter.md).

    The event queries that activate permanent event consumers are called [*event filters*](gloss-e.md). A single event filter can be associated with multiple logical event consumers. Furthermore, multiple event filters can be associated with a single logical event consumer. The filter is an instance of [**\_\_EventFilter**](--eventfilter.md).

    An NT Log event is generated when a permanent event consumer's query fails. The event's source is WinMgmt, the event ID is 10, and the event type is Error.

6.  [Link the event filter to the logical consumer](binding-an-event-filter-with-a-logical-consumer.md).

    By linking the event filter to the logical consumer, you instruct WMI about which event filter belongs to which logical consumer. Logical event consumers and event filters are linked by an association class instance of [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md). When an event is received that matches an event query described in an event filter, WMI finds the associated logical event consumer by looking at the association class instance. After the logical event consumer instance is located, WMI uses an instance of the [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) class to locate and run the physical event consumer associated with this instance.

7.  [Writing an event consumer provider](writing-an-event-consumer-provider.md).

    The event consumer provider is a COM object that locates the physical consumer for WMI.

 

 



