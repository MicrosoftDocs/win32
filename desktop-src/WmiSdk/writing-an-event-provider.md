---
description: An event provider is a COM object that supplies WMI with notifications of intrinsic and extrinsic events.
ms.assetid: 075bdc65-4ea3-4f91-9823-1d2d0dc13423
ms.tgt_platform: multiple
title: Writing an Event Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Event Provider

An event provider is a COM object that supplies WMI with notifications of intrinsic and extrinsic events. An intrinsic event reports an internal data change to WMI, while an extrinsic event reports a user-defined event not described by an intrinsic event. For example, an event in response to changes, creation, or deletion of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class would classify as an intrinsic event. An event that is generated on the basis of something other than the modification, creation, or deletion of an existing WMI object is an extrinsic event. Regardless of the supported class, you can implement all event providers in the same manner.

The following procedure describes how to implement an event provider.

**To implement an event provider**

1.  Design and register your class provider with WMI.

    Class providers register with WMI by creating a [**\_\_Win32Provider**](--win32provider.md) instance and an [**\_\_EventProviderRegistration**](--eventproviderregistration.md) class. For more information, see [Registering an Event Provider](registering-an-event-provider.md).

2.  Implement the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface for your provider.

    The [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface is a common interface WMI uses to load and initialize all providers. For more information, see [Initializing a Provider](initializing-a-provider.md).

3.  Implement the [**IWbemEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovider) as the primary interface for your provider.

    The [**IWbemEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovider) interface uses the **ProviderEvents** method to supply events to WMI. For more information, see [Implementing the Primary Interface for an Event Provider](implementing-the-primary-interface-for-an-event-provider.md).

    > [!Note]  
    > Event providers must use the multithreading model "Both".

     

4.  Optionally, you may also implement the [**IWbemEventProviderQuerySink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventproviderquerysink) interface to increase the performance of your event provider.

    The [**IWbemEventProviderQuerySink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventproviderquerysink) interface allows the provider to optimize queries before sending a response to WMI, and is most useful for a provider that supplies events of multiple types and that needs to perform as many internal optimizations as possible. For more information, see [Optimizing an Event Provider](optimizing-an-event-provider.md).

5.  Implement the [**IWbemEventProviderSecurity**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovidersecurity) interface to limit consumers to certain security identifiers (SIDs) or implement [**IWbemEventSink::SetSinkSecurity**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventsink-setsinksecurity) to secure the sink itself. The provider can also set the **SECURITY\_DESCRIPTOR** property in the event class to secure individual events in the MOF code. For more information, see [Securing WMI Events](securing-wmi-events.md).
6.  Add any additional code necessary for your provider.

    When designing your provider, you most likely need to call WMI interfaces. For more information, see [Calling a Method](calling-a-method.md).

    When retrieving information for a client, you may need to access the security levels for that client. For more information, see [Impersonating a Client](impersonating-a-client.md).

7.  Replace the preexisting provider with your new code.

    You do not need to perform this step if you do not have a preexisting provider to copy over. For more information, see [Updating a Provider](updating-a-provider.md).

A client application can request an event by registering itself with WMI as an event consumer. For more information, see [Receiving a WMI Event](receiving-a-wmi-event.md).

 

 
