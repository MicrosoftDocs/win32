---
Description: 'One of the first tasks you must code for a provider is the initialization process, which covers any tasks your provider must perform that allows it to send and receive information from WMI, control a managed object, and perform other tasks.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '3dc145b8-1ce4-4caa-b2ac-31a3681e76f1'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Initializing a Provider
---

# Initializing a Provider

One of the first tasks you must code for a provider is the initialization process, which covers any tasks your provider must perform that allows it to send and receive information from WMI, control a managed object, and perform other tasks. Each type of provider has a different set of tasks that it must perform and has an accompanying set of unique interfaces.

However, all providers initialize through the [**IWbemProviderInit**](iwbemproviderinit.md) interface, and inform WMI of their initialization status through the [**IWbemProviderInitSink**](iwbemproviderinitsink.md) interface.

The following procedure describes how to initialize a provider.

**To initialize a provider**

1.  Implement [**IWbemProviderInit::Initialize**](iwbemproviderinit-initialize.md) for your provider.

    When WMI determines that a client requires the services of a provider, WMI loads the provider by calling the [**IWbemProviderInit::Initialize**](iwbemproviderinit-initialize.md) method.

2.  Implement any interfaces unique to your type of provider.
3.  Inform WMI that your provider is finished with initialization by calling [**IWbemProviderInitSink::SetStatus**](iwbemproviderinitsink-setstatus.md).

    All implementations of [**IWbemProviderInit::Initialize**](iwbemproviderinit-initialize.md) must call [**IWbemProviderInitSink::SetStatus**](iwbemproviderinitsink-setstatus.md) to report initialization status to WMI. The **SetStatus** method allows WMI to determine if a provider is ready to receive requests and the type of requests that the provider is ready to receive.

The following procedure describes how to report a successful initialization.

**To report a successful initialization**

-   Set the *IStatus* parameter of [**SetStatus**](iwbemproviderinitsink-setstatus.md) to **WBEM\_S\_INITIALIZED**.

    By returning **WBEM\_S\_INITIALIZED**, a provider indicates a readiness to handle requests from applications, WMI, and other providers. After receiving WBEM\_S\_INITIALIZED, WMI makes a call to the [**IWbemProviderInit::QueryInterface**](iwbemproviderinit.md) method on the provider. This query retrieves a pointer to the primary interface of the provider.

The following procedure describes how to report an error during initialization.

**To report an error during initialization**

-   Set the *IStatus* parameter of [**SetStatus**](iwbemproviderinitsink-setstatus.md) to **WBEM\_E\_FAILED**. WMI views providers that return **WBEM\_E\_FAILED** as not functional.

    WMI releases the [**IWbemProviderInit**](iwbemproviderinit.md) pointer either after WMI has obtained a pointer to the primary interface of the provider or after initialization has failed.

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> </dl>

 

 



