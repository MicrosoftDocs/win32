---
description: An instance provider supplies instances of one or more given classes.
ms.assetid: d53c3399-cba8-4b5d-8da0-b5a23f94c0ae
ms.tgt_platform: multiple
title: Writing an Instance Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Instance Provider

An instance provider supplies instances of one or more given classes. For example, an instance provider can supply information regarding a CPU or other type of hardware. Because the objects managed by an instance provider tend to change on a regular basis, all instance providers are considered pull providers; that is, a provider that dynamically retrieves information regarding a managed object whenever WMI makes a request for the information. The name comes from the idea that WMI "pulls" the information from the provider on behalf of a client request. Using pull technology, an instance provider can support retrieval, enumeration, modification, deletion, and query processing of a specific instance.

High-performance providers can increase the efficiency of an instance provider or programmatically access the data that appears in System Monitor. For more information, see [Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md).

The following procedure describes how to write an instance provider.

**To write an instance provider**

1.  [Register your provider with WMI](registering-an-instance-provider.md).

    Instance providers register with WMI by creating a [**\_\_Win32Provider**](--win32provider.md) instance and an [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) class.

2.  [Initialize your provider](initializing-a-provider.md).

    WMI uses [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) to load and initialize a provider. This is a task common to all providers.

    > [!Note]  
    > Instance providers are strongly encouraged to use the multithreading model "Both".

     

3.  [Implement the IWbemServices interface for your provider](implementing-the-primary-interface-for-an-instance-provider.md).

    The [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface is the primary interface for an instance provider.

4.  Add any additional code necessary for your provider.

    When designing your provider, you will most likely need to call WMI interfaces. For more information, see [Making Calls to WMI](making-calls-to-wmi.md).

    When retrieving information for a client, you may need to access the security levels for that client. For more information, see [Impersonating a Client](impersonating-a-client.md).

5.  If necessary, [implement the high-performance interface](improving-the-efficiency-of-an-instance-provider.md).

    The high-performance interface increases the speed at which the provider can react to requests from WMI.

6.  If necessary, [implement support for partial-instance updates](supporting-partial-instance-operations.md).

    As the name implies, a partial-instance update is a technique use to update only part of an instance. For more information about calling a partial instance from a client, see [Updating Part of an Instance](updating-part-of-an-instance.md) and [Retrieving Part of a WMI Instance](retrieving-part-of-an-instance.md).

7.  Replace the preexisting provider with your new code.

    You do not need to perform this step if you do not have a preexisting provider to copy over. For more information, see [Updating a Provider](updating-a-provider.md).

 

 



