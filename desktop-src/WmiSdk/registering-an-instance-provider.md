---
description: To create a WMI instance provider you must register the \_\_Win32Provider instance that represents your provider using an instance of \_\_InstanceProviderRegistration.
ms.assetid: 5ac8e964-606f-4010-84a8-7c0ae6ca2133
ms.tgt_platform: multiple
title: Registering an Instance Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering an Instance Provider

To create a WMI [*instance provider*](gloss-i.md) you must register the [**\_\_Win32Provider**](--win32provider.md) instance that represents your provider using an instance of [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md). As a COM object, your provider must register with the operating system and WMI. The following procedure assumes that you have already implemented the registration process as described in [Registering a Provider](registering-a-provider.md).

The following procedure describes how to register an instance provider.

**To register an instance provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class that describes the provider.
2.  Create an instance of the [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) class that describes the feature set of the provider.

    The [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) class inherits many properties from the [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md) parent class, which provides Boolean values that indicate support for particular features and an array of strings to indicate query support.

    Be sure to tag the class with both the [**Dynamic**](standard-wmi-qualifiers.md) and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifiers. The qualifier signals that WMI should use a **Dynamic** provider to retrieve the class instances. The **Provider** qualifier specifies the name of the provider that WMI should use.

The following code example describes how to register a [**\_\_Win32Provider**](--win32provider.md) and [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) instance.

``` syntax
instance of __Win32Provider as $P
{
    Name="TestProv";
    CLSID="{A41602A4-C038-11d1-AEB6-00C04FB68820}";
};

instance of __InstanceProviderRegistration
{
    Provider = $P;
    SupportsGet = TRUE;
    SupportsEnumeration = TRUE;
    QuerySupportLevels = { "WQL:UnarySelect" };
};
```

 

 



