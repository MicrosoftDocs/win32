---
description: Like many other techniques in Managed Object Format (MOF), applying a qualifier to your code is a relatively simple process.
ms.assetid: aaa5c921-bdcd-40e6-ab4b-9441a1957e5b
ms.tgt_platform: multiple
title: Applying a Qualifier
ms.topic: article
ms.date: 05/31/2018
---

# Applying a Qualifier

Like many other techniques in Managed Object Format (MOF), applying a qualifier to your code is a relatively simple process.

The only real challenges are the following restrictions in naming conventions that WMI enforces:

-   A qualifier can describe a class, instance, property, method, or method parameter.
-   Qualifier names cannot have either leading or trailing underscores.
-   A qualifier name cannot begin with a digit.
-   A qualifier name cannot contain special characters such as & \* @ ! ~ \\ /.
-   All qualifier names are case-insensitive.
-   You cannot redefine the standard WMI qualifiers or any qualifiers described in the DMTF CIM specification.
-   Qualifier types are not explicitly declared.

    If you do not declare a qualifier type, WMI assumes the type as Boolean with a value of **TRUE**. Otherwise, WMI types qualifiers based on the qualifier values you declare.

-   When creating your own qualifiers, you should prefix your schema name to your qualifier name.

    The purpose of this rule is to avoid confusion with new qualifiers.

-   You can create homogeneous arrays of qualifiers.

    The following code example shows how qualifier arrays are specified with curly braces that surround the values.

    ``` syntax
    [StringArray{"hello", "there"}, SingleElementArray{3}]
    ```

-   WMI does not support automation types not listed in the reference, such as VT\_NULL. For more information, see [MOF Data Types](mof-data-types.md).

The following procedure helps you to use C++ to add a qualifier to a property.

**To apply a qualifier using C++**

-   Apply the qualifier with a call to the [**IWbemQualifierSet::Put**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemqualifierset-put) method.

    You can use other methods of [**IWbemQualifierSet**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemqualifierset) to retrieve or delete existing qualifiers.

The following procedure helps you to apply a qualifier in MOF files.

**To describe a keyword or identifier with a qualifier using MOF**

-   Place a qualifier in brackets before the keyword or identifier described by the qualifier.

    The following code example shows how qualifiers are used.

    ``` syntax
    [qualifiers...]
    class StdDisk
    {
      [qualifiers...]  uint32 dwNumCylinders;
      [qualifiers...]  uint32 dwNumHeads;
      [qualifiers...]  sint32 Method1();
      sint32 Method2([qualifiers...] Parameter1);
    };
    ```

    The following example describes the proper placement of qualifiers.

    ``` syntax
    [Abstract]
    class MyClass
    {
        [Amendment, InstanceOf]  uint32 dwNumber;
        sint32 MyMethod ([in] sint32 Param);
    };
    ```

 

 



