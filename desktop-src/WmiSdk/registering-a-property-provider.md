---
description: To create a WMI property provider you must register the \_\_Win32Provider instance that represents your provider using an instance of \_\_PropertyProviderRegistration.
ms.assetid: e7e30acc-ea41-41e2-9bb3-cd931e8d799e
ms.tgt_platform: multiple
title: Registering a Property Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Property Provider

To create a WMI [*property provider*](gloss-p.md) you must register the [**\_\_Win32Provider**](--win32provider.md) instance that represents your provider using an instance of [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md). As a COM object, your provider must register with the operating system and WMI. The following procedure assumes that you have already implemented the registration process as described in [Registering a Provider](registering-a-provider.md).

The following procedure describes how to register a property provider.

**To register a property provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class that describes the property provider.

    The [**\_\_Win32Provider**](--win32provider.md) class accepts the default values for other properties, such as the **TRUE** value for the **Pure** property. For more information, see [**\_\_Win32Provider**](--win32provider.md).

2.  Create an instance of the [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md) class that describes the feature set of the provider.

    The [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md) class inherits many properties from the [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md) parent class, which provides Boolean values that indicate support for particular features and an array of strings to indicate query support.

    Be sure to tag the class with both the [**Dynamic**](dynamic-qualifier.md) and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifiers. The **Dynamic** qualifier signals that WMI should use a dynamic provider to retrieve the class instances that contain the supported properties. The **Provider** qualifier specifies the name of the provider that WMI should use.

WMI calls NewQuery on an event provider when a client consumer registers an event filter query that contains references to events supported by that event provider. So the event provider responsible for instance modification events for the EmailClass class can be set up to generate notifications only for sender. When the provider receives a query requesting notification of changes to the subject property, the provider can start generating those notifications. In this scenario, WMI is not required to discard the notifications that report recipient changes only.

The following MOF code example describes instances that can be used to register a property provider.

``` syntax
  instance of __Win32Provider as $P
  {
    Name    = "PropProvider" ;
    ClsId   = "{E30EC6A0-23CF-11d1-8FDE-0000F804AA5C}" ;
  };    

  instance of __PropertyProviderRegistration
  {
    Provider = $P;
    SupportsGet = TRUE;
    SupportsPut = FALSE;
  };
```

> [!Note]  
> Only administrators can register or delete a property provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md).

 

 

 



