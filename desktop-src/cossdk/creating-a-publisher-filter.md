---
description: Creating a Publisher Filter
ms.assetid: d91efecc-f02a-41c6-acf7-37b74723e7e8
title: Creating a Publisher Filter
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Publisher Filter

There are two methods to establish the publisher filter: using the MultiPublisherFilterCLSID property of the event class, or using [**IEventControl::SetPublisherFilter**](/windows/desktop/api/Eventsys/nf-eventsys-ieventcontrol-setpublisherfilter).

-   Because it allows you to compose the event object with the [COM+ queued components](com--queued-components.md) service, the preferred method is to use the MultiPublisherFilterCLSID property in the event class to set the publisher filter. This establishes one filter object for all the methods of the event interfaces for an event object. The event object activates the publisher filter when the event class object is instantiated using [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).
-   You can also use [**SetPublisherFilter**](/windows/desktop/api/Eventsys/nf-eventsys-ieventcontrol-setpublisherfilter). However, if you choose this method, the interface is not queuable and therefore cannot use the event object with the COM+ queued components service between the publisher and the event class object. For additional information about using the queued components service with COM+ Events, see [Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md).

An event can have one or more filter objects or none at all. The publisher filter objects must support either [**IPublisherFilter**](/windows/desktop/api/EventSys/nn-eventsys-ipublisherfilter) or [**IMultiInterfacePublisherFilter**](/windows/desktop/api/EventSys/nn-eventsys-imultiinterfacepublisherfilter), depending on whether you have a single firing interface or multiple firing interfaces on the event class object. The **IPublisherFilter** and **IMultiInterfacePublisherFilter** interfaces both specify an **Initialize** method. The **Initialize** method is called by the event class object immediately after creating the filter object.

COM+ Events tries to invoke two methods on the filter. First it calls [**IPublisherFilter::PrepareToFire**](/windows/desktop/api/EventSys/nf-eventsys-ipublisherfilter-preparetofire) and passes an [**IFiringControl**](/windows/desktop/api/EventSys/nn-eventsys-ifiringcontrol) interface pointer to the filter. Then it queries the filter object for the event interface. If the filter supports the event interface, it invokes a method on it. This provides access to the publisher parameters for an event. The filter can use these parameters to determine which subscriptions to fire.

## Related topics

<dl> <dt>

[Filtering Events in COM+](filtering-events-in-com-.md)
</dt> </dl>

 

 
