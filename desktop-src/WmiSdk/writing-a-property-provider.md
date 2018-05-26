---
Description: A property provider retrieves and modifies individual property values for instances of a given class that is stored in the WMI repository.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fe150157-cf9d-47da-8f94-b18eb0502bd8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Writing a Property Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Writing a Property Provider

A property provider retrieves and modifies individual property values for instances of a given class that is stored in the WMI repository.

The following procedure describes how to create a property provider.

**To create a property provider**

1.  Design and register your provider with WMI.

    Instance providers register with WMI by creating a [**\_\_Win32Provider**](--win32provider.md) instance and a [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md) class. For more information, see [Registering a Property Provider](registering-a-property-provider.md).

2.  Implement the [**IWbemProviderInit**](/windows/win32/Wbemprov/nn-wbemprov-iwbemproviderinit?branch=master) interface for your provider.

    WMI uses [**IWbemProviderInit**](/windows/win32/Wbemprov/nn-wbemprov-iwbemproviderinit?branch=master) to load and initialize a provider. This is a task common to all providers. For more information, see [Initializing a Provider](initializing-a-provider.md).

    > [!Note]  
    > Property providers are strongly encouraged to use the multithreading model "Both".

     

3.  Implement the [**IWbemPropertyProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbempropertyprovider?branch=master) interface for your provider.

    The [**IWbemPropertyProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbempropertyprovider?branch=master) interface is the primary interface for a property provider. The two main methods are [**GetProperty**](/windows/win32/Wbemprov/nf-wbemprov-iwbempropertyprovider-getproperty?branch=master) and [**PutProperty**](/windows/win32/Wbemprov/nf-wbemprov-iwbempropertyprovider-putproperty?branch=master). For more information, see [Implementing the Primary Interface for a Property Provider](implementing-the-primary-interface-for-a-property-provider.md).

4.  Add any additional code necessary for your provider.

    When designing your provider, you will most likely need to call WMI interfaces. For more information, see [Calling a Method](calling-a-method.md) and [Maintaining Security Levels in a Provider](impersonating-a-client.md#maintaining-security-levels-in-a-provider).

    When retrieving information for a client, you may need to access the security levels for that client. For more information, see [Impersonating a Client](impersonating-a-client.md).

5.  Replace the preexisting provider with your new code.

    You do not need to perform this step if you do not have a preexisting provider to copy over. For more information, see [Updating a Provider](updating-a-provider.md).

 

 



