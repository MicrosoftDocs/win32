---
title: Handling Service-Defined Events
description: A Service object makes available all of the properties and methods that have been defined for the service that it represents, and it also makes available any service-defined events.
ms.assetid: a12beb30-a89b-4d3d-8794-8b71c924467c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Handling Service-Defined Events

A [**Service**](service-object.md) object makes available all of the properties and methods that have been defined for the service that it represents, and it also makes available any service-defined events.

WPD Automation matches each service-defined event with a dynamically generated *onEventName* property. Event handlers for these service events are registered by setting the corresponding *onEventName* property to the name of the event handler. Because the event handlers are set through properties, there can only be one event handler per event per instance of the service.

To write an event handler for a service-defined event, you must know the type and ordering of the event parameters from the service definition. WPD Automation will pass any parameters in the service definition directly to the event handler. Even though MTP events are limited to three parameters, WPD Automation supports more than this limit. If the JScript event handler has extra parameters, they will be "undefined". If the event handler has fewer parameters than required, the extra parameters will be dropped.

In the following JScript example, an event handler called HandleMyEvent is set for the service-defined event MyEvent using the onMyEvent property. In the DoSomethingToTriggerEvent function, a service-defined method DoSomethingCool is called, which triggers the event and causes WPD Automation to call the HandleMyEvent event handler.


```JScript
// This function is the event handler for the service defined
// event "MyEvent." This function can be written with any number
// of parameters. The parameter type and ordering comes directly
// from the service definition. The function should match that
// definition so that parameters are not dropped, or extra 
// parameters are not "undefined".

function HandleMyEvent(a)
{
    alert('Received my event!' + a);
}


function DoSomethingToTriggerEvent()
{
    // The event handler is set by using the "onMyEvent" property
    // that tells the service object which handler to use for 
    // the service-defined event "MyEvent".

    acmeService.onMyEvent = HandleMyEvent;

    // Calling this service-defined method triggers the event.
    acmeService.DoSomethingCool();  
}
```



> [!Note]  
> It is recommended that you clear the event handler of an object variable by setting it to **null**, before reusing that variable to represent a new object. This will keep an event handler object from persisting as a property of the old object. For examples of this, see the [**Service.onObjectAdded Event**](onobjectadded.md) and [**Storage.onObjectAdded Event**](storage-onobjectadded.md) reference pages.

 

## Related topics

<dl> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




