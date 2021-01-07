---
description: A method provider allows WMI access to the methods of a class. For example, a class that represents an application may have a method that terminates the application.
ms.assetid: bce87e65-5cba-4eef-91da-a3e13c80b8a6
ms.tgt_platform: multiple
title: Writing a Method Provider
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Method Provider

A method provider allows WMI access to the methods of a class. For example, a class that represents an application may have a method that terminates the application.

Changing the order of method input and output parameters when updating an existing method provider can cause failure for applications that call the method. The order of the input or output parameters is established by the value of the [**ID**](standard-wmi-qualifiers.md) qualifier on each parameter. The first parameter has an **ID** value of zero. Add new input parameters at the end of the existing parameters rather than inserting them in the already established sequence.

The following procedure describes how to implement a method provider.

**To implement a method provider**

1.  Design and register your class provider with WMI.

    Class providers register with WMI by creating a [**\_\_Win32Provider**](--win32provider.md) instance and a [**\_\_MethodProviderRegistration**](--methodproviderregistration.md) class. For more information, see [Registering a Method Provider](registering-a-method-provider.md).

2.  Implement the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface for your provider.

    > [!Note]  
    > Method providers are strongly encouraged to use the multithreading model "Both".

     

3.  Implement the [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync) method for your provider.

    The [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) interface is the primary interface for a method provider. For more information, see [Implementing the Primary Interface for a Method Provider](implementing-the-primary-interface-for-a-method-provider.md).

4.  Add any additional code necessary for your provider.

    When designing your provider, you will most likely need to call WMI interfaces. For more information, see [Calling a Method](calling-a-method.md) and [Maintaining Security Levels in a Provider](impersonating-a-client.md).

    When retrieving information for a client, you may need to access the security levels for that client. For more information, see [Impersonating a Client](impersonating-a-client.md).

5.  Replace the preexisting provider with your new code.

    You do not need to perform this step if you do not have a preexisting provider to copy over. For more information, see [Updating a Provider](updating-a-provider.md).

 

 



