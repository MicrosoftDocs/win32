---
description: To create a WMI event consumer provider you must register the \_\_Win32Provider instance that represents your provider using an instance of \_\_EventConsumerProviderRegistration.
ms.assetid: d1aa035c-f9ee-46b5-9fa5-8af77156f904
ms.tgt_platform: multiple
title: Registering an Event Consumer Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering an Event Consumer Provider

To create a WMI [*event consumer provider*](gloss-e.md) you must register the [**\_\_Win32Provider**](--win32provider.md) instance that represents your provider using an instance of [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md). As a COM object, your provider must register with the operating system and WMI. The following procedure assumes that you have already implemented the registration process as described in [Registering a Provider](registering-a-provider.md).

The following procedure describes how to register an event consumer provider.

**To register an event consumer provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class that describes the provider.
2.  Create an instance of the [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) class that describes the feature set of the provider.

    The properties that are defined by [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) include the object path to the provider and the names of the logical consumer classes that the event consumer provider supports.

    Be sure to tag the class with both the **Dynamic** and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifiers. The **Dynamic** qualifier signals that WMI should use a provider to retrieve the class instances. The **Provider** qualifier specifies the name of the provider that WMI should use.

The following code example shows how to register an event consumer provider.

``` syntax
// Provider registration.
// ======================

instance of __Win32Provider as $P
{
    Name  = "MyEventConsumer";
    CLSID = "{4916157B-FBE7-11d1-AEC4-00C04FB68820}";

    DefaultMachineName = NULL;
    ClientLoadableCLSID = NULL;
    ImpersonationLevel = 0;

    PerUserInitialization = FALSE;
    Pure = TRUE;
    UnloadTimeout = NULL;
};


instance of __EventConsumerProviderRegistration
{
    Provider = $P;
    ConsumerClassNames = { "MyConsumer" };
};
```

 

 



