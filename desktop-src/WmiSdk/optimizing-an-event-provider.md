---
Description: 'An event provider may devote a great deal of time to creating events.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '5cf414f0-b3a8-4623-9aaa-08e2a28b40c0'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Optimizing an Event Provider
---

# Optimizing an Event Provider

An event provider may devote a great deal of time to creating events. If no client applications use the created events, then the provider is wasting system resources. Further, WMI spends a considerable amount of resources parsing and sending complex queries to the appropriate provider. To avoid the waste of system resources and to improve the performance of your event provider, you can implement the [**IWbemEventProviderQuerySink**](iwbemeventproviderquerysink.md) interface. **IWbemEventProviderQuerySink** monitors the queries that client applications register with WMI by using the [**NewQuery**](iwbemeventproviderquerysink-newquery.md) and [**CancelQuery**](iwbemeventproviderquerysink-cancelquery.md) methods. By monitoring the registered client queries, your provider can determine what if any messages must be sent to WMI.

WMI calls [**NewQuery**](iwbemeventproviderquerysink-newquery.md) on an event provider when a client consumer registers an event filter query that contains references to events supported by that event provider. So the event provider responsible for instance modification events for the **EmailClass** class can be set up to generate notifications only for **sender**. When the provider receives a query requesting notification of changes to the **subject** property, the provider can start generating those notifications. In this scenario, WMI is not required to discard the notifications that report **recipient** changes only.

Similarly, WMI calls [**CancelQuery**](iwbemeventproviderquerysink-cancelquery.md) on an event provider when a client consumer deregisters an event filter query that contains references to events supported by the event provider. The purpose of **CancelQuery** is for the event provider to update the list of what events should be sent out.

> [!Note]  
> If your provider supports both [**IWbemEventProvider**](iwbemeventprovider.md) and [**IWbemEventProviderQuerySink**](iwbemeventproviderquerysink.md), ensure that your implementation of the **IUnknown::QueryInterface** method returns pointers to both interfaces.

 

 

 



