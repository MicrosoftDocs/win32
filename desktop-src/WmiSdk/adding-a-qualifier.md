---
description: A qualifier is a data string that provides more information about a class, instance, property, method, or parameter.
ms.assetid: 6984b575-b365-49dd-aeab-a763430f434c
ms.tgt_platform: multiple
title: Adding a Qualifier
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Qualifier

A qualifier is a data string that provides more information about a class, instance, property, method, or parameter.

The following class definition is an example of a derived class that has class qualifiers.

``` syntax
[Dynamic, Provider ("ProviderX")] 
class MyDerivedClass : MyClass
{
    [key] string sKey;
    [Implemented] sint32 ValueMethod();
    [Implemented] sint32 MyMethod ([in, Id(0)] sint32 Param);
};
```

Qualifiers can be divided into standard qualifiers, CIM qualifiers, and unique qualifiers include the following:

-   Standard qualifier

    A standard qualifier is a qualifier defined by WMI and commonly used in MOF code. For example, the [**Dynamic**](dynamic-qualifier.md) and [**Read**](standard-qualifiers.md) qualifiers are both standard qualifiers. For more information, see [WMI Qualifiers](wmi-qualifiers.md).

-   CIM qualifier

    A CIM qualifier is a qualifier included in the CIM specification. While use CIM qualifiers in MOF code, the standard qualifiers are designed specifically with WMI in mind. For more information, see the DMTF [CIM Specification](https://www.dmtf.org/spec/cims.html/).

-   Unique qualifier

    A unique qualifier is a qualifier defined specifically for a new class by a class provider. For example, the [**Units**](standard-qualifiers.md) qualifier is a nonstandard, provider-specific qualifier. You can create your own qualifiers for use with your provider. For more information about creating a provider, see [Developing a WMI Provider](developing-a-wmi-provider.md).

Whatever your qualifier does, the main process you perform is to use the qualifier in your MOF code. For more information, see [Applying a Qualifier](applying-a-qualifier.md). You can further describe a qualifier with a qualifier flavor. A qualifier flavor contains more information regarding how a provider should use a qualifier. For more information, see [Describing a Qualifier with a Qualifier Flavor](describing-a-qualifier-with-a-qualifier-flavor.md).

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 



