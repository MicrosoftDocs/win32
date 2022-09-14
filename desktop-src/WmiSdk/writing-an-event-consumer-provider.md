---
description: An event consumer provider is a component of the permanent consumer architecture that determines which permanent event consumer handles a given event.
ms.assetid: c5a0d0ec-99af-4815-9ad2-e59db70e04ce
ms.tgt_platform: multiple
title: Writing an Event Consumer Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Event Consumer Provider

An event consumer provider is a component of the permanent consumer architecture that determines which permanent event consumer handles a given event. You should create an event consumer provider along with your permanent event consumers to route events properly from WMI.

An event consumer provider links an event provider with a list of consumer classes. Instances of these consumer classes then receive events from that provider. WMI identifies which consumer provider the events are delivered to, based on the [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) instance, which associates the consumer provider [**\_\_Win32Provider**](--win32provider.md) instance with a logical consumer class. Users create instances of the consumer class as part of a permanent subscription. If the event provider is not running when an event occurs, then WMI starts the provider when it needs to deliver events.

The following procedure describes how to implement an event consumer provider.

**To implement an event consumer provider**

1.  Design consumer classes in Managed Object Format (MOF) and register them with WMI. For more information, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).

    Class providers register with WMI by creating a [**\_\_Win32Provider**](--win32provider.md) instance and an [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) class. For more information, see [Registering an Event Consumer Provider](registering-an-event-consumer-provider.md).

2.  Implement the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface for your provider.

    WMI uses [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) to load and initialize a provider. For more information, see [Initializing a Provider](initializing-a-provider.md).

    > [!Note]  
    > Event consumer providers are strongly encouraged to use the multithreading model "Both".

     

3.  Implement the [**IWbemEventConsumerProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventconsumerprovider) interface for your provider.

    The [**IWbemEventConsumerProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventconsumerprovider) interface is the primary interface for an event consumer provider.

4.  Supply one or more physical consumers to receive the event messages from WMI.

    A physical consumer is a COM object that represents a permanent event consumer. All physical consumers must implement the [**IWbemUnboundObjectSink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemunboundobjectsink) interface. For more information, see [Implementing a Physical Consumer](implementing-a-physical-consumer.md).

 

 



