---
description: 'There are two ways to implement a class provider: implement the interface as a push provider, or as a pull provider.'
ms.assetid: 2c6d3f73-e219-409b-9347-492035c1eb9f
ms.tgt_platform: multiple
title: Implementing the Primary Interface for a Class Provider
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Primary Interface for a Class Provider

There are two ways to implement a class provider: implement the interface as a push provider, or as a pull provider.

The following sections are discussed in this topic:

-   [Implementing the Primary Interface for a Push Class Provider](#implementing-the-primary-interface-for-a-push-class-provider)
-   [Implementing the Primary Interface for a Pull Class Provider](#implementing-the-primary-interface-for-a-pull-class-provider)

## Implementing the Primary Interface for a Push Class Provider

Whereas all providers implement [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) for initialization and at least one other interface as their primary interface, a push provider implements only **IWbemProviderInit**.

Ensure that your implementation performs the following tasks:

-   Retrieves the appropriate class data.
-   Places the data in the WMI repository.
-   Deletes obsolete data.

After completing the initialization process, WMI handles all application requests for classes belonging to the push provider without any further provider interaction. Afterward, the push provider effectively acts as a client of WMI rather than a provider. For more information about implementing [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit), see [Initializing a Provider](initializing-a-provider.md).

> [!Note]  
> When calling WMI to create, update, or remove data in a push provider, set the *lFlags* parameter to include the **WBEM\_FLAG\_OWNER\_UPDATE** flag in all calls to [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) methods.

 

## Implementing the Primary Interface for a Pull Class Provider

A class pull provider should implement [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) as the primary interface. The **IWbemServices** interface supports data retrieval, data update, data removal, enumeration, and query processing. However, because **IWbemServices** is also used by applications and providers to request services of WMI, **IWbemServices** contains many methods that are irrelevant to a class provider. Your implementation must support class retrieval and enumeration, through the [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) and [**CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync) methods respectively. The following table lists the additional asynchronous **IWbemServices** methods that you can implement for a class provider.



| Method                                                     | Feature      |
|------------------------------------------------------------|--------------|
| [**PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) | Modification |
| [**DeleteClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync) | Deletion     |



 

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

Your class provider should supply a stub implementation that returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** for all of other [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) methods that do not support your feature set. Specifically, WMI does not support query processing for class providers. As such, a class provider must return **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** from their implementation of [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync), set their **QuerySupportLevels** registration property to **NULL**, or both.

The interfaces that a class provider implements are very similar to the interfaces for an instance provider and a method provider. In fact, a single provider can act as all three types of provider by implementing all the methods and registering properly.

 

 



