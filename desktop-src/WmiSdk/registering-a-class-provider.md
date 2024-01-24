---
description: To create a WMI class provider you must register the \_\_Win32Provider instance that represents your provider using an instance of \_\_ClassProviderRegistration.
ms.assetid: ed834969-47e9-47df-9db8-c805b2eb71da
ms.tgt_platform: multiple
title: Registering a Class Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Class Provider

To create a WMI class provider you must register the [**\_\_Win32Provider**](--win32provider.md) instance that represents your provider using an instance of [**\_\_ClassProviderRegistration**](--classproviderregistration.md). As a COM object, your provider must register with the operating system and WMI. The following procedure assumes that you have already implemented the registration process as described in [Registering a Provider](registering-a-provider.md). If your provider stores most data in the WMI repository and that data is updated only on WMI initialization, then register your class as a push class provider. If the data you are providing changes frequently and is retrieved dynamically by your code on every request from WMI, then register your provider as a pull class provider.

The following procedure describes how to register a push class provider.

**To register a push class provider**

-   Set the **InteractionType** property of the [**\_\_ClassProviderRegistration**](--classproviderregistration.md) instance to 1.

    Creating an instance of [**\_\_ClassProviderRegistration**](--classproviderregistration.md) is part of the registration process.

The following procedure describes how to register a pull class provider.

**To register a pull class provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class that describes the provider.
2.  Create an instance of the [**\_\_ClassProviderRegistration**](--classproviderregistration.md) class that describes the feature set of the provider.

    Within the [**\_\_ClassProviderRegistration**](--classproviderregistration.md) instance:

    1.  Set the **InteractionType** property to indicate whether the provider is a push or pull provider.
    2.  Tag the class with both the [**Dynamic**](standard-wmi-qualifiers.md) and [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifiers.

        The [**Dynamic**](standard-wmi-qualifiers.md) qualifier signals that WMI should use a provider to retrieve the class instances. The [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier specifies the name of the provider that WMI should use.

    3.  Define the **ResultSetQueries**, **ReferencedSetQueries**, and **UnsupportedQueries** properties.

        These query properties describe detailed information about the supported class.

In addition to describing the various supported methods of a class, the [**\_\_ClassProviderRegistration**](--classproviderregistration.md) class also has three properties that describe a series of queries. When used together, these three properties describe the entire range of classes supplied by the class provider. Each query property contains a WQL SELECT statement, called a "schema query," to specify the types of supported classes. Schema queries specify a special class name called meta\_class. The following table lists the query properties.



| Property                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ResultSetQueries**     | Contains information about the result set the provider supplies. WMI uses the information to determine whether to invoke the provider to satisfy a query from an application. This property describes either the set of all classes that the provider can supply or a superset of the available classes, but never a subset. WMI requires a provider to specify at least one query in this property.<br/> The following example shows how to set **ResultSetQueries** when a provider supplies an association class that references the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class.<br/> `SELECT * FROM meta_class WHERE __Class = "Win32_LogicalDisk"`<br/> The following example shows how to specify a general query when a provider supplies classes that reference other unknown classes.<br/> `SELECT * FROM meta_class`<br/> The following example shows how to set **ResultSetQueries** when a provider supplies only subclasses, but not the parent class of a given class.<br/> `SELECT * FROM meta_class WHERE __Dynasty = "MyClass"`<br/> The following example shows how to use the special \_\_this property and set **ResultSetQueries** when a provider supplies all class and subclasses.<br/> `SELECT * FROM meta_class WHERE __this ISA "MyClass"`<br/> |
| **ReferencedSetQueries** | Determines whether to bypass the provider in schema queries where associations and references are being requested. Providers that can supply association classes must include at least one query in their **ReferencedSetQueries** property.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **UnsupportedQueries**   | Contains information about the result set that a class provider does not supply. WMI uses this property to subtract from the set of classes implied by **ResultSetQueries**. For example, a class provider can specify in **ResultSetQueries** support for all classes derived from MyClass and specify in **UnsupportedQueries** a lack of support for one particular derived class.<br/> The more information that a provider can register about its query processing capabilities, the faster it runs. Entering one or more queries in the **UnsupportedQueries** property is one way to be specific and is particularly important when a provider relies on a class that it does not supply. When a request is made for a class that is listed in a query in the **UnsupportedQueries** property, WMI can supply the class itself or invoke an alternate provider to supply it.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

Because WMI does not support the OR clause, you must create a separate query for each class.

The following queries are specified in **ResultSetQueries** when a class provider supplies MyClass1, MyClass2, and MyClass3.


```sql
SELECT * FROM meta_class WHERE __Class = "MyClass1"
SELECT * FROM meta_class WHERE __Class = "MyClass2"
SELECT * FROM meta_class WHERE __Class = "MyClass3"
```



Only administrators can register or delete a provider by creating an instance of [**\_\_Win32Provider**](--win32provider.md) and [**\_\_ClassProviderRegistration**](--classproviderregistration.md).

 

