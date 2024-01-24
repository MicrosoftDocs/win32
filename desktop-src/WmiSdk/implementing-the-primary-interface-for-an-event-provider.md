---
description: An event provider must implement the IWbemEventProvider interface to generate event notifications.
ms.assetid: ae33c9f5-61f7-4488-a281-01d7f9c62c46
ms.tgt_platform: multiple
title: Implementing the Primary Interface for an Event Provider
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Primary Interface for an Event Provider

An event provider must implement the [**IWbemEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovider) interface to generate event notifications. WMI calls the [**IWbemEventProvider::ProvideEvents**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventprovider-provideevents) method of the provider and passes in a pointer to the sink object, which is an implementation of the [**IWbemObjectSink**](iwbemobjectsink.md) interface. When the event provider is ready to generate a notification, the provider calls the [**IWbemObjectSink::Indicate**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate) method.

An event provider should place the notifications generated through [**IWbemEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovider) in event objects. You should implement event objects as entries in an array of [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) interfaces represented by the *ppObjArray* parameter of the [**Indicate**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate) method. Because **IWbemClassObjects** are COM objects, the provider must increment the reference count for the sink by calling the [**IWbemObjectSink::AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) method. Event providers that must supply many notifications (for example, 400 events) should create a unique event object for each notification by either spawning a new instance or cloning an existing one. WMI never holds onto an event object past the completion of the **Indicate** call, and has no special requirements for **AddRef** above and beyond the COM standard.

Consider the following guidelines when implementing an event provider:

-   Do not make any class changes while servicing a client call.
-   Do not issue any event-related calls, such as a call that modifies an event filter.
-   Process any requests that the Windows Management service issues, such as [**CancelQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-cancelquery), before refiring an event.

    If you do not process the request, then refiring the event might block the event from ever being accepted.

-   Never call [**IWbemObjectSink::SetStatus**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-setstatus) from within a provider.

 

 
