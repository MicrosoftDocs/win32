---
description: A class provider manages a class or series of classes for WMI.
ms.assetid: 755f1fde-a0bf-43f6-a01d-2da7d4e6c10d
ms.tgt_platform: multiple
title: Writing a Class Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Class Provider

A class provider manages a class or series of classes for WMI. A class provider can either be push or pull; that is, it can either store its own data or allow WMI to store data for it in the Windows Management Service. Although a class provider is installed on a specific machine, it can change the class definitions across an entire enterprise. Therefore, most developers do not often create class providers.

Before constructing a class provider, verify that the supported classes truly must be generated dynamically. In most cases, the list of classes is slow-changing and finite. If this is the case, you should not have to create a class provider. Instead, you can place your class definitions in the WMI repository using the WMI API or a MOF file.

The following procedure describes how to implement a class provider.

**To implement a class provider**

1.  Determine if your provider is a push or pull provider.

    A pull provider supplies data dynamically in response to an application request, whereas push providers store their data once in the WMI repository. For more information, see [Determining Push or Pull Status](determining-push-or-pull-status.md).

2.  Design and register your class provider with WMI.

    Class providers register with WMI by creating a [**\_\_Win32Provider**](--win32provider.md) instance and a [**\_\_ClassProviderRegistration**](--classproviderregistration.md) instance. For more information, see [Registering a Class Provider](registering-a-class-provider.md).

3.  Implement the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface for your provider.

    WMI uses [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) to load and initialize a provider. If you are designing a push provider, **IWbemProviderInit** is the only interface you will implement. For more information, see [Initializing a Provider](initializing-a-provider.md).

    > [!Note]  
    > Class providers are strongly encouraged to use the multithreading model "Both".

     

4.  Add any additional code necessary for your provider.

    When designing your provider, you will most likely need to call WMI interfaces. For more information, see [Calling a Method](calling-a-method.md) and [Maintaining Security Levels in a Provider](impersonating-a-client.md).

    When retrieving information for a client, you may need to access the security levels for that client. For more information, see [Impersonating a Client](impersonating-a-client.md).

5.  Implement the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface for your provider.

    The [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface is the primary interface for a pull class provider. For more information, see [Implementing the Primary Interface for a Class Provider](implementing-the-primary-interface-for-a-class-provider.md).

6.  Replace the preexisting provider with your new code.

    You do not need to perform this step if you do not have a preexisting provider to copy over. For more information, see [Updating a Provider](updating-a-provider.md).

 

 



