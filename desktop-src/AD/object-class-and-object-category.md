---
title: Object Class and Object Category
description: Each instance of an object class has a multi-valued objectClass property that identifies the class of which the object is an instance, as well as all structural or abstract superclasses from which that class is derived.
ms.assetid: b3c5f9ee-98e0-42dd-9b61-3731e14b9cd4
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Object Class and Object Category

Each instance of an object class has a multi-valued [**objectClass**](/windows/desktop/ADSchema/a-objectclass) property that identifies the class of which the object is an instance, as well as all structural or abstract superclasses from which that class is derived. Thus, the **objectClass** property of a user object would identify the [**top**](/windows/desktop/ADSchema/c-top), [**person**](/windows/desktop/ADSchema/c-person), [**organizationalPerson**](/windows/desktop/ADSchema/c-organizationalperson), and [**user**](/windows/desktop/ADSchema/c-user) classes. The **objectClass** property does not include auxiliary classes in the list. The system sets the **objectClass** value when the object instance is created and it cannot be changed.

Each instance of an object class also has an [**objectCategory**](/windows/desktop/ADSchema/a-objectcategory) property, which is a single-valued property that contains the distinguished name of either the class of which the object is an instance or one of its superclasses. When an object is created, the system sets its **objectCategory** property to the value specified by the [**defaultObjectCategory**](/windows/desktop/ADSchema/a-defaultobjectcategory) property of its object class. An object's **objectCategory** property cannot be changed.

For more information, and a code example that retrieves an object's [**objectClass**](/windows/desktop/ADSchema/a-objectclass) property, see [Retrieving the objectClass Attribute](retrieving-the-objectclass-property.md).

> [!IMPORTANT]
> Prior to Windows Server 2008, the [**objectClass**](/windows/desktop/ADSchema/a-objectclass) attribute is not indexed. This is because it has multiple values and is highly non-unique; that is, every instance of the **objectClass** attribute includes the [**top**](/windows/desktop/ADSchema/c-top) class. This means an index would be very large and ineffective. To locate objects of a given class, use the [**objectCategory**](/windows/desktop/ADSchema/a-objectcategory) attribute, which is single-valued and indexed. For more information about using these properties in search filters, see [Deciding What to Find](deciding-what-to-find.md).

 

For most classes, the [**defaultObjectCategory**](/windows/desktop/ADSchema/a-defaultobjectcategory) is the distinguished name of the class's [**classSchema**](/windows/desktop/ADSchema/c-classschema) object. For example, the **defaultObjectCategory** for the [**organizationalUnit**](/windows/desktop/ADSchema/c-organizationalunit) class is "CN=Organizational-Unit,CN=Schema,CN=Configuration,<DC=forestroot>". However, some classes refer to another class as their **defaultObjectCategory**. This allows a query to readily find groups of related objects, even if they are of differing classes. For example, the [**user**](/windows/desktop/ADSchema/c-user), [**person**](/windows/desktop/ADSchema/c-person), [**organizationalPerson**](/windows/desktop/ADSchema/c-organizationalperson), and [**contact**](/windows/desktop/ADSchema/c-contact) classes all identify the **person** class in their **defaultObjectCategory** properties. This allows search filters like (objectCategory=person) to locate instances of all these classes with a single query. Queries for people are very common, so this is a simple optimization.

If you create a subclass from a structural class, the best practice is to set the [**defaultObjectCategory**](/windows/desktop/ADSchema/a-defaultobjectcategory) value of the new class to the same distinguished name of the superclass. This allows the standard UI to "find" the subclass.

 

 