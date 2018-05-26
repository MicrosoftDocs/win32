---
Description: An event provider must implement the IWbemEventProvider interface to generate event notifications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae33c9f5-61f7-4488-a281-01d7f9c62c46
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Implementing the Primary Interface for an Event Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing the Primary Interface for an Event Provider

An event provider must implement the [**IWbemEventProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventprovider?branch=master) interface to generate event notifications. WMI calls the [**IWbemEventProvider::ProvideEvents**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventprovider-provideevents?branch=master) method of the provider and passes in a pointer to the sink object, which is an implementation of the [**IWbemObjectSink**](iwbemobjectsink.md) interface. When the event provider is ready to generate a notification, the provider calls the [**IWbemObjectSink::Indicate**](/windows/win32/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate?branch=master) method.

An event provider should place the notifications generated through [**IWbemEventProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventprovider?branch=master) in event objects. You should implement event objects as entries in an array of [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) interfaces represented by the *ppObjArray* parameter of the [**Indicate**](/windows/win32/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate?branch=master) method. Because **IWbemClassObjects** are COM objects, the provider must increment the reference count for the sink by calling the [**IWbemObjectSink::AddRef**](_com_iunknown_addref) method. Event providers that must supply many notifications (for example, 400 events) should create a unique event object for each notification by either spawning a new instance or cloning an existing one. WMI never holds onto an event object past the completion of the **Indicate** call, and has no special requirements for **AddRef** above and beyond the COM standard.

Consider the following guidelines when implementing an event provider:

-   Do not make any class changes while servicing a client call.
-   Do not issue any event-related calls, such as a call that modifies an event filter.
-   Process any requests that the Windows Management service issues, such as [**CancelQuery**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-cancelquery?branch=master), before refiring an event.

    If you do not process the request, then refiring the event might block the event from ever being accepted.

-   Never call [**IWbemObjectSink::SetStatus**](/windows/win32/Wbemcli/nf-wbemcli-iwbemobjectsink-setstatus?branch=master) from within a provider.

 

 



