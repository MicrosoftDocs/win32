---
description: A qualifier flavor is a flag that describes more information about a qualifier.
ms.assetid: a7d9d1c0-9386-4c90-9788-993b35ed12db
ms.tgt_platform: multiple
title: Describing a Qualifier with a Qualifier Flavor
ms.topic: article
ms.date: 05/31/2018
---

# Describing a Qualifier with a Qualifier Flavor

A [*qualifier flavor*](gloss-q.md) is a flag that describes more information about a qualifier. For example, the Restricted qualifier flavor states that WMI should not propagate the associated qualifier to any derived classes or instances. You can set flavors using either MOF code or programmatically. While you can describe a variety of effects with flavors, the main purposes of flavor flags is to define how WMI propagates qualifiers through inheritance.

WMI defines several qualifier flavors that you can attach to any qualifier, regardless of the origin of the qualifier. However, some flavors are not appropriate for all qualifier types. The **ToSubClass** flavor, for example, is appropriate only for qualifiers defined for a class. You cannot attach **ToSubClass** to a qualifier used to describe an instance.

You can use flavors to describe a variety of different effects for qualifiers. For example, flavor can indicate if a qualifier can be localized. However, one of the main purposes of a qualifier flavor is to describe whether a parent class can pass qualifiers to a subclass or class instance. You can also use flavors to determine if a class property passes a qualifier on to an instance property. Finally, use flavors to state whether a subclass can override the original value of an inherited qualifier. However, qualifiers that you declare for a class or instance do not propagate to the properties of that class or instance. Further, flavors that establish override permissions are valid only if you also set the **ToInstance** or **ToSubClass** flavors.

A flavor can be globally assigned to a qualifier for an entire MOF file using the following syntax in which white space acts as the delimiter when multiple flavors are specified.

``` syntax
Qualifier QualifierName : flavor1 <flavor2...>;
```

Global flavors apply to all subsequent uses of the qualifier in the MOF file. Global flavor statements may occur anywhere in the file outside of an object declaration block. Flavors redefined at the class, instance, or property level override the global flavor declarations for the scope of that object.

You cannot define a new flavor. Although you can create a new qualifier, use only existing [Qualifier Flavors](qualifier-flavors.md) to describe your new qualifier.

**To define qualifier flavors in MOF**

-   Declare the flavors that describe a given qualifier after the qualifier name, between the qualifier brackets. Use white space as the delimiter between multiple flavors.

    The following example shows the pattern for attaching predefined qualifiers.

    ``` syntax
    [qualifier1 : flavor1 flavor2 flavor3, qualifier2 : flavor1]
    ```

You can add qualifier flavors programmatically only in C++. This operation is not available in the [Scripting API for WMI](scripting-api-for-wmi.md), although you can add a new qualifier by calling [**SWbemQualifierSet.Add**](swbemqualifierset-add.md).

**To assign a flavor using C++**

-   Call the [**IWbemQualifierSet::Put**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemqualifierset-put) method with the *lFlavor* parameter set to one of the constants defined for the method.

 

 



