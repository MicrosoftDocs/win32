---
title: Dynamic Auxiliary Classes
description: Similar to structural and abstract object classes, auxiliary classes are defined by a classSchema object in the Active Directory schema.
ms.assetid: bd5f6aed-c79a-4c03-ad03-a4ae00f0b888
ms.tgt_platform: multiple
keywords:
- Dynamic Auxiliary Classes AD
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Auxiliary Classes

Similar to structural and abstract object classes, auxiliary classes are defined by a [**classSchema**](/windows/desktop/ADSchema/c-classschema) object in the Active Directory schema. For more information, see [Structural, Abstract, and Auxiliary Classes](structural-abstract-and-auxiliary-classes.md). This schema definition specifies various characteristics of the class, including the attributes associated with the class.

Unlike with structural classes, You cannot create an instance of an auxiliary class as you can with a structural class. Instead, you use an auxiliary class to extend the list of attributes that is associated with another structural, abstract, or auxiliary object class.

In the initial release of Windows 2000, Active Directory Domain Services provided support for statically linking auxiliary classes to the [**classSchema**](/windows/desktop/ADSchema/c-classschema) definition of another object class. When an auxiliary class is used in this way, every instance of the object class supports the attributes of the auxiliary class.

**Windows 2000 Server and earlier:** Active Directory Domain Services does not provide support for dynamically linking auxiliary classes to individual objects, and not just to entire classes of objects. In addition, auxiliary classes that have been attached to an object instance cannot subsequently be removed from the instance.

**Windows Server 2003:** Dynamic Auxiliary Classes are supported when all domain controllers in the forest are running Windows Server 2003 and the forest functional mode is Windows Server 2003.

For more information about auxiliary classes, see:

-   [Dynamically Linked Auxiliary Classes](dynamically-linked-auxiliary-classes.md)
-   [Statically Linked Auxiliary Classes](statically-linked-auxiliary-classes.md)
-   [Determining the Classes Associated With an Object Instance](determining-the-classes-associated-with-an-object-instance.md)
-   [Adding an Auxiliary Class to an Object Instance](adding-an-auxiliary-class-to-an-object-instance.md)

For more information about forest functional levels, see "How to raise Active Directory domain and forest functional levels" in the Help and Support Knowledge Base at [https://support/microsoft.com/kb/322692\#4](https://support.microsoft.com/kb/322692).

 

 