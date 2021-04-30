---
description: An event provider may devote a great deal of time to creating events.
ms.assetid: 5cf414f0-b3a8-4623-9aaa-08e2a28b40c0
ms.tgt_platform: multiple
title: Optimizing an Event Provider
ms.topic: article
ms.date: 05/31/2018
---

# Optimizing an Event Provider

An event provider may devote a great deal of time to creating events. If no client applications use the created events, then the provider is wasting system resources. Further, WMI spends a considerable amount of resources parsing and sending complex queries to the appropriate provider. To avoid the waste of system resources and to improve the performance of your event provider, you can implement the [**IWbemEventProviderQuerySink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventproviderquerysink) interface. **IWbemEventProviderQuerySink** monitors the queries that client applications register with WMI by using the [**NewQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-newquery) and [**CancelQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-cancelquery) methods. By monitoring the registered client queries, your provider can determine what if any messages must be sent to WMI.

WMI calls [**NewQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-newquery) on an event provider when a client consumer registers an event filter query that contains references to events supported by that event provider. So the event provider responsible for instance modification events for the **EmailClass** class can be set up to generate notifications only for **sender**. When the provider receives a query requesting notification of changes to the **subject** property, the provider can start generating those notifications. In this scenario, WMI is not required to discard the notifications that report **recipient** changes only.

Similarly, WMI calls [**CancelQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-cancelquery) on an event provider when a client consumer deregisters an event filter query that contains references to events supported by the event provider. The purpose of **CancelQuery** is for the event provider to update the list of what events should be sent out.

> [!Note]  
> If your provider supports both [**IWbemEventProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventprovider) and [**IWbemEventProviderQuerySink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemeventproviderquerysink), ensure that your implementation of the **IUnknown::QueryInterface** method returns pointers to both interfaces.

 

 

 



