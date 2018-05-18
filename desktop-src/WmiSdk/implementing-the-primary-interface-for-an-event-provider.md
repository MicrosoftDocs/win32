---
Description: 'An event provider must implement the IWbemEventProvider interface to generate event notifications.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ae33c9f5-61f7-4488-a281-01d7f9c62c46'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Implementing the Primary Interface for an Event Provider
---

# Implementing the Primary Interface for an Event Provider

An event provider must implement the [**IWbemEventProvider**](iwbemeventprovider.md) interface to generate event notifications. WMI calls the [**IWbemEventProvider::ProvideEvents**](iwbemeventprovider-provideevents.md) method of the provider and passes in a pointer to the sink object, which is an implementation of the [**IWbemObjectSink**](iwbemobjectsink.md) interface. When the event provider is ready to generate a notification, the provider calls the [**IWbemObjectSink::Indicate**](iwbemobjectsink-indicate.md) method.

An event provider should place the notifications generated through [**IWbemEventProvider**](iwbemeventprovider.md) in event objects. You should implement event objects as entries in an array of [**IWbemClassObject**](iwbemclassobject.md) interfaces represented by the *ppObjArray* parameter of the [**Indicate**](iwbemobjectsink-indicate.md) method. Because **IWbemClassObjects** are COM objects, the provider must increment the reference count for the sink by calling the [**IWbemObjectSink::AddRef**](_com_iunknown_addref) method. Event providers that must supply many notifications (for example, 400 events) should create a unique event object for each notification by either spawning a new instance or cloning an existing one. WMI never holds onto an event object past the completion of the **Indicate** call, and has no special requirements for **AddRef** above and beyond the COM standard.

Consider the following guidelines when implementing an event provider:

-   Do not make any class changes while servicing a client call.
-   Do not issue any event-related calls, such as a call that modifies an event filter.
-   Process any requests that the Windows Management service issues, such as [**CancelQuery**](iwbemeventproviderquerysink-cancelquery.md), before refiring an event.

    If you do not process the request, then refiring the event might block the event from ever being accepted.

-   Never call [**IWbemObjectSink::SetStatus**](iwbemobjectsink-setstatus.md) from within a provider.

 

 



