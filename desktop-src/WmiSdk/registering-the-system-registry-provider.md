---
description: The System Registry provider is registered as part of the WMI installation process on Windows.
ms.assetid: ce5d0785-6e1b-411c-91df-f25767310530
ms.tgt_platform: multiple
title: Registering the System Registry Provider
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registering the System Registry Provider

The System Registry provider is registered as part of the WMI installation process on Windows. If you are using another platform and want to use the System Registry provider, you must first register the provider yourself following the steps described below.

The following procedure describes how to register the System Registry provider.

**To register the System Registry provider**

1.  Register the provider as a COM server.

    If necessary, you may need to create registry entries. This process applies to all COM servers and is unrelated to WMI. For more information, see the [COM](https://msdn.microsoft.com/library/aa139695.aspx) documentation in the Microsoft Windows Software Development Kit (SDK).

2.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class to describe the implementation of the System Registry provider.

    The [**\_\_Win32Provider**](--win32provider.md) instance describes the name of the provider and its class identifier (**CLSID**).

    The following example describes how to register [**\_\_Win32Provider**](--win32provider.md) as an instance property, event, or method provider.

    ``` syntax
    // Instance provider
    instance of __Win32Provider as $InstProv
    {
        Name    = "RegProv" ;
        ClsId   = "{fe9af5c0-d3b6-11ce-a5b6-00aa00680c3f}" ;
    };    
    // Property provider 
    instance of __Win32Provider as $PropProv 
    {
        Name = "RegPropProv"; 
        Clsid = "{72967901-68EC-11d0-B729-00AA0062CBB7}"; 
    }; 
    // Event provider
    instance of __Win32Provider as $RegEvent
    {
        Name = "RegistryEventProvider";
        Clsid = "{fa77a74e-e109-11d0-ad6e-00c04fd8fdff}";
    };
    instance of __Win32Provider as $RegMethod
    {
        Name = "RegistryMethodProvider";
        Clsid = "{44DE513E-60C2-11d3-AF33-00C04F79FEB1}";
    };
    ```

3.  Create one or more instances of classes derived from the [**\_\_ProviderRegistration**](--providerregistration.md) class to describe the logical implementation of the System Registry provider.

    Depending on the purpose for which you are registering the System Registry provider, you can create one or more of the following classes.

    [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md)

    [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md)

    [**\_\_EventProviderRegistration**](--eventproviderregistration.md)

    [**\_\_MethodProviderRegistration**](--methodproviderregistration.md)

    The following MOF code example describes how you can register the System Registry provider as an instance, property, event, or method provider.

    ``` syntax
    instance of __InstanceProviderRegistration
    {
        Provider = $InstProv;
        SupportsPut = TRUE;
        SupportsGet = TRUE;
        SupportsDelete = FALSE;
        SupportsEnumeration = TRUE;
    };
    instance of __PropertyProviderRegistration
    {
        Provider = $PropProv;
        SupportsPut = TRUE;
        SupportsGet = TRUE;
    }; 
    instance of __EventProviderRegistration
    {
        Provider = $RegEvent;
        EventQueryList = {
                "select * from RegistryKeyChangeEvent",
                "select * from RegistryValueChangeEvent",
                "select * from RegistryTreeChangeEvent"};
    };
    // Method provider
    instance of __MethodProviderRegistration
    {
        Provider = $RegMethod;
    };
    ```

4.  Compile the MOF file using the MOF compiler or the [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) interface.

The RegEvent.mof file provided in the WMI section of the Windows SDK contains the [**\_\_Win32Provider**](--win32provider.md) and [**\_\_EventProviderRegistration**](--eventproviderregistration.md) instances necessary to register the System Registry provider as an event provider. For more information about registering a provider, see [Registering a Provider](registering-a-provider.md) and [Receiving a WMI Event](receiving-a-wmi-event.md).

 

 



