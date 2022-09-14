---
description: To create a WMI method provider you must register the \_\_Win32Provider instance that represents your provider using an instance of \_\_MethodProviderRegistration.
ms.assetid: 1cfb16ae-8dcf-437d-b779-db2f30bb0d34
ms.tgt_platform: multiple
title: Registering a Method Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Method Provider

To create a WMI [*method provider*](gloss-m.md) you must register the [**\_\_Win32Provider**](--win32provider.md) instance that represents your provider using an instance of [**\_\_MethodProviderRegistration**](--methodproviderregistration.md). After creating an instance of [**\_\_Win32Provider**](--win32provider.md), you must register that provider with WMI. As a COM object, your provider must register with the operating system and WMI. The following procedure assumes that you have already implemented the registration process as described in [Registering a Provider](registering-a-provider.md).

The following procedure describes how to register a method provider.

**To register a method provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class that describes the provider.

    The [**\_\_MethodProviderRegistration**](--methodproviderregistration.md) system class inherits many properties from the [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md) parent class, However, the only property relevant for a method provider is the object path to the [**\_\_Win32Provider**](--win32provider.md) instance.

2.  Create an instance of the [**\_\_MethodProviderRegistration**](--methodproviderregistration.md) class that describes the feature set of the provider.

    Be sure to tag the class with both the [**Dynamic**](dynamic-qualifier.md) and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifiers. The **Dynamic** qualifier signals that WMI should use a provider to retrieve the class instances. The **Provider** qualifier specifies the name of the provider that WMI should use.

The following code example describes how to register a method provider.

``` syntax
  instance of __Win32Provider as $P
  {
    Name    = "MethProvider" ;
    ClsId   = "{E30EC6A0-23CF-11d1-8FDE-0000F804AA5C}" ;
  };    

  instance of __MethodProviderRegistration
  {
    Provider = $P;
  };
```

 

 



