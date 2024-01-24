---
description: The COM+ Events service uses an event class object to manage the connection between publisher and subscriber.
ms.assetid: 877c5890-588d-4978-8fb2-b4ecf4134068
title: The COM+ Event Class Object
ms.topic: article
ms.date: 05/31/2018
---

# The COM+ Event Class Object

The COM+ Events service uses an *event class object* to manage the connection between publisher and subscriber. The event class object is a COM+ component that is managed and stored by the COM+ Events system and contains the interfaces and methods used by a publisher to fire events. It is a persistent object that indicates the events that can occur and, optionally, identifies the publisher. You specify the interfaces and methods you want an event class to contain by providing a type library.

To fire an event, the publisher instantiates the event class object by calling [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) or the Microsoft Visual Basic **CreateObject** method and requesting the event interface be returned. The instantiated event class object contains the event system's implementation of the requested interface. An interested subscriber must also implement the event class interface to receive events from a given publisher. When the event class object is instantiated, the event system associates it with the appropriate subscribers. The list of subscribers is maintained for the lifetime of the event class object. An event can be delivered to multiple subscribers either serially or in parallel.

When you implement an event class object, you should provide a self-registering DLL that exports the [**DllRegisterServer**](/windows/desktop/api/olectl/nf-olectl-dllregisterserver) and [**DllUnregisterServer**](/windows/desktop/api/olectl/nf-olectl-dllunregisterserver) functions. The **DllRegisterServer** function registers a COM class, and the **DllUnregisterServer** function unregisters the component. Event class objects are stored in the COM+ catalog, either by using the Component Services administration tool or programmatically by using the methods of the [**ICOMAdminCatalog::InstallEventClass**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-installeventclass) or [**ICOMAdminCatalog::InstallMultipleEventClasses**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-installmultipleeventclasses) interfaces. For detailed information about registering event class objects, see [Registering an Event Class](registering-an-event-class.md).

Because event class objects are configured components, other attributes, such as queuing, transactions, security, and so on, can be configured for them by using either the Component Services administration tool or the COM+ Administrative SDK functions.

> [!Note]  
> The COM+ Events service uses type library marshaling. This places some restrictions on event class interfaces. For example, the type library marshaler does not support the MIDL attributes [**size\_is**](/windows/desktop/Midl/size-is) and [**length\_is**](/windows/desktop/Midl/length-is).

 

An event class object possesses publication attributes that determine the way events are published, as well as the following properties:

-   **EventCLSID**. A unique identifier that specifies the CLSID of the component.
-   **EventClassName**. A unique identifier that specifies the PROGID of the component.
-   **TypeLibrary**. Provides a list of interfaces offered by the event class object. There is no need to implement the firing interfaces specified in the type library.

## Related topics

<dl> <dt>

[COM+ Events Security Considerations](com--events-security-considerations.md)
</dt> <dt>

[Filtering Events in COM+](filtering-events-in-com-.md)
</dt> <dt>

[Publishing and Delivering Events in COM+](publishing-and-delivering-events-in-com-.md)
</dt> <dt>

[Subscriptions](subscriptions.md)
</dt> <dt>

[Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md)
</dt> </dl>

 

 
