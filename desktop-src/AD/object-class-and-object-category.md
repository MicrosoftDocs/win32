---
title: Object Class and Object Category
description: Each instance of an object class has a multi-valued objectClass property that identifies the class of which the object is an instance, as well as all structural or abstract superclasses from which that class is derived.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b3c5f9ee-98e0-42dd-9b61-3731e14b9cd4'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Object Class and Object Category

Each instance of an object class has a multi-valued [**objectClass**](https://msdn.microsoft.com/library/ms679012) property that identifies the class of which the object is an instance, as well as all structural or abstract superclasses from which that class is derived. Thus, the **objectClass** property of a user object would identify the [**top**](https://msdn.microsoft.com/library/ms683975), [**person**](https://msdn.microsoft.com/library/ms683895), [**organizationalPerson**](https://msdn.microsoft.com/library/ms683883), and [**user**](https://msdn.microsoft.com/library/ms683980) classes. The **objectClass** property does not include auxiliary classes in the list. The system sets the **objectClass** value when the object instance is created and it cannot be changed.

Each instance of an object class also has an [**objectCategory**](https://msdn.microsoft.com/library/ms679011) property, which is a single-valued property that contains the distinguished name of either the class of which the object is an instance or one of its superclasses. When an object is created, the system sets its **objectCategory** property to the value specified by the [**defaultObjectCategory**](https://msdn.microsoft.com/library/ms675486) property of its object class. An object's **objectCategory** property cannot be changed.

For more information, and a code example that retrieves an object's [**objectClass**](https://msdn.microsoft.com/library/ms679012) property, see [Retrieving the objectClass Attribute](retrieving-the-objectclass-property.md).

> \[!Important\]  
> Prior to Windows Server 2008, the [**objectClass**](https://msdn.microsoft.com/library/ms679012) attribute is not indexed. This is because it has multiple values and is highly non-unique; that is, every instance of the **objectClass** attribute includes the [**top**](https://msdn.microsoft.com/library/ms683975) class. This means an index would be very large and ineffective. To locate objects of a given class, use the [**objectCategory**](https://msdn.microsoft.com/library/ms679011) attribute, which is single-valued and indexed. For more information about using these properties in search filters, see [Deciding What to Find](deciding-what-to-find.md).

 

For most classes, the [**defaultObjectCategory**](https://msdn.microsoft.com/library/ms675486) is the distinguished name of the class's [**classSchema**](https://msdn.microsoft.com/library/ms680982) object. For example, the **defaultObjectCategory** for the [**organizationalUnit**](https://msdn.microsoft.com/library/ms683886) class is "CN=Organizational-Unit,CN=Schema,CN=Configuration,&lt;DC=forestroot&gt;". However, some classes refer to another class as their **defaultObjectCategory**. This allows a query to readily find groups of related objects, even if they are of differing classes. For example, the [**user**](https://msdn.microsoft.com/library/ms683980), [**person**](https://msdn.microsoft.com/library/ms683895), [**organizationalPerson**](https://msdn.microsoft.com/library/ms683883), and [**contact**](https://msdn.microsoft.com/library/ms680995) classes all identify the **person** class in their **defaultObjectCategory** properties. This allows search filters like (objectCategory=person) to locate instances of all these classes with a single query. Queries for people are very common, so this is a simple optimization.

If you create a subclass from a structural class, the best practice is to set the [**defaultObjectCategory**](https://msdn.microsoft.com/library/ms675486) value of the new class to the same distinguished name of the superclass. This allows the standard UI to "find" the subclass.

 

 




