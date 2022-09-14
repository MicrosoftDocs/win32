---
description: Properties in WMI classes describe data about a managed object.
ms.assetid: 4046bfc7-9528-4737-ad61-bbb8419d0b51
ms.tgt_platform: multiple
title: Adding a WMI Property
ms.topic: article
ms.date: 05/31/2018
---

# Adding a WMI Property

Properties in WMI classes describe data about a managed object. For example, **Handle**, **ProcessId**, and **PageFaults** are defined as properties of the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class and describe aspects of an operating system process. For more information, see [Writing a Property Provider](writing-a-property-provider.md).

## Defining a Property in MOF

A WMI property represents an aspect or state in the object. Rather than create methods that simply get and set a value, you can create a property. For example, the **NetEnabled** property of [**Win32\_NetworkAdapter**](/windows/desktop/CIMWin32Prov/win32-networkadapter) displays whether the state of the adapter is enabled or disabled. However, the [**Enable**](/windows/desktop/CIMWin32Prov/enable-method-in-class-win32-networkadapter) and [**Disable**](/windows/desktop/CIMWin32Prov/disable-method-in-class-win32-networkadapter) methods actually perform the action of changing the adapter state.

A property must have a data type. The data type of the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) property **Handle** is **string** and the data type of **PageFaults** is **uint32**. If a property can have only two states, the data type of the property is normally set to **boolean**.

The property may also be an array. For example, the security identifier (**SID**) property of [**Win32\_Trustee**](/previous-versions/windows/desktop/secrcw32prov/win32-trustee) is a byte array (**uint8**) that contains the SID. Properties can contain embedded objects which are references to one or more instances of another WMI class. The discretionary access control list **(DACL)** and system access control list **(SACL)** properties of [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor), for example, are arrays of [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace) objects that describe the groups and accounts that have access. The **Group** property in **Win32\_SecurityDescriptor** contains a reference to a single instance of **Win32\_Trustee**. For more information, see [Embedding Objects in a Class](embedded-objects.md).

A property may have several [*qualifiers*](gloss-q.md). These [qualifiers](wmi-qualifiers.md) may be [*Common Information Model (CIM)*](gloss-c.md) or WMI qualifiers or may be specific to certain types of classes, for example, the [performance Counter](qualifiers-specific-to-wmi-performance-classes.md) class qualifiers. Qualifiers specify some aspect of the property, such as if it is read-only or if it cannot be changed without a specific privilege. An application which attempts to write to the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor)**DACL** property, for example, requires the privileges **SeSecurityPrivilege** and **SeRestorePrivilege**. For more information, see [Adding a Qualifier](adding-a-qualifier.md).

Finally, a property must have a name. You may name a property anything within the bounds of standard programming practice. However, there are two main exceptions. First, you may not use any MOF keyword, such as "class", as a property name. Second, you may not use any WQL keywords, such as "group", as a property name either. For more information on MOF and WQL keywords, see [MOF Data Types](mof-data-types.md) and [WQL (SQL for WMI)](wql-sql-for-wmi.md).

For both C++ and Managed Object Format (MOF) code, you declare the properties of a class at the same time that you declare the class.

**To define a property**

-   Include the property data type, name, and an optional default value and qualifier between the curly braces of the class description.

    ``` syntax
    class MyClass 
    {
        [key] string   strProp;
        sint32         dwProp1 = 21;
        uint32         dwProp2;
    };
    ```

    The MyClass class in the preceding example has three properties: a character string, a 32-bit signed integer, and a 32-bit unsigned integer. Each property is assigned a case-insensitive name and a MOF data type.

    The [**Key**](key-qualifier.md) qualifier defines the string property as the key property that uniquely identifies an instance of the class. For more information about qualifiers, see [Adding a Qualifier](adding-a-qualifier.md).

## Related topics

<dl> <dt>

[Creating a Class](creating-a-class.md)
</dt> </dl>

 

 
