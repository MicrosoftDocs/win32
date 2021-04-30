---
description: Like other instance providers, you register a high-performance provider with Microsoft Windows&\#160;Management Instrumentation (WMI) by creating an instance of the \_\_Win32Provider and \_\_InstanceProviderRegistration classes.
ms.assetid: 6ff3f8c6-71ca-4589-bca7-b864e24a473d
ms.tgt_platform: multiple
title: Registering a High-Performance Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering a High-Performance Provider

Like other instance providers, you register a high-performance provider with Microsoft Windows Management Instrumentation (WMI) by creating an instance of the [**\_\_Win32Provider**](--win32provider.md) and [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) classes. The **\_\_Win32Provider** instance defines the provider's physical implementation, and the **\_\_InstanceProviderRegistration** instance defines the provider's feature set. For more information, see [Registering a Provider](registering-a-provider.md).

The following procedure describes how to register a high-performance instance provider.

**To register a high-performance instance provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class describing the provider.

    Be sure to add a **ClientLoadableCLSID** property to the [**\_\_Win32Provider**](--win32provider.md) instance. If both the provider and client reside on the same computer, WMI loads the provider in-process to the client using **ClientLoadableCLSID** as the class identifier. When the provider and client reside on different computers, WMI loads the provider in-process to WMI. WMI also uses **ClientLoadableCLSID** to support refresh operations.

2.  Create an instance of the [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) class that describes the feature set of the provider.

    Be sure to tag the class with both the [**Dynamic**](dynamic-qualifier.md) and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifiers. The **Dynamic** qualifier signals that WMI should use a provider to retrieve the class instances. The **Provider** qualifier specifies the name of the provider that WMI should use.

    A high-performance provider also needs to state support for operations, enumeration operations, or both. Make sure you use the **SupportsGet** and **SupportsEnumeration** properties in your implementation.

The following code example shows you how to implement the [**\_\_Win32Provider**](--win32provider.md) and [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) classes for a high-performance provider.

``` syntax
instance of __Win32Provider as $P
{
    Name="TestProv";
    CLSID="{A41602A4-C038-11d1-AEB6-00C04FB68820}";
    ClientLoadableCLSID="{423B32C9-B033-4242-EFB6-55C044242821}";
};

instance of __InstanceProviderRegistration
{
    Provider = $P;
    SupportsGet = TRUE;
    SupportsEnumeration = TRUE;
};

[ dynamic, 
  provider("TestProv")
]

class TestClass
{
    [key] string KeyVal;
    
    string StrVal1;

    sint32 IntVal1;
    sint32 IntVal2;

    sint32 IntArray2[];
};
```

## Related topics

<dl> <dt>

[Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)
</dt> </dl>

 

 



